const ExcelJS = require('exceljs');
const fs = require('fs');

async function main() {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile('C:\\Users\\Administrator\\Desktop\\速卖通最新运费单.xlsx');
  
  // Extract all country data from each sheet
  // Strategy: find rows where col A has a Chinese country name (not header text)
  
  const sheetData = {};
  
  for (const ws of wb.worksheets) {
    const name = ws.name;
    const countries = [];
    
    for (let r = 1; r <= ws.rowCount; r++) {
      const a = ws.getCell(r, 1).value;
      const b = ws.getCell(r, 2).value;
      const c = ws.getCell(r, 3).value;
      const d = ws.getCell(r, 4).value;
      const e = ws.getCell(r, 5).value;
      
      // Skip header/structural rows
      if (!a || typeof a !== 'string') continue;
      if (a.includes('运达') || a.includes('上门') || a.includes('介绍') || a.includes('报价') || a.includes('配送') || a.includes('深圳') || a.includes('北京') || a.includes('元（')) continue;
      if (a.length > 20) continue; // skip long description rows
      
      // Should have a code in col C (2-3 letter country code) and numeric in col D
      if (!c || typeof c !== 'string' || c.length > 3) continue;
      if (typeof d !== 'number') continue;
      
      countries.push({
        cn: a,
        en: b,
        code: c,
        kgRate: d,
        regFee: typeof e === 'number' ? e : null,
        row: r
      });
    }
    
    sheetData[name] = countries;
    console.log(`${name}: ${countries.length} countries`);
    // Print first 5
    countries.slice(0, 3).forEach(c => console.log(`  ${c.cn} (${c.code}): KG=${c.kgRate}, Fee=${c.regFee}`));
  }
  
  fs.writeFileSync('extracted_rates.json', JSON.stringify(sheetData, null, 2));
  console.log('\nSaved to extracted_rates.json');
}

main().catch(console.error);
