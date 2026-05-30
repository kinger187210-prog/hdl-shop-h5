import json
all_products = []
all_products.extend([
    {"title": f"Car Air Freshener Model {i}", "sPicUrl": f"https://s.alicdn.com/img/air_{i}.jpg", "moq": f"{i%5+1} pcs", "prod_id": f"AF{1000+i}", "price": f"${0.5+i*0.1:.2f}", "category": "Car air fresheners"} for i in range(1, 101)
])
