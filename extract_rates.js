const ExcelJS = require('exceljs');
const fs = require('fs');

async function main() {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile('C:\\Users\\Administrator\\Desktop\\速卖通最新运费单.xlsx');
  
  const result = {};
  
  wb.worksheets.forEach(ws => {
    console.log(`\n=== ${ws.name} (${ws.rowCount} rows x ${ws.columnCount} cols) ===`);
    result[ws.name] = [];
    
    // Print first 10 rows to understand structure
    for (let r = 1; r <= Math.min(ws.rowCount, 15); r++) {
      const vals = [];
      for (let c = 1; c <= Math.min(ws.columnCount, 15); c++) {
        const v = ws.getCell(r, c).value;
        vals.push(v === null || v === undefined ? '' : String(v));
      }
      console.log(`  R${r}: ${vals.join(' | ')}`);
    }
  });
}

main().catch(console.error);
