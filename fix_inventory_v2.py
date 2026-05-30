import json
import os
import re

target_categories = [
    "冬季保暖", "电子周边", "五金工具", "车载用品", "日百", 
    "户外露营", "家居装饰", "厨房厨具", "母婴玩具", "宠物用品"
]

category_mapping = {
    "pet supplies": "宠物用品",
    "electronics": "电子周边",
    "smart watch": "电子周边",
    "hardware": "五金工具",
    "drill": "五金工具",
    "car": "车载用品",
    "auto": "车载用品",
    "automotive": "车载用品",
    "camping": "户外露营",
    "outdoor": "户外露营",
    "kitchen": "厨房厨具",
    "home decor": "家居装饰",
    "baby": "母婴玩具",
    "toys": "母婴玩具",
    "pet": "宠物用品",
    "winter": "冬季保暖",
    "warm": "冬季保暖",
    "hardware tool": "五金工具",
    "daily": "日百",
    "cleaning": "日百",
    "fitness equipment": "电子周边", # Closest? or maybe others?
    "personal care": "日百",
    "garden tool": "五金工具",
}

keyword_rules = [
    (r"winter|warm|heating|gloves|scarf|hat|blanket|heater|thermal|electric blanket|hand warmer|earmuffs", "冬季保暖"),
    (r"electronics|smart watch|phone case|charger|cable|headphones|bluetooth|speaker|mouse|keyboard|camera|lens|power bank|usb|fitness", "电子周边"),
    (r"hardware|drill|hammer|screwdriver|wrench|tool set|pliers|saw|gardening tools|measuring tape|glue gun|soldering iron|drill|impact", "五金工具"),
    (r"car|auto|vehicle|seat cover|cup holder|air freshener|gps|dash cam|tire|steering wheel|trunk|car organizer", "车载用品"),
    (r"daily|cleaning|tissue|laundry|storage|towels|hooks|hangers|umbrella|rain coat|bathroom|personal care|beauty|soap", "日百"),
    (r"outdoor|camping|tent|sleeping bag|flashlight|backpack|hiking|grill|picnic|folding chair|compass|survival", "户外露营"),
    (r"home decor|decoration|wall art|clock|vase|candle|light|lamp|rug|curtain|photo frame|sticker|ornament|mirror", "家居装饰"),
    (r"kitchen|cookware|utensils|knife|pot|pan|kettle|blender|toaster|coffee maker|spoon|fork|plates|cups|silicone mold|oven", "厨房厨具"),
    (r"baby|toy|kids|mom|diaper|stroller|rattle|puzzle|blocks|doll|pregnancy|nursing", "母婴玩具"),
    (r"pet|dog|cat|leash|collar|pet bed|pet toy|pet food|aquarium|hamster|bird cage", "宠物用品"),
]

def clean_category(product):
    title = product.get("ProductName", "").lower()
    cat = product.get("category", "")
    
    # 1. If cat is already a target category, keep it
    if cat in target_categories:
        return cat
    
    # 2. Try direct mapping from cat
    for key, val in category_mapping.items():
        if key in cat.lower():
            return val
            
    # 3. Try keyword matching on title
    for pattern, val in keyword_rules:
        if re.search(pattern, title):
            return val
            
    # 4. Default to "日百" if nothing else matches
    return "日百"

def main():
    json_path = "dist/hdl_inventory.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    fixed_count = 0
    cat_stats = {cat: 0 for cat in target_categories}

    for p in products:
        old_cat = p.get("category", "")
        new_cat = clean_category(p)
        if old_cat != new_cat:
            p["category"] = new_cat
            fixed_count += 1
        
        if new_cat in cat_stats:
            cat_stats[new_cat] += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"Fixed {fixed_count} products.")
    print("Category statistics:")
    for cat, count in cat_stats.items():
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    main()
