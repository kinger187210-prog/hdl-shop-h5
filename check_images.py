import json

def main():
    with open('dist/hdl_inventory.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cats = ["冬季保暖", "电子周边", "五金工具", "车载用品", "日百", "户外露营", "家居装饰", "厨房厨具", "母婴玩具", "宠物用品"]
    results = {}
    for cat in cats:
        for p in data:
            if p.get('category') == cat:
                results[cat] = p['sPicUrl']
                break
    
    for cat, url in results.items():
        print(f"{cat}: {url}")

if __name__ == "__main__":
    main()
