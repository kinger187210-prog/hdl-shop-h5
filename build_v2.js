const ExcelJS = require('exceljs');
const path = require('path');

// ===== DEFAULTS (written to param cells) =====
const COST = 13, WEIGHT = 100, PRICE_USD = 4.96, FX_RATE = 7.25;

// ===== STYLING =====
const C = {
  DARK_BLUE: '1F4E78', HEADER_BG: '4472C4', HEADER_BG2: '2E75B6',
  LIGHT_BLUE: 'D6E4F0', GREEN_INPUT: 'E2EFDA', GRAY: 'F2F2F2',
  WHITE: 'FFFFFF', ALT: 'F7F9FB', RED_BG: 'FFC7CE', RED_FONT: '9C0006',
  GREEN_FONT: '006100', GREEN_BG: 'C6EFCE', OLIVE_HEADER: '808000', OLIVE_BG: 'F5F5DC',
};
const THIN = { style: 'thin', color: { argb: 'D9D9D9' } };
const BORDER = { top: THIN, bottom: THIN, left: THIN, right: THIN };
const hFill = (c) => ({ type: 'pattern', pattern: 'solid', fgColor: { argb: c || C.HEADER_BG } });
const sFill = (c) => ({ type: 'pattern', pattern: 'solid', fgColor: { argb: c } });
const hFont = { name: '微软雅黑', size: 9.5, bold: true, color: { argb: C.WHITE } };
const dFont = { name: '微软雅黑', size: 9 };
const bFont = { name: '微软雅黑', size: 9, bold: true };

// ===== EXTRACT DATA =====
async function extractAllRates() {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(path.join('C:', 'Users', 'Administrator', 'Desktop', '速卖通最新运费单.xlsx'));
  const methods = {};
  for (const ws of wb.worksheets) {
    const name = ws.name;
    if (name === '无忧物流-陆运大件专线') continue; // SKIP 陆运大件
    const isUSD = name === '超级经济' || name === '无忧物流-特惠';
    const countries = new Map();
    for (let r = 1; r <= ws.rowCount; r++) {
      const a = ws.getCell(r, 1).value;
      if (!a || typeof a !== 'string') continue;
      if (a.includes('运达') || a.includes('上门') || a.includes('介绍') || a.includes('报价') ||
          a.includes('配送') || a.includes('深圳') || a.includes('北京') || a.includes('元（') ||
          a.includes('美元') || a.length > 20) continue;
      const c3 = ws.getCell(r, 3).value;
      if (!c3 || typeof c3 !== 'string' || c3.length > 4) continue;
      const d = ws.getCell(r, 4).value;
      const e = ws.getCell(r, 5).value;
      if (typeof d !== 'number') continue;
      const code = c3, cn = a, en = ws.getCell(r, 2).value || '';
      let tierHeader = '';
      for (let hr = r - 1; hr >= Math.max(1, r - 6); hr--) {
        const hv = ws.getCell(hr, 4).value;
        if (hv && typeof hv === 'string' && hv.includes('g')) { tierHeader = hv; break; }
      }
      const existing = countries.get(code);
      const ok = !tierHeader || tierHeader.includes('0~') || tierHeader.includes('1-') || tierHeader.includes('1-2000');
      if (!existing) {
        countries.set(code, { cn, en, code, kgRate: d, regFee: typeof e === 'number' ? e : 0 });
      } else if (ok && !existing._locked) {
        countries.set(code, { cn, en, code, kgRate: d, regFee: typeof e === 'number' ? e : 0, _locked: true });
      }
    }
    methods[name] = { isUSD, countries: Array.from(countries.values()) };
    console.log(`  ${name}: ${countries.size} countries (${isUSD ? 'USD' : 'RMB'})`);
  }
  return methods;
}

// Convert column number to letter(s): 1->A, 2->B, ..., 27->AA
function colLetter(n) {
  let s = '';
  while (n > 0) { n--; s = String.fromCharCode(65 + (n % 26)) + s; n = Math.floor(n / 26); }
  return s;
}

