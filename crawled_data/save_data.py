
import json
import os

delivery_path = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\crawled_data"
file_path = os.path.join(delivery_path, "products.json")

def save_products(products):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_products = json.load(f)
    else:
        existing_products = []
    
    existing_products.extend(products)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_products, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(products)} products. Total: {len(existing_products)}")

# Clear existing data
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump([], f)

# Clothes Drying Racks
drying_products = [
    {"prod_id": "1601691751440", "title": "Special Offer Multifunction Clothes Drying Rack X-shaped Adjustable Ba...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H6beb95e5cd6d47af96f9dfbd5b6fe8c88.png_640x640.png", "price": "$23", "moq": "1 bag", "category": "clothes drying racks"},
    {"prod_id": "1600838746456", "title": "Factory Supply Foldable Clothes Drying Rack Saves Space Portable Dryer...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H7e39eb6186ad4084aa4ce63d9adef4b3o.png_640x640.png", "price": "$25.96", "moq": "50 pieces", "category": "clothes drying racks"},
    {"prod_id": "62385895566", "title": "OEM Clothes drying rack Bamboo Wooden clothes rack heavy duty cloth dr...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/He8bfdb684424407c87759ed273eff4cdl.jpg_640x640.jpg", "price": "$8-9", "moq": "2000 units", "category": "clothes drying racks"},
    {"prod_id": "1601402857011", "title": "Clothes Drying Hanger Rack Space Saving Laundry Rack Clothes Drying Ra...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H777b577bb39b45efba6d58601bcf14949.jpg_640x640.jpg", "price": "$4.90-5.50", "moq": "200 sets", "category": "clothes drying racks"},
    {"prod_id": "1601712464725", "title": "Foldable Clothes Drying Rack Floor Standing Three Layers Multifunction...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H45e77f317748439db9b9ccefe71c4e76V.jpg_640x640.jpg", "price": "$5.45-5.80", "moq": "1 set", "category": "clothes drying racks"},
    {"prod_id": "1600093806189", "title": "Wholesale Hanging Cloth Drying Racks Garment Rack Clothes Living Room ...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H56aee2b25387450099715e5c46bb2b530.jpg_640x640.jpg", "price": "$4.30-5.90", "moq": "50 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601425212110", "title": "Portable Home Garment Drying Rack Practical Household Daily Use Clothe...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H0d51d3064a9e4f13969bb0e135714e54M.jpg_640x640.jpg", "price": "$6", "moq": "5 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600909319199", "title": "High Quality Clothes Drying Rack 3 Tier Foldable Laundry Drying Rack H...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hdd2278456d3d4e0faed4d9ae10505893j.jpg_640x640.jpg", "price": "$9.20", "moq": "100 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600548074687", "title": "Factory Outlet Drying Rack Stand Floor Type Clothes Airer Drying Rack ...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hb5f5a1d122cf4be69eabd0275be36364n.jpg_640x640.jpg", "price": "$6.99-12.79", "moq": "10 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601418396193", "title": "Brand New 8M 3 Tier Extendable Dry Hanger Clothes Rack Dryer Cloth Dry...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H8dfac070d93040aa8d37d23a7b33bbb9x.jpg_640x640.jpg", "price": "$6.03-6.49", "moq": "1220 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601018082129", "title": "Hot Sale Garment Racks Para Ropa Clothes Drying Rack Folding Clothing ...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H5e39b069fce441f6982d44ae27396152G.jpg_640x640.jpg", "price": "$8.90-12.90", "moq": "1000 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601025740069", "title": "SONGMICS Gullwing Laundry Drying Rack Clothes Dryer Stand Clothes Dryi...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H4826e152c037485a99452bdd276bc171G.jpg_640x640.jpg", "price": "$10.99-13.75", "moq": "200 sets", "category": "clothes drying racks"},
    {"prod_id": "1600934180126", "title": "Clothes Drying Rack 3 Tier Drying Laundry Racks With Coating Adjustabl...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H6056d6e874c94999a28a3f4611679a4cX.png_640x640.png", "price": "$7.99", "moq": "1000 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600655902976", "title": "New Space Saving Pole System Clothes Drying Rack Foldable Ceiling Stan...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H79ffd7c33a2a44aa96131150fdcf31925.jpg_640x640.jpg", "price": "$28.50", "moq": "1 set", "category": "clothes drying racks"},
    {"prod_id": "1601651188546", "title": "New Model Fashion Stainless Steel Clothes Drying Foldable Towel Rack I...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H1083c424f1c94c42b949c6b03bf58020C.jpg_640x640.jpg", "price": "$4.49-5.99", "moq": "1 piece", "category": "clothes drying racks"},
    {"prod_id": "1601567937294", "title": "Hot Sale Clothes Drying Rack Folding Multi-layer Tier Clothes Horses R...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hef634e05557f413c864d01dfc6d5a674X.png_640x640.png", "price": "$6.80", "moq": "2 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601651417896", "title": "JANKO Heavy Duty Clothes Drying Stand, Wire Airer Racks for Bulk Laund...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H601db4f336814251a3bdcce41681b759y.jpg_640x640.jpg", "price": "$5.25", "moq": "300 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601435301617", "title": "Best Sale Portable Dryer Folding Drying Clothes Balcony Adjustable Ind...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H7826fdb5e1ae4eada516be3c798b17d1X.jpg_640x640.jpg", "price": "$6.60-7", "moq": "600 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601041380425", "title": "Clothes Drying Rack, Foldable 2-Layer Stainless Steel Drying Rack, Fre...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hfe8dc38d66344673ba945ed3a16341d1y.jpg_640x640.jpg", "price": "$15", "moq": "500 sets", "category": "clothes drying racks"},
    {"prod_id": "1600444507534", "title": "Foldable Drying Rack Clothes Dry Line Rack Cloths Drying Racks Clothes", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hde9048158b8e475889dca7d758ddbcbbf.jpg_640x640.jpg", "price": "$5.35", "moq": "100 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600993585064", "title": "22M Multi-Function Clothes Drying Racks Extendable Fold Space-Saving A...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Heef659e53aae4d97a2ccb5d24b340845M.jpg_640x640.jpg", "price": "$11.50-11.80", "moq": "500 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601741965443", "title": "Foldable Family Clothes Drying Rack with Wheels Iron Metal Constructio...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H73493fe3f7cb4d1597ec1e9e86e8d027q.png_640x640.png", "price": "$4.99", "moq": "1 piece", "category": "clothes drying racks"},
    {"prod_id": "1601252752110", "title": "Heavy Duty 3 Tier Laundry Clothes Hanger Drying Racks Stand Indoor Bam...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hf1edc15c4d4340c4809c89773431526dO.jpg_640x640.jpg", "price": "$7.20-7.70", "moq": "200 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600890279100", "title": "2023 New Style China Factory 3 Layers Clothes Drying Rack Cloth Dryer ...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H583ff922719044daba068f2f9a2671402.jpg_640x640.jpg", "price": "$6.50", "moq": "50 pieces", "category": "clothes drying racks"},
    {"prod_id": "11000010967517", "title": "Extendable Clothes Drying Rack Multifunction Drying Balcony Rack Heavy...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/A9b4438d5bac643499d09815667872b3f8.jpg_640x640.jpg", "price": "$18.90-34.80", "moq": "50 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600861800091", "title": "Promotion High Quality Foldable Cloth Drying Clothing Rack Drying Rack...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/He41e2a3b7f8f4f68ba794ee8c9cfb891P.jpg_640x640.jpg", "price": "$5.45-5.85", "moq": "96 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600844857198", "title": "Wholesale Hot Sale Metal Clothes Dryer Rack Heavy Duty Laundry Airer C...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H8493fa2cb405451c9732b1ffadd962b0E.jpg_640x640.jpg", "price": "$5.68", "moq": "200 pieces", "category": "clothes drying racks"},
    {"prod_id": "1600250523638", "title": "Collapsible Clothes Drying Rack Cloth Dryer Hanger Stand Folding Laund...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H5acf701904d94698b54353bd3ceda318w.jpg_640x640.jpg", "price": "$5.50", "moq": "100 pieces", "category": "clothes drying racks"},
    {"prod_id": "1601379043256", "title": "Wall Mounted Foldable Clothes Drying Rack with 7 Wood Arms Space Savin...", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H6bc687f7c7444f4aa6814ebf211d3a47H.jpg_640x640.jpg", "price": "$23", "moq": "2 pieces", "category": "clothes drying racks"},
    {"prod_id": "60033066374", "title": "3 Tier Standing Collapsible Clothes Drying Rack", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hda15523e24e541568d93397571e1e9f4c.jpg_640x640.jpg", "price": "$4.87-6.56", "moq": "1000 pieces", "category": "clothes drying racks"}
]
save_products(drying_products)


save_products(vacuum_products)
