import re
import json
import os

def extract_products(text, category):
    # Regex to find product links and titles
    # Format: [**Title**](URL)
    pattern = r'\[\*\*(.*?)\*\*\]\((https://www\.alibaba\.com/product-detail/.*?)\)'
    matches = re.finditer(pattern, text)
    
    products = []
    for match in matches:
        title = match.group(1).strip()
        url = match.group(2).strip()
        
        # Try to find price after the match
        # Price is usually like "$14.20-15"
        start_pos = match.end()
        # Look at the next 100 characters for price
        context = text[start_pos:start_pos+150]
        price_match = re.search(r'\$(\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?)', context)
        price = price_match.group(0) if price_match else "N/A"
        
        # Try to find MOQ
        moq_match = re.search(r'MOQ:\s*(\d+\s*\w+)', context)
        moq = moq_match.group(1) if moq_match else "N/A"
        
        products.append({
            "category": category,
            "title": title.replace('**', ''),
            "price": price,
            "moq": moq,
            "url": url
        })
    return products

def main():
    # The actual data is in the previous tool outputs.
    # Since I cannot easily "read" the tool output from a file, 
    # I'll have to rely on the fact that I've seen it.
    # Actually, I'll pass the filenames or content to the script if I can.
    # But wait, I don't have the content in a file.
    
    # I will create a dummy file to store the content I've already fetched
    # or I will just use the content directly if I can pass it.
    
    # Since I am writing this script to be executed, I'll use placeholders 
    # and I'll use another tool to append the content or just read from stdin.
    
    import sys
    content = sys.stdin.read()
    
    # Identify categories based on URLs in the content
    # I'll split the content by "URL: " markers
    parts = content.split('URL: ')
    all_products = []
    
    for part in parts[1:]:
        lines = part.split('\n', 1)
        url = lines[0].strip()
        text = lines[1] if len(lines) > 1 else ""
        
        category = "Unknown"
        if "electric-blanket" in url: category = "Electric Blankets"
        elif "portable-space-heater" in url: category = "Portable Space Heaters"
        elif "oil-filled-radiator" in url: category = "Oil-filled Radiators"
        elif "winter-bedding-set" in url: category = "Winter Bedding Sets"
        
        products = extract_products(text, category)
        all_products.extend(products)
    
    # Remove duplicates by URL
    unique_products = {p['url']: p for p in all_products}.values()
    
    # Save to file
    output_dir = 'tool-results'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, 'warmth_products.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(list(unique_products), f, indent=2, ensure_ascii=False)
    
    print(f"Extracted {len(unique_products)} products.")

if __name__ == "__main__":
    main()
