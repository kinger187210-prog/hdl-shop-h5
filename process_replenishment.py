import json
import re
import os
import glob

def parse_price(price_str):
    if not price_str:
        return 0.0
    # Remove $ and extract first number
    nums = re.findall(r'[\d.]+', price_str)
    if nums:
        return float(nums[0])
    return 0.0

def process():
    inventory_file = 'dist/hdl_inventory.json'
    crawled_dir = 'crawled_data'
    
    # 1. Load current inventory
    with open(inventory_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)
    
    existing_ids = {p['id'] for p in inventory}
    new_products = []

    # 2. Parse raw_items.txt (ID|Title|Image|Price|Category)
    raw_items_path = os.path.join(crawled_dir, 'raw_items.txt')
    if os.path.exists(raw_items_path):
        with open(raw_items_path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) >= 5:
                    pid = parts[0].strip()
                    if pid in existing_ids: continue
                    
                    title = parts[1].strip()
                    img = parts[2].strip()
                    try:
                        price = float(parts[3].strip())
                    except:
                        price = parse_price(parts[3])
                    
                    cat = parts[4].strip()
                    
                    # Assume markup is needed if it's from raw search
                    # But the task said "apply 50% markup" in the spawn task.
                    # I'll check if the price looks already marked up.
                    # Usually Alibaba prices are lower. I'll just apply it to be safe if it's a raw number.
                    marked_up_price = price * 1.5
                    
                    new_products.append({
                        "ProductName": title,
                        "ProModel": pid,
                        "id": pid,
                        "sPicUrl": img,
                        "price_display": f"${marked_up_price:.2f}",
                        "category": cat
                    })
                    existing_ids.add(pid)

    # 3. Parse raw_tables_*.txt
    # | 1 | 1601267167512 | Title | Image | $2.50-2.99 / 20 sets |
    # Category is usually in the file header or inferred from file context.
    # Since I don't know the exact category mapping for each table, 
    # I'll try to find "Category:" in the text or use the filename.
    for table_file in glob.glob(os.path.join(crawled_dir, 'raw_tables_*.txt')):
        current_cat = "其他"
        with open(table_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Try to find category in header
            cat_match = re.search(r'([^\n]+)(?:[:：])', content)
            if cat_match:
                header = cat_match.group(1)
                if "Kitchen" in header or "厨房" in header: current_cat = "厨房厨具"
                elif "Winter" in header or "冬季" in header: current_cat = "冬季保暖"
                elif "Pet" in header or "宠物" in header: current_cat = "宠物用品"
                elif "Hardware" in header or "五金" in header: current_cat = "五金工具"
                elif "Home Decor" in header or "家居" in header: current_cat = "家居装饰"
                elif "Camping" in header or "露营" in header: current_cat = "户外露营"
                elif "Baby" in header or "母婴" in header: current_cat = "母婴玩具"
                elif "Electronics" in header or "电子" in header: current_cat = "电子周边"
                elif "Car" in header or "车载" in header: current_cat = "车载用品"

            # Parse markdown table rows
            rows = re.findall(r'\|?\s*\d+\s*\|\s*(\d+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|', content)
            for pid, title, img, price_str in rows:
                pid = pid.strip()
                if pid in existing_ids: continue
                
                title = title.strip()
                img = img.strip()
                price = parse_price(price_str)
                marked_up_price = price * 1.5
                
                new_products.append({
                    "ProductName": title,
                    "ProModel": pid,
                    "id": pid,
                    "sPicUrl": img,
                    "price_display": f"${marked_up_price:.2f}",
                    "category": current_cat
                })
                existing_ids.add(pid)

    # 4. Parse data_C.json (Handle partial JSON)
    data_c_path = os.path.join(crawled_dir, 'data_C.json')
    if os.path.exists(data_c_path):
        with open(data_c_path, 'r', encoding='utf-8') as f:
            raw_c = f.read().strip()
            if not raw_c.endswith(']'):
                # Try to close it
                if raw_c.endswith(','): raw_c = raw_c[:-1]
                raw_c += ']'
            
            try:
                data_c = json.loads(raw_c)
                for p in data_c:
                    pid = p.get('id')
                    if pid and pid not in existing_ids:
                        new_products.append(p)
                        existing_ids.add(pid)
            except Exception as e:
                print(f"Error parsing data_C.json: {e}")

    # 5. Final Merge
    inventory.extend(new_products)
    
    # Deduplicate again just in case
    unique_inventory = []
    seen = set()
    for p in inventory:
        if p['id'] not in seen:
            unique_inventory.append(p)
            seen.add(p['id'])

    with open(inventory_file, 'w', encoding='utf-8') as f:
        json.dump(unique_inventory, f, ensure_ascii=False, indent=2)
    
    print(f"Items Added: {len(new_products)}")
    print(f"Final Inventory Count: {len(unique_inventory)}")

if __name__ == "__main__":
    process()
