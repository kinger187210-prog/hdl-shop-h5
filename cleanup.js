
const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'dist', 'hdl_inventory.json');

try {
    const rawData = fs.readFileSync(filePath, 'utf8');
    const data = JSON.parse(rawData);
    console.log(`Original count: ${data.length}`);

    const filtered = data.filter(p => {
        const isHdlModel = p.ProModel && p.ProModel.startsWith('HDL-');
        const isAlibaba = p.description && p.description.includes('1688/Alibaba');
        return isHdlModel || isAlibaba;
    });

    console.log(`Filtered count: ${filtered.length}`);

    const updated = filtered.map(p => {
        // Map material to category if category doesn't exist
        return {
            ...p,
            category: p.category || p.material || '其他'
        };
    });

    fs.writeFileSync(filePath, JSON.stringify(updated, null, 2));
    console.log('Successfully updated dist/hdl_inventory.json');
} catch (err) {
    console.error('Error processing JSON:', err);
}
