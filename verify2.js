const ExcelJS = require('exceljs');
async function v() {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile('C:\\Users\\Administrator\\Desktop\\2019维格运费利润计算表_最新运费更新版.xlsx');
  const s = wb.getWorksheet('主要国家利润率对比');
  
  for (let g = 0; g < 3; g++) {
    const sc = g * 9 + 1;
    console.log('\nGroup ' + (g + 1) + ':');
    for (let r = 3; r <= 12; r++) {
      const cn = s.getCell(r, sc).value;
      if (!cn) continue;
      const v = [];
      for (let m = 0; m < 7; m++) {
        const x = s.getCell(r, sc + 1 + m).value;
        v.push(typeof x === 'number' ? (x * 100).toFixed(1) + '%' : '-');
      }
      console.log('  ' + cn + ': ' + v.join(' | '));
    }
  }
  
  // Check some negative profit cells for red formatting
  const cell = s.getCell(3, 5); // 俄罗斯 无忧标准
  console.log('\nRU 无忧标准 fill:', JSON.stringify(cell.fill));
  console.log('RU 无忧标准 font:', JSON.stringify(cell.font));
  
  // Check a negative one
  const cell2 = s.getCell(3, 6); // 俄罗斯 陆运大件
  console.log('\nRU 陆运大件 fill:', JSON.stringify(cell2.fill));
  console.log('RU 陆运大件 font:', JSON.stringify(cell2.font));
}
v().catch(e => console.error(e.message));
