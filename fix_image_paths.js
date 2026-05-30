const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'dist', 'hdl_inventory.json');
const baseUrl = 'https://s.alicdn.com/@sc04/kf/';

try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    let count = 0;

    data.forEach(item => {
        if (item.sPicUrl && !item.sPicUrl.startsWith('http')) {
            item.sPicUrl = baseUrl + item.sPicUrl;
            count++;
        }
    });

    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
    console.log(`Successfully updated ${count} image paths.`);
} catch (error) {
    console.error('Error processing JSON:', error);
    process.exit(1);
}
