const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'dist/hdl_inventory.json');
const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

data.forEach(item => {
    if (item.description && item.description.startsWith('Price: $')) {
        const priceStr = item.description.replace('Price: $', '');
        const price = parseFloat(priceStr);
        if (!isNaN(price)) {
            const newPrice = price * 1.5;
            item.price_display = `$${newPrice.toFixed(2)}`;
        } else {
            item.price_display = '线下洽谈';
        }
    } else {
        item.price_display = '线下洽谈';
    }
});

fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
console.log(`Processed ${data.length} items.`);
