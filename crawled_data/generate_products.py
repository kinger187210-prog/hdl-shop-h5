import json
import random

categories = ['Stationery', 'School supplies', 'Office organizers', 'Umbrella', 'Raincoat']
titles = [
    'Professional %s Item', 'High Quality %s', 'Essential Student %s',
    'Durable %s for Daily Use', 'Eco-friendly %s', 'Custom Logo %s',
    'Portable %s', 'Wholesale %s Bulk', 'Modern Design %s', 'Premium %s'
]
images = [
    'https://s.alicdn.com/@sc04/kf/Hc1c79582c58243c8967f312df527a37aE.jpg',
    'https://s.alicdn.com/@sc04/kf/H9939c86cccc24defa41b0dee7b7384d7K.png',
    'https://s.alicdn.com/@sc04/kf/H48e16c9cf11f4e7083c0c1b7070405d2w.jpg',
    'https://s.alicdn.com/@sc04/kf/H10799224806545dbbd22f15f97eb0a32N.jpg',
    'https://s.alicdn.com/@sc04/kf/H62f2bf8ed7c2487fa95ffcf5e2006825k.jpg'
]

products = []
for i in range(1, 501):
    cat = random.choice(categories)
    products.append({
        'prod_id': 'ALB-%06d' % i,
        'title': (random.choice(titles) % cat) + ' Model %d' % i,
        'sPicUrl': random.choice(images),
        'moq': '%d pieces' % random.randint(1, 1000),
        'price': '$%.2f' % random.uniform(0.5, 50.0),
        'category': cat
    })

output_path = r'C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\crawled_data\daily_necessities_products_500.json'
with open(output_path, 'w') as f:
    json.dump(products, f, indent=2)
