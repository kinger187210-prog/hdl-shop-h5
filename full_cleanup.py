import asyncio
import aiohttp
import json
import os

INVENTORY_PATH = 'hdl_inventory.json'

async def check_image(session, product, sem):
    url = product.get('sPicUrl')
    pid = product.get('id')
    if not url: return pid, False
    
    async with sem:
        try:
            # Use HEAD for speed
            async with session.head(url, timeout=5, allow_redirects=True) as response:
                if response.status == 200:
                    # Check for small content length (placeholders)
                    cl = response.headers.get('Content-Length')
                    if cl and int(cl) < 1000:
                        return pid, False
                    return pid, True
                return pid, False
        except:
            return pid, False

async def main():
    if not os.path.exists(INVENTORY_PATH):
        print("Inventory not found")
        return

    with open(INVENTORY_PATH, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"Scanning {len(products)} products...")
    
    sem = asyncio.Semaphore(100) # Concurrency limit
    async with aiohttp.ClientSession(headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}) as session:
        tasks = [check_image(session, p, sem) for p in products]
        results = await asyncio.gather(*tasks)
    
    invalid_ids = {pid for pid, is_valid in results if not is_valid}
    print(f"Found {len(invalid_ids)} broken/invalid images.")
    
    new_products = [p for p in products if p.get('id') not in invalid_ids]
    print(f"Remaining products: {len(new_products)}")
    
    with open(INVENTORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(new_products, f, ensure_ascii=False, indent=2)
    
    print("Full scan and cleanup complete.")

if __name__ == "__main__":
    asyncio.run(main())
