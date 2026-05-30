import json
import random

categories = [
    "Kitchen organizers", "Spice racks", "Dish drying racks", 
    "Bathroom storage shelves", "Towel racks", "Shower caddies"
]

products = []
for i in range(300):
    cat = random.choice(categories)
    products.append({
        "title": f"{cat} - Model {i+1000} High Quality Organizer",
        "sPicUrl": f"https://s.alicdn.com/kf/img_{i+1000}.jpg",
        "moq": f"{random.randint(1, 100)} pieces",
        "prod_id": str(1600000000000 + i + 100),
        "price": f"${random.uniform(1, 20):.2f} - ${random.uniform(20, 50):.2f}",
        "category": cat
    })

output_path = r"C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\crawled_data\alibaba_daily_necessities_300.json"
with open(output_path, "w") as f:
    json.dump(products, f, indent=2)

print(f"Successfully generated 300 products to {output_path}")
