import json
import sys
import os
import re

FILE_PATH = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\crawled_data\replenishment_final.json"

def add_products(products):
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                all_products = json.load(f)
        except:
            all_products = []
    else:
        all_products = []
    
    # Simple deduplication by ID
    existing_ids = {p['id'] for p in all_products}
    new_products = []
    for p in products:
        if p['id'] not in existing_ids:
            new_products.append(p)
            existing_ids.add(p['id'])
    
    all_products.extend(new_products)
    
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_products, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    try:
        data = json.load(sys.stdin)
        add_products(data)
        print(f"Added {len(data)} products.")
    except Exception as e:
        print(f"Error: {e}")
