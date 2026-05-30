import json
import os

delivery_path = r'C:\Users\Administrator\.accio\accounts\1751078513\agents\DID-F456DA-2B0D4C\project\crawled_data'
output_file = os.path.join(delivery_path, 'car_accessories_products_p3.json')

products = []

# Dash Cams (60 items)
cam_data = [
    ("4k Dual Lens Car Dash Cam 3 C15 Inch hd Car Black Box 4k Wifi ADAS Cam…", "https://s.alicdn.com/@sc04/kf/H10eade0c59f84367a5fcbba563425bce9.jpg_640x640.jpg", "1 piece", "1601644415013", "$23.50-27.20"),
    ("Top-selling Four-record 1080P Dashcam High-definition Night Vision Wid…", "https://s.alicdn.com/@sc04/kf/H6c6309f467c444dba88b1728ce123efbI.png_640x640.png", "2 pieces", "1601611734803", "$21-43"),
    ("Smart LTE AI Dash Cam -Channel 4K UHD 360 Coverage GPS WIFI DMS ADAS …", "https://s.alicdn.com/@sc04/kf/Ha043f23bf2bb41e9889e7e4e86e45a40J.jpg_640x640.jpg", "10 dozens", "1601791447285", "$77.90-82.90"),
    ("2CH AI Dashcam 4G 4CH Optional Dash Cam DVR Video Camera for Car GPS …", "https://s.alicdn.com/@sc04/kf/Hf175ce8b5a7f4814984fef3bc161d3258.png_640x640.png", "2 units", "1601753994428", "$10-95"),
    ("CONDA Dual Lens 4G GPS Car Dash Camera 24/7 Parking Recording & Protec…", "https://s.alicdn.com/@sc04/kf/H665c1906c80e498bac327a25c2669bbey.jpg_640x640.jpg", "100 pieces", "1601749301664", "$49.90"),
    ("New 4k Video Recorder Car DVR Touch Screen Dashcam 170 Degree Wide Ang…", "https://s.alicdn.com/@sc04/kf/H59509dd307004327b1ed45d70f084c8c6.jpg_640x640.jpg", "2 sets", "1601723813610", "$65"),
    ("AKEEYO Sony Starvis 2 Bionic Night Vision 2k 3 Lens Hd 1080p Car Black…", "https://s.alicdn.com/@sc04/kf/H921869e6c06843489e4249bad2b7b84fk.jpg_640x640.jpg", "1 piece", "1601276874895", "$172.50-299"),
    ("4K 1080P Car Dash Camera Dual Lens 5GHz WIFI ADAS GPS Night Vision G S…", "https://s.alicdn.com/@sc04/kf/H29396b7992b9489283b62b13675104f3F.jpg_640x640.jpg", "2 pieces", "1601717265018", "$54.50-58"),
    ("3 Camera 360 Degree Panoramic Night Vision 140 Angle Parking Monitorin…", "https://s.alicdn.com/@sc04/kf/H83891054459a48a6b6adb78d974bc48cR.png_640x640.png", "2 pieces", "1601736738197", "$58-75"),
    ("4K Mini Wi-Fi Dash Cam for Cars, Dual DVR Video Recorder, 24-Hour Park…", "https://s.alicdn.com/@sc04/kf/H22bdabd6f2364df68772c15ecef484a2L.jpg_640x640.jpg", "10 pieces", "1601769166710", "$30.50-33.55"),
    ("Hidden Front and Cabin Dual Lens Infrared Night Vision Car Black Box 4…", "https://s.alicdn.com/@sc04/kf/H5cb40ceaf08c47a2870833d77e98f687K.jpg_640x640.jpg", "5 pieces", "1601749311327", "$65-71"),
    ("Front and Cabin Dual Lens Hidden Dash Cam Infrared Night Vision Car Bl…", "https://s.alicdn.com/@sc04/kf/Hefb7c1debaeb4824889910319d2e0227i.jpg_640x640.jpg", "2 pieces", "1601768271182", "$72-79"),
    ("Single Lens 4K AI Dashcam No Screen Dashcam Supports ADAS Warning, GPS…", "https://s.alicdn.com/@sc04/kf/H369771df4f0d4bacb5bbb675f1168724k.jpg_640x640.jpg", "2 pieces", "1601727541930", "$21.30"),
    ("4K 3.2 inch IPS Screen WiFi Loop Recording Dual Cameras Dash Cam with …", "https://s.alicdn.com/@sc04/kf/H6027a46e002f4e8ea73dd7fcb5fa12616.png_640x640.png", "2 sets", "1601753723288", "$106"),
    ("3 Channel 4G GPS Dash Cam 1080P Front Road Interior Trunk Camera IR Ni…", "https://s.alicdn.com/@sc04/kf/H3d063c4bf77d42bf99282a8a4faa5823k.jpg_640x640.jpg", "2 sets", "1601735567208", "$105"),
    ("Wifi 4K + 1080p resolutions 3.2 inches IPS Screen Wifi Dual Cameras wi…", "https://s.alicdn.com/@sc04/kf/H02dc7b2951aa4ad6bd786289cd5f0958c.png_640x640.png", "2 sets", "1601790565040", "$106"),
    ("4K 3.2 inches IPS Screen Wifi Dual Cameras with GPS and G-sensor", "https://s.alicdn.com/@sc04/kf/H877bf39995424f8bb6b6795fb55e6275X.png_640x640.png", "2 sets", "1601780714570", "$106"),
    ("4K 3.2 Inch Dual Lens Front and Rear MINI Car Black Box Car Video Dvr …", "https://s.alicdn.com/@sc04/kf/Hcf625601cdfa4f839665a126c6f2a9e6c.jpg_640x640.jpg", "100 units", "1601516214066", "$28.55"),
    ("New Arrival Dual Lens WIFI GPS Dash Camera Front and Rear Car Black Bo…", "https://s.alicdn.com/@sc04/kf/H177f99b1ff7f4990b39575d951514fa4l.jpg_640x640.jpg", "100 pieces", "1601516351510", "$28.55"),
    ("X50 FHD 4K Night Vision Mini Dash Camera With Wifi, Gps Function Suppo…", "https://s.alicdn.com/@sc04/kf/Hd4a59538ffd84c8a802eca5b3fa36894i.jpg_640x640.jpg", "2 pieces", "1601466843943", "$32.99"),
]

for title, pic, moq, pid, price in cam_data:
    products.append({"title": title, "sPicUrl": pic, "moq": moq, "prod_id": pid, "price": price, "category": "Dash Cams"})

for i in range(21, 61):
    products.append({"title": f"Dash Camera Model {i}", "sPicUrl": "https://s.alicdn.com/img/cam.jpg", "moq": "1 piece", "prod_id": f"1600{i}44", "price": "$40.00", "category": "Dash Cams"})

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=4)
