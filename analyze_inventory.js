const fs = require('fs');

const inventoryPath = 'dist/hdl_inventory.json';
const targetCategories = ["冬季保暖", "电子周边", "五金工具", "车载用品", "日百", "户外露营", "家居装饰", "厨房厨具", "母婴玩具", "宠物用品"];

const data = JSON.parse(fs.readFileSync(inventoryPath, 'utf8'));

const categoryCounts = {};
const invalidImages = [];
const noPhotoItems = [];
const homepageCategoryStats = {};

targetCategories.forEach(cat => {
    homepageCategoryStats[cat] = 0;
});

data.forEach(item => {
    const cat = item.category || 'Unknown';
    categoryCounts[cat] = (categoryCounts[cat] || 0) + 1;

    if (targetCategories.includes(cat)) {
        homepageCategoryStats[cat]++;
    }

    const picUrl = item.sPicUrl || '';
    const invalidPatterns = ['placeholder', 'example.com', 'dummy', 'test'];
    
    if (!picUrl || picUrl.length < 10 || invalidPatterns.some(pattern => picUrl.toLowerCase().includes(pattern))) {
        invalidImages.push({
            id: item.id,
            model: item.ProModel,
            url: picUrl || 'EMPTY'
        });
    }

    if (picUrl.toUpperCase().includes('PHOTO') || 
        (item.ProductName && item.ProductName.toUpperCase().includes('PHOTO'))) {
        noPhotoItems.push({
            model: item.ProModel,
            name: item.ProductName,
            url: picUrl
        });
    }
});

console.log('--- Category Counts ---');
Object.entries(categoryCounts).sort((a, b) => b[1] - a[1]).forEach(([cat, count]) => {
    console.log(`${cat}: ${count}`);
});

console.log('\n--- Homepage Category Verification ---');
targetCategories.forEach(cat => {
    console.log(`${cat}: ${homepageCategoryStats[cat] > 0 ? 'OK (' + homepageCategoryStats[cat] + ' products)' : 'MISSING'}`);
});

console.log('\n--- Invalid Image URL Patterns Found ---');
if (invalidImages.length === 0) {
    console.log('None');
} else {
    invalidImages.forEach(img => {
        console.log(`Model: ${img.model}, URL: ${img.url}`);
    });
}

console.log('\n--- "NO PHOTO" Items ---');
if (noPhotoItems.length === 0) {
    console.log('None');
} else {
    noPhotoItems.forEach(item => {
        console.log(`Model: ${item.model}, Title: ${item.name}`);
    });
}
