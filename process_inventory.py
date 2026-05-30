import json
import re
import os

tool_results_dir = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-DB9653-765527\agent-core\tool-results\agent_DID-DB9653-765527_dm_agent_DID-F456DA-2B0D4C_ccnlxx22"
files_to_categories = {
    "product_supplier_search_e27fcae8-f938-4dfb-baf3-d6779d6adfb3.txt": "冬季保暖",
    "product_supplier_search_742cfe80-9177-4d80-ae9c-1bdf3d4ac2b9.txt": "电子周边",
    "product_supplier_search_0556d32c-3d4a-4b89-b893-6b1bcacbb093.txt": "五金工具",
    "product_supplier_search_d27c73f7-3372-4d97-a95a-64e68c7f1204.txt": "车载用品",
    "product_supplier_search_9a9f4350-e81e-4571-bae5-8e333c4951f3.txt": "日百",
    "product_supplier_search_7c90a365-e2c8-48b1-92cf-d02cde5ad61a.txt": "户外露营",
    "product_supplier_search_21ea5d80-44cb-40b2-863e-3800c1099070.txt": "家居装饰",
    "product_supplier_search_68b3d4fb-e54d-4826-9289-d37b34d8803e.txt": "厨房厨具",
    "product_supplier_search_37b32c57-32b5-4843-b4b4-49efa770449b.txt": "母婴玩具",
    "product_supplier_search_029c434e-b29d-42a2-8c3e-4b4c34cad694.txt": "宠物用品",
    "product_supplier_search_ed07536a-6f96-4ff4-bee2-6e898707925f.txt": "日百",
    "product_supplier_search_925ecb38-1199-498c-ac8c-b9166ba0fd91.txt": "车载用品",
    "product_supplier_search_a07e3ddc-ed03-4775-bd0f-91eb0bfc9fff.txt": "电子周边",
    "product_supplier_search_16d414a8-a0a9-4327-ac97-3d2c60ce23a1.txt": "厨房厨具"
}

def parse_price(price_str):
    match = re.search(r'\$?(\d+\.?\d*)', price_str)
    if match:
        return float(match.group(1))
    return 0.0

new_items = []
seen_ids = set()

for filename, category in files_to_categories.items():
    filepath = os.path.join(tool_results_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rows = re.findall(r'\| \d+ \| (\d+) \| (.*?) \| (.*?) \| (.*?) \|', content)
    
    for product_id, title, image, price_moq in rows:
        pid = product_id.strip()
        if pid in seen_ids:
            continue
        seen_ids.add(pid)
        
        img_url = image.strip()
        if img_url.startswith('!['):
            img_match = re.search(r'\((.*?)\)', img_url)
            if img_match:
                img_url = img_match.group(1)
        
        if not img_url.startswith('http'):
            if img_url.endswith('.jpg') or img_url.endswith('.png'):
                img_url = "https://s.alicdn.com/@sc04/kf/" + img_url
        
        price = parse_price(price_moq)
        marked_up_price = price * 1.5
        
        new_items.append({
            "ProductName": title.strip(),
            "category": category,
            "sPicUrl": img_url,
            "ProModel": pid,
            "id": pid,
            "price_display": f"${marked_up_price:.2f}"
        })

# Load cleaned inventory
inventory_path = r"dist/hdl_inventory_cleaned.json"
with open(inventory_path, 'r', encoding='utf-8') as f:
    inventory = json.load(f)

# Combine
inventory.extend(new_items)

# Write final
final_path = r"dist/hdl_inventory.json"
with open(final_path, 'w', encoding='utf-8') as f:
    json.dump(inventory, f, indent=2, ensure_ascii=False)

print(f"Added {len(new_items)} unique items. Total items: {len(inventory)}")

# Print 5 samples for verification
for item in new_items[:5]:
    print(f"SAMPLE: {item['category']} | {item['ProductName']} | {item['sPicUrl']}")
