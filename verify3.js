const ExcelJS = require('exceljs');
async function v() {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile('C:\\Users\\Administrator\\Desktop\\2019维格运费利润计算表_最新运费更新版.xlsx');

  console.log('Sheets:', wb.worksheets.map(s => s.name));

  // === Sheet 1: 总览 ===
  const ws1 = wb.getWorksheet('总览');
  console.log('\n=== 总览 ===');
  console.log('Rows:', ws1.rowCount, 'Cols:', ws1.columnCount);

  // Check methods (should be 6, no 陆运大件)
  for (let m = 0; m < 6; m++) {
    console.log('Method', m, ':', ws1.getCell(2, m * 4 + 1).value);
  }
  // Verify no 7th method
  console.log('Col 25 (should be empty):', ws1.getCell(2, 25).value);

  // Check params
  console.log('\nParams:');
  for (let r = 3; r <= 6; r++) {
    console.log(' ', ws1.getCell(r, 26).value, '=', ws1.getCell(r, 27).value);
  }

  // Check formula in first profit cell (col D, row 4) — 超级经济Global RMB
  const f1 = ws1.getCell(4, 4).value;
  console.log('\n超级经济G profit formula (D4):', JSON.stringify(f1));

  // Check formula for USD method (col L, row 4) — 超级经济 USD
  const f2 = ws1.getCell(4, 8).value;
  console.log('超级经济 profit formula (H4):', JSON.stringify(f2));

  // Check formula for 无忧特惠 USD (col L)
  const f3 = ws1.getCell(4, 12).value;
  console.log('无忧特惠 profit formula (L4):', JSON.stringify(f3));

  // Check formula for 无忧标准 RMB (col P)
  const f4 = ws1.getCell(4, 16).value;
  console.log('无忧标准 profit formula (P4):', JSON.stringify(f4));

  // Check conditional formatting
  console.log('\nConditional formatting rules:', ws1.conditionalFormattings?.length || 'none found');

  // === Sheet 2: 主要国家利润率对比 ===
  const ws2 = wb.getWorksheet('主要国家利润率对比');
  console.log('\n=== 主要国家利润率对比 ===');

  // Check first country formula (cross-sheet ref)
  const f5 = ws2.getCell(3, 2).value; // 俄罗斯, 超级经济G
  console.log('RU 超级经济G formula (B3):', JSON.stringify(f5));

  const f6 = ws2.getCell(3, 5).value; // 俄罗斯, 无忧标准
  console.log('RU 无忧标准 formula (E3):', JSON.stringify(f6));

  // Check group 2 and 3
  console.log('\nGroup 2 col 9:', ws2.getCell(3, 9).value); // AU country name
  console.log('Group 3 col 17:', ws2.getCell(3, 17).value); // PL country name

  // Check a gray cell (no coverage)
  const grayCell = ws2.getCell(3, 3); // 俄罗斯, 超级经济 — should exist
  console.log('\nRU 超级经济:', JSON.stringify(grayCell.value));

  // File size
  const fs = require('fs');
  console.log('\nFile size:', (fs.statSync('C:\\Users\\Administrator\\Desktop\\2019维格运费利润计算表_最新运费更新版.xlsx').size / 1024).toFixed(1) + ' KB');
}
v().catch(e => console.error(e.message));
