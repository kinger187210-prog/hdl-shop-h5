import json
import re

data_str = """
[PASTE_DATA_HERE]
"""

products = []
seen_ids = set()

# Pattern to match table rows
# | 1 | 1601490294971 | Tuya HD Smart Home WiFi Indoor Camera ... | https://... | $9.99-12.99 / 2 pieces | ...
row_pattern = re.compile(r"\| (\d+) \| (\d+) \| (.*?) \| (.*?) \| (.*?) \|")

# Mapping queries to categories
# Since I'll process strings one by one, I'll handle category assignment manually or by sections.

def parse_section(section_text, category):
    count = 0
    for match in row_pattern.finditer(section_text):
        _, prod_id, title, pic_url, price_moq = match.groups()
        if prod_id in seen_ids:
            continue
        
        # Parse Price and MOQ
        if " / " in price_moq:
            price, moq = price_moq.split(" / ", 1)
        else:
            price = price_moq
            moq = "1 piece"
        
        products.append({
            "title": title.strip(),
            "sPicUrl": pic_url.strip(),
            "moq": moq.strip(),
            "prod_id": int(prod_id),
            "price": price.strip(),
            "category": category
        })
        seen_ids.add(prod_id)
        count += 1
        if len(products) >= 200:
            return True
    return False

# Sections and their categories
# (I will populate these in the next step)
