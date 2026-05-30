import json

products = []

def add_products(data_list):
    for pid, title, pic, price, moq, cat in data_list:
        products.append({
            "title": title,
            "sPicUrl": pic,
            "moq": moq,
            "prod_id": int(pid),
            "price": price,
            "category": cat
        })

# Batch 1
data1 = [
    ("1601490294971", "Tuya HD Smart Home WiFi Indoor Camera", "https://s.alicdn.com/@sc04/kf/H98489e2809dc474884b014b8b9142ad8w.png_640x640.png", "$9.99-12.99", "2 pieces", "Smart Home Camera"),
    ("1601634348591", "Versatile WiFi Smart Home Camera 1080P", "https://s.alicdn.com/@sc04/kf/H19f7228710734eb9bccf60c4ef0e5b6aR.jpg_640x640.jpg", "$13.72", "1 unit", "Smart Home Camera"),
    ("1601405307734", "Tuya Wifi Camera Indoor Monitor", "https://s.alicdn.com/@sc04/kf/H1718801c512d4a3e890297bfac11402fr.jpg_640x640.jpg", "$8.55-11.55", "2 pieces", "Smart Home Camera"),
    ("1601248823782", "Tuya Smart Home Indoor Camera", "https://s.alicdn.com/@sc04/kf/H42c05d508f2749329a8cfdbe906b686es.jpg_640x640.jpg", "$9.90-12.40", "10 pieces", "Smart Home Camera"),
    ("1601481948003", "Smart Home Indoor Camera", "https://s.alicdn.com/@sc04/kf/H01f88711657a4ea48c86e1247c9b9734l.jpg_640x640.jpg", "$8.40", "10 pieces", "Smart Home Camera"),
    ("1600485331881", "UEMON Smart Home Tuya App Control", "https://s.alicdn.com/@sc04/kf/H837f01d6f0f8499eb3b10f71a076552aB.png_640x640.png", "$9.80-12.80", "10 pieces", "Smart Home Camera"),
    ("1601609340507", "Hot Sale Tuya Smart Home Wireless", "https://s.alicdn.com/@sc04/kf/Hc35f7a65065944f38eef51b945519875m.jpg_640x640.jpg", "$13.30", "1 piece", "Smart Home Camera"),
    ("1601420058392", "Q7 Best Selling Smart Home Security", "https://s.alicdn.com/@sc04/kf/H4342c409192e470caf3d5f669a5f6267U.jpg_640x640.jpg", "$7", "5 pieces", "Smart Home Camera"),
    ("1601434250476", "On Sale 1080P 2MP Smart Home", "https://s.alicdn.com/@sc04/kf/He66b706a1d694c18b0116fcc518e5591s.png_640x640.png", "$11.50", "1 piece", "Smart Home Camera"),
    ("1600895103883", "Smart Home System Cameras Mini", "https://s.alicdn.com/@sc04/kf/H7670a89b7e2b40a89c18c7f8e5f3064bB.jpg_640x640.jpg", "$9.75-11", "500 pieces", "Smart Home Camera"),
    ("1601421083582", "Smart Home HD Security Camera", "https://s.alicdn.com/@sc04/kf/H41b1783830a44d9b8e1959812618e583N.png_640x640.png", "$14.49-15.12", "100 pieces", "Smart Home Camera"),
    ("1600094378484", "Smart Home Camera IPC360home APP", "https://s.alicdn.com/@sc04/kf/Hc2e42c31d90d4673a5b1f936bcb785bc1.jpg_640x640.jpg", "$7.99-8.25", "2 pieces", "Smart Home Camera"),
    ("1601061460273", "Tuya Wireless Smart Home Cctv", "https://s.alicdn.com/@sc04/kf/H2f6172dcbf97478fa2e5608c02d2badeK.jpg_640x640.jpg", "$10.99", "1 piece", "Smart Home Camera"),
    ("1600826349609", "2023 New Arrival Smart Linkage", "https://s.alicdn.com/@sc04/kf/Hb3b7714b8546425ea459c8d941af8e10K.jpg_640x640.jpg", "$8.99-12.99", "50 pieces", "Smart Home Camera"),
    ("62497017763", "Smart Home Surveillance Camera", "https://s.alicdn.com/@sc04/kf/Hea2ed914a37842a389b54f1143feec4fT.jpg_640x640.jpg", "$10.50", "10 pieces", "Smart Home Camera"),
    ("1600987201332", "White High Quality Smart Home WIFI", "https://s.alicdn.com/@sc04/kf/H0a21738a759b4c2a88075f0fbd474eb49.jpeg_640x640.jpeg", "$6.75-8.33", "1 piece", "Smart Home Camera"),
    ("1601280883421", "Smart Home Dual Lens E27 HD Camera", "https://s.alicdn.com/@sc04/kf/H9b369ad5189546dc91c98f55f442a01b1.jpg_640x640.jpg", "$8.35-9.36", "200 pieces", "Smart Home Camera"),
    ("1601009526432", "Smart Home Battery Wireless WIFI", "https://s.alicdn.com/@sc04/kf/Hfffd5a577f9f453bab10345e5d87016cD.jpg_640x640.jpg", "$23", "2 units", "Smart Home Camera"),
    ("62549342981", "JOAREON Smart Home H.265 1080P", "https://s.alicdn.com/@sc04/kf/Hb43b299aec1e430691152715244567a6k.jpg_640x640.jpg", "$9.80", "1 piece", "Smart Home Camera"),
    ("1600166682718", "Tuya Smart Life IP Camera 1080P", "https://s.alicdn.com/@sc04/kf/Hcaa2d7a2e830467b832d118f4b6b05cdt.jpg_640x640.jpg", "$19.40-19.50", "500 pieces", "Smart Home Camera"),
    ("1601221413821", "Tuya 2MP/3MP WiFi Smart IP Camera", "https://s.alicdn.com/@sc04/kf/H2c55dff69d73419a8056bd4bd6669dbfI.jpg_640x640.jpg", "$11.50", "10 pieces", "Smart Home Camera"),
    ("1601639920008", "Glomarket Smart Home WiFi 1080p", "https://s.alicdn.com/@sc04/kf/H59c79f5e102649cf8b11ba79317329748.jpg_640x640.jpg", "$12.50-15", "2 pieces", "Smart Home Camera"),
    ("1601392454937", "New V380 Home Wireless Camera", "https://s.alicdn.com/@sc04/kf/He52ad2384d1a49cea8aa91920d20ee71L.jpg_640x640.jpg", "$12.50-16.90", "1 piece", "Smart Home Camera"),
    ("1600942169991", "Indoor Tuya Ai Smart Wifi Camera", "https://s.alicdn.com/@sc04/kf/H7b07edebb5b54c11ad45ec4e646e258dw.png_640x640.png", "$5.66-6.56", "100 pieces", "Smart Home Camera"),
    ("1600622055329", "1080P WiFi Smart Home Camera", "https://s.alicdn.com/@sc04/kf/H9763f74f87664136ab0640baa2676754X.jpg_640x640.jpg", "$4.99", "1 piece", "Smart Home Camera"),
    ("1601339169809", "Wholesale Supply Xiaomi C500 Pro", "https://s.alicdn.com/@sc04/kf/H1df8ad9ce4514e99b35a6f1f387e8cb43.jpg_640x640.jpg", "$33.90", "48 pieces", "Smart Home Camera"),
    ("1600759842107", "Glomarket Smart Home Wifi 1080p", "https://s.alicdn.com/@sc04/kf/H33c004ab35d343ff9856d9a549a851f96.jpg_640x640.jpg", "$15", "2 pieces", "Smart Home Camera"),
    ("1601669804333", "SONOFF CAM PT2 Smart Home Security", "https://s.alicdn.com/@sc04/kf/Hf355b7ae1f624dd89a86c20b52b21c6aY.png_640x640.png", "$35.88", "1 piece", "Smart Home Camera"),
    ("1601781194357", "Smart Home Security Camera 2MP", "https://s.alicdn.com/@sc04/kf/H00efa93fbf134ebfa54422df28f53ccef.jpg_640x640.jpg", "$8.50", "2 pieces", "Smart Home Camera"),
    ("1601432421875", "New 1080P Tuya Smart Home IOT", "https://s.alicdn.com/@sc04/kf/Hd55b814ca30245fc8d914acbd9bd1e20z.jpg_640x640.jpg", "$21.50", "20 sets", "Smart Home Camera")
]
add_products(data1)
# Batch 2
data2 = [
    ("1601023286459", "HIK Compatible ColorVu Face Detection", "https://s.alicdn.com/@sc04/kf/Haecf32d989a842a9bfc382148dabc69eW.jpg_640x640.jpg", "$53-86", "2 pieces", "IP Camera"),
    ("1600706834794", "Original Dahua Ready Stock POE", "https://s.alicdn.com/@sc04/kf/Ha8ca1fe6c9484fc3adaad94d9f3922c39.jpg_640x640.jpg", "$90", "1 piece", "IP Camera"),
    ("1600838051720", "2Mp Auto Motion Tracking Ptz Ip", "https://s.alicdn.com/@sc04/kf/Hfbe4f0b6963c4756986ef083b2753fe90.jpg_640x640.jpg", "$15.50", "1 piece", "IP Camera"),
    ("10000019121740", "Long Range IP for Construction Site", "https://s.alicdn.com/@sc04/kf/H250ca6bf15a047a1bcb2ba258db7291fb.jpg_640x640.jpg", "$119-128", "2 pieces", "IP Camera"),
    ("1601224194975", "IPC-HDW1439V-A-IL in Stock IP Camera", "https://s.alicdn.com/@sc04/kf/H7cdf40d544ac4714ba0ca577718e73e9j.jpg_640x640.jpg", "$36-42", "2 pieces", "IP Camera"),
    ("1601016942624", "5MP Full Color Xmeye IP Camera", "https://s.alicdn.com/@sc04/kf/Ha5de46ca6cf146019d9d7688c8d4c0a3D.jpg_640x640.jpg", "$21.80", "10 pieces", "IP Camera"),
    ("1601582473318", "High Quality Icsee 3MP Network Camera", "https://s.alicdn.com/@sc04/kf/H4c0e7f9778f041749b8f2e7ece254bb0v.jpg_640x640.jpg", "$17.51", "1 piece", "IP Camera"),
    ("1601606573501", "Black 8MP H.265 POE IP Camera", "https://s.alicdn.com/@sc04/kf/H5ca283f5199c4fa18fb5de41f8e22091I.jpg_640x640.jpg", "$35-38", "2 pieces", "IP Camera"),
    ("60807875451", "OEM Full Color Panoramic Varifocal", "https://s.alicdn.com/@sc04/kf/H9b898346b39a4744aee4ae0aa8454ad0j.png_640x640.png", "$127.99-329", "1 piece", "IP Camera"),
    ("1601696711346", "PoE IP Camera 4MP All-Metal Dome", "https://s.alicdn.com/@sc04/kf/Hd27b81727c764f1982dea0413e6e0a94W.png_640x640.png", "$16-18", "2 pieces", "IP Camera"),
    ("1600214062610", "Aluminum Infrared IP Camera 4MP", "https://s.alicdn.com/@sc04/kf/H6cd6ca72223a47c6a89fe0d89cfaa1e1y.jpg_640x640.jpg", "$19.50", "60 pieces", "IP Camera"),
    ("1601038085334", "Outdoor Wifi IP Camera 2MP 4K", "https://s.alicdn.com/@sc04/kf/H5f3520c6ed05448eabe353dabfbfaa253.jpg_640x640.jpg", "$13.20", "10 pieces", "IP Camera"),
    ("1600128404258", "5MP Turret POE IP Camera", "https://s.alicdn.com/@sc04/kf/H3c8ab71f3c5e4d0387cd91e73e8c70bd6.png_640x640.png", "$38.50", "2 pieces", "IP Camera"),
    ("1601171361905", "3MP Smart IP Wifi PTZ Camera", "https://s.alicdn.com/@sc04/kf/Had98dc765b424e9992d471f5aed4ea91J.png_640x640.png", "$13.30-15", "1 piece", "IP Camera"),
    ("1601050523720", "A12 HD 1080P Ptz Wifi Ip Cameras", "https://s.alicdn.com/@sc04/kf/Hc556667dafea497fbfd95cda5a43c4d9o.jpg_640x640.jpg", "$5.80", "2 pieces", "IP Camera"),
    ("1601588897465", "Indoor Dome Camera Built-in Mic", "https://s.alicdn.com/@sc04/kf/H475ff6bf8000467eb30ec4e0ac3a9bd8B.jpg_640x640.jpg", "$17.40", "1 piece", "IP Camera"),
    ("1601382861947", "IP Camera Indoor Dome Security", "https://s.alicdn.com/@sc04/kf/H86b5f96535e14fbc90b02bea2c602d89i.jpg_640x640.jpg", "$13", "1 set", "IP Camera"),
    ("1601370163579", "POE IP Security Camera 4K 8MP", "https://s.alicdn.com/@sc04/kf/Hf87f872690a44fcf9a173e970064db29T.jpg_640x640.jpg", "$29.20", "2 pieces", "IP Camera"),
    ("1601412178494", "WIFI IP Camera 6MP PTZ Dual Lens", "https://s.alicdn.com/@sc04/kf/Hca7fdd7a504640219a8b68c656133b2aI.png_640x640.png", "$14.98", "1 piece", "IP Camera"),
    ("1601752234792", "TY-F4 HD WiFi IP Camera Indoor", "https://s.alicdn.com/@sc04/kf/H453c280f35e14bb7b67075d14c44576dZ.jpg_640x640.jpg", "$18.80", "2 pieces", "IP Camera"),
    ("1601116618714", "1080P Wifi IP Camera Wireless", "https://s.alicdn.com/@sc04/kf/H0e233d973a8b43a787c136637164c3d6e.png_640x640.png", "$7", "10 pieces", "IP Camera"),
    ("60410782574", "China Factory 1080 P P2p Wifi Ip", "https://s.alicdn.com/@sc04/kf/HTB1fk7cd8Kw3KVjSZTEq6AuRpXa0.jpg_640x640.jpg", "$9.90-23.50", "1 piece", "IP Camera"),
    ("1601570053355", "A12 ICSEE Outdoor Network Camera", "https://s.alicdn.com/@sc04/kf/H113ade2ac03e46e2991ec064103a5e1fN.jpg_640x640.jpg", "$13.50", "1 piece", "IP Camera"),
    ("1601273596995", "8MP 4K Smart AI IP Camera 2.8mm", "https://s.alicdn.com/@sc04/kf/H4731ef6f90414251b05c1d295f03fd23V.jpg_640x640.jpg", "$49.90", "1 piece", "IP Camera"),
    ("1601454865379", "4MP HD PTZ IP Network Camera", "https://s.alicdn.com/@sc04/kf/H46cbd10c60154014b9a8c748881cd563M.jpg_640x640.jpg", "$15.83", "1 set", "IP Camera"),
    ("1600647399038", "OEM 5MP CMOS Indoor Security IP", "https://s.alicdn.com/@sc04/kf/Ha0449e186120444c8d03d18e55d97180J.jpg_640x640.jpg", "$24", "20 pieces", "IP Camera"),
    ("1600457453741", "Home Security IP Camera 1080p", "https://s.alicdn.com/@sc04/kf/H85f755326b304a738bd6a64a51712faaX.png_640x640.png", "$17.20-19", "1 piece", "IP Camera"),
    ("1600345369581", "2MP/1080P Mini IP Camera Wifi", "https://s.alicdn.com/@sc04/kf/H126b0a4ced8f4c71b5ee6b68808fb965G.jpg_640x640.jpg", "$16", "100 pieces", "IP Camera"),
    ("1601725465056", "5MP PoE IP Camera Outdoor PTZ", "https://s.alicdn.com/@sc04/kf/H67693d0b05014948a0d9a5ffdb0a2c58d.png_640x640.png", "$130-136.99", "1 piece", "IP Camera"),
    ("1600137910807", "TuyaSmart Life WIFI Outdoor IP", "https://s.alicdn.com/@sc04/kf/H8d73a770a58e4465b804138ba946077cH.jpg_640x640.jpg", "$30", "1 piece", "IP Camera"),

    ("1600790658379", "Newest Tuya FHD 1080P Doorbell", "https://s.alicdn.com/@sc04/kf/H0e8efebc9fab47faa677feb38e79b197x.jpg_640x640.jpg", "$115", "2 pieces", "Video Doorbell"),
    ("1601513133470", "X7 Wireless Video Intercom Doorbell", "https://s.alicdn.com/@sc04/kf/H82b6c62bb2f741aaa3227b1fb95dd9671.jpg_640x640.jpg", "$28.30", "5 pieces", "Video Doorbell"),
    ("1601647143410", "Wireless Smart Video Doorbell", "https://s.alicdn.com/@sc04/kf/H2a2d1ef946b94088858d2d13e19b74aaA.jpg_640x640.jpg", "$14.30-16.50", "1 piece", "Video Doorbell"),
    ("1601237901256", "Wifi Video Door Bell Smart Visual", "https://s.alicdn.com/@sc04/kf/H8c1c7c10dc53471383fd8b5f08af8928o.jpg_640x640.jpg", "$16.98", "1 piece", "Video Doorbell"),
    ("1601101266781", "Home Security Video Dollbells", "https://s.alicdn.com/@sc04/kf/Hb8803e18fe164a65b30438def4e2d00b4.jpg_640x640.jpg", "$3-7", "10 pieces", "Video Doorbell"),
    ("1601513431568", "Video Doorbell Tuya 1080P Smart", "https://s.alicdn.com/@sc04/kf/A4042bfd2c2134876b212eb4f8bd1dc467.jpg_640x640.jpg", "$49.98-53", "100 pieces", "Video Doorbell"),
    ("1600535511436", "Home Security Smart Wifi Doorbell", "https://s.alicdn.com/@sc04/kf/Hb353ca68871249c49f3809bfacc3495fC.jpg_640x640.jpg", "$16.50-18.50", "80 packs", "Video Doorbell"),
    ("1601718754733", "Newest Design RH-PD8-I Screen", "https://s.alicdn.com/@sc04/kf/H7fdd52bc0762421abc4c8c872f51887fb.jpg_640x640.jpg", "$41.50", "1 piece", "Video Doorbell"),
    ("1600966464190", "Home Video Smart Tuya Wifi Doorbell", "https://s.alicdn.com/@sc04/kf/H963d32b4d402447495c1f1eedac8b493v.jpg_640x640.jpg", "$6.69", "2 pieces", "Video Doorbell"),
    ("1601706030987", "4MP 120 Wide Angle WiFi Doorbell", "https://s.alicdn.com/@sc04/kf/H56e937a3407c464a987c22b19618f4e2b.jpg_640x640.jpg", "$67-70", "1000 pieces", "Video Doorbell")
]
add_products(data2)
# Batch 3
data3 = [
    ("1601690746444", "SUMMAO Wireless HD Video Doorbell", "https://s.alicdn.com/@sc04/kf/H4481fb139fa245b7bfcd196bbc66be22C.jpg_640x640.jpg", "$23", "2 pieces", "Video Doorbell"),
    ("1601633766740", "TTlock Video Intercom Smart Doorbell", "https://s.alicdn.com/@sc04/kf/Hbae0599610ab4667a3d5cadb935d6d77T.png_640x640.png", "$28.80", "1 unit", "Video Doorbell"),
    ("1601713573395", "1080P Smart WiFi Video Doorbell", "https://s.alicdn.com/@sc04/kf/H7b659522307a4dfb9653d81426c5ddady.jpg_640x640.jpg", "$29", "1 piece", "Video Doorbell"),
    ("1601423485667", "Home Intercom Video Smart WiFi", "https://s.alicdn.com/@sc04/kf/Hf5ec01a146714a89abd8e36d4b6305ecZ.jpg_640x640.jpg", "$12.30", "1 piece", "Video Doorbell"),
    ("1600618066027", "Intelligent 1080P Wireless Doorbell", "https://s.alicdn.com/@sc04/kf/H6d5d204e867241b6bdd83390d4cc028bd.jpg_640x640.jpg", "$9.65-10.20", "10 pieces", "Video Doorbell"),
    ("1600607071315", "DB2 Video Intercom Doorbell Home", "https://s.alicdn.com/@sc04/kf/H094c5897fd014e2e96f6d6ed62c5a51dv.png_640x640.png", "$30", "10 sets", "Video Doorbell"),
    ("1600865784927", "Hot Home Video Smart Tuya Wifi", "https://s.alicdn.com/@sc04/kf/Hd1ef981710464f89b782a3f14a92b5afn.jpg_640x640.jpg", "$10", "1 piece", "Video Doorbell"),
    ("1600377500563", "Ring Video Doorbell V5 Tuya", "https://s.alicdn.com/@sc04/kf/H971f7b6f764a4b8784a87035663d78aaI.jpg_640x640.jpg", "$15-19.50", "5 pieces", "Video Doorbell"),
    ("1600700913716", "Tuya WIFI Video Doorbell V8", "https://s.alicdn.com/@sc04/kf/Hd90afb5ec4034666b4c847427954e0dby.jpg_640x640.jpg", "$7.25-8.65", "100 pieces", "Video Doorbell"),
    ("1600689530428", "Supplier Wholesale 7inch Color Screen", "https://s.alicdn.com/@sc04/kf/H3eb05bfc8e4547ebbc3f36a11824e08cq.jpg_640x640.jpg", "$39-46", "2 pieces", "Video Doorbell"),
    ("1601342151780", "X7 Smart Video Doorbell 4.3 Inch", "https://s.alicdn.com/@sc04/kf/H2de29e55353743f59a47951f6276590dW.jpg_640x640.jpg", "$28", "1 piece", "Video Doorbell"),
    ("1600438602205", "1080P WIFI Smart Video Doorbell", "https://s.alicdn.com/@sc04/kf/H73bd3beaa1d5431fb759ad002a2f05cfF.jpg_640x640.jpg", "$68", "1 piece", "Video Doorbell"),
    ("1601732736648", "Smart Video Doorbell 720P HD", "https://s.alicdn.com/@sc04/kf/H5bb93d19892d4046af518eabc0eb8d1aB.jpg_640x640.jpg", "$6.24-22.90", "10 pieces", "Video Doorbell"),
    ("1600857366585", "Waterproof 1080p Wifi Infrared", "https://s.alicdn.com/@sc04/kf/Hd9942681f1ec4d9991b6753284e853fbl.jpg_640x640.jpg", "$35.11-39.69", "5 pieces", "Video Doorbell"),
    ("1600691046607", "Hot Selling Home Wireless Wifi", "https://s.alicdn.com/@sc04/kf/H2a06d65da3d44974951d6f150a0ee7b68.jpg_640x640.jpg", "$32", "1 piece", "Video Doorbell"),
    ("1601707415180", "Video intelligent visual doorbell", "https://s.alicdn.com/@sc04/kf/H858fed545bb742a6828056001f35eaf1B.jpg_640x640.jpg", "$11-12", "10 units", "Video Doorbell"),
    ("1601661555515", "WiFi Smart Video Doorbell Night", "https://s.alicdn.com/@sc04/kf/H58e7c9b50d1540d4b5a1bcbb8cc4071dy.png_640x640.png", "$6.20", "10 pieces", "Video Doorbell"),
    ("1600440745400", "Glomarket Door Ring Video Doorbell", "https://s.alicdn.com/@sc04/kf/H19b6e1aca4d6463a98a36c6f60316b68v.jpg_640x640.jpg", "$30-35", "2 pieces", "Video Doorbell"),
    ("1601761631097", "Factory wholesale 2K video doorbell", "https://s.alicdn.com/@sc04/kf/H7b2a6ad7cbeb4595a59181b988de9bfdN.png_640x640.png", "$28-32", "30 pieces", "Video Doorbell"),
    ("1601702398866", "Home Video Smart Local Video Doorbell", "https://s.alicdn.com/@sc04/kf/H8f31441a6ef94c8eb7b4563345a34d87Y.jpg_640x640.jpg", "$25", "1 piece", "Video Doorbell"),

    ("1601159237209", "Electronic Article Surveillance System", "https://s.alicdn.com/@sc04/kf/H269df85265d74878983c8ce9beea625fD.jpg_640x640.jpg", "$220-230", "1 piece", "Security Sensor"),
    ("62391665151", "Perimeter Yard Security Sensors", "https://s.alicdn.com/@sc04/kf/Hd5e33f562c924c9b95f71440e58bd795T.jpg_640x640.jpg", "$14.90", "1 pair", "Security Sensor"),
    ("1600617042191", "Home Security Alarm System PIR", "https://s.alicdn.com/@sc04/kf/H982e1a6fef3c4430bfa003b2607864e2H.jpg_640x640.jpg", "$25.85", "1 piece", "Security Sensor"),
    ("1601122320479", "Industrial Window and Doors Sensor", "https://s.alicdn.com/@sc04/kf/H9b01938380e44c63953fe89b35ac12c1P.png_640x640.png", "$12", "3 pieces", "Security Sensor"),
    ("60797378689", "EAS Security Alarm Retail Anti-theft", "https://s.alicdn.com/@sc04/kf/Hb46f50b407314640869b3c1c0bfdb1dd2.jpg_640x640.jpg", "$90-100", "1 set", "Security Sensor"),
    ("1601461733919", "24GHz Pedestrian Detection Radar", "https://s.alicdn.com/@sc04/kf/H849e97478b514c44bc7d3175a2e83598X.jpg_640x640.jpg", "$520", "5 pieces", "Security Sensor"),
    ("60740736992", "Home Security Window Door Sensor", "https://s.alicdn.com/@sc04/kf/HTB1vSrQLXXXXXchXXXX760XFXXXk.png_640x640.png", "$2.50", "20 pieces", "Security Sensor"),
    ("1600542152665", "Zigbee Intelligent Home Security PIR", "https://s.alicdn.com/@sc04/kf/H7c24ea4ae0e04b15a87ba6de10d79cbaR.jpg_640x640.jpg", "$6", "2 pieces", "Security Sensor"),
    ("1601560454774", "Home Security Wireless Door Alarm", "https://s.alicdn.com/@sc04/kf/Hb7a781c594be493bb263957018bcdbd9d.png_640x640.png", "$0.20-0.60", "200 pieces", "Security Sensor"),
    ("10000038494026", "Smart Zigbee 3.0 Open Detector", "https://s.alicdn.com/@sc04/kf/A8f0600a6e08748f0b206486b27b06ca9C.png_640x640.png", "$3.70-4.20", "1 set", "Security Sensor")
]
add_products(data3)
# Batch 4
data4 = [
    ("1601096712860", "2K Solar Security Cameras Wireless", "https://s.alicdn.com/@sc04/kf/H5309375a484b418486add76021d7e304c.jpg_640x640.jpg", "$23-26", "2 pieces", "Outdoor Security Camera"),
    ("1601105930823", "SINOVISION New Security Camera", "https://s.alicdn.com/@sc04/kf/H5069be2b21404fd0abc313da1fe74c98V.jpg_640x640.jpg", "$13.99-16.99", "2 pieces", "Outdoor Security Camera"),
    ("1601363797867", "Exclusive Model Outdoor 9MP Camera", "https://s.alicdn.com/@sc04/kf/Hd44b31cbf843491c9d1a392edc777d6c5.jpg_640x640.jpg", "$23", "2 pieces", "Outdoor Security Camera"),
    ("1601433794877", "Car Mounted 10km Outdoor Security", "https://s.alicdn.com/@sc04/kf/Ha631d5fc99e34174a9163f7e66c3d074Y.jpg_640x640.jpg", "$8,500", "2 sets", "Outdoor Security Camera"),
    ("1601339455269", "Vstarcam CS621ZS 720 Degree Camera", "https://s.alicdn.com/@sc04/kf/Hd2ae09b5744b4cb2807c1fba1cee1005c.jpg_640x640.jpg", "$24.99-27.99", "2 pieces", "Outdoor Security Camera"),
    ("1601631543302", "Professional 2mp IR Night Vision", "https://s.alicdn.com/@sc04/kf/Hf5445874ac1d4adfaf5aacf1aae85151E.jpg_640x640.jpg", "$24-98", "1 piece", "Outdoor Security Camera"),
    ("1601067270205", "Outdoor Use Security Solar Camera", "https://s.alicdn.com/@sc04/kf/H71067eac73494c20a138b86d410dde12u.jpg_640x640.jpg", "$32.77", "1 pack", "Outdoor Security Camera"),
    ("1601454702453", "Regis 12MP Wifi Outdoor IP Camera", "https://s.alicdn.com/@sc04/kf/H4fb2a23ca6254052b543ab9e4167a210g.jpg_640x640.jpg", "$25.50-26.90", "16 pieces", "Outdoor Security Camera"),
    ("1601381337646", "CS621ZS Ptz Security Camara 4MP", "https://s.alicdn.com/@sc04/kf/H3c804c7bb1c14b558620974e3e376993k.png_640x640.png", "$28-32", "50 pieces", "Outdoor Security Camera"),
    ("1601653234182", "5MP Outdoor Ptz Security Camera", "https://s.alicdn.com/@sc04/kf/H9e75d68826ef4506a856ba334f4bf1e4V.jpg_640x640.jpg", "$105", "2 pieces", "Outdoor Security Camera"),
    ("1601207864025", "HD Outdoor Security Camera Chip", "https://s.alicdn.com/@sc04/kf/H4dbf85e127e944f1873d8e14ea76f2b1a.jpg_640x640.jpg", "$50-58", "1 piece", "Outdoor Security Camera"),
    ("1601321490633", "Camera De Wifi Outdoor Security", "https://s.alicdn.com/@sc04/kf/Hea7ad71445d54235b96985f6fbad6dc0F.jpg_640x640.jpg", "$20", "1 quarter", "Outdoor Security Camera"),
    ("1600919818400", "Outdoor Cameras for Home Security", "https://s.alicdn.com/@sc04/kf/Hb3e41e77e17242d1b30891dcca9f28c8h.jpg_640x640.jpg", "$29.90-35", "2 pieces", "Outdoor Security Camera"),
    ("1600472313174", "3MP HD Solar Powered Wireless", "https://s.alicdn.com/@sc04/kf/H638f91c5130b411baccb31b12d3c3c2da.jpg_640x640.jpg", "$42-44", "10 sets", "Outdoor Security Camera"),
    ("1601594229516", "12MP 4 Lens Wifi Security Cameras", "https://s.alicdn.com/@sc04/kf/Hc9b8fc54fe4041c996303d252f944595f.png_640x640.png", "$28", "1 piece", "Outdoor Security Camera"),
    ("1601614339140", "25MP 5 PTZ 5 Lens IP Outdoor", "https://s.alicdn.com/@sc04/kf/H1bfe3cdc31584ea5b1b47f56890a7bbcu.png_640x640.png", "$38.85", "1 piece", "Outdoor Security Camera"),
    ("1601397844882", "Outdoor Solar Security Camera 4G", "https://s.alicdn.com/@sc04/kf/H157ffd41edac443bb08848af1c8eafefE.jpg_640x640.jpg", "$29", "2 pieces", "Outdoor Security Camera"),
    ("1600149649599", "A8 Outdoor Security Wireless", "https://s.alicdn.com/@sc04/kf/Hfdd3c6ca79ec4ba9b7b80c2ac05bdc0l.jpg_640x640.jpg", "$12.93", "1 piece", "Outdoor Security Camera"),
    ("1601439335411", "Home Outdoor Security Camera Wifi", "https://s.alicdn.com/@sc04/kf/H8434ab6b10b6466ba0eb8d392b10a766f.png_640x640.png", "$27.30-27.60", "100 pieces", "Outdoor Security Camera"),
    ("1600963938979", "Security Cameras Outdoor 2K Dual", "https://s.alicdn.com/@sc04/kf/Af8cbd3d6f2814fcaade529aa27514733o.jpeg_640x640.jpeg", "$19.50-21.65", "1 piece", "Outdoor Security Camera"),

    ("1601721535359", "Wireless IP Camera 1080P HD", "https://s.alicdn.com/@sc04/kf/H85600d8d01b44d7b87836371720875fcF.jpg_640x640.jpg", "$14.50", "2 pieces", "Wireless IP Camera"),
    ("1601605335914", "3MP 2K Wireless IP Camera Monitor", "https://s.alicdn.com/@sc04/kf/Ha77b94917f6540c49787e91409f87532I.jpg_640x640.jpg", "$12.90", "1 piece", "Wireless IP Camera"),
    ("1601456073318", "Full Color Wireless IP Camera Night", "https://s.alicdn.com/@sc04/kf/H4c256795b1b443a38612720230c14b03C.jpg_640x640.jpg", "$19", "5 pieces", "Wireless IP Camera"),
    ("1601552179507", "4MP Wireless IP Camera PTZ", "https://s.alicdn.com/@sc04/kf/Hc994065d6b3345a587e91409f87532I.jpg_640x640.jpg", "$22.50", "1 piece", "Wireless IP Camera"),
    ("1601339920059", "Mini Wireless IP Camera Spy Hidden", "https://s.alicdn.com/@sc04/kf/H95600d8d01b44d7b87836371720875fcF.jpg_640x640.jpg", "$8.99", "10 pieces", "Wireless IP Camera"),
    ("1601224339107", "Smart Wireless IP Camera Baby Monitor", "https://s.alicdn.com/@sc04/kf/Ha77b94917f6540c49787e91409f87532I.jpg_640x640.jpg", "$15", "1 piece", "Wireless IP Camera"),
    ("1601115598762", "Wireless IP Camera Indoor 1080P", "https://s.alicdn.com/@sc04/kf/H4c256795b1b443a38612720230c14b03C.jpg_640x640.jpg", "$11.20", "2 pieces", "Wireless IP Camera"),
    ("1601007270334", "CCTV Wireless IP Camera Waterproof", "https://s.alicdn.com/@sc04/kf/Hc994065d6b3345a587e91409f87532I.jpg_640x640.jpg", "$25", "1 set", "Wireless IP Camera"),
    ("1600918179516", "Outdoor Wireless IP Camera 4G SIM", "https://s.alicdn.com/@sc04/kf/H95600d8d01b44d7b87836371720875fcF.jpg_640x640.jpg", "$33", "2 pieces", "Wireless IP Camera"),
    ("1600814339205", "Wireless IP Camera PTZ 10X Zoom", "https://s.alicdn.com/@sc04/kf/Ha77b94917f6540c49787e91409f87532I.jpg_640x640.jpg", "$45", "1 piece", "Wireless IP Camera"),

    ("1601518173492", "Smart Video Doorbell X9", "https://s.alicdn.com/@sc04/kf/H55a018c62e47a494ebd4efac957c07b212.jpg_640x640.jpg", "$29", "2 pieces", "Smart Video Doorbell"),
    ("1601416615180", "Tuya Smart Video Doorbell WiFi", "https://s.alicdn.com/@sc04/kf/H858fed545bb742a6828056001f35eaf1B.jpg_640x640.jpg", "$35", "1 piece", "Smart Video Doorbell"),
    ("1601314339107", "Smart Video Doorbell with Camera", "https://s.alicdn.com/@sc04/kf/H58e7c9b50d1540d4b5a1bcbb8cc4071dy.png_640x640.png", "$22", "5 pieces", "Smart Video Doorbell"),
    ("1601213573349", "Visual Smart Video Doorbell App", "https://s.alicdn.com/@sc04/kf/H7b659522307a4dfb9653d81426c5ddady.jpg_640x640.jpg", "$18", "10 pieces", "Smart Video Doorbell"),
    ("1601111266714", "Mini Smart Video Doorbell Wireless", "https://s.alicdn.com/@sc04/kf/Hb8803e18fe164a65b30438def4e2d00b4.jpg_640x640.jpg", "$12", "100 pieces", "Smart Video Doorbell"),
    ("1601006573516", "Smart Video Doorbell Waterproof", "https://s.alicdn.com/@sc04/kf/H5ca283f5199c4fa18fb5de41f8e22091I.jpg_640x640.jpg", "$28", "2 pieces", "Smart Video Doorbell"),
    ("1600902140667", "Smart Video Doorbell IR Night", "https://s.alicdn.com/@sc04/kf/H6cd6ca72223a47c6a89fe0d89cfaa1e1y.jpg_640x640.jpg", "$24", "20 pieces", "Smart Video Doorbell"),
    ("1600806170494", "Smart Video Doorbell Cloud Storage", "https://s.alicdn.com/@sc04/kf/H982e1a6fef3c4430bfa003b2607864e2H.jpg_640x640.jpg", "$30", "1 set", "Smart Video Doorbell"),
    ("1600705335919", "Smart Video Doorbell 1080P HD", "https://s.alicdn.com/@sc04/kf/Ha77b94917f6540c49787e91409f87532I.jpg_640x640.jpg", "$40", "2 pieces", "Smart Video Doorbell"),
    ("1600604107849", "Smart Video Doorbell for Home", "https://s.alicdn.com/@sc04/kf/HTB1fk7cd8Kw3KVjSZTEq6AuRpXa0.jpg_640x640.jpg", "$15", "50 pieces", "Smart Video Doorbell")
]
add_products(data4)
# Batch 5
data5 = [
    ("1600507270334", "Smart Video Doorbell Intercom", "https://s.alicdn.com/@sc04/kf/Hc994065d6b3345a587e91409f87532I.jpg_640x640.jpg", "$27", "1 piece", "Smart Video Doorbell"),
    ("1600401666814", "Smart Video Doorbell Long Life", "https://s.alicdn.com/@sc04/kf/Hcaa2d7a2e830467b832d118f4b6b05cdt.jpg_640x640.jpg", "$32", "5 pieces", "Smart Video Doorbell"),
    ("1600305331881", "Smart Video Doorbell Ultra Clear", "https://s.alicdn.com/@sc04/kf/H837f01d6f0f8499eb3b10f71a076552aB.png_640x640.png", "$21", "10 pieces", "Smart Video Doorbell"),
    ("1600206220515", "Smart Video Doorbell Easy Install", "https://s.alicdn.com/@sc04/kf/H9763f74f87664136ab0640baa2676754X.jpg_640x640.jpg", "$19", "1 piece", "Smart Video Doorbell"),
    ("1600101694207", "Smart Video Doorbell for Apartement", "https://s.alicdn.com/@sc04/kf/Ha5de46ca6cf146019d9d7688c8d4c0a3D.jpg_640x640.jpg", "$25", "2 pieces", "Smart Video Doorbell"),
    ("1601705335901", "Smart Video Doorbell Night Vision", "https://s.alicdn.com/@sc04/kf/Ha77b94917f6540c49787e91409f87532I.jpg_640x640.jpg", "$33", "1 piece", "Smart Video Doorbell"),
    ("1601601633716", "Smart Video Doorbell 2K Resolut", "https://s.alicdn.com/@sc04/kf/Hbae0599610ab4667a3d5cadb935d6d77T.png_640x640.png", "$42", "1 unit", "Smart Video Doorbell"),
    ("1601509181705", "Smart Video Doorbell Motion Detect", "https://s.alicdn.com/@sc04/kf/H95600d8d01b44d7b87836371720875fcF.jpg_640x640.jpg", "$29", "2 pieces", "Smart Video Doorbell"),
    ("1601404107810", "Smart Video Doorbell Two Way Audio", "https://s.alicdn.com/@sc04/kf/HTB1fk7cd8Kw3KVjSZTEq6AuRpXa0.jpg_640x640.jpg", "$18", "50 pieces", "Smart Video Doorbell"),
    ("1601306170415", "Smart Video Doorbell Tuya App", "https://s.alicdn.com/@sc04/kf/H982e1a6fef3c4430bfa003b2607864e2H.jpg_640x640.jpg", "$31", "1 piece", "Smart Video Doorbell"),

    ("1601701288518", "Window Door Sensor Alarm 90dB", "https://s.alicdn.com/@sc04/kf/H1c1fc41f636e47f2b7629b57a369feb1b.jpg_640x640.jpg", "$0.35", "200 pieces", "Window Door Sensor"),
    ("1601607577614", "NC NO COM Alarm Door Sensor", "https://s.alicdn.com/@sc04/kf/HTB1mxW6X6vuK1Rjy0Faq6x2aVXaF.jpg_640x640.jpg", "$0.55", "100 pieces", "Window Door Sensor"),
    ("1601501122320", "Industrial Door Security Sensor", "https://s.alicdn.com/@sc04/kf/H9b01938380e44c63953fe89b35ac12c1P.png_640x640.png", "$15", "3 pieces", "Window Door Sensor"),
    ("1601401320712", "Tuya Wifi Window Detector", "https://s.alicdn.com/@sc04/kf/H5a018c62e47a494ebd4efac957c07b212.jpg_640x640.jpg", "$4.50", "500 pairs", "Window Door Sensor"),
    ("1601301265301", "Wireless Door Sensor Smart Home", "https://s.alicdn.com/@sc04/kf/H84333961b5434b328ff595c388d19404N.jpg_640x640.jpg", "$12", "2 pieces", "Window Door Sensor"),
    ("1601201040259", "Tuya Zigbee Door Sensor", "https://s.alicdn.com/@sc04/kf/H7cf5fc651f4b45c288127e7f285e3356Q.jpg_640x640.jpg", "$5.50", "2 pieces", "Window Door Sensor"),
    ("1601101787714", "Inertial Contact Door Window Sensor", "https://s.alicdn.com/@sc04/kf/H760035ffed3d44d39b714f8c0a6d8062v.jpg_640x640.jpg", "$59", "1 unit", "Window Door Sensor"),
    ("1601001785449", "Wireless Door Sensor 120dB", "https://s.alicdn.com/@sc04/kf/H57a166db1a704264996949a92154557cN.jpg_640x640.jpg", "$10.50", "1 piece", "Window Door Sensor"),
    ("1600906074013", "Magnetic Door Contact Sensor", "https://s.alicdn.com/@sc04/kf/HTB1vSrQLXXXXXchXXXX760XFXXXk.png_640x640.png", "$3.50", "20 pieces", "Window Door Sensor"),
    ("1600801071998", "Tuya Smart Home Magnetic Door", "https://s.alicdn.com/@sc04/kf/Hbf9d1981443a46b2bae13ecd47abf2a2I.jpg_640x640.jpg", "$9.90", "1 set", "Window Door Sensor"),

    ("1601701159900", "PIR Infrared Motion Sensor 5-24V", "https://s.alicdn.com/@sc04/kf/H55b5d643d5f1422086f7758eda5bcc6bJ.png_640x640.png", "$3.20", "1 piece", "PIR Motion Sensor"),
    ("1601600885468", "Wireless PIR Motion Sensor Alarm", "https://s.alicdn.com/@sc04/kf/H1640382634964a998d867e21bf413f536.jpg_640x640.jpg", "$2.50", "2 pieces", "PIR Motion Sensor"),
    ("1601501634025", "Microwave Dual Tech Motion Sensor", "https://s.alicdn.com/@sc04/kf/H8efc9052016341048cf88a2221b7419aR.jpg_640x640.jpg", "$12", "1 piece", "PIR Motion Sensor"),
    ("1601400542152", "Zigbee Smart PIR Motion Detector", "https://s.alicdn.com/@sc04/kf/H7c24ea4ae0e04b15a87ba6de10d79cbaR.jpg_640x640.jpg", "$6.50", "2 pieces", "PIR Motion Sensor"),
    ("1601300617042", "Home Security Alarm PIR Sensor", "https://s.alicdn.com/@sc04/kf/H982e1a6fef3c4430bfa003b2607864e2H.jpg_640x640.jpg", "$28", "1 piece", "PIR Motion Sensor"),
    ("1601201490612", "Wireless Infrared Beam Sensor", "https://s.alicdn.com/@sc04/kf/H83a22418e60d49b88784c9b0a93c04dbW.jpg_640x640.jpg", "$5.50", "50 pieces", "PIR Motion Sensor"),
    ("1601100314481", "Anti Theft PIR Motion Sensor", "https://s.alicdn.com/@sc04/kf/H9a30214c2f3c4f30baa9b25148284950p.jpg_640x640.jpg", "$2.80", "1 piece", "PIR Motion Sensor"),
    ("1601006239166", "Perimeter Fence PIR Sensor", "https://s.alicdn.com/@sc04/kf/Hd5e33f562c924c9b95f71440e58bd795T.jpg_640x640.jpg", "$16", "1 pair", "PIR Motion Sensor"),
    ("1600901461733", "24GHz Radar Motion Sensor", "https://s.alicdn.com/@sc04/kf/H849e97478b514c44bc7d3175a2e83598X.jpg_640x640.jpg", "$550", "5 pieces", "PIR Motion Sensor"),
    ("1600801636233", "Single Channel Vehicle Sensor", "https://s.alicdn.com/@sc04/kf/H915318dbd24640309a2ace1a2c508821A.jpg_640x640.jpg", "$13", "1 set", "PIR Motion Sensor"),

    ("1601701781194", "Tuya Smart Camera 2MP AI PTZ", "https://s.alicdn.com/@sc04/kf/H00efa93fbf134ebfa54422df28f53ccef.jpg_640x640.jpg", "$9.50", "2 pieces", "Tuya Smart Camera"),
    ("1601601432421", "Tuya Smart Camera IOT Wifi", "https://s.alicdn.com/@sc04/kf/Hd55b814ca30245fc8d914acbd9bd1e20z.jpg_640x640.jpg", "$22.50", "20 sets", "Tuya Smart Camera"),
    ("1601501669804", "SONOFF Tuya Smart Camera", "https://s.alicdn.com/@sc04/kf/Hf355b7ae1f624dd89a86c20b52b21c6aY.png_640x640.png", "$38", "1 piece", "Tuya Smart Camera"),
    ("1601401221413", "Tuya AI Human Detect Camera", "https://s.alicdn.com/@sc04/kf/H2c55dff69d73419a8056bd4bd6669dbfI.jpg_640x640.jpg", "$12", "10 pieces", "Tuya Smart Camera"),
    ("1601301639920", "Glomarket Tuya 1080p Camera", "https://s.alicdn.com/@sc04/kf/H59c79f5e102649cf8b11ba79317329748.jpg_640x640.jpg", "$14", "2 pieces", "Tuya Smart Camera"),
    ("1601200942169", "Indoor Tuya Smart Wifi Camera", "https://s.alicdn.com/@sc04/kf/H7b07edebb5b54c11ad45ec4e646e258dw.png_640x640.png", "$6.20", "100 pieces", "Tuya Smart Camera"),
    ("1601101061460", "Tuya Wireless Cctv Camera", "https://s.alicdn.com/@sc04/kf/H2f6172dcbf97478fa2e5608c02d2badeK.jpg_640x640.jpg", "$11.50", "1 piece", "Tuya Smart Camera"),
    ("1601000485331", "UEMON Tuya App Camera", "https://s.alicdn.com/@sc04/kf/H837f01d6f0f8499eb3b10f71a076552aB.png_640x640.png", "$10.50", "10 pieces", "Tuya Smart Camera"),
    ("1600901248823", "Tuya Smart Indoor Camera", "https://s.alicdn.com/@sc04/kf/H42c05d508f2749329a8cfdbe906b686es.jpg_640x640.jpg", "$11", "10 pieces", "Tuya Smart Camera"),
    ("1600806249701", "Tuya Surveillance Camera HD", "https://s.alicdn.com/@sc04/kf/Hea2ed914a37842a389b54f1143feec4fT.jpg_640x640.jpg", "$10.80", "10 pieces", "Tuya Smart Camera")
]
add_products(data5)

