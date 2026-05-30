import json
import re
import sys

def process_table(content, category_name, limit):
    products = []
    lines = content.strip().split('\n')
    start_parsing = False
    for line in lines:
        if '| # | Product ID |' in line:
            start_parsing = True
            continue
        if start_parsing and line.startswith('| ---'):
            continue
        if start_parsing and line.startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 6: continue
            
            product_id = parts[2]
            product_name = parts[3]
            pic_url = parts[4]
            img_match = re.search(r'\((https?://[^\)]+)\)', pic_url)
            if img_match:
                pic_url = img_match.group(1)
            
            price_raw = parts[5]
            price_match = re.search(r'\$(\d+\.?\d*)', price_raw)
            if price_match:
                price = float(price_match.group(1))
                markup_price = price * 1.5
                price_display = f"${markup_price:.2f}"
            else:
                price_display = "$0.00"
            
            products.append({
                "Product ID": product_id,
                "ProductName": product_name,
                "sPicUrl": pic_url,
                "price_display": price_display,
                "category": category_name
            })
            if len(products) >= limit:
                break
    return products

if __name__ == "__main__":
    category = sys.argv[1]
    limit = int(sys.argv[2])
    output_file = "batch1.json"
    
    # Read from stdin
    content = sys.stdin.read()
    new_products = process_table(content, category, limit)
    
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.extend(new_products)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added {len(new_products)} products to {output_file}. Total: {len(data)}")
