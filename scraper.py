import asyncio
import aiohttp
import json
import re
from bs4 import BeautifulSoup
import time
import os

COOKIES = {
    'adminuserName': '004BC433F91D74B1D754FE20E05065DA',
    'NickName': '492926D63D1ADEAA01EDDCB754E96BC7',
    'mjid': '004BC433F91D74B1D754FE20E05065DA',
    'memberUserId': '38792',
    'admintrue': '1'
}

BASE_URL = "https://hdl.corereach.cn"
LIST_API = f"{BASE_URL}/ajax/getcp.ashx"
DETAIL_URL = f"{BASE_URL}/productqx.aspx?id="
OUTPUT_FILE = r"C:\Users\Administrator\Desktop\hdl_inventory.json"

async def fetch_list_page(session, page):
    params = {
        'page': page,
        'pageSize': 28,
        'classId': 0
    }
    try:
        async with session.get(LIST_API, params=params, cookies=COOKIES, timeout=10) as resp:
            return await resp.json(content_type=None)
    except Exception as e:
        print(f"Error fetching list page {page}: {e}")
        return None

async def fetch_detail_page(session, product_id):
    try:
        async with session.get(f"{DETAIL_URL}{product_id}", cookies=COOKIES, timeout=10) as resp:
            html = await resp.text()
            return product_id, html
    except Exception as e:
        print(f"Error fetching detail {product_id}: {e}")
        return product_id, None

def parse_detail(html, base_data):
    if not html:
        return base_data
    
    soup = BeautifulSoup(html, 'html.parser')
    data = base_data.copy()
    
    # Extract attributes based on common labels in the site
    # Looking at the screenshot, attributes are in spans or divs with labels
    text = soup.get_text()
    
    def extract(label):
        match = re.search(fr"{label}[:：]?\s*([^\n|\r|\s]+)", text)
        return match.group(1) if match else ""

    data['barcode'] = extract("条码")
    data['brand'] = extract("品牌")
    data['material'] = extract("材质")
    data['remarks'] = extract("备注")
    data['description'] = "" # Placeholder for long description if found
    
    # Try to find specific description block if exists
    # If no specific block, the attributes table is the description
    desc_node = soup.find('div', class_=re.compile('description|content|detail'))
    if desc_node:
        data['description'] = desc_node.decode_contents()

    return data

async def main():
    all_data = []
    async with aiohttp.ClientSession() as session:
        print("Starting list scrape...")
        # Get total pages first
        initial = await fetch_list_page(session, 1)
        if not initial:
            print("Failed to get initial page")
            return
        
        total_count = int(initial['TotalCount'])
        target_count = 30000
        pages_to_fetch = (target_count // 28) + 1
        print(f"Total available: {total_count}. Targeting {target_count} ({pages_to_fetch} pages).")

        product_list = []
        for p in range(1, pages_to_fetch + 1):
            data = await fetch_list_page(session, p)
            if data and 'data' in data:
                product_list.extend(data['data'])
            if len(product_list) >= target_count:
                break
            if p % 10 == 0:
                print(f"Fetched {len(product_list)} product stubs...")

        product_list = product_list[:target_count]
        print(f"Collected {len(product_list)} product IDs. Starting detail fetch...")

        # Batch detail fetch to avoid overwhelming server and hitting limits
        batch_size = 50
        for i in range(0, len(product_list), batch_size):
            batch = product_list[i:i+batch_size]
            tasks = [fetch_detail_page(session, item['id']) for item in batch]
            results = await asyncio.gather(*tasks)
            
            for (pid, html), item in zip(results, batch):
                full_item = parse_detail(html, item)
                all_data.append(full_item)
            
            print(f"Processed {len(all_data)} / {target_count}...")
            
            # Save progress every 500 items
            if len(all_data) % 500 == 0:
                with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                    json.dump(all_data, f, ensure_ascii=False, indent=2)

        # Final save
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        print(f"Scraping complete. Saved {len(all_data)} items to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
