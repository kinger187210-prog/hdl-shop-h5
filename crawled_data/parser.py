import json
import re
import sys

def parse_markdown_table(table_str, category_name):
    products = []
    lines = table_str.strip().split('\n')
    if len(lines) < 3: return []
    
    # Identify headers
    headers = [h.strip() for h in lines[0].split('|') if h.strip()]
    
    id_idx = -1
    title_idx = -1
    image_idx = -1
    price_idx = -1
    
    for i, h in enumerate(headers):
        if 'Product ID' in h or 'ID' in h: id_idx = i
        elif 'Product Title' in h or 'Title' in h: title_idx = i
        elif 'Image' in h: image_idx = i
        elif 'Price' in h: price_idx = i
        
    if id_idx == -1 or title_idx == -1 or image_idx == -1 or price_idx == -1:
        return []
        
    for line in lines[2:]:
        cols = [c.strip() for c in line.split('|') if c.strip()]
        if len(cols) < len(headers): continue
        
        prod_id = cols[id_idx]
        title = cols[title_idx]
        pic_url = cols[image_idx]
        price_str = cols[price_idx]
        
        if "H123456789" in pic_url: continue
        
        # Extract price
        match = re.search(r'(\d+\.\d+|\d+)', price_str)
        if not match: continue
        
        lower_bound = float(match.group(1))
        price_display = f"${lower_bound * 1.5:.2f}"
        
        products.append({
            "ProductName": title,
            "sPicUrl": pic_url,
            "ProModel": prod_id,
            "id": prod_id,
            "price_display": price_display,
            "category": category_name
        })
    return products

if __name__ == "__main__":
    # Example usage: python extract.py "Category Name" < markdown_table.txt
    category = sys.argv[1]
    table_data = sys.stdin.read()
    products = parse_markdown_table(table_data, category)
    # Take up to 25 if not enough, otherwise take 25
    print(json.dumps(products[:25]))
