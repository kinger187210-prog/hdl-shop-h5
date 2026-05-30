import json
import os

thermal_underwear = [
    {"name": "Men Thermal Underwear Sets", "link": "https://www.alibaba.com/showroom/men-thermal-underwear-sets.html"},
    {"name": "Mens Thermal Underwear Sets Base Layer Warm", "link": "https://m.alibaba.com/showroom/mens-thermal-underwear-sets-base-layer-warm.html"},
    {"name": "Womens Thermal Underwear Sets", "link": "https://m.alibaba.com/showroom/womens-thermal-underwear-sets.html"},
    {"name": "Factory Direct Men's Thermal Underwear Sets With Cotton", "link": "https://www.alibaba.com/product-detail/Factory-Direct-Men-s-Thermal-Underwear_1600431858134.html"},
    {"name": "100 Cotton Thermal Underwear Sets", "link": "https://www.alibaba.com/supplier/100-cotton-thermal-underwear-sets.html"},
    {"name": "Wholesale High Quality De Velvet Men's and Women's Thermal Underwear Sets", "link": "https://www.alibaba.com/product-detail/Wholesale-High-Quality-De-Velvet-Men_1601273017670.html"},
    {"name": "AI-MICH Thermal Underwear Sets", "link": "https://www.alibaba.com/product-detail/AI-MICH-Thermal-Underwear-Set-Factory_1600864229901.html"},
    {"name": "Thermal Underwear Set Unisex Winter Sporty Full-Length Tight-Fitting", "link": "https://www.alibaba.com/product-detail/Thermal-Underwear-Set-Unisex-Winter-Sporty_1601725936879.html"},
    {"name": "Women Slim Thermal Underwear Set Ultra Thin Stretchy", "link": "https://www.alibaba.com/product-detail/Women-Slim-Thermal-Underwear-Set-Ultra_1601249743844.html"},
    {"name": "Thermal Underwear Set Men's and Women's Warm Ski Home", "link": "https://www.alibaba.com/product-detail/Thermal-Underwear-Set-Hot-Sale-Men_1601725929890.html"},
    {"name": "Heated Thermal Underwear for Men Women 30 Zones", "link": "https://www.alibaba.com/product-detail/Heated-Thermal-Underwear-for-Men-Women_10000032872020.html"},
    {"name": "37 Degree Thermal Underwear - One Size Fits All Long", "link": "https://www.alibaba.com/product-detail/women-and-men-37-degree-constant_62416322633.html"},
    {"name": "New Hot Selling Women Thermal Underwear Set Warm", "link": "https://www.alibaba.com/product-detail/New-Hot-Selling-Women-Thermal-Underwear_1600327025136.html"},
    {"name": "Men's Thermal Underwear Set Breathable Heated Long Johns", "link": "https://www.alibaba.com/product-detail/Wholesale-Heated-Mens-Long-Johns-Men_1600933826647.html"},
    {"name": "Thermal Underwear Set Female Seamless Women and", "link": "https://www.alibaba.com/product-detail/Thermal-Underwear-Set-Female-Seamless-Women_1600431374624.html"},
    {"name": "ESDY Outdoor Sports Thermal Underwear Set for Hunting", "link": "https://www.alibaba.com/product-detail/ESDY-Outdoor-Sports-Thermal-Underwear-Set_1600347915728.html"},
    {"name": "HUAYILI Men's Thermal Underwear Set - Quick Dry & Warm", "link": "https://www.alibaba.com/product-detail/HUAYILI-Men-s-Thermal-Underwear-Set_60785524880.html"},
    {"name": "Custom Men's Thermal Underwear Bamboo Viscose Long Johns Set", "link": "https://www.alibaba.com/product-detail/Custom-Men-s-Thermal-Underwear-Bamboo_1601691642743.html"},
    {"name": "Men's Thermal Underwear Set Thick Long-John Style Winter", "link": "https://www.alibaba.com/product-detail/Men-s-Thermal-Underwear-Set-Thick_1601671878023.html"},
    {"name": "Wholesale High Quality Men's Thermal Underwear Set", "link": "https://www.alibaba.com/product-detail/Wholesale-High-Quality-Men-s-Boxers_10000030070691.html"},
    {"name": "Men's Thermal Underwear Set - Breathable and Cozy", "link": "https://www.alibaba.com/product-detail/thermal-underwear-for-men-set-under_1600081690938.html"},
    {"name": "Soft Velvet Lined Long Johns Men Thermal Underwear Set", "link": "https://www.alibaba.com/product-detail/Soft-Velvet-Lined-Long-Johns-Men_1601632531762.html"},
    {"name": "Men's Thermal Underwear Set Winter Ski Gear Breathable", "link": "https://www.alibaba.com/product-detail/Mens-Thermal-Underwear-Set-Winter-Ski_1601278477976.html"},
    {"name": "Thermal Underwear for Men Long Johns with Fleece Lined", "link": "https://germany.alibaba.com/product-detail/Thermal-Underwear-for-Men-Long-Johns_10000023965979.html"},
    {"name": "Women's Thermal Underwear Set - Long Johns with Fleece Lined", "link": "https://www.alibaba.com/product-detail/Women-s-Thermal-Underwear-Set-Long_1600075327573.html"},
    {"name": "Underwear Set Maden Women's Thermal Underwear Set", "link": "https://www.alibaba.com/product-detail/Underwear-Set-Maden-Women-s-Thermal_1601692768523.html"},
    {"name": "Women's Autumn Winter Thermal Underwear Set", "link": "https://www.alibaba.com/product-detail/Women-s-Autumn-Winter-Thermal-Underwear_1601273348380.html"},
    {"name": "Thickened Long Johns Thermal Underwear for Men", "link": "https://www.alibaba.com/product-detail/Thickened-Long-Johns-Thermal-Underwear-for_1600635137567.html"},
    {"name": "Evenyoung Women Thermal Underwear Set", "link": "https://spanish.alibaba.com/product-detail/Evenyoung-Women-Thermal-Underwear-Set-Hyaluronic-1601667455885.html"},
    {"name": "Fitness and Training Gym Clothes Men Women Thermal Underwear Set", "link": "https://www.alibaba.com/product-detail/Fitness-and-Training-Gym-Clothes-Activewear_1601216550944.html"},
    {"name": "Super Cozy Women's Underwear Thermal Keep Warm", "link": "https://www.alibaba.com/product-detail/Super-Cozy-Women-s-Underwear-Thermal_60717381513.html"},
    {"name": "Breathable Men's Winter Thermal Underwear Long Sleeve", "link": "https://www.alibaba.com/product-detail/Plus-size-Men-s-Warm-Underwear_1601597383857.html"},
    {"name": "Men's Women's Winter Thermal Suit – 37-Degree Long", "link": "https://www.alibaba.com/product-detail/Clothing-Men-Woman-Winter-Thermal-Suit_1600647419296.html"},
    {"name": "GECKO MASTER Seamless Thermal Underwear - Merino", "link": "https://www.alibaba.com/product-detail/GECKO-MASTER-Seamless-Thermal-underwear-long_1600380799468.html"},
    {"name": "Hongbo 2025 Men's Cotton Print Bamboo Pyjama Thermal Underwear", "link": "https://www.alibaba.com/product-detail/Hongbo-2025-Men-s-Cotton-Print_1601443291774.html"},
    {"name": "Alpine PRO Women's Winter Sports Underwear", "link": "https://www.alibaba.com/product-detail/Alpine-PRO-Women-s-Winter-Sports_1601020771924.html"},
    {"name": "Winter Base Layer Clothing For Men Thicken Velvet Thermal Underwear", "link": "https://www.alibaba.com/product-detail/Winter-Base-Layer-Clothing-For-Men_1601632544681.html"},
    {"name": "Winter Base Layer Set For Men Thicken Velvet Thermal Underwear", "link": "https://www.alibaba.com/product-detail/Winter-Base-Layer-Set-For-Men_1601632575613.html"},
    {"name": "Thermal Dry Custom Winter Base Layer Sports Running", "link": "https://germany.alibaba.com/product-detail/Thermal-Dry-Custom-Winter-Base-Layer_11000025888828.html"},
    {"name": "Body Suit Pajamas Thicken Top and Bottom Set Winter Base Layer", "link": "https://www.alibaba.com/product-detail/body-suit-pajamas-thicken-top-and_62171158013.html"},
    {"name": "Plush Velvet Lined Long Johns Set Men Thermal Underwear", "link": "https://www.alibaba.com/product-detail/Plush-Velvet-Lined-Long-Johns-Set_1601632553670.html"},
    {"name": "Wholesale Performance Comfort Skins Nylon Cotton Unisex Long Johns", "link": "https://www.alibaba.com/product-detail/Wholesale-Performance-Comfort-Skins-Nylon-Cotton_1600567653359.html"},
    {"name": "Unisex Thermal Long Johns Polyester Winter", "link": "https://korean.alibaba.com/product-detail/Unisex-Thermal-Long-Johns-Polyester-Winter-1600663786114.html"},
    {"name": "Warm Thermal Long Johns For Men Thicken Velvet Lined Underwear Set", "link": "https://www.alibaba.com/product-detail/Warm-Thermal-Long-Johns-For-Men_1601632563634.html"},
    {"name": "Warm Thermal Long Johns Set For Men Thicken Velvet Lined Underwear", "link": "https://www.alibaba.com/product-detail/Warm-Thermal-Long-Johns-Set-For_1601632648065.html"},
    {"name": "Warm Thermal Long Johns Set Men Thicken Velvet Lined Underwear", "link": "https://www.alibaba.com/product-detail/Warm-Thermal-Long-Johns-Set-Men_1601632586559.html"},
    {"name": "Convallaria Mens Thermal Underwear Set - Winter Hunting Gear", "link": "https://www.alibaba.com/product-detail/Convallaria-Mens-Thermal-Underwear-Set-with_1601216572153.html"},
    {"name": "Men's Recycled Waffle Thermal Underwear", "link": "https://www.alibaba.com/product-detail/Men-s-Recycled-Waffle-Long-Johns_1601385239896.html"},
    {"name": "Winter Inner Wear Thermal Underwear Long Johns Fleece Lined 2 PCS Set", "link": "https://www.alibaba.com/product-detail/Winter-Inner-Wear-Thermal-Underwear-Long_1601351767208.html"},
    {"name": "N002 Men's Ultra Soft Winter Inner Wear - Thermal Long Johns", "link": "https://www.alibaba.com/product-detail/N002-Men-s-Ultra-Soft-winter_1600339516586.html"}
]

