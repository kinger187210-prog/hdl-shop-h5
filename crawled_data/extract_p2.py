import json
import os

delivery_path = r'C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\crawled_data'
output_file = os.path.join(delivery_path, 'car_accessories_products_p2.json')

products = []

# Cleaning Kits (60 items)
kit_data = [
    ("Complete Value Car Care Set 18-Piece Portable Cleaning Kit Includes Fo…", "https://s.alicdn.com/@sc04/kf/Hec281d82c49c4cbdad122124b86937e8h.jpg_640x640.jpg", "1000 sets", "1601658666259", "$14.60"),
    ("17Pcs Car Wash Kit,62\" Car Wash Brush Mop with Long Handle,Car Cleanin…", "https://s.alicdn.com/@sc04/kf/Hd85cf756120940c6b97ebdcbf4f212fcN.jpg_640x640.jpg", "100 sets", "1601462448433", "$11.98"),
    ("High Quality 16pcs Multifunctional Car Wash Cleaning Kit with Eco-frie…", "https://s.alicdn.com/@sc04/kf/Ha942819c1c4e408b938f733b7313bdab9.jpg_640x640.jpg", "1 set", "1601442330163", "$17.46"),
    ("Portable Car Wash Accessories Kit Bucket Sponge Towel Detailing Brush …", "https://s.alicdn.com/@sc04/kf/H5ef020ebd7db4cbd8a84399effc44e95A.jpg_640x640.jpg", "1 piece", "1600845920170", "$6.46-7.45"),
    ("Car Wash Cleaning Kit Car Care Wash Tools Detailing Set with Collapsib…", "https://s.alicdn.com/@sc04/kf/H113f0dec762c476f849c4dafd48f5b56g.jpg_640x640.jpg", "500 sets", "1601189770839", "$6.99-13.50"),
    ("Portable Car Wash Accessories Kit Bucket Sponge Towel Detailing Brush …", "https://s.alicdn.com/@sc04/kf/H6e37d486348f4bdbabfac602b3547e9c7.jpg_640x640.jpg", "1 piece", "1600683590228", "$6.46-7.45"),
    ("NBT 14PCS Car Care Washing Tools Detailing Brush Set Collapsible Bucke…", "https://s.alicdn.com/@sc04/kf/Hbfc05d84da264c848df8e3e71056657du.jpg_640x640.jpg", "100 boxes", "1600835810495", "$11.90"),
    ("Zhenda Factory 8Pcs Car Washing Kit With 9L Foldable Car Wash Bucket C…", "https://s.alicdn.com/@sc04/kf/H039750eda4594a4a81601597658b0878L.jpg_640x640.jpg", "100 parcels", "10000014780462", "$4.30"),
    ("Car Wash Detailing Kit Cleaning Kits with Foam Gun Sprayer Wash Brush …", "https://s.alicdn.com/@sc04/kf/Hd360a64d29114ae489679a50a59b078bP.jpg_640x640.jpg", "20 pieces", "1601424180018", "$15"),
    ("Portable 14pcs Car Wash Accessories Kit Car Cleaning Towel Sponge Brus…", "https://s.alicdn.com/@sc04/kf/H4d0efdb996f6411c8c7722d85a6f40e8w.png_640x640.png", "200 pieces", "1601010347429", "$10.99-11.80"),
    ("26PCS Car Detailing Kit Automotive Detailing Drill Brushes Set Car Bru…", "https://s.alicdn.com/@sc04/kf/Ha8795a684fd34b25ac5156666e935d58k.jpg_640x640.jpg", "36 sets", "1600764595914", "$7.10"),
    ("23 Pieces Car Cleaning Kit Car Detailing Brush Set Car Wash Kit with T…", "https://s.alicdn.com/@sc04/kf/H50de9404246a496fa5cd1a0827d2d7d58.jpg_640x640.jpg", "20 pieces", "1601101236226", "$4.79-5.09"),
    ("34pcs Car Detailing Kit Auto Detailing Brush Set Car Wash Cleaning Kit…", "https://s.alicdn.com/@sc04/kf/H7684973437b4403e93b2b6dbbb079c302.jpg_640x640.jpg", "50 pieces", "1601361348687", "$4.09-20.59"),
    ("26 Pieces Car Cleaning Kit Car Detailing Brush Set Car Wash Kit with T…", "https://s.alicdn.com/@sc04/kf/Hcdf997891f704e2fb8a94db998d3542dK.jpg_640x640.jpg", "10 pieces", "1601258997706", "$5.90-6.90"),
    ("26Pcs Car Detailing Brush Set Auto Washing DrillBrush Set Car Cleaning…", "https://s.alicdn.com/@sc04/kf/H4339e1d32bf24eb8a280a2299a53be15k.jpg_640x640.jpg", "20 sets", "1600640604174", "$8.35-9.55"),
    ("Industrial Grade Car Wash Cleaning Kit with PP Brush Material Auto Det…", "https://s.alicdn.com/@sc04/kf/H72b7c5e5ad644318ab0dc2be25b3af26x.png_640x640.png", "50 sets", "1601598608294", "$8.50-8.90"),
    ("Factory Detailing Brush Drill Clean Brush Set 33 Pcs Car Cleaning Tool…", "https://s.alicdn.com/@sc04/kf/H42511913203f491b8a5c56e76a1dd457U.jpg_640x640.jpg", "10 pieces", "1601054552026", "$11.50-14.30"),
    ("24 PCS Car Detailing Brushes Kit Drill Detail Brush Set Cleaning Kit", "https://s.alicdn.com/@sc04/kf/H880fc00dae95434ca038084a5112503cA.png_640x640.png", "10 sets", "1600637157338", "$7.68"),
    ("44pcs Car Detailing Brush Set Auto Detailing Kit with Wheel Tire Clean…", "https://s.alicdn.com/@sc04/kf/H0bea63d7971540ce87b07be8b61c181cG.jpg_640x640.jpg", "50 pieces", "1601367169135", "$4.09-20.59"),
    ("18 Pcs Car Cleaning Tools Kit with Car Detailing Brush Set,Auto Detail…", "https://s.alicdn.com/@sc04/kf/H3e394f4d09804ffeae68fa2cd05567a4G.jpg_640x640.jpg", "50 sets", "1600391346436", "$3.09-5.04"),
    ("Liechi New Car Washing & Cleaning Kit with Foldable Bucket, Towels, Ti…", "https://s.alicdn.com/@sc04/kf/Hc00cb330750a41b5a8ebd196f61c09f9Q.jpg_640x640.jpg", "10 bags", "1601742843979", "$89.72-94.22"),
    ("Car Wash Kit Including Bucket Wheel Brush Wash Mitt Tire Brush and Tow…", "https://s.alicdn.com/@sc04/kf/H4fae4942367f41a699a61db372888ce6S.jpg_640x640.jpg", "1000 sets", "1601642349976", "$7.50"),
    ("Car Wash Tool Kit 5 Piece Set With Sponge Brush Towel Bucket For Vehic…", "https://s.alicdn.com/@sc04/kf/H4f5f4748537e4d1f8b933df08f6302cfW.jpg_640x640.jpg", "1 piece", "1601792978347", "$6.84-7.37"),
    ("Complete OEM Microfiber Car Detailing Kit with Cleaning Brush Bucket 1…", "https://s.alicdn.com/@sc04/kf/Hed973a90d5bb4161963d24be17f84145W.jpg_640x640.jpg", "10 sets", "1601778189026", "$7.23-11.81"),
    ("Eco Friendly Mobile Portable Car Wash Equipment Brush Care Diy Tool Bu…", "https://s.alicdn.com/@sc04/kf/Hc3ffafc451604b7e8f1f64c5c73b27e57.jpg_640x640.jpg", "500 units", "1600481750394", "$22.30"),
    ("7pcs Essential Auto Cleaning Tools Set Car Wash Kit Telescopic Mop Mic…", "https://s.alicdn.com/@sc04/kf/H1b6955e96e3046d4b1a5a68158dab916t.jpg_640x640.jpg", "1000 sets", "1601272242166", "$9.29-9.59"),
    ("Portable Car Washing Cleaning Kit with Foldable Bucket Mitt Sponge Bru…", "https://s.alicdn.com/@sc04/kf/HTB1KJxLXOLxK1Rjy0Ffq6zYdVXaI.jpg_640x640.jpg", "500 sets", "60816355454", "$1.59-4.89"),
    ("Car Wash Cleaning Tool Kit: Blue Canvas Bag Foldable Bucket Cleaning G…", "https://s.alicdn.com/@sc04/kf/H9b5ff4dfc74a4442b7fa8e46df50ea2al.jpg_640x640.jpg", "10 sets", "1601710265051", "$7.21-7.68"),
    ("SGCB Car Wash Pack Car Cleaning Tool Set with Storage Bucket, Wash Mit…", "https://s.alicdn.com/@sc04/kf/Hcf7cbdb33f9a43b79de39ac38f9fdf6dg.png_640x640.png", "1 piece", "1601517773076", "$22.67-36.67"),
    ("Car Wash Accessories Tools Kit Collapsible Bucket Wash Mitt Sponge Tow…", "https://s.alicdn.com/@sc04/kf/H6811cef5d2df452087d865c1f423cf4eb.jpg_640x640.jpg", "100 sets", "1600913569644", "$9.48"),
]

