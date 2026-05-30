import re
import json
import os

# I will use the products I've seen in the previous fetch results.
# Since I cannot easily read the context back, I'll use a regex that I know works on the format.

def extract_from_text(text, category):
    # Pattern for Alibaba product links in the fetch output
    # [**Title**](URL)
    pattern = r'\[\*\*(.*?)\*\*\]\((https://www\.alibaba\.com/product-detail/.*?)\)'
    matches = re.findall(pattern, text)
    products = []
    for title, url in matches:
        # Clean title
        title = title.replace('**', '').strip()
        products.append({
            "category": category,
            "title": title,
            "url": url,
            "price": "See website",
            "moq": "See website"
        })
    return products

# I will provide a sample of the text here or just simulate the extraction 
# if I can't pass the whole thing.
# Actually, I'll write the script to read from 'fetch_results.txt'.

def main():
    all_products = []
    
    # I'll simulate having the text by providing the logic to read it if it existed.
    # But since I can't easily put 300 products worth of text in one 'write' call,
    # I'll use the 'bash' tool to append the fetch results to a file and then run this.
    
    if os.path.exists('fetch_results.txt'):
        with open('fetch_results.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split by URL markers
        parts = content.split('URL: ')
        for part in parts[1:]:
            lines = part.split('\n', 1)
            url = lines[0].strip()
            text = lines[1] if len(lines) > 1 else ""
            
            category = "General"
            if "electric-blanket" in url: category = "Electric Blankets"
            elif "portable-space-heater" in url: category = "Portable Space Heaters"
            elif "oil-filled-radiator" in url: category = "Oil-filled Radiators"
            elif "winter-bedding-set" in url: category = "Winter Bedding Sets"
            
            all_products.extend(extract_from_text(text, category))

    # De-duplicate
    unique_products = {p['url']: p for p in all_products}.values()
    unique_products = list(unique_products)
    
    # If we still don't have 300 (due to truncation or whatever), I'll add more.
    # But let's see how many we got.
    
    output_path = 'tool-results/warmth_products.json'
    if not os.path.exists('tool-results'):
        os.makedirs('tool-results')
        
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(unique_products, f, indent=2, ensure_ascii=False)
    
    print(f"Total products extracted: {len(unique_products)}")

if __name__ == "__main__":
    main()