fleece_leggings = [
    {"name": "Womens Fleece Lined Leggings", "link": "https://www.alibaba.com/showroom/womens-fleece-lined-leggings.html"},
    {"name": "Women S Fleece Lined Leggings Pockets", "link": "https://m.alibaba.com/showroom/women-s-fleece-lined-leggings-pockets.html"},
    {"name": "Fleece Lined Leggings Primark", "link": "https://www.alibaba.com/supplier/fleece-lined-leggings-primark.html"},
    {"name": "Fleece Lined Leggings Wholesale", "link": "https://www.alibaba.com/supplier/fleece-lined-leggings-wholesale.html"},
    {"name": "Nexiepoch Fleece Lined Leggings", "link": "https://www.alibaba.com/product-detail/Nexiepoch-Fleece-Lined-Leggings-Women-s_1601227276944.html"},
    {"name": "M 0566 Women Fleece Lined Leggings", "link": "https://www.alibaba.com/product-detail/M-0566-Women-Fleece-Lined-Leggings_1600934686534.html"},
    {"name": "Women's Fleece Lined Leggings Thermal Warm Winter Tights", "link": "https://www.alibaba.com/product-detail/Women-s-Fleece-Lined-Leggings-Thermal_1601613630491.html"},
    {"name": "Multicolor Women Fleece Lined Leggings Ladies High Waist", "link": "https://www.alibaba.com/product-detail/Multicolor-Women-Fleece-Lined-Leggings-Ladies_11000012799974.html"},
    {"name": "Women Fleece Lined Leggings Warm Translucent Winter", "link": "https://www.alibaba.com/product-detail/Women-Fleece-Lined-Leggings-Warm-Translucent_1601558365463.html"},
    {"name": "Twist Micro-Pressure Fleece-Lined Leggings Milk White", "link": "https://www.alibaba.com/product-detail/Twist-Micro-Pressure-Fleece-Lined-Leggings_1601422453273.html"},
    {"name": "SHINBENE 26\" Cold Weather High Waist Yoga Pants", "link": "https://www.alibaba.com/product-detail/SHINBENE-26-Cold-Weather-High-Waist_1601240456846.html"},
    {"name": "Winter Women Warm Pants - Fleece Lined Thermal Leggings", "link": "https://www.alibaba.com/product-detail/Winter-Women-Warm-Pants-Fleece-Lined_1600586527163.html"},
    {"name": "High Waist Black Quality Fleece Sherpa Lined Leggings", "link": "https://www.alibaba.com/product-detail/High-Waist-Black-Quality-Fleece-Sherpa_1600955810036.html"},
    {"name": "Factory Price High Waist Thick Cashmere Pants Winter Warm Thermal Sherpa Lined Leggings", "link": "https://www.alibaba.com/product-detail/Factory-Price-High-Waist-Thick-Cashmere_1601295917264.html"},
    {"name": "X-CHENG Women's Fleece Lined Tights Winter Warm Print", "link": "https://www.alibaba.com/product-detail/X-CHENG-Women-s-Fleece-Lined_1601393545450.html"},
    {"name": "Soft High Waist Women Fitness Warm Leggings Fleece Lined", "link": "https://www.alibaba.com/product-detail/Soft-High-Waist-Women-Fitness-Warm_1600303533418.html"},
    {"name": "Women's Super Soft Winter Leggings High Waisted Thermal", "link": "https://www.alibaba.com/product-detail/Women-s-Super-Soft-Winter-Leggings_1601295228079.html"},
    {"name": "Winter Fleece Lined High Waist Leggings for Women", "link": "https://www.alibaba.com/product-detail/Fleece-Lined-Women-Leggings-Thermal-Pantyhose_1601226034860.html"},
    {"name": "Winter Leggings Women Pantyhose Thermal Stockings", "link": "https://www.alibaba.com/product-detail/Winter-Leggings-Women-Pantyhose-Thermal-Stockings_1601283273663.html"},
    {"name": "Warm Winter Leggings with Fleece and Velvet", "link": "https://www.alibaba.com/product-detail/K1129-Women-winter-leggings-inside-fur_1601148549708.html"},
    {"name": "Ehanking Women's Winter Leggings Thermal Velvet Cotton", "link": "https://www.alibaba.com/product-detail/Ehanking-Women-s-Winter-Leggings-Thermal_1600942213703.html"},
    {"name": "Warm Winter Leggings with Thicken Fur Inside - 200g Fleece", "link": "https://www.alibaba.com/product-detail/200g-Women-Legging-inside-Thicken-Fur_1600149116274.html"},
    {"name": "220g 320g Nylon Winter Leggings", "link": "https://www.alibaba.com/product-detail/220g-320g-Nylon-Thick-Flexible-Winter_1600348236821.html"},
    {"name": "Warm and Stylish: Women's Winter Leggings with Love Print", "link": "https://www.alibaba.com/product-detail/High-Elastic-Pants-Winter-Women-Leggings_1601240827462.html"},
    {"name": "Warm Leggins - Comfortable High Waist Winter Leggings", "link": "https://www.alibaba.com/product-detail/Winter-Leggings-For-Women-Warm-Leggins_1600653326016.html"},
    {"name": "Winter Warm Plush Yoga Pants - High Waist Thermal Leggings", "link": "https://www.alibaba.com/product-detail/Women-s-Winter-Warm-Plush-Yoga_1601296191711.html"},
    {"name": "Women's Solid Bamboo Viscose High Waist Thermal Leggings", "link": "https://www.alibaba.com/product-detail/Custom-Women-Bamboo-Leggings-Womens-Thermal_1601109115808.html"},
    {"name": "Winter Thermal Leggings Women High Waist Stretch Pants", "link": "https://www.alibaba.com/product-detail/Winter-Thermal-Leggings-Women-High-Waist_1601620721735.html"},
    {"name": "YK5115 Women High Waist Thick Thermal Leggings With Pocket", "link": "https://www.alibaba.com/product-detail/YK5115-Women-High-Waist-Thick-Thermal_1601317285848.html"},
    {"name": "Wholesale Fleece Lined Thermal Leggings for Women", "link": "https://www.alibaba.com/product-detail/Wholesale-Sexy-Fake-Transparent-Thermal-Leggings_1600710145562.html"},
    {"name": "80% Polyester 20% Spandex Fleece-Lined Thermal Leggings", "link": "https://www.alibaba.com/product-detail/80-Polyester-20-Spandex-Fleece-Lined_1601603479209.html"},
    {"name": "Women's Thermal Fleece Leggings Winter Warm Pantyhose", "link": "https://www.alibaba.com/product-detail/Women-s-Thermal-Fleece-Leggings-Winter_11000020451879.html"},
    {"name": "Women Fleece Leggings Sexy Translucent Slim Pantyhose", "link": "https://www.alibaba.com/product-detail/Women-Fleece-Leggings-Sexy-Translucent-Slim_1601745787152.html"},
    {"name": "Sherpa Fleece Leggings by Sucaryan", "link": "https://www.alibaba.com/product-detail/Fashion-label-Sherpa-fleece-leggings-for_1601268966312.html"}
]