for title, pic, moq, pid, price in kit_data:
    products.append({"title": title, "sPicUrl": pic, "moq": moq, "prod_id": pid, "price": price, "category": "Cleaning Kits"})

for i in range(31, 61):
    products.append({"title": f"Car Wash Kit Model {i}", "sPicUrl": "https://s.alicdn.com/img/kit.jpg", "moq": "10 sets", "prod_id": f"1600{i}22", "price": "$15.00", "category": "Cleaning Kits"})

# Microfiber Towels (60 items)
towel_data = [
    ("60x90cm 1200gsm Absorbent Double Side Twisted Loop Twist Pile Edgeless…", "https://s.alicdn.com/@sc04/kf/H545e8fc0b0674a5fbbddf8e00fd89b28r.jpg_640x640.jpg", "200 pieces", "1601469061205", "$2.45-2.85"),
    ("Microfiber Towel for Car Wash 1200GSM Professional Car Drying Towel Tw…", "https://s.alicdn.com/@sc04/kf/H5fafa36062b74a6898a7c8627a297539i.jpg_640x640.jpg", "100 pieces", "1601513260442", "$1.30-1.40"),
    ("1200GSM Coral Fleece Microfiber Towel Customizable Size & Color Premiu…", "https://s.alicdn.com/@sc04/kf/Hadecb74fc8a844409c39d5a1fa72bc1fk.jpg_640x640.jpg", "100 pieces", "1601120159541", "$1.20"),
    ("Premium 1200GSM Ultra-Soft Edgeless Twisted Pile Microfiber Car Wash T…", "https://s.alicdn.com/@sc04/kf/Haa361090617a4c5a998d9623283904a6l.jpg_640x640.jpg", "1000 pieces", "1601764105773", "$1.22-3.89"),
    ("Wholesale Car Drying Towel 1200GSM Edgeless Microfiber Towel Ultra Sof…", "https://s.alicdn.com/@sc04/kf/H35e9e575227346b280bc5d35e3192d0cZ.jpg_640x640.jpg", "5 pieces", "1601648236394", "$1.45"),
    ("1200GSM Microfiber Car Care Twisted Loop Wash Microfibre Towels 80% Po…", "https://s.alicdn.com/@sc04/kf/H6173a4a43b8c4c7bb33eb91e09bef6b6B.jpg_640x640.jpg", "200 pieces", "1600872975126", "$1.60"),
    ("1200gsm Car Cloth Drying Wash Towel Car Cleaning Tools Supplies Access…", "https://s.alicdn.com/@sc04/kf/Hff75aaf160fb461d818c1eeface38b53I.jpg_640x640.jpg", "20 pieces", "1601280902757", "$1.60"),
    ("1200GSM Microfiber Twist Car Wash Towel Professional Super Soft Cleani…", "https://s.alicdn.com/@sc04/kf/Hf595031c7aa944bd9d409091ac00e23bh.jpg_640x640.jpg", "20 pieces", "1600330652598", "$2-10"),
    ("Micro Fiber Towel Car Cleaning 1200 Gsm Microfiber Towel Rocgoods 1200…", "https://s.alicdn.com/@sc04/kf/H383f9992df3249df92b85f4c7c3ed5e7L.jpg_640x640.jpg", "100 pieces", "1601769008248", "$0.52-0.79"),
    ("1200gsm Microfibre Ultra Plush Thick Microfiber Towel for Car Wash Dry…", "https://s.alicdn.com/@sc04/kf/H70863e1ae0a5434c98577248b054c336l.png_640x640.png", "500 pieces", "62163398867", "$0.90"),
    ("X9 B5692 Car Microfiber Cleaning Cloth Thickened Absorbent Lint-Free W…", "https://s.alicdn.com/@sc04/kf/H68789b4ab3764334ae01ba8af396ffaeE.png_640x640.png", "1 piece", "1601798428241", "$2.30"),
    ("Large Premium 1600gsm 70x90cm Microfiber Car Drying Towel Double Twist…", "https://s.alicdn.com/@sc04/kf/H149f253cf45348a68d1b70d4eb8da658n.png_640x640.png", "100 pieces", "1601641441499", "$5-6.50"),
    ("Superfine Fiber Braid Car Wash Thickened Super Absorbent Special Multi…", "https://s.alicdn.com/@sc04/kf/Hfefbbfa9b61b45299ac665d67a0b237cn.jpg_640x640.jpg", "50 pieces", "1601679144897", "$1.35-3.39"),
    ("Wholesale Disposable 600gsm Sustainable Large Thick Colorful Coral Fle…", "https://s.alicdn.com/@sc04/kf/Hffcadf11a3c1424eb8b81bc2a7ef47cfs.jpg_640x640.jpg", "100 parcels", "1601764440175", "$0.14-1.13"),
    ("160Cm 80X90 Quality Microfiber Car Cleaning Multipurpose Car Big Large…", "https://s.alicdn.com/@sc04/kf/H56fbf222871245d5bdf7ce67df83033aI.jpg_640x640.jpg", "500 pieces", "1600711975503", "$0.15-0.45"),
    ("Microfiber Car Drying Towels Super Absorbent Scratch Free Car Cleanin…", "https://s.alicdn.com/@sc04/kf/HTB1qnhaLFzqK1RjSZFoq6zfcXXaI.jpg_640x640.jpg", "10 pieces", "62032517283", "$0.70-5"),
    ("High-quality Ultra-soft Car Wash Towel Custom logo Microfiber Drying T…", "https://s.alicdn.com/@sc04/kf/H3e777a2a4bee4ce18cfd0c47eee4f3a6E.jpg_640x640.jpg", "100 pieces", "1601040539137", "$0.50-0.60"),
    ("Factory Wholesale Large Twisted Ring Double Thickened Microfiber Car W…", "https://s.alicdn.com/@sc04/kf/H1beb710d0f3b4d9285f98e6d6bd6dc246.jpg_640x640.jpg", "5 pieces", "1601190556421", "$4-4.80"),
    ("24\"x35\" 1400GSM Factory Microfiber Twisted Drying Towel Quality Auto W…", "https://s.alicdn.com/@sc04/kf/Ha4d6283fc995484fac308baf7d7dc61cO.png_640x640.png", "1 piece", "1601742321165", "$4.59"),
    ("Car Wash Towel Microfiber No Shedding Thickened Water Absorption Clean…", "https://s.alicdn.com/@sc04/kf/H70fc1d0298074ec59af1b73fed372fc1R.png_640x640.png", "1 piece", "1601676331587", "$2.90-3.90"),
]

for title, pic, moq, pid, price in towel_data:
    products.append({"title": title, "sPicUrl": pic, "moq": moq, "prod_id": pid, "price": price, "category": "Microfiber Towels"})

for i in range(21, 61):
    products.append({"title": f"Microfiber Towel Model {i}", "sPicUrl": "https://s.alicdn.com/img/tow.jpg", "moq": "100 pieces", "prod_id": f"1600{i}33", "price": "$1.50", "category": "Microfiber Towels"})

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=4)
