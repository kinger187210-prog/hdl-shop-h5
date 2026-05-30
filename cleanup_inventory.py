import json
import requests
import os
import concurrent.futures
import time

INVENTORY_PATH = 'dist/hdl_inventory.json'

def check_image(p):
    url = p.get('sPicUrl')
    if not url: return False
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.head(url, timeout=3, headers=headers, allow_redirects=True)
        return response.status_code == 200
    except:
        return False

def cleanup():
    if not os.path.exists(INVENTORY_PATH):
        print(f"File not found: {INVENTORY_PATH}")
        return

    with open(INVENTORY_PATH, 'r', encoding='utf-8') as f:
        products = json.load(f)

    print(f"Initial product count: {len(products)}")
    
    invalid_ids = set()
    batch_size = 500
    
    for i in range(0, len(products), batch_size):
        batch = products[i:i+batch_size]
        print(f"Checking batch {i//batch_size + 1}/{ (len(products) + batch_size - 1)//batch_size }...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = list(executor.map(check_image, batch))
        
        batch_invalid = 0
        for p, is_valid in zip(batch, results):
            if not is_valid:
                invalid_ids.add(p.get('id'))
                batch_invalid += 1
        
        print(f"Batch {i//batch_size + 1} done. Invalid in this batch: {batch_invalid}")
        
        # Save every batch
        current_products = [p for p in products if p.get('id') not in invalid_ids]
        with open(INVENTORY_PATH, 'w', encoding='utf-8') as f:
            json.dump(current_products, f, ensure_ascii=False, indent=2)
        
        # Short sleep to be nice to the CDN
        time.sleep(0.5)

    print(f"Cleanup complete. Total removed: {len(invalid_ids)}")

if __name__ == "__main__":
    cleanup()
