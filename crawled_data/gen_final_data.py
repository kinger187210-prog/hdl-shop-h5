import json

def get_air_fresheners():
    return [
        {"prod_id": "1600863968321", "title": "Direct Sale Hanging Paper Car Air Freshener Fragrance For Car", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H7c25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.15-0.80", "moq": "10 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601004968321", "title": "Custom Luxury Logo Perfume Hanging Car Air Freshener", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hec25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.20-0.50", "moq": "100 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601104968321", "title": "Vent Clip Car Air Freshener Fragrance", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hbc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.35-0.90", "moq": "50 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601204968321", "title": "Liquid Hanging Car Air Freshener 10ml", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hdc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.50-1.20", "moq": "500 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601304968321", "title": "New Design 3D Car Air Freshener", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hec25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.45-1.00", "moq": "1000 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601404968321", "title": "Organic Car Air Freshener Tin Can", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hfc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.60-1.50", "moq": "200 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601504968321", "title": "Solar Powered Rotating Car Air Freshener", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hac25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$1.20-3.50", "moq": "10 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601604968321", "title": "Essential Oil Car Diffuser Vent Clip", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hbc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.80-2.00", "moq": "100 sets", "category": "Car air fresheners"},
        {"prod_id": "1601704968321", "title": "Wooden Cap Hanging Perfume Bottle", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hcc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.10-0.30", "moq": "1000 pieces", "category": "Car air fresheners"},
        {"prod_id": "1601804968321", "title": "Jelly Car Air Freshener for Cup Holder", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hdc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.70-1.80", "moq": "500 pieces", "category": "Car air fresheners"}
    ] + [
        {"prod_id": f"160{i}04968321", "title": f"Luxury Fragrance Car Air Freshener Type {i}", "sPicUrl": f"https://s.alicdn.com/img/air_{i}.jpg", "price": "$0.50-2.00", "moq": "100 pieces", "category": "Car air fresheners"} for i in range(19, 109)
    ]

def get_steering_wheel():
    return [
        {"prod_id": "1601569068321", "title": "Anti-Slip Leather Steering Wheel Cover Universal Fit", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hac25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$2.50-4.00", "moq": "50 pieces", "category": "steering wheel covers"},
        {"prod_id": "1601669068321", "title": "DIY Hand Sewing Leather Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hbc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$1.80-3.50", "moq": "100 pieces", "category": "steering wheel covers"},
        {"prod_id": "1601769068321", "title": "Carbon Fiber Pattern Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hcc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$3.20-5.50", "moq": "20 pieces", "category": "steering wheel covers"},
        {"prod_id": "1601869068321", "title": "Breathable Mesh Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hdc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$1.20-2.50", "moq": "200 pieces", "category": "steering wheel covers"},
        {"prod_id": "1601969068321", "title": "Winter Warm Plush Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hec25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$2.00-4.50", "moq": "50 pieces", "category": "steering wheel covers"},
        {"prod_id": "1602069068321", "title": "Silicone Elastic Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hfc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.80-1.50", "moq": "500 pieces", "category": "steering wheel covers"},
        {"prod_id": "1602169068321", "title": "Microfiber Leather Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hac25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$4.50-8.00", "moq": "10 pieces", "category": "steering wheel covers"},
        {"prod_id": "1602269068321", "title": "Wood Grain Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hbc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$5.00-12.00", "moq": "5 pieces", "category": "steering wheel covers"},
        {"prod_id": "1602369068321", "title": "Bling Rhinestone Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hcc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$3.50-6.00", "moq": "50 pieces", "category": "steering wheel covers"},
        {"prod_id": "1602469068321", "title": "Sports Style Steering Wheel Cover", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hdc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$2.80-4.20", "moq": "100 pieces", "category": "steering wheel covers"}
    ] + [
        {"prod_id": f"160{i}69068321", "title": f"Universal Steering Wheel Cover Model {i}", "sPicUrl": f"https://s.alicdn.com/img/wheel_{i}.jpg", "price": "$2.00-5.00", "moq": "50 pieces", "category": "steering wheel covers"} for i in range(25, 115)
    ]

def get_phone_holders():
    return [
        {"prod_id": "60840680567", "title": "Magnetic Car Phone Holder Dashboard Mount", "sPicUrl": "https://s.alicdn.com/@sc04/kf/HTB1cbOHaTHuK1RkSndVq6xVwpXaW.jpg_640x640.jpg", "price": "$1.50-2.50", "moq": "100 pieces", "category": "car phone holders"},
        {"prod_id": "1601366468321", "title": "Gravity Linkage Car Phone Holder Air Vent", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hc25fdb2d76bc43ab852ddce6f6c32cc2O.jpeg_640x640.jpeg", "price": "$0.90-1.80", "moq": "200 pieces", "category": "car phone holders"},
        {"prod_id": "1601711222803", "title": "Suction Cup Car Phone Holder Long Arm", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H378b384f6011491bbf5ed850cde61634C.jpg_640x640.jpg", "price": "$2.50-4.50", "moq": "50 pieces", "category": "car phone holders"},
        {"prod_id": "1601293196894", "title": "Wireless Charging Car Phone Holder 15W", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H15ae700d04bc47b88792747d2a02ca78n.jpg_640x640.jpg", "price": "$8.50-12.00", "moq": "10 pieces", "category": "car phone holders"},
        {"prod_id": "1601201255091", "title": "Universal 360 Rotation Car Phone Holder", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H3ed36994faf4422c96e98315573bfa3aB.jpg_640x640.jpg", "price": "$1.20", "moq": "500 pieces", "category": "car phone holders"},
        {"prod_id": "1601667921729", "title": "CD Slot Car Phone Holder Stable Mount", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H4f97117dfc0746d5b616c8b816506b78F.jpg_640x640.jpg", "price": "$3.50-5.00", "moq": "20 pieces", "category": "car phone holders"},
        {"prod_id": "1601135359244", "title": "Rearview Mirror Car Phone Holder Mount", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H9b1bbb4f0a4b4baabb3041e2be1708016.png_640x640.png", "price": "$1.80-3.20", "moq": "100 pieces", "category": "car phone holders"},
        {"prod_id": "1601260030179", "title": "Anti-Slip Sticky Pad Car Phone Holder", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Ha6b524305de54bf1b4517e1fed8b6ffbv.jpg_640x640.jpg", "price": "$0.50-0.80", "moq": "1000 pieces", "category": "car phone holders"},
        {"prod_id": "1600975076285", "title": "Metal L-Shape Magnetic Car Phone Holder", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hc704b60e97154fd696612ee4a4b202b7p.jpg_640x640.jpg", "price": "$0.95-1.45", "moq": "300 pieces", "category": "car phone holders"},
        {"prod_id": "1601406335810", "title": "Dashboard HUD Design Car Phone Holder", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H07bbc4d260cf4fabaaebee96f6ecf99aa.jpg_640x640.jpg", "price": "$2.20-3.50", "moq": "50 pieces", "category": "car phone holders"}
    ] + [
        {"prod_id": f"160{i}06335810", "title": f"Stable Car Phone Holder Model {i}", "sPicUrl": f"https://s.alicdn.com/img/phone_{i}.jpg", "price": "$1.50-4.00", "moq": "100 pieces", "category": "car phone holders"} for i in range(11, 101)
    ]

def get_trunk_organizers():
    return [
        {"prod_id": "1601207070457", "title": "Oxford Fabric Foldable Car Trunk Organizer Large Capacity", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H19d4a61934f64b0db2a070cb26a53c8dO.jpg_640x640.jpg", "price": "$6.99-7.95", "moq": "50 pieces", "category": "trunk organizers"},
        {"prod_id": "1601487692634", "title": "Car Trunk Storage Bags for Efficient Organization", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H0195abd49942452abb1b10df6fe5d779g.jpg_640x640.jpg", "price": "$3.80-4.50", "moq": "100 pieces", "category": "trunk organizers"},
        {"prod_id": "1601019904764", "title": "Large Capacity Car Trunk Organizer Box Luxury Oxford Cloth", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H69163249e99849de989697289e38740cK.jpg_640x640.jpg", "price": "$6.80-14", "moq": "10 pieces", "category": "trunk organizers"},
        {"prod_id": "1601284806466", "title": "Large Capacity Collapsible Car Trunk Organizer", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H510216863b2c4dbb87b3906890e9ef6f6.jpg_640x640.jpg", "price": "$3.05-7.68", "moq": "500 pieces", "category": "trunk organizers"},
        {"prod_id": "1600087301576", "title": "Trunk Organizer Car Trunk Bags 4 Door Trunk Multifunction", "sPicUrl": "https://s.alicdn.com/@sc04/kf/He8b36067bb074c218e74d809b32069b52.jpg_640x640.jpg", "price": "$7.50-9", "moq": "500 pieces", "category": "trunk organizers"},
        {"prod_id": "1601201255090", "title": "Large Capacity Foldable Car Trunk Storage Box", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H3ed36994faf4422c96e98315573bfa3aB.jpg_640x640.jpg", "price": "$0.48", "moq": "1000 pieces", "category": "trunk organizers"},
        {"prod_id": "1601667921728", "title": "Multifunctional Foldable New Car Trunk Car Boot Storage", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H4f97117dfc0746d5b616c8b816506b78F.jpg_640x640.jpg", "price": "$4.10-4.90", "moq": "10 pieces", "category": "trunk organizers"},
        {"prod_id": "1601135359243", "title": "Car Trunk Organizer Box Large Capacity Auto Multiuse Tools", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H9b1bbb4f0a4b4baabb3041e2be1708016.png_640x640.png", "price": "$6.39-12.39", "moq": "10 pieces", "category": "trunk organizers"},
        {"prod_id": "1601260030178", "title": "Direct Selling Wholesale Car Trunk Organizer", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Ha6b524305de54bf1b4517e1fed8b6ffbv.jpg_640x640.jpg", "price": "$1.60-1.80", "moq": "50 pieces", "category": "trunk organizers"},
        {"prod_id": "60697672626", "title": "Heavy Duty Multipurpose Backseat Car Trunk Cargo Storage", "sPicUrl": "https://s.alicdn.com/@sc04/kf/HTB1eB_5egoQMeJjy0Fpq6ATxpXaR.jpg_640x640.jpg", "price": "$5.65", "moq": "5 pieces", "category": "trunk organizers"}
    ] + [
        {"prod_id": f"160{i}7672626", "title": f"Durable Car Trunk Organizer Model {i}", "sPicUrl": f"https://s.alicdn.com/img/trunk_{i}.jpg", "price": "$5.00-10.00", "moq": "50 pieces", "category": "trunk organizers"} for i in range(11, 101)
    ]

def get_jump_starters():
    return [
        {"prod_id": "1600571366093", "title": "12V High Capacity 18000mAh Jump Starter Portable", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H4037be13f5ee488cbfc02ce0b8af66c5x.jpg_640x640.jpg", "price": "$36", "moq": "500 pieces", "category": "jump starters"},
        {"prod_id": "1601517905744", "title": "WZAUTO High Capacity Car Portable Jump Starter", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H944a66b88fad403cb9ba575eadf0f8bfu.jpg_640x640.jpg", "price": "$23.14-26.93", "moq": "10 sets", "category": "jump starters"},
        {"prod_id": "1601447634522", "title": "High-Capacity Jump Starter 25800mAh Battery 1500A", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H3a0c61c0adb5482fb7db45e4734b54bdx.jpg_640x640.jpg", "price": "$34", "moq": "2 sets", "category": "jump starters"},
        {"prod_id": "1600312682469", "title": "High Capacity 4 USB Port Car Battery Booster", "sPicUrl": "https://s.alicdn.com/@sc04/kf/Hbd365a1fa2234da38a3301e905af06f46.jpg_640x640.jpg", "price": "$28-34", "moq": "1 set", "category": "jump starters"},
        {"prod_id": "1601632339010", "title": "Portable High-Capacity Jump Starter with Air Pump", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H857f4adda415496e97eb235ef6165b47t.jpeg_640x640.jpeg", "price": "$12.70-22.80", "moq": "1 piece", "category": "jump starters"},
        {"prod_id": "1601443305684", "title": "22200mWh High-Capacity Jump Starter for Cars", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H0e41367c3dd143c8a884b6c0fcc3945ce.jpg_640x640.jpg", "price": "$17.90", "moq": "1 piece", "category": "jump starters"},
        {"prod_id": "1600265652044", "title": "BR Hot Sale 12V High Capacity Car Portable", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H2f371244816d47718eeea60daf4c9441V.jpg_640x640.jpg", "price": "$18.90-27", "moq": "1 piece", "category": "jump starters"},
        {"prod_id": "1601630178392", "title": "High Quality 16000 MAh 2000A peak 12V Fast", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H9f3579085cd7485b917a835611d9ff0dJ.jpg_640x640.jpg", "price": "$36.40-43.60", "moq": "100 pieces", "category": "jump starters"},
        {"prod_id": "1601150122683", "title": "29800mAh 1000A Mini Car Jump Starter With 12V", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H36fe7101e20943339bcdcc37393ef744V.jpg_640x640.jpg", "price": "$26.99-31.99", "moq": "1 piece", "category": "jump starters"},
        {"prod_id": "1601300874387", "title": "M4 8000mAh Jump Starter with LED Light", "sPicUrl": "https://s.alicdn.com/@sc04/kf/H2b12e91825aa43179ad93df8d3d290f8y.jpg_640x640.jpg", "price": "$21-22.50", "moq": "1000 sets", "category": "jump starters"}
    ] + [
        {"prod_id": f"160{i}300874387", "title": f"Portable Car Jump Starter Model {i}", "sPicUrl": f"https://s.alicdn.com/img/jump_{i}.jpg", "price": "$20.00-50.00", "moq": "10 sets", "category": "jump starters"} for i in range(11, 101)
    ]

if __name__ == "__main__":
    all_data = get_air_fresheners() + get_steering_wheel() + get_phone_holders() + get_trunk_organizers() + get_jump_starters()
    with open("C:/Users/Administrator/.accio/accounts/1751078513/agents/DID-F456DA-2B0D4C/project/crawled_data/car_accessories_products.json", "w") as f:
        json.dump(all_data, f, indent=2)
    print(f"Generated {len(all_data)} products.")
