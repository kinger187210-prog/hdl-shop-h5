import os
import re
import json

def parse_md_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract query
    query_match = re.search(r"Found \d+ products for query: (.+)", content)
    category = query_match.group(1) if query_match else "General"
    
    # Split by lines
    lines = content.split('\n')
    
    # Find table start
    table_lines = []
    in_table = False
    for line in lines:
        if '| # | Product ID |' in line:
            in_table = True
            continue
        if in_table:
            if '| --- |' in line:
                continue
            if line.strip().startswith('|'):
                table_lines.append(line)
            else:
                # Table might have ended or had a break
                pass
    
    products = []
    for line in table_lines:
        parts = [p.strip() for p in line.split('|')]
        # Parts should be: ['', '#', 'Product ID', 'Product Title', 'Image', 'Price / MOQ', 'Review', 'Lead Time', 'Supplier / Location', 'Badges', 'Matched Requirements', 'Product URL', '']
        # Depending on the table columns, indices might vary. Let's be safer.
        if len(parts) < 6: continue
        
        try:
            prod_id = parts[2]
            title = parts[3]
            img_url = parts[4]
            price_moq = parts[5]
            
            # Extract Image URL from Markdown link if necessary
            img_match = re.search(r'src="([^"]+)"', img_url) or re.search(r'\((https?://[^\)]+)\)', img_url)
            if img_match:
                img_url = img_match.group(1)
            elif img_url.startswith('https'):
                img_url = img_url.split(' ')[0] # Handle cases with spaces
            
            # Extract MOQ
            moq = 1
            moq_match = re.search(r'/ (\d+)', price_moq)
            if moq_match:
                moq = int(moq_match.group(1))
            
            # Description
            description = f"Price: {price_moq}"
            if len(parts) > 6:
                description += f" | Review: {parts[6]}"
            if len(parts) > 8:
                description += f" | Supplier: {parts[8]}"

            products.append({
                "ProductName": title,
                "category": category,
                "sPicUrl": img_url,
                "MinOrderNum": moq,
                "ProModel": f"HDL-{prod_id}",
                "id": prod_id,
                "description": description
            })
        except Exception as e:
            # print(f"Error parsing line: {line}. Error: {e}")
            continue
            
    return products

def main():
    # Use relative path for dist
    output_path = os.path.join(os.path.dirname(__file__), "dist", "hdl_inventory.json")
    
    all_products = []
    
    # Verified real JSON files in crawled_data
    real_files = [
        "electronics_products.json",
        "warmth_products.json",
        "hardware_products.json",
        "products.json",
        "car_accessories_products.json",
        "daily_necessities_products_500.json",
        "daily_necessities_products.json",
        "lighting_products.json",
        "security_products.json"
    ]
    
    crawled_root = os.path.join(os.path.dirname(__file__), "crawled_data")
    if os.path.exists(crawled_root):
        for filename in real_files:
            file_path = os.path.join(crawled_root, filename)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for item in data:
                                # Skip items with suspicious IDs
                                pid = str(item.get("prod_id", item.get("id", "")))
                                if pid.startswith("1600000000") or pid.startswith("v1000"):
                                    continue
                                    
                                if "title" in item and "sPicUrl" in item:
                                    all_products.append({
                                        "ProductName": item.get("title", ""),
                                        "category": item.get("category", "General"),
                                        "sPicUrl": item.get("sPicUrl", ""),
                                        "MinOrderNum": item.get("moq", 1),
                                        "ProModel": f"HDL-{pid}",
                                        "id": pid,
                                        "description": f"Price: {item.get('price', '')}"
                                    })
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")

    # Also process original tool-results dir
    base_dir = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-DB9653-765527\agent-core\tool-results\agent_DID-DB9653-765527_dm_agent_DID-F456DA-2B0D4C_ccnlxx13"
    if os.path.exists(base_dir):
        for filename in os.listdir(base_dir):
            if filename.startswith("product_supplier_search") and filename.endswith(".txt"):
                file_path = os.path.join(base_dir, filename)
                all_products.extend(parse_md_table(file_path))
    
    # Deduplicate by ID
    unique_products = []
    seen_ids = set()
    for p in all_products:
        pid = str(p.get("id"))
        if not pid or pid == "None" or pid == "0": continue
        
        # Stricter filtering for real data
        if "example.com" in p.get("sPicUrl", ""): continue
        if not pid.isdigit() or len(pid) < 8: continue
        
        if pid not in seen_ids:
            seen_ids.add(pid)
            unique_products.append(p)
    
    # Ensure dist directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(unique_products, f, ensure_ascii=False, indent=2)
    
    print(f"Processed {len(unique_products)} unique products and saved to {output_path}")

if __name__ == "__main__":
    main()
