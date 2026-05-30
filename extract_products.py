import re
import sys
import json
import urllib.request

def fetch_and_extract(url, category):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        # Regex for product name, price, and link
        # This is a bit tricky with regex on HTML, but let's try some common patterns
        # <h2 class="search-card-e-title"><a ... href="//www.alibaba.com/product-detail/...">...</a></h2>
        # <div class="search-card-e-price-main">...</div>
        
        products = []
        # Find all product cards
        # Pattern: search-card-e-title
        titles = re.findall(r'class="[^"]*search-card-e-title[^"]*".*?href="([^"]+)".*?>(.*?)</a>', html, re.DOTALL)
        prices = re.findall(r'class="[^"]*search-card-e-price-main[^"]*".*?>(.*?)</div>', html, re.DOTALL)
        
        for i in range(min(len(titles), len(prices))):
            link, name = titles[i]
            price = prices[i]
            # Clean name and price
            name = re.sub('<[^<]+?>', '', name).strip()
            price = re.sub('<[^<]+?>', '', price).strip()
            if not link.startswith('http'):
                link = 'https:' + link
            products.append({
                'category': category,
                'name': name,
                'price': price,
                'link': link
            })
        return products
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

urls = [
    ("https://www.alibaba.com/showroom/men-thermal-underwear-sets.html", "Men Thermal Underwear"),
    ("https://www.alibaba.com/showroom/men-thermal-underwear-sets_2.html", "Men Thermal Underwear"),
    ("https://www.alibaba.com/showroom/womens-thermal-underwear-sets.html", "Women Thermal Underwear"),
    ("https://www.alibaba.com/showroom/womens-thermal-underwear-sets_2.html", "Women Thermal Underwear"),
    ("https://www.alibaba.com/showroom/fleece-lined-leggings.html", "Fleece-lined Leggings"),
    ("https://www.alibaba.com/showroom/fleece-lined-leggings_2.html", "Fleece-lined Leggings"),
    ("https://www.alibaba.com/showroom/wool-socks.html", "Wool Socks"),
    ("https://www.alibaba.com/showroom/wool-socks_2.html", "Wool Socks"),
    ("https://www.alibaba.com/showroom/winter-gloves.html", "Winter Gloves"),
    ("https://www.alibaba.com/showroom/winter-gloves_2.html", "Winter Gloves"),
]

all_products = []
for url, cat in urls:
    print(f"Fetching {url}...")
    prods = fetch_and_extract(url, cat)
    print(f"Found {len(prods)} products.")
    all_products.extend(prods)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, ensure_ascii=False, indent=2)

print(f"Total products: {len(all_products)}")
