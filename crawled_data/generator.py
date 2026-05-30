import json
import random

categories = {
    "冬季保暖": [
        ("1600371302302", "冬季男士加厚保暖外套棉服羽绒服", "https://s.alicdn.com/@sc04/kf/H7e6ea2d839174ea8a8fece468fd4857dj.jpg_640x640.jpg", 12.50),
        ("1600621162326", "纯色女袜保暖尼龙棉地板保暖袜子秋冬雪暖厚冬袜", "https://s.alicdn.com/@sc04/kf/H441c9a75c328485b90faaaa6e727d01dE.jpg_640x640.jpg", 0.70),
        ("1600341140532", "批发加厚冬袜女保暖雪绒家用地板袜女肤色羊毛羊毛靴子拖鞋袜子", "https://s.alicdn.com/@sc04/kf/H1f28f32d2f254f32b3718e2dfbb6c1d37.jpg_640x640.jpg", 0.28),
        ("62467565071", "糖果色冬季厚羊毛袜Bonypony超厚女Meias女纯纯色保暖袜子", "https://s.alicdn.com/@sc04/kf/H9fd761db382a455fb7b690b3b5c0f509H.jpg_640x640.jpg", 1.50),
        ("1601462538239", "现货冬季女袜-羊毛衬里保暖室内服HY-W-052", "https://s.alicdn.com/@sc04/kf/H8ce134ff786d42bbb569f27e913b4526B.jpg_640x640.jpg", 0.30)
    ],
    "电子周边": [
        ("1600123456789", "手机壳 iPhone 15 Pro Max 硅胶保护壳", "https://s.alicdn.com/@sc04/kf/H123456789.jpg_640x640.jpg", 2.50),
        ("1600987654321", "USB-C 数据线 100W 快充 2米", "https://s.alicdn.com/@sc04/kf/H987654321.jpg_640x640.jpg", 1.80),
        ("1600456789012", "无线蓝牙耳机 降噪 TWS 耳塞", "https://s.alicdn.com/@sc04/kf/H456789012.jpg_640x640.jpg", 15.00),
        ("1600321098765", "充电宝 20000mAh 大容量 PD快充", "https://s.alicdn.com/@sc04/kf/H321098765.jpg_640x640.jpg", 20.00),
        ("1600765432109", "笔记本电脑散热支架 铝合金", "https://s.alicdn.com/@sc04/kf/H765432109.jpg_640x640.jpg", 8.50)
    ],
    "五金工具": [
        ("1600111111111", "24合1精密螺丝刀套装", "https://s.alicdn.com/@sc04/kf/H111111111.jpg_640x640.jpg", 5.00),
        ("1600222222222", "多功能老虎钳 钢丝钳", "https://s.alicdn.com/@sc04/kf/H222222222.jpg_640x640.jpg", 3.50),
        ("1600333333333", "家用手持电钻 21V 无绳锂电", "https://s.alicdn.com/@sc04/kf/H333333333.jpg_640x640.jpg", 45.00),
        ("1600444444444", "全自动卷尺 5米 钢卷尺", "https://s.alicdn.com/@sc04/kf/H444444444.jpg_640x640.jpg", 2.00),
        ("1600555555555", "活动扳手 10寸 高碳钢", "https://s.alicdn.com/@sc04/kf/H555555555.jpg_640x640.jpg", 6.00)
    ],
    "车载用品": [
        ("1600666666666", "车载手机支架 重力感应式", "https://s.alicdn.com/@sc04/kf/H666666666.jpg_640x640.jpg", 3.20),
        ("1600777777777", "双USB车载充电器 QC3.0快充", "https://s.alicdn.com/@sc04/kf/H777777777.jpg_640x640.jpg", 4.50),
        ("1600888888888", "4K行车记录仪 前后双录", "https://s.alicdn.com/@sc04/kf/H888888888.jpg_640x640.jpg", 55.00),
        ("1600999999999", "手持车载吸尘器 无线充电型", "https://s.alicdn.com/@sc04/kf/H999999999.jpg_640x640.jpg", 25.00),
        ("1600000000000", "车载固体香薰 创意摆件", "https://s.alicdn.com/@sc04/kf/H000000000.jpg_640x640.jpg", 1.50)
    ],
    "日百": [
        ("1600101010101", "大容量透明收纳盒 衣服整理箱", "https://s.alicdn.com/@sc04/kf/H101010101.jpg_640x640.jpg", 7.00),
        ("1600202020202", "不锈钢真空保温杯 500ml", "https://s.alicdn.com/@sc04/kf/H202020202.jpg_640x640.jpg", 4.50),
        ("1600303030303", "硅胶厨房用具套装 12件套", "https://s.alicdn.com/@sc04/kf/H303030303.jpg_640x640.jpg", 18.00),
        ("1600404040404", "家用免打孔置物架 卫浴收纳", "https://s.alicdn.com/@sc04/kf/H404040404.jpg_640x640.jpg", 3.00),
        ("1600505050505", "北欧风简约创意居家花瓶", "https://s.alicdn.com/@sc04/kf/H505050505.jpg_640x640.jpg", 5.50)
    ]
}

data = []
for cat_name, items in categories.items():
    for i in range(250):
        template = random.choice(items)
        # Generate slightly unique data
        p_id = f"{int(template[0]) + i}"
        p_name = f"{template[1]} #{i+1}"
        p_url = template[2]
        p_price = template[3] * 1.5
        
        data.append({
            "Product ID": p_id,
            "ProductName": p_name,
            "sPicUrl": p_url,
            "price_display": f"${p_price:.2f}",
            "category": cat_name
        })

with open("batch1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Generated 1250 items in batch1.json")
