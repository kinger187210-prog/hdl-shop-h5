import json

raw_results = [
    # Smart Home Cameras
    {"cat": "Smart Home Camera", "rows": [
        ["1601490294971", "Tuya HD Smart Home WiFi Indoor Camera Great Quality Two-Way Audio Auto…", "https://s.alicdn.com/@sc04/kf/H98489e2809dc474884b014b8b9142ad8w.png_640x640.png", "$9.99-12.99", "2 pieces"],
        ["1601634348591", "Versatile WiFi Smart Home Camera 1080P HD CMOS Sensor H.264 Night Visi…", "https://s.alicdn.com/@sc04/kf/H19f7228710734eb9bccf60c4ef0e5b6aR.jpg_640x640.jpg", "$13.72", "1 unit"],
        ["1601405307734", "Tuya Wifi Camera Indoor Monitor App Real-time Monitoring Night Vision …", "https://s.alicdn.com/@sc04/kf/H1718801c512d4a3e890297bfac11402fr.jpg_640x640.jpg", "$8.55-11.55", "2 pieces"],
        ["1601248823782", "Tuya Smart Home Indoor Camera Smart Home Security Video Wireless Two W…", "https://s.alicdn.com/@sc04/kf/H42c05d508f2749329a8cfdbe906b686es.jpg_640x640.jpg", "$9.90-12.40", "10 pieces"],
        ["1601481948003", "Smart Home Indoor Camera Smart Home Security Video Wireless Two Way Au…", "https://s.alicdn.com/@sc04/kf/H01f88711657a4ea48c86e1247c9b9734l.jpg_640x640.jpg", "$8.40", "10 pieces"],
        ["1600485331881", "UEMON Smart Home Tuya App Control Camera House Security Two Way Voice …", "https://s.alicdn.com/@sc04/kf/H837f01d6f0f8499eb3b10f71a076552aB.png_640x640.png", "$9.80-12.80", "10 pieces"],
        ["1601609340507", "Hot Sale Tuya Smart Home Wireless Network Camera 1080p 3MP CMOS Sensor…", "https://s.alicdn.com/@sc04/kf/Hc35f7a65065944f38eef51b945519875m.jpg_640x640.jpg", "$13.30", "1 piece"],
        ["1601420058392", "Q7 Best Selling Smart Home Security Wireless Camera 360 Degree Smart I…", "https://s.alicdn.com/@sc04/kf/H4342c409192e470caf3d5f669a5f6267U.jpg_640x640.jpg", "$7", "5 pieces"],
        ["1601434250476", "On Sale 1080P 2MP Smart Home Indoor Wireless 2.4G 5G Dual Band WiFi PT…", "https://s.alicdn.com/@sc04/kf/He66b706a1d694c18b0116fcc518e5591s.png_640x640.png", "$11.50", "1 piece"],
        ["1600895103883", "Smart Home System Cameras Mini Camera Phone App  Wifi  Mobile High Res…", "https://s.alicdn.com/@sc04/kf/H7670a89b7e2b40a89c18c7f8e5f3064bB.jpg_640x640.jpg", "$9.75-11", "500 pieces"],
        ["1601421083582", "Smart Home HD Security Camera 3MP Auto IR-CUT Color Night Vision 2.4/5…", "https://s.alicdn.com/@sc04/kf/H41b1783830a44d9b8e1959812618e583N.png_640x640.png", "$14.49-15.12", "100 pieces"],
        ["1600094378484", "Smart Home Camera IPC360home APP Two-Way Audio Night Vision Crying & M…", "https://s.alicdn.com/@sc04/kf/Hc2e42c31d90d4673a5b1f936bcb785bc1.jpg_640x640.jpg", "$7.99-8.25", "2 pieces"],
        ["1601061460273", "Tuya Wireless Smart Home Cctv 3MP Wifi Camera", "https://s.alicdn.com/@sc04/kf/H2f6172dcbf97478fa2e5608c02d2badeK.jpg_640x640.jpg", "$10.99", "1 piece"],
        ["1600826349609", "2023 New Arrival Smart Linkage Home Security Camera 2MP 4MP ICSee Dual…", "https://s.alicdn.com/@sc04/kf/Hb3b7714b8546425ea459c8d941af8e10K.jpg_640x640.jpg", "$8.99-12.99", "50 pieces"],
        ["62497017763", "Smart Home Surveillance Camera Support TUYA Best for Home Use Ip Wirel…", "https://s.alicdn.com/@sc04/kf/Hea2ed914a37842a389b54f1143feec4fT.jpg_640x640.jpg", "$10.50", "10 pieces"],
        ["1600987201332", "White High Quality Smart Home WIFI 3 Megapixel Cameras for Home Securi…", "https://s.alicdn.com/@sc04/kf/H0a21738a759b4c2a88075f0fbd474eb49.jpeg_640x640.jpeg", "$6.75-8.33", "1 piece"],
        ["1601280883421", "Smart Home Dual Lens E27 HD Camera 360 Wifi Network PTZ IP 4MP 2K Mini…", "https://s.alicdn.com/@sc04/kf/H9b369ad5189546dc91c98f55f442a01b1.jpg_640x640.jpg", "$8.35-9.36", "200 pieces"],
        ["1601009526432", "Smart Home Battery Wireless WIFI 4G Camera With Motion Detection Night…", "https://s.alicdn.com/@sc04/kf/Hfffd5a577f9f453bab10345e5d87016cD.jpg_640x640.jpg", "$23", "2 units"],
        ["62549342981", "JOAREON Smart Home H.265 1080P Mini Digital Camera V380 IR Security Ca…", "https://s.alicdn.com/@sc04/kf/Hb43b299aec1e430691152715244567a6k.jpg_640x640.jpg", "$9.80", "1 piece"],
        ["1600166682718", "Tuya Smart Life IP Camera 1080P High Definition Baby Cam IR Night Visi…", "https://s.alicdn.com/@sc04/kf/Hcaa2d7a2e830467b832d118f4b6b05cdt.jpg_640x640.jpg", "$19.40-19.50", "500 pieces"],
        ["1601221413821", "Tuya 2MP/3MP WiFi Smart IP Camera AI Human Detect Color Night Vision C…", "https://s.alicdn.com/@sc04/kf/H2c55dff69d73419a8056bd4bd6669dbfI.jpg_640x640.jpg", "$11.50", "10 pieces"],
        ["1601639920008", "Glomarket Smart Home WiFi 1080p Wireless IP Camera Indoor 2.4G/5G Netw…", "https://s.alicdn.com/@sc04/kf/H59c79f5e102649cf8b11ba79317329748.jpg_640x640.jpg", "$12.50-15", "2 pieces"],
        ["1601392454937", "New V380 Home Wireless Camera Indoor HD Night Vision Remote Snowman Wi…", "https://s.alicdn.com/@sc04/kf/He52ad2384d1a49cea8aa91920d20ee71L.jpg_640x640.jpg", "$12.50-16.90", "1 piece"],
        ["1600942169991", "Indoor Tuya Ai Smart Wifi Camera Home Security Wireless, Web Wi Fi Wir…", "https://s.alicdn.com/@sc04/kf/H7b07edebb5b54c11ad45ec4e646e258dw.png_640x640.png", "$5.66-6.56", "100 pieces"],
        ["1600622055329", "1080P WiFi Smart Home Camera with Two-Way Audio, Digital Zoom, Night V…", "https://s.alicdn.com/@sc04/kf/H9763f74f87664136ab0640baa2676754X.jpg_640x640.jpg", "$4.99", "1 piece"],
        ["1601339169809", "Wholesale Supply Xiaomi Camara Inteligente Xiaomi C500 Pro 3K HDR 5MP …", "https://s.alicdn.com/@sc04/kf/H1df8ad9ce4514e99b35a6f1f387e8cb43.jpg_640x640.jpg", "$33.90", "48 pieces"],
        ["1600759842107", "Glomarket Smart Home Wifi 1080p Wireless Ip Camera Indoor 2.4G/5G Netw…", "https://s.alicdn.com/@sc04/kf/H33c004ab35d343ff9856d9a549a851f96.jpg_640x640.jpg", "$15", "2 pieces"],
        ["1601669804333", "SONOFF CAM PT2 Smart Home Security Camera Smart Night Vision 360 Panor…", "https://s.alicdn.com/@sc04/kf/Hf355b7ae1f624dd89a86c20b52b21c6aY.png_640x640.png", "$35.88", "1 piece"],
        ["1601781194357", "Smart Home Security Camera 2MP Smart AI PTZ Camera Home Security Night…", "https://s.alicdn.com/@sc04/kf/H00efa93fbf134ebfa54422df28f53ccef.jpg_640x640.jpg", "$8.50", "2 pieces"],
        ["1601432421875", "New 1080P Tuya Smart Home IOT Wifi Camera Alarm System Wireless Securi…", "https://s.alicdn.com/@sc04/kf/Hd55b814ca30245fc8d914acbd9bd1e20z.jpg_640x640.jpg", "$21.50", "20 sets"]
    ]},
    # IP Cameras
    {"cat": "IP Camera", "rows": [
        ["1601023286459", "HIK Compatible ColorVu Face Detection 4MP 6MP 8MP Fixed Eyeball Bullet…", "https://s.alicdn.com/@sc04/kf/Haecf32d989a842a9bfc382148dabc69eW.jpg_640x640.jpg", "$53-86", "2 pieces"],
        ["1600706834794", "Original Dahua Ready Stock IPC-HDBW2431R-ZS-S2  4MP Lite IP POE IR Var…", "https://s.alicdn.com/@sc04/kf/Ha8ca1fe6c9484fc3adaad94d9f3922c39.jpg_640x640.jpg", "$90", "1 piece"],
        ["1600838051720", "2Mp Auto Motion Tracking Ptz Ip Camera 1080P Night Vision Outdoor Cctv…", "https://s.alicdn.com/@sc04/kf/Hfbe4f0b6963c4756986ef083b2753fe90.jpg_640x640.jpg", "$15.50", "1 piece"],
        ["10000019121740", "Factory Wholesale Long Range IP for Construction Site Monitoring Outdo…", "https://s.alicdn.com/@sc04/kf/H250ca6bf15a047a1bcb2ba258db7291fb.jpg_640x640.jpg", "$119-128", "2 pieces"],
        ["1601224194975", "IPC-HDW1439V-A-IL in Stock IP Camera Full Color 4MP Entry Smart Dual L…", "https://s.alicdn.com/@sc04/kf/H7cdf40d544ac4714ba0ca577718e73e9j.jpg_640x640.jpg", "$36-42", "2 pieces"],
        ["1601016942624", "5MP Full Color Xmeye IP Camera Night Vision Color Video New Technology…", "https://s.alicdn.com/@sc04/kf/Ha5de46ca6cf146019d9d7688c8d4c0a3D.jpg_640x640.jpg", "$21.80", "10 pieces"],
        ["1601582473318", "High Quality Icsee 3MP Network Camera WIFI IP Camera Outdoor HD PTZ Wa…", "https://s.alicdn.com/@sc04/kf/H4c0e7f9778f041749b8f2e7ece254bb0v.jpg_640x640.jpg", "$17.51", "1 piece"],
        ["1601606573501", "Black 8MP H.265 Active Deterrence POE IP Camera Red Blue Light Indoor …", "https://s.alicdn.com/@sc04/kf/H5ca283f5199c4fa18fb5de41f8e2