// ===== MAIN =====
async function main() {
  console.log('Extracting rates...');
  const methods = await extractAllRates();

  // 6 methods (陆运大件 removed)
  const METHOD_ORDER = [
    '超级经济Global', '超级经济', '无忧物流-特惠', '无忧物流-标准',
    '燕文航空挂号小包', '4PX新邮挂号小包'
  ];
  const METHOD_SHORT = ['超级经济G', '超级经济', '无忧特惠', '无忧标准', '燕文小包', '4PX小包'];
  const METHOD_COLORS = ['4472C4', '5B9BD5', '2E75B6', '1F4E78', 'BF8F00', 'C00000'];
  const COLS_PER = 4; // 国家 | 公布价 | 挂号费 | 利润率

  const wb = new ExcelJS.Workbook();
  wb.creator = 'Accio'; wb.created = new Date();

  // ==================== SHEET 1: 总览 ====================
  const ws1 = wb.addWorksheet('总览', { views: [{ state: 'frozen', xSplit: 0, ySplit: 3 }] });

  // --- Param cells location: after all method columns ---
  // 6 methods * 4 cols = 24 data cols → param label at col 26, value at col 27
  const P_COL = METHOD_ORDER.length * COLS_PER + 2; // 26
  const V_COL = P_COL + 1; // 27
  const P_LET = colLetter(V_COL); // "AA"
  // Params: row 3=成本, row 4=重量, row 5=售价, row 6=汇率
  // Absolute refs: $AA$3=成本, $AA$4=重量, $AA$5=售价, $AA$6=汇率
  const REF_COST   = `$${P_LET}$3`;
  const REF_WEIGHT = `$${P_LET}$4`;
  const REF_PRICE  = `$${P_LET}$5`;
  const REF_FX     = `$${P_LET}$6`;

  // Title
  const lastDataCol = METHOD_ORDER.length * COLS_PER;
  ws1.mergeCells(1, 1, 1, lastDataCol);
  const t1 = ws1.getCell('A1');
  t1.value = '速卖通运费利润计算表 — 6种物流方式总览 (2026最新运费)';
  t1.font = { name: '微软雅黑', size: 14, bold: true, color: { argb: C.DARK_BLUE } };
  t1.alignment = { horizontal: 'center', vertical: 'middle' };
  ws1.getRow(1).height = 32;

  // Section headers (row 2) + column headers (row 3)
  for (let m = 0; m < METHOD_ORDER.length; m++) {
    const sc = m * COLS_PER + 1;
    const md = methods[METHOD_ORDER[m]];
    const unit = md.isUSD ? 'USD' : 'RMB';
    ws1.mergeCells(2, sc, 2, sc + COLS_PER - 1);
    const sh = ws1.getCell(2, sc);
    sh.value = `${METHOD_SHORT[m]} (${unit})`;
    sh.fill = hFill(METHOD_COLORS[m]); sh.font = { ...hFont, size: 10 };
    sh.alignment = { horizontal: 'center', vertical: 'middle' }; sh.border = BORDER;
    ['国家', '公布价', '挂号费', '利润率'].forEach((h, i) => {
      const c = ws1.getCell(3, sc + i);
      c.value = h; c.fill = sFill(C.LIGHT_BLUE);
      c.font = { ...bFont, color: { argb: C.DARK_BLUE } };
      c.alignment = { horizontal: 'center', vertical: 'middle' }; c.border = BORDER;
    });
  }
  ws1.getRow(2).height = 22; ws1.getRow(3).height = 20;

  // --- Parameter cells ---
  ws1.mergeCells(2, P_COL, 2, V_COL);
  ws1.getCell(2, P_COL).value = '参数设置';
  ws1.getCell(2, P_COL).font = { ...hFont, size: 10 };
  ws1.getCell(2, P_COL).fill = hFill(); ws1.getCell(2, P_COL).alignment = { horizontal: 'center' };
  ws1.getCell(2, V_COL).fill = hFill();

  const paramRows = [
    ['产品成本(RMB)', COST, 3],
    ['产品重量(g)', WEIGHT, 4],
    ['产品售价(USD)', PRICE_USD, 5],
    ['汇率(RMB/USD)', FX_RATE, 6],
  ];
  paramRows.forEach(([label, val, row]) => {
    const lc = ws1.getCell(row, P_COL);
    lc.value = label; lc.font = bFont; lc.fill = sFill(C.GRAY);
    lc.border = BORDER; lc.alignment = { horizontal: 'right' };
    const vc = ws1.getCell(row, V_COL);
    vc.value = val; vc.fill = sFill(C.GREEN_INPUT);
    vc.font = { ...bFont, color: { argb: '0000FF' } };
    vc.border = BORDER; vc.alignment = { horizontal: 'center' };
  });

  // --- Data rows with FORMULAS ---
  const DATA_START = 4;
  let maxDataRow = DATA_START;

  for (let m = 0; m < METHOD_ORDER.length; m++) {
    const sc = m * COLS_PER + 1;
    const md = methods[METHOD_ORDER[m]];
    const list = md.countries;
    const rateCol = colLetter(sc + 1); // 公布价 column letter
    const feeCol  = colLetter(sc + 2); // 挂号费 column letter

    for (let i = 0; i < list.length; i++) {
      const r = DATA_START + i;
      if (r > maxDataRow) maxDataRow = r;
      const c = list[i];
      const isAlt = i % 2 === 1;
      const fill = isAlt ? sFill(C.ALT) : undefined;

      // Country name, KG rate, registration fee (static values)
      const c1 = ws1.getCell(r, sc);
      c1.value = c.cn; c1.font = dFont; c1.border = BORDER; if (fill) c1.fill = fill;
      const c2 = ws1.getCell(r, sc + 1);
      c2.value = c.kgRate; c2.font = dFont; c2.numFmt = '#,##0.00'; c2.border = BORDER; if (fill) c2.fill = fill;
      const c3 = ws1.getCell(r, sc + 2);
      c3.value = c.regFee; c3.font = dFont; c3.numFmt = '#,##0.00'; c3.border = BORDER; if (fill) c3.fill = fill;

      // Profit rate FORMULA referencing param cells
      const c4 = ws1.getCell(r, sc + 3);
      let formula;
      if (md.isUSD) {
        // (售价 - 成本/汇率 - (重量/1000*公布价 + 挂号费)) / 售价
        formula = `(${REF_PRICE}-${REF_COST}/${REF_FX}-((${REF_WEIGHT}/1000)*${rateCol}${r}+${feeCol}${r}))/${REF_PRICE}`;
      } else {
        // (售价*汇率 - 成本 - (重量/1000*公布价 + 挂号费)) / (售价*汇率)
        formula = `(${REF_PRICE}*${REF_FX}-${REF_COST}-((${REF_WEIGHT}/1000)*${rateCol}${r}+${feeCol}${r}))/(${REF_PRICE}*${REF_FX})`;
      }
      c4.value = { formula };
      c4.font = dFont; c4.numFmt = '0.00%'; c4.border = BORDER;
      if (fill) c4.fill = fill;
    }
  }

  // --- Conditional formatting for all 利润率 columns ---
  for (let m = 0; m < METHOD_ORDER.length; m++) {
    const profitCol = colLetter(m * COLS_PER + 4);
    const range = `${profitCol}${DATA_START}:${profitCol}${maxDataRow}`;
    // Red for negative
    ws1.addConditionalFormatting({
      ref: range,
      rules: [{
        type: 'cellIs', operator: 'lessThan', priority: 1,
        formulae: [0],
        style: {
          fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: C.RED_BG } },
          font: { color: { argb: C.RED_FONT }, bold: true }
        }
      }]
    });
    // Green for > 15%
    ws1.addConditionalFormatting({
      ref: range,
      rules: [{
        type: 'cellIs', operator: 'greaterThan', priority: 2,
        formulae: [0.15],
        style: {
          fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: C.GREEN_BG } },
          font: { color: { argb: C.GREEN_FONT } }
        }
      }]
    });
  }

  // Column widths
  for (let m = 0; m < METHOD_ORDER.length; m++) {
    const s = m * COLS_PER + 1;
    ws1.getColumn(s).width = 16;
    ws1.getColumn(s + 1).width = 9;
    ws1.getColumn(s + 2).width = 8;
    ws1.getColumn(s + 3).width = 8;
  }
  ws1.getColumn(P_COL).width = 16;
  ws1.getColumn(V_COL).width = 10;

  // ==================== SHEET 2: 主要国家利润率对比 ====================
  const ws2 = wb.addWorksheet('主要国家利润率对比', { views: [{ state: 'frozen', xSplit: 0, ySplit: 2 }] });

  const TOP30 = [
    ['RU','俄罗斯'],['FR','法国'],['ES','西班牙'],['NL','荷兰'],['DE','德国'],
    ['GB','英国'],['IL','以色列'],['US','美国'],['CA','加拿大'],['UA','乌克兰'],
    ['AU','澳大利亚'],['CL','智利'],['KR','韩国'],['JP','日本'],['IT','意大利'],
    ['BY','白俄罗斯'],['LV','拉脱维亚'],['CZ','捷克'],['BR','巴西'],['CH','瑞士'],
    ['PL','波兰'],['TR','土耳其'],['MX','墨西哥'],['SE','瑞典'],['TH','泰国'],
    ['SG','新加坡'],['ID','印度尼西亚'],['MY','马来西亚'],['KZ','哈萨克斯坦'],['SA','沙特阿拉伯'],
  ];

  const GS = 10; // group size
  const GM = METHOD_ORDER.length; // 6 methods
  const GC = 1 + GM; // 7 cols per group
  const GAP = 1;

  // Sheet2 also needs param cells. Place them at a known location for formulas.
  // We'll put params in row 14-17, col 1-2 (below the data, labeled)
  const S2_PARAM_START = 3 + GS + 2; // row 15
  // Or better: reference Sheet1's params via cross-sheet reference
  // Use: 总览!$AA$3, 总览!$AA$4, etc.
  const XR_COST   = `总览!${REF_COST}`;
  const XR_WEIGHT = `总览!${REF_WEIGHT}`;
  const XR_PRICE  = `总览!${REF_PRICE}`;
  const XR_FX     = `总览!${REF_FX}`;

  // Title
  const totalCols2 = 3 * GC + 2 * GAP;
  ws2.mergeCells(1, 1, 1, totalCols2);
  const t2 = ws2.getCell('A1');
  t2.value = '全球30个主要国家 × 6种物流方式 利润率对比 (2026)';
  t2.font = { name: '微软雅黑', size: 13, bold: true, color: { argb: C.DARK_BLUE } };
  t2.alignment = { horizontal: 'center', vertical: 'middle' };
  ws2.getRow(1).height = 30;

  // Build lookup: for each country, find KG rate & reg fee per method
  // We need to embed the actual rates in Sheet2 so formulas can reference them
  // Strategy: put rate data in hidden rows or use INDIRECT... 
  // Simplest: embed kgRate and regFee as values in Sheet2, build formulas referencing them
  // But that doubles columns. Better: put a "data block" below the display area.
  //
  // Layout: 
  //   Row 2: headers
  //   Row 3-12: display (30 countries, 3 groups of 10) — profit rate formulas
  //   Row 15+: hidden data block with kgRate & regFee for each country×method
  //   Each group's data block: 国家 | isUSD | m1_kg | m1_fee | m2_kg | m2_fee | ...

  // Actually, the simplest approach for Sheet2: 
  // Store kgRate and regFee per country-method right in the sheet, 
  // and have the display cells be formulas referencing those + params.
  // 
  // Cleanest approach: For each cell in the display grid, embed the kgRate and regFee
  // directly in the formula as constants, and reference only the 4 params from Sheet1.
  // This way the profit changes when params change, but rates stay fixed (they are from the rate table).

  // Headers
  for (let g = 0; g < 3; g++) {
    const sc = g * (GC + GAP) + 1;
    const ch = ws2.getCell(2, sc);
    ch.value = '国家'; ch.fill = hFill(C.OLIVE_HEADER); ch.font = { ...hFont, size: 9 };
    ch.alignment = { horizontal: 'center' }; ch.border = BORDER;
    for (let m = 0; m < GM; m++) {
      const c = ws2.getCell(2, sc + 1 + m);
      c.value = METHOD_SHORT[m];
      c.fill = hFill(METHOD_COLORS[m]);
      c.font = { ...hFont, size: 8.5 };
      c.alignment = { horizontal: 'center', vertical: 'middle', wrapText: true };
      c.border = BORDER;
    }
  }
  ws2.getRow(2).height = 28;

  // Data rows — formulas with embedded rate constants + param references
  for (let g = 0; g < 3; g++) {
    const sc = g * (GC + GAP) + 1;
    for (let i = 0; i < GS; i++) {
      const idx = g * GS + i;
      if (idx >= TOP30.length) break;
      const [code, cn] = TOP30[idx];
      const r = 3 + i;
      const isAlt = i % 2 === 1;
      const fill = isAlt ? sFill(C.OLIVE_BG) : sFill(C.WHITE);

      const cc = ws2.getCell(r, sc);
      cc.value = cn; cc.font = bFont; cc.fill = fill; cc.border = BORDER;

      for (let m = 0; m < GM; m++) {
        const cell = ws2.getCell(r, sc + 1 + m);
        const md = methods[METHOD_ORDER[m]];
        const found = md.countries.find(c => c.code === code);

        if (found) {
          const kg = found.kgRate;
          const fee = found.regFee;
          let formula;
          if (md.isUSD) {
            // (售价 - 成本/汇率 - (重量/1000*kg + fee)) / 售价
            formula = `(${XR_PRICE}-${XR_COST}/${XR_FX}-((${XR_WEIGHT}/1000)*${kg}+${fee}))/${XR_PRICE}`;
          } else {
            // (售价*汇率 - 成本 - (重量/1000*kg + fee)) / (售价*汇率)
            formula = `(${XR_PRICE}*${XR_FX}-${XR_COST}-((${XR_WEIGHT}/1000)*${kg}+${fee}))/(${XR_PRICE}*${XR_FX})`;
          }
          cell.value = { formula };
          cell.numFmt = '0.00%';
          cell.alignment = { horizontal: 'center' };
          cell.border = BORDER; cell.font = dFont;
          // No static fill — conditional formatting handles colors
        } else {
          cell.value = '';
          cell.fill = sFill(C.GRAY);
          cell.border = BORDER;
        }
      }
    }
  }

  // Conditional formatting for Sheet2
  for (let g = 0; g < 3; g++) {
    const sc = g * (GC + GAP) + 1;
    for (let m = 0; m < GM; m++) {
      const col = colLetter(sc + 1 + m);
      const range = `${col}3:${col}12`;
      ws2.addConditionalFormatting({
        ref: range,
        rules: [{
          type: 'cellIs', operator: 'lessThan', priority: 1,
          formulae: [0],
          style: {
            fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: C.RED_BG } },
            font: { color: { argb: C.RED_FONT }, bold: true }
          }
        }]
      });
      ws2.addConditionalFormatting({
        ref: range,
        rules: [{
          type: 'cellIs', operator: 'greaterThan', priority: 2,
          formulae: [0.15],
          style: {
            fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: C.GREEN_BG } },
            font: { color: { argb: C.GREEN_FONT } }
          }
        }]
      });
    }
  }

  // Column widths
  for (let g = 0; g < 3; g++) {
    const sc = g * (GC + GAP) + 1;
    ws2.getColumn(sc).width = 12;
    for (let m = 0; m < GM; m++) ws2.getColumn(sc + 1 + m).width = 9;
    if (g < 2) ws2.getColumn(sc + GC).width = 2;
  }

  // Params note below table
  const noteRow = 3 + GS + 1;
  ws2.getCell(noteRow, 1).value = '参数来源:';
  ws2.getCell(noteRow, 1).font = { ...bFont, color: { argb: C.DARK_BLUE } };
  ws2.getCell(noteRow, 2).value = '所有利润率公式引用「总览」表参数设置 → 修改参数后本表自动更新';
  ws2.getCell(noteRow, 2).font = dFont;
  ws2.mergeCells(noteRow, 2, noteRow, 10);
  ws2.getCell(noteRow + 1, 1).value = '图例:';
  ws2.getCell(noteRow + 1, 1).font = bFont;
  ws2.getCell(noteRow + 1, 2).value = '绿色=利润率>15% | 红色=亏损 | 灰色=不覆盖该国家';
  ws2.getCell(noteRow + 1, 2).font = dFont;
  ws2.mergeCells(noteRow + 1, 2, noteRow + 1, 10);

  // ==================== SHEET 3: 快速计算 ====================
  const ws3 = wb.addWorksheet('快速计算');
  const h3 = ['拿货价(RMB)', '运费(RMB)', '成本(RMB)', '售价(USD)', '0.75标价', '0.85标价'];
  h3.forEach((h, i) => {
    const c = ws3.getCell(1, i + 1);
    c.value = h; c.fill = hFill(); c.font = hFont;
    c.alignment = { horizontal: 'center' }; c.border = BORDER;
  });
  ws3.getCell('A2').value = 18.5; ws3.getCell('A2').fill = sFill(C.GREEN_INPUT);
  ws3.getCell('B2').value = 0; ws3.getCell('B2').fill = sFill(C.GREEN_INPUT);
  ws3.getCell('C2').value = { formula: 'A2+B2' }; ws3.getCell('C2').numFmt = '#,##0.00';
  ws3.getCell('D2').value = { formula: 'C2/7.25/(1-0.13-0.2)' }; ws3.getCell('D2').numFmt = '"$"#,##0.00';
  ws3.getCell('E2').value = { formula: 'D2/0.75' }; ws3.getCell('E2').numFmt = '"$"#,##0.00';
  ws3.getCell('F2').value = { formula: 'D2/0.85' }; ws3.getCell('F2').numFmt = '"$"#,##0.00';
  [1,2,3,4,5,6].forEach(i => { ws3.getColumn(i).width = 13; });

  // ==================== SAVE ====================
  const outPath = path.join('C:', 'Users', 'Administrator', 'Desktop', '2019维格运费利润计算表_最新运费更新版.xlsx');
  await wb.xlsx.writeFile(outPath);
  console.log('\n✓ File saved: ' + outPath);

  console.log('\n=== SUMMARY ===');
  for (const mName of METHOD_ORDER) {
    const md = methods[mName];
    console.log(`  ${mName}: ${md.countries.length} countries (${md.isUSD ? 'USD' : 'RMB'})`);
  }
  const total = METHOD_ORDER.reduce((s, m) => s + methods[m].countries.length, 0);
  console.log(`  Total: ${total} country-method entries`);
  console.log(`  Param cells: ${P_LET}3(成本), ${P_LET}4(重量), ${P_LET}5(售价), ${P_LET}6(汇率)`);
  console.log('  All profit rates are FORMULAS — change params to update instantly');
}

main().catch(e => { console.error(e); process.exit(1); });