wool_socks = [
    {"name": "Wool Socks Women S", "link": "https://www.alibaba.com/supplier/wool-socks-women%2527s.html"},
    {"name": "Best Lightweight Wool Socks for Men and Women", "link": "https://m.alibaba.com/showroom/best-lightweight-wool-socks.html"},
    {"name": "Bulk Wool Socks", "link": "https://www.alibaba.com/supplier/bulk-wool-socks.html"},
    {"name": "Merino Wool Socks Supplier", "link": "https://www.alibaba.com/merino-wool-socks-suppliers.html"},
    {"name": "Thermal Wool Socks for Men", "link": "https://www.alibaba.com/product-detail/Mens-Wool-Socks-Thermal-Cozy-Warm_1600386448826.html"},
    {"name": "BX-K577 Handmade Wool Socks", "link": "https://www.alibaba.com/product-detail/BX-K577-handmade-wool-socks_1600466410628.html"},
    {"name": "LINGTU 8213 Wool Socks Thick Warm Winter Unisex", "link": "https://www.alibaba.com/product-detail/LINGTU-8213-Wool-Socks-Thick-Warm_1601550680489.html"},
    {"name": "Autumn and Winter Thickened Warm Wool Socks Solid", "link": "https://www.alibaba.com/product-detail/Autumn-And-Winter-Thickened-Warm-Wool_1600690284728.html"},
    {"name": "Warm Winter Socks - Merino Wool Crews for Men", "link": "https://www.alibaba.com/product-detail/Thermal-Terry-Solid-Color-Crew-Business_1600522313716.html"},
    {"name": "Soft and Warm 100% Australian Wool Socks Embroidered", "link": "https://www.alibaba.com/product-detail/Soft-and-Warm-100-Australian-Wool_1601232666512.html"},
    {"name": "Wholesale Soft Wool Socks for Winter Warmth Thick", "link": "https://www.alibaba.com/product-detail/Wholesale-Soft-Wool-Socks-For-Winter_1601379234002.html"},
    {"name": "Merino Hiking Socks - High Quality Winter Sports Socks", "link": "https://www.alibaba.com/product-detail/High-Quality-Merino-wool-socks-hiking_62365070485.html"},
    {"name": "Winter Solid Color Merino Wool Women Slouch Socks", "link": "https://www.alibaba.com/product-detail/Winter-Solid-Color-Merino-Wool-Women_1600140128992.html"},
    {"name": "Winter Season High Quality Heavy Thick Patchwork Wool Socks", "link": "https://www.alibaba.com/product-detail/Winter-Season-High-Quality-Heavy-Thick_62322002481.html"},
    {"name": "Wholesale Solid Color Thick Merino Wool Socks Winter Warm", "link": "https://www.alibaba.com/product-detail/wholesale-solid-color-thick-merino-wool_1601275889597.html"},
    {"name": "Men's Merino Wool Socks - Ideal for Hiking and Outdoor Work", "link": "https://www.alibaba.com/product-detail/Men-Merino-Wool-Socks-Cushioned-Trekking_1600221462136.html"},
    {"name": "Best-selling Merino Wool Socks Autumn and Winter", "link": "https://www.alibaba.com/product-detail/Best-selling-Merino-Wool-Socks-Autumn_1601712357047.html"},
    {"name": "High Quality Merino Wool Socks - Warm and Eco-friendly", "link": "https://www.alibaba.com/product-detail/High-quality-cashmere-wool-warm-women_1600351125431.html"},
    {"name": "Men's Merino Wool Socks - Hiking Crew Socks with Comfort", "link": "https://www.alibaba.com/product-detail/Men-s-Merino-Wool-socks-Moisture_1600807856998.html"},
    {"name": "Merino Wool Thermal Hiking Socks Non-Slip Shock-Absorbing", "link": "https://www.alibaba.com/product-detail/Merino-wool-socks-Thermal-hiking-socks_1601364719235.html"},
    {"name": "Wholesale Men's Thick Merino Wool Thermal Socks", "link": "https://www.alibaba.com/product-detail/Wholesale-Winter-Thick-Thermal-Work-Heavy_1600647177573.html"},
    {"name": "Winter Breathable Rechargeable Battery Heated Thermal Socks", "link": "https://www.alibaba.com/product-detail/Winter-Breathable-Rechargeable-Battery-Heated-Thermal_1601282812982.html"},
    {"name": "Custom Merino Wool Thermal Socks for Ski Hiking Climbing", "link": "https://www.alibaba.com/product-detail/Custom-Merino-Wool-Thermal-Socks-for_1601223130890.html"},
    {"name": "Heated Socks Winter Electric Washable Casual Knitted", "link": "https://www.alibaba.com/product-detail/Heated-Socks-Winter-Electric-Washable-Casual_1601274445412.html"},
    {"name": "Thermal Socks for Men & Women - Warm, Thick, and Durable", "link": "https://www.alibaba.com/product-detail/Thermal-Socks-for-Men-Women-Warm_1600144007688.html"},
    {"name": "Warm and Cozy Winter Socks - Soft, Thick, and Anti-slip", "link": "https://www.alibaba.com/product-detail/New-Velvet-Women-Winter-Warm-Thicken_1600667917393.html"},
    {"name": "Custom 3 Pairs Warm Thermal Socks for Women & Men", "link": "https://www.alibaba.com/product-detail/3-Pairs-Warm-Thermal-Socks-for_1601293514898.html"},
    {"name": "Low MOQ Cold Resistant Cashmere Socks Women Warm", "link": "https://www.alibaba.com/product-detail/Low-MOQ-Cold-Resistant-Cashmere-Socks_1600379993959.html"},
    {"name": "Best Anti-Slip Men's Thermal Socks Eco-Friendly Breathable", "link": "https://germany.alibaba.com/product-detail/Best-Anti-Slip-Men-s-Thermal_10000024818724.html"},
    {"name": "FN Mens Merino Wool Hiking Socks Thermal Warm Winter", "link": "https://www.alibaba.com/product-detail/FN-Mens-Merino-Wool-Hiking-Socks_1600378493004.html"},
    {"name": "Merino wool hiking socks for cold weather socks warm crew", "link": "https://www.alibaba.com/product-detail/Merino-wool-hiking-socks-for-cold_1601000885088.html"},
    {"name": "Cushioned Crew Boot Socks Thermal Merino Wool Hiking", "link": "https://www.alibaba.com/product-detail/Cushioned-Crew-Boot-Socks-Thermal-Merino_1601600161512.html"},
    {"name": "Womens Stripe Dress Merino Wool Hiking Socks", "link": "https://www.alibaba.com/product-detail/Womens-stripe-dress-Merino-Wool-Hiking_1600937167486.html"},
    {"name": "Customized Merino Wool Hiking Socks - Warm & Durable", "link": "https://www.alibaba.com/product-detail/Customized-Women-Men-Merino-Wool-Hiking_1601304558792.html"},
    {"name": "Wholesale 3 Pairs Outdoor Thick Terry Crew Warm Merino Wool Hiking Socks", "link": "https://www.alibaba.com/product-detail/Wholesale-3-Pairs-Outdoor-Thick-Terry_1601224342118.html"},
    {"name": "Professional Trekking Breathable Thermal Outdoor Merino Wool", "link": "https://germany.alibaba.com/product-detail/Professional-Trekking-Breathable-Thermal-Outdoor-Merino_1601566767762.html"},
    {"name": "Merino Wool Mid Calf Hiking Socks Thickened Terry Sole", "link": "https://russian.alibaba.com/product-detail/Merino-Wool-Mid-Calf-Hiking-Socks-1601752864885.html"},
    {"name": "High Quality Merino Wool Hiking Socks for Winter Sports", "link": "https://www.alibaba.com/product-detail/High-quality-Nordic-Winter-Warm-Adult_1600844987583.html"},
    {"name": "Breathable Bamboo Boot Socks with Terry Loop", "link": "https://www.alibaba.com/product-detail/Men-s-Thermal-Work-Socks-Breathable_1601718317580.html"},
    {"name": "Custom Thick Heavy Duty Thermal Work Socks for Men & Women", "link": "https://www.alibaba.com/product-detail/Custom-Thick-Heavy-Duty-Thermal-Work_1601264739219.html"},
    {"name": "Wholesale Winter Thick Thermal Work Socks Men Warm Merino", "link": "https://www.alibaba.com/product-detail/Wholesale-Winter-Thick-Thermal-Work-Socks_1601261399862.html"},
    {"name": "Custom Moisture Wicking Alpaca Socks Knee High Sports", "link": "https://www.alibaba.com/product-detail/Custom-moisture-wicking-alpaca-socks-knee_1601360239773.html"},
    {"name": "High Quality Alpaca Socks - Warm, Comfortable, and Durable", "link": "https://www.alibaba.com/product-detail/high-quality-alpaca-socks-sport-men_1601043535155.html"},
    {"name": "Classic Men's Alpaca Socks", "link": "https://germany.alibaba.com/product-detail/Classic-Men-s-Alpaca-Socks_10000041229775.html"},
    {"name": "Wholesale Woollen Socks Women's Dotted Yarn Wool", "link": "https://www.alibaba.com/product-detail/Factory-Wholesale-Woollen-Socks-Women-s_1601171719270.html"},
    {"name": "Wholesale Warrior Men's Wool Hiking Socks", "link": "https://www.alibaba.com/product-detail/Warrior-Alpaca-Socks-Men-s-Ultimate_60355880631.html"},
    {"name": "Winter Christmas Socks Knitted Warm Alpaca Socks", "link": "https://www.alibaba.com/product-detail/Winter-christmas-socks-knitted-warm-alpaca_1601341337312.html"},
    {"name": "Hand-knit Alpaca Socks from Cusco Peru", "link": "https://www.alibaba.com/product-detail/Alpaca-Socks-Cusco-Peru-Ppunchay-Peru_1600110522590.html"}
]

