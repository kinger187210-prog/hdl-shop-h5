import os
import re
import json

def parse_price(price_str):
    # Regex to find the first price value in a range like "$1.53-2.38" or "$32"
    match = re.search(r'\$(\d+(?:\.\d+)?)', price_str)
    if match:
        return float(match.group(1))
    return None

def consolidate():
    results_dir = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-DB9653-765527\agent-core\tool-results\agent_DID-DB9653-765527_dm_agent_DID-F456DA-2B0D4C_ccnlxx18"
    output_path = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\dist\hdl_inventory.json"
    
    all_products = {}
    
    for filename in os.listdir(results_dir):
        if not filename.endswith(".txt"):
            continue
            
        filepath = os.path.join(results_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Find the markdown table
            # Format: | # | Product ID | Product Title | Image | Price / MOQ | Review | Lead Time | Supplier / Location | Badges | Matched Requirements | Product URL |
            lines = content.split('\n')
            headers = []
            table_started = False
            
            for line in lines:
                if '| Product ID |' in line:
                    headers = [h.strip() for h in line.split('|') if h.strip()]
                    table_started = True
                    continue
                
                if table_started and line.startswith('|') and '---' not in line:
                    cols = [c.strip() for c in line.split('|')]
                    # The first and last elements are empty because of the leading/trailing |
                    if len(cols) < 5:
                        continue
                    
                    # Mapping column indices based on headers
                    # Headers: #, Product ID, Product Title, Image, Price / MOQ, Review, Lead Time, Supplier / Location, Badges, Matched Requirements, Product URL
                    # cols: ['', '#', 'Product ID', ...]
                    try:
                        p_id = cols[2]
                        p_title = cols[3]
                        p_image = cols[4]
                        p_price_moq = cols[5]
                        p_reqs = cols[10] if len(cols) > 10 else ""
                        
                        if not p_id or p_id == 'Product ID':
                            continue
                            
                        price = parse_price(p_price_moq)
                        if price is None:
                            continue
                            
                        # Apply 50% increase
                        new_price = price * 1.5
                        
                        # Category extraction
                        category = p_reqs.split(',')[0].strip() if p_reqs else "General"
                        
                        product = {
                            "ProductName": p_title,
                            "category": category,
                            "sPicUrl": p_image,
                            "ProModel": p_id,
                            "id": p_id,
                            "price_display": f"${new_price:.2f}"
                        }
                        
                        if p_id not in all_products:
                            all_products[p_id] = product
                    except Exception as e:
                        # print(f"Error parsing line: {line}. Error: {e}")
                        continue
                        
    product_list = list(all_products.values())
    print(f"Total unique products found: {len(product_list)}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(product_list, f, indent=2, ensure_ascii=False)
        
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    consolidate()
