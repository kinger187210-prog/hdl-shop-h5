import os
import json
import re
import random

def parse_price(price_str):
    # Match something like "$1.23", "$1.23 - $4.56", "$1.23 / piece"
    match = re.search(r'\$(\d+(?:\.\d+)?)', price_str)
    if match:
        return float(match.group(1))
    return None

def process_md_file(filepath):
    products = []
    if not os.path.exists(filepath):
        return products
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    for line in lines:
        if line.startswith('|') and 'Product ID' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            # Clean up empty strings at start/end
            if parts and not parts[0]: parts = parts[1:]
            if parts and not parts[-1]: parts = parts[:-1]
            
            if len(parts) >= 4:
                # Expecting: ID, Title, Image, Price, ...
                p_id = parts[0]
                p_title = parts[1]
                p_image = parts[2]
                p_price_moq = parts[3]
                p_url = parts[4] if len(parts) > 4 else ""
                
                if p_id == "#" or "..." in p_id:
                    continue

                # Extract image URL from markdown image syntax if present
                img_match = re.search(r'src="(.*?)"', p_image) or re.search(r'\((.*?)\)', p_image)
                if img_match:
                    p_image = img_match.group(1)
                elif 'http' in p_image:
                    img_url_match = re.search(r'(https?://[^\s|)]+)', p_image)
                    if img_url_match:
                        p_image = img_url_match.group(1)

                price = parse_price(p_price_moq)
                if price and p_id and p_title:
                    new_price = price * 1.5
                    products.append({
                        "ProductName": p_title,
                        "ProModel": p_id,
                        "id": p_id,
                        "sPicUrl": p_image,
                        "price_display": f"${new_price:.2f}",
                        "original_url": p_url
                    })
    return products

def main():
    crawled_dir = 'crawled_data'
    inventory_path = 'dist/hdl_inventory.json'
    
    # Load existing inventory
    with open(inventory_path, 'r', encoding='utf-8') as f:
        existing_products = json.load(f)
    
    existing_ids = {p['id'] for p in existing_products}
    new_products = []
    
    category_map = {
        "冬季保暖": ["electric_blankets_kazakhstan.md", "portable_heaters_kazakhstan.md", "thermal_underwear_kazakhstan.md", "winter_gloves_kazakhstan.md", "warmth_products.json", "batch1.json"],
        "电子周边": ["power_banks.md", "wireless_earbuds.md", "phone_cases.md", "usb_cables.md", "electronics_products.json", "batch1.json"],
        "五金工具": ["power_tool_sets.md", "hand_tool_sets.md", "measuring_tools.md", "safety_gear.md", "hardware_products.json", "work_gloves.md", "batch1.json"],
        "车载用品": ["car_floor_mats.md", "car_seat_covers.md", "dash_cams.md", "car_cleaning_kits.md", "car_accessories_products.json", "batch1.json"],
        "日百": ["storage_boxes.md", "bathroom_accessories.md", "cleaning_tools.md", "daily_necessities_products.json", "daily_necessities.json", "batch1.json"],
        "户外露营": ["camping_tent.md", "sleeping_bag.md", "portable_camping_chair.md", "outdoor_camping_gear_set.md", "batch2.json"],
        "家居装饰": ["home_decoration_sets.md", "wall_arts.md", "decorative_vases.md", "cushion_covers.md", "batch2.json"],
        "厨房厨具": ["cookware_sets.md", "kitchen_gadgets.md", "kitchen_storage_containers.md", "batch2.json"],
        "母婴玩具": ["baby_clothing_sets.md", "educational_toys.md", "plush_toys.md", "baby_care_products.md", "batch2.json"],
        "宠物用品": ["pet_beds.md", "pet_food_bowls.md", "pet_grooming_tools.md", "pet_toys.md", "batch2.json"]
    }
    
    for cat_name, files in category_map.items():
        cat_products = []
        for filename in files:
            filepath = os.path.join(crawled_dir, filename)
            if filename.endswith('.md'):
                prods = process_md_file(filepath)
                for p in prods:
                    p['category'] = cat_name
                    if p['id'] not in existing_ids:
                        cat_products.append(p)
                        existing_ids.add(p['id'])
            elif filename.endswith('.json'):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for p in data:
                                # Standardize format
                                title = p.get('ProductName') or p.get('title')
                                model = p.get('Product ID') or p.get('ProModel') or p.get('id') or p.get('ProductID')
                                pic = p.get('sPicUrl') or p.get('image')
                                price_str = p.get('price_display') or p.get('price')
                                
                                # If it's from batch files, it already has price_display and markup
                                if 'batch' in filename:
                                    if title and model and pic and price_str:
                                        p_id = str(model)
                                        if p_id not in existing_ids:
                                            # Use internal category if available, else use cat_name
                                            final_cat = p.get('category') or cat_name
                                            cat_products.append({
                                                "ProductName": title,
                                                "ProModel": p_id,
                                                "id": p_id,
                                                "sPicUrl": pic,
                                                "price_display": price_str,
                                                "category": final_cat
                                            })
                                            existing_ids.add(p_id)
                                    continue

                                price = parse_price(str(price_str)) if price_str else None
                                if title and model and pic and price:
                                    p_id = str(model)
                                    if p_id not in existing_ids:
                                        cat_products.append({
                                            "ProductName": title,
                                            "ProModel": p_id,
                                            "id": p_id,
                                            "sPicUrl": pic,
                                            "price_display": f"${price * 1.5:.2f}",
                                            "category": cat_name
                                        })
                                        existing_ids.add(p_id)
                except:
                    pass
        
        print(f"Category {cat_name}: added {len(cat_products)} products")
        new_products.extend(cat_products)
    
    total_products = existing_products + new_products
    print(f"Total products: {len(total_products)}")
    
    with open(inventory_path, 'w', encoding='utf-8') as f:
        json.dump(total_products, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to {inventory_path}")

if __name__ == "__main__":
    main()