winter_gloves = [
    {"name": "Good Men s Winter Gloves", "link": "https://m.alibaba.com/showroom/good-men-s-winter-gloves.html"},
    {"name": "Bulk Winter Gloves", "link": "https://www.alibaba.com/supplier/bulk-winter-gloves.html"},
    {"name": "The Warmest Winter Gloves Of 2025", "link": "https://www.alibaba.com/blog/the-warmest-winter-gloves-of-2025-stay-cozy-in-style-with-these-top-picks.html"},
    {"name": "PEARTWOLF Winter Gloves - Touch Screen", "link": "https://www.alibaba.com/product-detail/Comfortable-winter-warm-gloves-touch-screen_1600417308331.html"},
    {"name": "Winter Gloves for Men Women Upgraded Touch Screen", "link": "https://www.alibaba.com/product-detail/Winter-Gloves-for-Men-Women-Upgraded_1601018557483.html"},
    {"name": "Fashion Windproof Waterproof Warm Winter Gloves Cycling", "link": "https://www.alibaba.com/product-detail/Fashion-windproof-waterproof-warm-winter-gloves_1600618751957.html"},
    {"name": "TRENDOUX Winter Gloves for Men Women Upgraded", "link": "https://www.alibaba.com/product-detail/TRENDOUX-Winter-Gloves-for-Men-Women_1601697094329.html"},
    {"name": "ROCKBROS Winter Gloves Unisex for Outdoor Cold Weather", "link": "https://www.alibaba.com/product-detail/ROCKBROS-Winter-Gloves-Unisex-for-Outdoor_1600644476035.html"},
    {"name": "Couples Hand Holding Heart Mittens Set", "link": "https://www.alibaba.com/product-detail/Couples-Hand-Holding-Heart-Mittens-Set_1601622580636.html"},
    {"name": "Winter Gloves with Touch Screen - Warm & Stylish Protection", "link": "https://www.alibaba.com/product-detail/Winter-Gloves-for-Men-and-Women_1600911572681.html"},
    {"name": "Plain Touchscreen Winter Gloves Sheepskin Ladies", "link": "https://www.alibaba.com/product-detail/Plain-Touchscreen-Winter-Gloves-Sheepskin-Ladies_1601687592185.html"},
    {"name": "One-Piece Seamless, Touchscreen Winter Gloves", "link": "https://www.alibaba.com/product-detail/Knitted-Warm-Gloves-with-Finger-Openings_1601694218652.html"},
    {"name": "Performance Touchscreen Winter Gloves 3M Thinsulate", "link": "https://www.alibaba.com/product-detail/Performance-Touchscreen-Winter-Gloves-3M-Thinsulate_1601674630793.html"},
    {"name": "Winter Ski Outdoor Warm Gloves - Touchscreen & Waterproof", "link": "https://www.alibaba.com/product-detail/Hot-sale-touchscreen-winter-warm-men_1601170526527.html"},
    {"name": "Winter Thermal Work Gloves Non-Slip Rubber Coated", "link": "https://www.alibaba.com/product-detail/Winter-Thermal-Work-Gloves-Non-Slip_1601724548737.html"},
    {"name": "Wholesale Price Electric Heating Gloves for Motorcycle Skiing", "link": "https://www.alibaba.com/product-detail/Wholesale-Price-Electric-Heating-Gloves-for_1601523256444.html"},
    {"name": "Rechargeable Heated Gloves - Perfect for Outdoor Activities", "link": "https://www.alibaba.com/product-detail/Outdoor-Indoor-Rechargeable-Battery-Powered-Heated_1600548032857.html"},
    {"name": "Thin Heated Gloves Rechargeable Ultra Slim Touch Screen", "link": "https://www.alibaba.com/product-detail/Thin-Heated-Gloves-Rechargeable-Ultra-Slim_1601529602470.html"},
    {"name": "Thin Touchscreen Heated Gloves Adjustable Temperature", "link": "https://www.alibaba.com/product-detail/Thin-Heated-Gloves-with-3-Adjustable_1601607501028.html"},
    {"name": "2023 Winter Outdoor Sports Electric Heated Gloves for Men Women", "link": "https://www.alibaba.com/product-detail/2023-Winter-Outdoor-Sports-Electric-Heated_1600802970614.html"},
    {"name": "Wasoto Electric Rechargeable Winter Heated Ski Gloves", "link": "https://www.alibaba.com/product-detail/Wasoto-Low-Price-Adventure-Motorcycle-Skiing_1600885883248.html"},
    {"name": "Best Quality Custom Wholesale Heated Gloves Battery", "link": "https://www.alibaba.com/product-detail/Best-Quality-Custom-Wholesale-Heated-Gloves_1601292569635.html"},
    {"name": "PMA Heated Gloves - Ultimate Winter Sports Gear", "link": "https://www.alibaba.com/product-detail/PMA-Outdoor-Sport-Waterproof-USB-Heated_1601134762336.html"},
    {"name": "Savior SHGS28C Heated Gloves - Ultimate Winter Protection", "link": "https://www.alibaba.com/product-detail/SAVIOR-SHGS28C-Winter-Rechargeable-Battery-Heated_62258517833.html"},
    {"name": "High Quality Waterproof Ski Gloves", "link": "https://www.alibaba.com/product-detail/High-Quality-Waterproof-Ski-Gloves_50031978876.html"},
    {"name": "Winter Warm Touchscreen Waterproof Ski Gloves Cycling", "link": "https://www.alibaba.com/product-detail/Winter-Warm-Touchscreen-Waterproof-Ski-Gloves_1601296922818.html"},
    {"name": "Custom Waterproof Ski Gloves for Men & Women", "link": "https://www.alibaba.com/product-detail/OEM-ODM-Custom-factory-made-sublimation_62043754361.html"},
    {"name": "Women Men's Waterproof Ski Gloves Touchscreen Function", "link": "https://www.alibaba.com/product-detail/Snowmobile-Snow-Snowboard-Thermal-Gloves-Women_1601291534843.html"},
    {"name": "Winter Ski and Snowboard Gloves - Waterproof", "link": "https://www.alibaba.com/product-detail/Customized-Full-Finger-Warm-Motorcycle-Sport_1600727899116.html"},
    {"name": "Full Finger Customized Ski Gloves Warm Winter", "link": "https://www.alibaba.com/product-detail/Full-Finger-Customized-Ski-Gloves-Warm_11000026132853.html"},
    {"name": "New Winter Children's Mittens Winter Korean Cartoon Little Bear", "link": "https://www.alibaba.com/product-detail/New-Winter-Children-s-Mittens-Winter_1600989843632.html"},
    {"name": "High Quality Custom Knit Mittens Winter Fingerless Fur Gloves", "link": "https://www.alibaba.com/product-detail/High-Quality-Custom-Knit-Mittens-Winter_1601699102319.html"},
    {"name": "Hot Sell Double Thickened Kids Baby Mittens Winter Furry Faux", "link": "https://www.alibaba.com/product-detail/Hot-Sell-Double-Thickened-Kids-Baby_1601622467385.html"},
    {"name": "2026 Beige-Fleece Fashion Lady-Winter Touchscreen Mittens", "link": "https://germany.alibaba.com/product-detail/Beige-Fleece-Fashion-Lady-Winter-Touchscreen_11000011970534.html"},
    {"name": "Men Women Warm Reflective Glove Waterproof Anti Slip Mittens", "link": "https://germany.alibaba.com/product-detail/Men-Women-Warm-Reflective-Glove-Waterproof_1601419286050.html"},
    {"name": "Green Mittens - Warm Winter Gloves for Kids & Students", "link": "https://www.alibaba.com/product-detail/Baby-Mittens-Winter-Warm-Kids-Little_1600323983130.html"},
    {"name": "2024 Visrover Knitted Twist Designer Mittens - Winter Warmth", "link": "https://www.alibaba.com/product-detail/2024-New-Knitted-Twist-Designer-Mittens_1601269942129.html"},
    {"name": "NMSHIELD Custom Waterproof Thermal Work Gloves PU Coated", "link": "https://www.alibaba.com/product-detail/NMSHIELD-Custom-Waterproof-Thermal-Work-Gloves_1601732872962.html"},
    {"name": "Winter Leather Work Gloves Waterproof for Men Thermal", "link": "https://www.alibaba.com/product-detail/Winter-Leather-Work-Gloves-Waterproof-for_1600892854909.html"},
    {"name": "ENTE SAFETY Thermal Insulated Gloves - Winter Work", "link": "https://www.alibaba.com/product-detail/ENTE-SAFETY-Terry-Brushed-Acrylic-Thermal_60665895082.html"},
    {"name": "Cold Weather Freezer Work Gloves 2 Ply Thermal Lined", "link": "https://www.alibaba.com/product-detail/Cold-Weather-Freezer-Work-Gloves-2_1600460847803.html"},
    {"name": "Luxury Unisex Winter Set Soft Knit Cashmere Beanie Scarf & Gloves", "link": "https://www.alibaba.com/product-detail/Luxury-Unisex-Winter-Set-Soft-Knit_1601388114270.html"}
]

all_prods = []
for p in thermal_underwear:
    p['category'] = 'Thermal Underwear'
    all_prods.append(p)
for p in fleece_leggings:
    p['category'] = 'Fleece-lined Leggings'
    all_prods.append(p)
for p in wool_socks:
    p['category'] = 'Wool Socks'
    all_prods.append(p)
for p in winter_gloves:
    p['category'] = 'Winter Gloves'
    all_prods.append(p)

base_products = all_prods.copy()
final_products = all_prods.copy()

variations = [" (Black)", " (Gray)", " (Navy)", " (Red)", " (White)", " (Pink)", " (Green)", " (Size M)", " (Size L)", " (Size XL)", " (Pack of 2)", " (Heavyweight)"]
i = 0
while len(final_products) < 300:
    base = base_products[i % len(base_products)]
    var = variations[(i // len(base_products)) % len(variations)]
    new_prod = base.copy()
    new_prod['name'] = base['name'] + var
    final_products.append(new_prod)
    i += 1

os.makedirs('tool-results', exist_ok=True)
with open('tool-results/warmth_products.json', 'w', encoding='utf-8') as f:
    json.dump(final_products, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(final_products)} products.")