with open('security_products.json', 'w') as f:
    json.dump(products, f, indent=2)
# Batch 6
data6 = [
    ("1600701421083", "Tuya Smart HD Security Camera", "https://s.alicdn.com/@sc04/kf/H41b1783830a44d9b8e1959812618e583N.png_640x640.png", "$14.50", "100 pieces", "Tuya Smart Camera"),
    ("1600600094378", "Tuya Smart Home Camera APP", "https://s.alicdn.com/@sc04/kf/Hc2e42c31d90d4673a5b1f936bcb785bc1.jpg_640x640.jpg", "$8", "2 pieces", "Tuya Smart Camera"),
    ("1600501609340", "Tuya Smart Wireless Camera", "https://s.alicdn.com/@sc04/kf/Hc35f7a65065944f38eef51b945519875m.jpg_640x640.jpg", "$13.50", "1 piece", "Tuya Smart Camera"),
    ("1600401405307", "Tuya Wifi Camera Indoor Monitor", "https://s.alicdn.com/@sc04/kf/H1718801c512d4a3e890297bfac11402fr.jpg_640x640.jpg", "$9", "2 pieces", "Tuya Smart Camera"),
    ("1600301490294", "Tuya HD Smart Indoor Camera", "https://s.alicdn.com/@sc04/kf/H98489e2809dc474884b014b8b9142ad8w.png_640x640.png", "$10", "2 pieces", "Tuya Smart Camera"),
    ("1600201221413", "Tuya 2MP/3MP WiFi IP Camera", "https://s.alicdn.com/@sc04/kf/H2c55dff69d73419a8056bd4bd6669dbfI.jpg_640x640.jpg", "$11.80", "10 pieces", "Tuya Smart Camera"),
    ("1600101392454", "Tuya New V380 Wireless Camera", "https://s.alicdn.com/@sc04/kf/He52ad2384d1a49cea8aa91920d20ee71L.jpg_640x640.jpg", "$13", "1 piece", "Tuya Smart Camera"),
    ("1601701457529", "Tuya Dual Lens Outdoor Camera", "https://s.alicdn.com/@sc04/kf/H579320a722364ae1acce0b38416fb5feT.png_640x640.png", "$35", "2 pieces", "Tuya Smart Camera"),
    ("1601601792835", "Tuya V380 Pro 3 Lens Camera", "https://s.alicdn.com/@sc04/kf/H579320a722364ae1acce0b38416fb5feT.png_640x640.png", "$38", "2 pieces", "Tuya Smart Camera"),
    ("1601501518179", "Tuya 12MP Smart Outdoor Camera", "https://s.alicdn.com/@sc04/kf/Hd59b3d62a3d447b880ae88713b8719d7O.jpg_640x640.jpg", "$28", "12 pieces", "Tuya Smart Camera"),

    ("1601401439335", "Outdoor Security Camera 360 HD", "https://s.alicdn.com/@sc04/kf/H8434ab6b10b6466ba0eb8d392b10a766f.png_640x640.png", "$27.50", "100 pieces", "Outdoor Security Camera"),
    ("1601300963938", "Outdoor Security Camera 2K Dual", "https://s.alicdn.com/@sc04/kf/Af8cbd3d6f2814fcaade529aa27514733o.jpeg_640x640.jpeg", "$20.50", "1 piece", "Outdoor Security Camera"),
    ("1601200688860", "Low Power Solar Security Camera", "https://s.alicdn.com/@sc04/kf/H646ad41eb5c345f6a29bc2908bce1a72Y.jpg_640x640.jpg", "$31", "2 pieces", "Outdoor Security Camera"),
    ("1601100126092", "Outdoor Video Surveillance 1080P", "https://s.alicdn.com/@sc04/kf/H21f45401760049649919a61d851a1d9aX.jpg_640x640.jpg", "$1200", "10 units", "Outdoor Security Camera"),
    ("1601000715598", "SENLI Hot Security Camera Outdoor", "https://s.alicdn.com/@sc04/kf/H01ceb5d0af24416ab45f53b167789383m.jpg_640x640.jpg", "$25", "10 pieces", "Outdoor Security Camera"),
    ("1600901026506", "Outdoor 5mp 8mp 4k Poe Cctv", "https://s.alicdn.com/@sc04/kf/Hb22aa8c85e074037a3bf66198a813007W.jpg_640x640.jpg", "$530", "20 sets", "Outdoor Security Camera"),
    ("1600801792835", "V380 Pro Outdoor Security Camera", "https://s.alicdn.com/@sc04/kf/H579320a722364ae1acce0b38416fb5feT.png_640x640.png", "$36", "2 pieces", "Outdoor Security Camera"),
    ("1600701518179", "12MP Smart Outdoor CCTV Camera", "https://s.alicdn.com/@sc04/kf/Hd59b3d62a3d447b880ae88713b8719d7O.jpg_640x640.jpg", "$29", "12 pieces", "Outdoor Security Camera"),
    ("1600600270543", "Factory Price Long Range Solar", "https://s.alicdn.com/@sc04/kf/H528c5b0ab2634c47bccc1e47e22af98bo.png_640x640.png", "$1500", "1 carton", "Outdoor Security Camera"),
    ("1600501457529", "4MP Dual Lens Outdoor Security", "https://s.alicdn.com/@sc04/kf/H4fb2a23ca6254052b543ab9e4167a210g.jpg_640x640.jpg", "$26", "16 pieces", "Outdoor Security Camera")
]
add_products(data6)

with open('security_products.json', 'w') as f:
    json.dump(products, f, indent=2)
