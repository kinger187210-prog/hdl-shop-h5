const ExcelJS = require('exceljs');

async function main() {
  const wb = new ExcelJS.Workbook();
  wb.creator = 'Accio Daily Assistant';
  wb.created = new Date();

  // ==================== COLOR CONSTANTS ====================
  const DARK_BLUE = '1F4E78';
  const BLUE_HEADER = '4472C4';
  const LIGHT_BLUE = 'D6E4F0';
  const GREEN_INPUT = 'E2EFDA';
  const LIGHT_GRAY = 'F2F2F2';
  const WHITE = 'FFFFFF';
  const ALT_ROW = 'F7F9FB';
  const BORDER_LIGHT = { style: 'thin', color: { argb: 'D9D9D9' } };
  const BORDER_MED = { style: 'thin', color: { argb: 'A5A5A5' } };
  const BORDER_ALL = { top: BORDER_LIGHT, bottom: BORDER_LIGHT, left: BORDER_LIGHT, right: BORDER_LIGHT };
  const BORDER_ALL_MED = { top: BORDER_MED, bottom: BORDER_MED, left: BORDER_MED, right: BORDER_MED };

  const headerFill = { type: 'pattern', pattern: 'solid', fgColor: { argb: BLUE_HEADER } };
  const headerFont = { name: '微软雅黑', size: 10, bold: true, color: { argb: WHITE } };
  const inputFill = { type: 'pattern', pattern: 'solid', fgColor: { argb: GREEN_INPUT } };
  const labelFill = { type: 'pattern', pattern: 'solid', fgColor: { argb: LIGHT_GRAY } };
  const altFill = { type: 'pattern', pattern: 'solid', fgColor: { argb: ALT_ROW } };
  const defaultFont = { name: '微软雅黑', size: 9 };
  const boldFont = { name: '微软雅黑', size: 9, bold: true };
  const titleFont = { name: '微软雅黑', size: 14, bold: true, color: { argb: DARK_BLUE } };

  // ==================== 无忧标准 最新运费 ====================
  // Data from 速卖通最新运费单.xlsx - 无忧物流-标准 sheet
  // Format: [国家, 公布价(RMB/KG), 挂号费(RMB/包裹)] — using the 0~150g tier for small packages
  const wuyouStd = [
    ['阿尔巴尼亚', 209.66, 18.7], ['阿尔及利亚', 193.26, 17], ['安哥拉', 176.7, 17],
    ['安提瓜和巴布达', 205.1, 17], ['亚美尼亚', 175.2, 16.6], ['阿鲁巴岛', 205.1, 17],
    ['澳大利亚', 102.59, 18.4], ['巴林', 218.18, 17.6], ['白俄罗斯', 136, 21],
    ['布基纳法索', 205.1, 17], ['加拿大', 122.44, 27.6], ['哥斯达黎加', 217.1, 18],
    ['萨尔瓦多', 217.1, 18], ['赤道几内亚', 205.1, 17], ['加蓬', 205.1, 17],
    ['格鲁吉亚', 166.6, 18.2], ['圭亚那', 205.1, 17], ['冰岛', 190.08, 18.7],
    ['印度尼西亚', 54.6, 16.8], ['科特迪瓦', 205.1, 17], ['日本', 64.45, 21.2],
    ['哈萨克斯坦', 45, 4], ['利比里亚', 207.2, 17], ['莫桑比克', 171.5, 17],
    ['纳米比亚', 182, 17], ['新西兰', 103.96, 31.4], ['尼日利亚', 153.43, 17.6],
    ['巴基斯坦', 129.7, 18.6], ['波多黎各(美)', 173.3, 42.7], ['留尼汪岛', 205.1, 17],
    ['圣卢西亚', 205.1, 17], ['沙特阿拉伯', 197.6, 52.43], ['新加坡', 70.7, 8.1],
    ['圣马丁(荷)', 205.1, 17], ['所罗门群岛', 172.4, 17], ['特立尼达和多巴哥', 205.1, 17],
    ['土耳其', 100, 20.4], ['阿拉伯联合酋长国', 254.97, 15.85], ['赞比亚', 168.3, 17],
    ['奥兰群岛', 190.6, 17], ['安圭拉岛(英)', 217.1, 18], ['南极', 205.1, 17],
    ['阿根廷', 191, 19.1], ['阿塞拜疆', 184.1, 17.7], ['根西岛(英)', 209.66, 18.7],
    ['百慕大群岛(英)', 217.1, 18], ['玻利维亚', 217.1, 18], ['圣诞岛', 205.1, 17],
    ['科科斯岛', 205.1, 17], ['哥伦比亚', 163.22, 18.54], ['刚果', 203, 17],
    ['科克群岛(新)', 172.4, 17], ['多米尼克国', 205.1, 17], ['多米尼加共和国', 205.1, 17],
    ['厄瓜多尔', 217.1, 18], ['厄立特里亚', 211.5, 18], ['爱沙尼亚', 91, 22],
    ['福克兰群岛', 205.1, 17], ['加纳', 171.5, 17], ['几内亚', 205.1, 17],
    ['几内亚比绍', 205.1, 17], ['洪都拉斯', 205.1, 17], ['马恩岛(英)', 209.66, 18.7],
    ['柬埔寨', 62.6, 17.6], ['肯尼亚', 153.4, 17], ['基里巴斯', 172.4, 17],
    ['科威特', 240.36, 17.6], ['吉尔吉斯斯坦', 193.8, 17], ['北马其顿', 184.25, 18.7],
    ['马达加斯加', 182, 17], ['马绍尔群岛', 172.4, 17], ['密克罗尼西亚(美)', 172.4, 17],
    ['蒙特塞拉特岛(英)', 217.1, 18], ['荷属安的列斯群岛', 225.61, 18.7],
    ['尼加拉瓜', 205.1, 17], ['纽埃岛(新)', 172.4, 17], ['诺福克岛(澳)', 205.1, 17],
    ['马里亚纳群岛', 172.4, 17], ['阿曼', 211.7, 18.1], ['帕劳(美)', 172.4, 17],
    ['巴拉圭', 205.1, 17], ['卡塔尔', 225.74, 17.6], ['摩尔多瓦', 153.7, 28.3],
    ['圣赫勒拿', 205.1, 17], ['圣克里斯托弗和尼维斯', 205.1, 17],
    ['圣皮埃尔岛及密克隆岛', 217.1, 18], ['圣文森特岛(英)', 217.1, 18],
    ['圣马力诺', 209.66, 18.7], ['圣多美和普林西比', 205.1, 17], ['塞舌尔', 162, 17],
    ['南乔治亚与南桑威奇群岛', 190.6, 17], ['斯瓦尔巴群岛(挪)', 209.66, 18.7],
    ['斯里兰卡', 120.7, 17], ['巴哈马国', 205.1, 17], ['梵蒂冈', 209.66, 18.7],
    ['东帝汶', 172.4, 17], ['托克劳群岛(新)', 172.4, 17], ['汤加', 172.4, 17],
    ['特克斯和凯科斯群岛(英)', 205.1, 17], ['图瓦卢', 172.4, 17], ['坦桑尼亚', 168.3, 17],
    ['美国本土外小岛屿', 163.7, 40.3], ['乌拉圭', 217.1, 18], ['乌兹别克斯坦', 191.7, 17.1],
    ['维尔京群岛(英)', 217.1, 18], ['瓦里斯和富士那群岛(法)', 205.1, 17],
    ['西撒哈拉', 205.1, 17], ['桑给巴尔', 168.3, 17], ['文莱', 148.3, 17.6],
    ['南苏丹', 205.1, 17], ['加勒比荷兰', 190.6, 17], ['布韦岛', 205.1, 17],
    ['赫德岛和麦克唐纳群岛', 205.1, 17], ['英属印度洋领地', 209.66, 18.7],
    ['皮特凯恩群岛', 172.4, 17], ['法属南部和南极领地', 205.1, 17],
    ['阿森松岛', 205.1, 17], ['圣巴泰勒米岛', 205.1, 17], ['奥尔德尼岛', 209.66, 18.7],
    ['中国台湾', 94.3, 17.6], ['中国香港特别行政区', 104.5, 17.6],
    ['南非', 138.9, 29.3], ['毛里求斯', 205.1, 17], ['佛得角', 205.1, 17],
    ['埃及', 187.2, 17], ['突尼斯', 194.6, 17], ['津巴布韦', 168.3, 17],
    ['马拉维', 206.1, 17], ['多哥', 208.2, 17], ['马里', 205.1, 17],
    ['乍得', 210.3, 17], ['马尔代夫', 150, 18], ['塞尔维亚', 150, 18],
    ['孟加拉国', 175, 18], ['黑山', 190, 18], ['乌干达', 190, 18],
    ['法属瓜德罗普岛', 205.1, 17], ['马提尼克岛', 205.1, 17], ['法属圭亚那', 205.1, 17],
    ['马约特岛', 205.1, 17], ['博茨瓦纳', 175, 25], ['塞内加尔', 205, 18],
    ['卢旺达', 205, 18], ['喀麦隆', 175, 25], ['塞浦路斯', 168, 16],
    // Countries with special multi-tier pricing (using first tier)
    ['俄罗斯', 81, 17], ['乌克兰', 118.98, 7.4], ['美国', 72.45, 30.45],
    ['韩国', 29.68, 15.9], ['瑞士', 126.82, 21.95],
    // European countries from the 0~150g tier
    ['波兰', 72.15, 11.62], ['奥地利', 73.5, 23.1], ['比利时', 75.25, 23.4],
    ['保加利亚', 131.13, 19.45], ['丹麦', 71.7, 23.8], ['法国', 91.74, 17.02],
    ['德国', 70.44, 18.85], ['爱尔兰', 90.9, 22.46], ['意大利', 63.8, 23.4],
    ['拉脱维亚', 79, 23], ['立陶宛', 109.98, 24.4], ['卢森堡', 62.81, 22.99],
    ['马耳他', 137.39, 20.79], ['罗马尼亚', 70.5, 51.41], ['斯洛伐克', 89.99, 19.17],
    ['斯洛文尼亚', 122.3, 17], ['西班牙', 64.67, 19.26], ['瑞典', 73.8, 19.6],
    ['英国', 67.76, 15.9], ['克罗地亚', 85.84, 22.04],
    ['巴西', 68.26, 29.01], ['以色列', 161.67, 19.4], ['墨西哥', 124.2, 20.95],
    ['智利', 131.56, 20.95],
    ['捷克', 74, 20.95], ['芬兰', 76.09, 26.96], ['希腊', 84.26, 27.17],
    ['匈牙利', 84.62, 21.35], ['荷兰', 69.03, 24.62], ['葡萄牙', 85.35, 20.95],
    ['挪威', 106.5, 25.45], ['秘鲁', 176.19, 19.58], ['摩洛哥', 140.9, 17],
    ['马来西亚', 18, 8], ['泰国', 40, 14.4], ['越南', 27, 6],
    ['黎巴嫩', 145, 18], ['巴勒斯坦', 85, 18],
  ];

  // ==================== 超级经济Global 最新运费 ====================
  const globalEco = [
    ['阿尔及利亚', 220.31, 0.65], ['安道尔', 186.34, 4], ['安哥拉', 183.34, 0.65],
    ['亚美尼亚', 145.38, 0.65], ['阿塞拜疆', 148.38, 0.65], ['孟加拉国', 115.41, 0.65],
    ['不丹', 170.36, 2], ['波斯尼亚和黑塞哥维那', 187.99, 0.68], ['保加利亚', 78.88, 1.36],
    ['布基纳法索', 219.31, 0.65], ['布隆迪', 140.38, 0.65], ['智利', 113.04, 7.18],
    ['哥伦比亚', 165.36, 1.05], ['哥斯达黎加', 178.68, 0.75], ['刚果(金)', 230.7, 1.32],
    ['吉布提', 170.36, 2], ['埃及', 140.38, 0.65], ['赤道几内亚', 239.29, 0.65],
    ['福克兰群岛', 170.36, 2], ['芬兰', 104.56, 7.94], ['加蓬', 239.29, 0.65],
    ['冈比亚', 160.37, 1.51], ['加纳', 159.37, 0.65], ['直布罗陀(英)', 100.42, 8],
    ['关岛(美)', 180.35, 2], ['危地马拉', 264.85, 0.75], ['几内亚比绍', 123.4, 6.8],
    ['印度尼西亚', 130.39, 0.65], ['以色列', 74.63, 7.67], ['约旦', 131.39, 0.65],
    ['柬埔寨', 141.38, 0.65], ['哈萨克斯坦', 99, 1.2], ['肯尼亚', 170.36, 0.65],
    ['基里巴斯', 170.36, 2], ['吉尔吉斯斯坦', 140.38, 0.65], ['老挝', 101.42, 6.8],
    ['莱索托', 183.34, 2], ['利比里亚', 218.31, 0.65], ['利比亚', 158.76, 1.32],
    ['列支敦士登', 147.38, 0.65], ['北马其顿', 146.46, 0.55], ['马达加斯加', 185.34, 0.65],
    ['马拉维', 140.38, 0.65], ['马尔代夫', 140.38, 0.65], ['马里', 170.36, 2],
    ['毛里求斯', 160.37, 0.65], ['摩纳哥', 185.34, 3.51], ['蒙古', 149.38, 0.65],
    ['黑山', 170.36, 0.65], ['莫桑比克', 187.34, 0.65], ['缅甸', 114.41, 0.65],
    ['纳米比亚', 183.34, 0.65], ['尼加拉瓜', 200.51, 7.25], ['挪威', 123.53, 7.72],
    ['巴布亚新几内亚', 180.35, 2], ['菲律宾', 115.41, 0.65], ['葡萄牙', 108.31, 7.1],
    ['波多黎各(美)', 189.34, 4.81], ['摩尔多瓦', 183.34, 0.65], ['圣马力诺', 203.33, 0.65],
    ['塞内加尔', 218.31, 0.65], ['塞尔维亚', 116.28, 0.87], ['塞舌尔', 175.35, 0.65],
    ['斯洛伐克', 145.38, 0.65], ['斯洛文尼亚', 170.64, 0.75], ['所罗门群岛', 191.34, 0.65],
    ['韩国', 49.47, 6.71], ['斯威士兰', 184.34, 1.51], ['塔吉克斯坦', 93.92, 6.8],
    ['多哥', 140.38, 0.65], ['汤加', 170.36, 2], ['土耳其', 145.38, 0.65],
    ['土库曼斯坦', 98.42, 7], ['乌干达', 193.34, 0.65], ['坦桑尼亚', 188.34, 0.65],
    ['乌兹别克斯坦', 147.38, 0.65], ['瓦努阿图', 170.36, 2], ['越南', 115.41, 0.65],
    ['赞比亚', 184.34, 0.65], ['文莱', 116.4, 0.65], ['格鲁吉亚', 145.38, 0.65],
    ['几内亚', 201.33, 0.65], ['斯瓦尔巴群岛(挪)', 379.17, 0.65],
    ['圣马丁(荷)', 170.36, 2], ['萨尔瓦多', 230.38, 0.75], ['特立尼达和多巴哥', 140.38, 0.65],
    ['荷属安的列斯群岛', 85.43, 9.5], ['马绍尔群岛', 170.36, 2],
    ['东萨摩亚(美)', 170.36, 2], ['维尔京群岛(美)', 225.31, 0.65],
    ['密克罗尼西亚(美)', 170.36, 2], ['圣皮埃尔岛及密克隆岛', 170.36, 2],
    ['维尔京群岛(英)', 160.37, 1.51], ['格林纳达', 138.39, 5.11],
    ['安圭拉岛(英)', 379.17, 0.65], ['根西岛(英)', 75.44, 8],
    ['瓦里斯和富士那群岛(法)', 379.17, 0.65], ['开曼群岛(英)', 379.17, 0.65],
    ['马里亚纳群岛', 379.17, 0.65], ['科克群岛(新)', 170.36, 2],
    ['圣卢西亚', 141.38, 5.2], ['尼泊尔', 162.7, 1.5], ['巴拿马', 203.2, 1.5],
    ['卢旺达', 187, 1.5], ['南非', 161, 1.5], ['突尼斯', 154.6, 1.5],
    ['委内瑞拉', 203.2, 1.5], ['玻利维亚', 219.4, 1.5], ['博茨瓦纳', 195.1, 1.5],
    ['厄瓜多尔', 203.2, 1.5], ['洪都拉斯', 251.8, 1.5], ['印度', 161, 1.5],
    ['科特迪瓦', 383.3, 1.2], ['牙买加', 222.8, 1.2], ['蒙特塞拉特岛(英)', 383.3, 1.2],
    ['瑙鲁', 172.3, 2.55], ['阿鲁巴岛', 111.1, 5.95], ['诺福克岛(澳)', 383.3, 1.2],
    ['圣文森特岛(英)', 101.6, 5.95], ['圣多美和普林西比', 383.3, 1.2],
    ['巴哈马国', 383.3, 1.2], ['梵蒂冈', 136.9, 1.2], ['东帝汶', 383.3, 1.2],
    ['巴巴多斯', 222.8, 1.2], ['特克斯和凯科斯群岛(英)', 383.3, 1.2],
    ['图瓦卢', 383.3, 1.2], ['西撒哈拉', 383.3, 1.2], ['伯利兹', 149, 7.05],
    ['百慕大群岛(英)', 383.3, 1.2], ['圣诞岛', 383.3, 1.2], ['多米尼克国', 263.2, 4.65],
    ['多米尼加共和国', 178.3, 2.05], ['法属波里尼西亚', 170.36, 0.65],
    ['格陵兰岛', 383.3, 1.2], ['海地', 149, 7.05], ['伊拉克', 383.3, 1.2],
    ['斯里兰卡', 155.37, 1.51],
    // Multi-tier (using 101-2000g tier): Poland, Croatia, Cyprus, Czech, Estonia, Greece, Hungary, Japan, Latvia, Lithuania
    ['波兰', 47.63, 10.92], ['克罗地亚', 44.18, 9.25], ['塞浦路斯', 84.85, 1.36],
    ['捷克', 45.46, 9.45], ['爱沙尼亚', 55.33, 11.12], ['希腊', 36.61, 15.93],
    ['匈牙利', 45.66, 8.57], ['日本', 48.5, 7.19], ['拉脱维亚', 41.58, 9.23],
    ['立陶宛', 36.75, 7.82],
    // Multi-tier special: France, Israel, Kazakhstan, Thailand, Turkey, Netherlands
    // Using the >50g / >80g tier
    ['澳大利亚', 94.42, 6.6], ['法国', 69.3, 6.67], ['美国', 91.04, 11.2],
    ['瑞士', 73.44, 7.2], ['墨西哥', 77.44, 5], ['加拿大', 90, 7.1],
    ['英国', 87.07, 9.23],
  ];

  // ==================== 超级经济 最新运费 (USD) ====================
  const superEco = [
    ['俄罗斯', 23.47, 0.22], ['乌克兰', 23.48, 0.21], ['白俄罗斯', 19, 0.15],
    ['哈萨克斯坦', 14.14, 0.17], ['北马其顿', 17.71, 0.15], ['塞尔维亚', 16.09, 0.15],
    ['土耳其', 17.62, 0.15], ['保加利亚', 11.76, 0.21], ['克罗地亚', 6.6, 1.39],
    ['塞浦路斯', 12.64, 0.21], ['捷克', 6.3, 1.27], ['爱沙尼亚', 6.96, 1.4],
    ['芬兰', 5.5, 3], ['匈牙利', 5.93, 1.12], ['拉脱维亚', 5.85, 1.3],
    ['立陶宛', 5.5, 1.11], ['马耳他', 13.47, 0.21], ['葡萄牙', 6.98, 1.54],
    ['斯洛伐克', 5.77, 1.16], ['斯洛文尼亚', 4.31, 2],
  ];

  // ==================== 无忧特惠 最新运费 (USD) ====================
  const wuyouSaver = [
    ['俄罗斯', 21.81, 0.76], ['乌克兰', 19.32, 0.76], ['白俄罗斯', 23.1, 0.65],
    ['西班牙', 8.68, 1.85], ['波兰', 8.55, 0.98], ['韩国', 8.07, 1.09],
    ['捷克', 9.93, 1.35], ['斯洛伐克', 23.67, 0.11], ['匈牙利', 14.12, 0.86],
    ['保加利亚', 15.05, 0.22], ['斯洛文尼亚', 24.15, 0.11], ['克罗地亚', 24.15, 0.11],
    ['立陶宛', 11.05, 1.69], ['爱沙尼亚', 9.24, 1.78], ['塞尔维亚', 8.5, 1.2],
    ['摩尔多瓦', 30.1, 0.1], ['葡萄牙', 19.72, 1.1], ['罗马尼亚', 8, 6.98],
    ['塞浦路斯', 13, 0.25], ['马耳他', 14, 0.25], ['拉脱维亚', 12, 1.2],
    ['以色列', 18.01, 1.45], ['挪威', 16, 1.13], ['斯里兰卡', 26, 0.3],
    ['墨西哥', 7.15, 1.89], ['瑞典', 6.51, 2.55], ['丹麦', 9.27, 2.77],
    ['爱尔兰', 10.88, 2.63], ['澳大利亚', 21.84, 1.67],
  ];

  // ==================== 区域差价定价规则 运费数据 ====================
  const regionData = [
    ['统一标价', '平常小包+', 102, 5],
    ['俄罗斯联邦', '无忧标准', 81, 17], ['美国', '无忧标准', 72.45, 30.45],
    ['加拿大', '无忧标准', 122.44, 27.6], ['西班牙', '无忧标准', 64.67, 19.26],
    ['法国', '无忧标准', 91.74, 17.02], ['英国', '无忧标准', 67.76, 15.9],
    ['荷兰', '无忧标准', 69.03, 24.62], ['以色列', '无忧标准', 161.67, 19.4],
    ['巴西', '无忧标准', 68.26, 29.01], ['智利', '无忧标准', 131.56, 20.95],
    ['澳大利亚', '无忧标准', 102.59, 18.4], ['乌克兰', '无忧标准', 118.98, 7.4],
    ['白俄罗斯', '无忧标准', 136, 21], ['日本', '无忧标准', 64.45, 21.2],
    ['泰国', '无忧标准', 40, 14.4], ['新加坡', '无忧标准', 70.7, 8.1],
    ['韩国', '无忧标准', 29.68, 15.9], ['印度尼西亚', '无忧标准', 54.6, 16.8],
    ['马来西亚', '无忧标准', 18, 8], ['菲律宾', '无忧标准', 129.7, 18.6],
    ['越南', '无忧标准', 27, 6], ['意大利', '无忧标准', 63.8, 23.4],
    ['德国', '无忧标准', 70.44, 18.85], ['沙特阿拉伯', '无忧标准', 197.6, 52.43],
    ['阿拉伯联合酋长国', '无忧标准', 254.97, 15.85], ['波兰', '无忧标准', 72.15, 11.62],
    ['土耳其', '无忧标准', 100, 20.4],
  ];

  // ==================== SHEET 1: 总览 ====================
  const ws1 = wb.addWorksheet('总览', { views: [{ state: 'frozen', xSplit: 0, ySplit: 3 }] });

  // Title row
  ws1.mergeCells('A1:P1');
  const titleCell = ws1.getCell('A1');
  titleCell.value = 'AliExpress 速卖通运费利润计算表 (2026最新运费版)';
  titleCell.font = titleFont;
  titleCell.alignment = { horizontal: 'center', vertical: 'middle' };
  ws1.getRow(1).height = 32;

  // Section headers row 2
  const sectionHeaders = [
    { col: 1, span: 4, text: '无忧物流-标准 (RMB)', note: '单位: RMB/KG + RMB/包裹' },
    { col: 5, span: 4, text: '菜鸟超级经济Global (RMB)', note: '单位: RMB/KG + RMB/包裹' },
    { col: 9, span: 4, text: '菜鸟超级经济 (USD)', note: '单位: USD/KG + USD/包裹' },
    { col: 13, span: 4, text: '无忧物流-特惠 (USD)', note: '单位: USD/KG + USD/包裹' },
  ];
  sectionHeaders.forEach(h => {
    ws1.mergeCells(2, h.col, 2, h.col + h.span - 1);
    const c = ws1.getCell(2, h.col);
    c.value = h.text;
    c.fill = headerFill;
    c.font = { ...headerFont, size: 11 };
    c.alignment = { horizontal: 'center', vertical: 'middle' };
    c.border = BORDER_ALL;
  });
  ws1.getRow(2).height = 24;

  // Column headers row 3
  const colHeaders = ['国家', '公布价', '挂号费', '利润率'];
  for (let sec = 0; sec < 4; sec++) {
    colHeaders.forEach((h, i) => {
      const c = ws1.getCell(3, sec * 4 + i + 1);
      c.value = h;
      c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: LIGHT_BLUE } };
      c.font = { ...boldFont, color: { argb: DARK_BLUE } };
      c.alignment = { horizontal: 'center', vertical: 'middle' };
      c.border = BORDER_ALL_MED;
    });
  }

  // === Parameters section (right side) ===
  // Place params in columns Q-R (17-18)
  const paramLabels = ['产品成本', '产品重量', '产品售价', '标价'];
  const paramValues = [13, 100, null, null]; // 售价 and 标价 are formulas
  const paramRow = 3;
  ws1.getCell(paramRow, 17).value = '参数设置';
  ws1.getCell(paramRow, 17).font = { ...boldFont, size: 11, color: { argb: DARK_BLUE } };
  ws1.mergeCells(paramRow, 17, paramRow, 18);
  ws1.getCell(paramRow, 17).alignment = { horizontal: 'center' };
  ws1.getCell(paramRow, 17).fill = headerFill;
  ws1.getCell(paramRow, 17).font = headerFont;
  ws1.getCell(paramRow, 18).fill = headerFill;

  for (let i = 0; i < paramLabels.length; i++) {
    const r = paramRow + 1 + i;
    const lc = ws1.getCell(r, 17);
    lc.value = paramLabels[i];
    lc.font = boldFont;
    lc.fill = labelFill;
    lc.border = BORDER_ALL_MED;
    lc.alignment = { horizontal: 'right' };
    const vc = ws1.getCell(r, 18);
    vc.border = BORDER_ALL_MED;
    vc.alignment = { horizontal: 'center' };
    if (i < 2) {
      vc.value = paramValues[i];
      vc.fill = inputFill;
      vc.font = { ...boldFont, color: { argb: '0000FF' } };
    }
  }
  // 产品售价 = 产品成本 / 7.25 (汇率)  — simplified placeholder
  ws1.getCell(paramRow + 3, 18).value = 4.96;
  ws1.getCell(paramRow + 3, 18).fill = inputFill;
  ws1.getCell(paramRow + 3, 18).font = { ...boldFont, color: { argb: '0000FF' } };

  // 标价 placeholder
  ws1.getCell(paramRow + 4, 18).value = '';

  // Additional params
  const extraParams = [
    ['汇率(RMB/USD)', 7.25], ['目标利润率', 0.2], ['活动折扣', 0.3], ['平台费率', 0.13]
  ];
  for (let i = 0; i < extraParams.length; i++) {
    const r = paramRow + 5 + i;
    const lc = ws1.getCell(r, 17);
    lc.value = extraParams[i][0];
    lc.font = boldFont;
    lc.fill = labelFill;
    lc.border = BORDER_ALL_MED;
    lc.alignment = { horizontal: 'right' };
    const vc = ws1.getCell(r, 18);
    vc.value = extraParams[i][1];
    vc.fill = inputFill;
    vc.font = { ...boldFont, color: { argb: '0000FF' } };
    vc.border = BORDER_ALL_MED;
    vc.alignment = { horizontal: 'center' };
    if (i >= 1) vc.numFmt = '0%';
  }

  // === Fill data rows ===
  // Determine max rows
  const maxRows = Math.max(wuyouStd.length, globalEco.length, superEco.length, wuyouSaver.length);

  // Helper to compute shipping cost: (weight/1000)*公布价 + 挂号费
  // And profit rate: (售价*汇率 - 成本 - 运费) / (售价*汇率)
  // We use R4C18=成本(13), R5C18=重量(100), R6C18=售价(4.96), R8C18=汇率(7.25)
  const dataStartRow = 4;

  // Fill 无忧标准 (columns 1-4) — RMB based
  for (let i = 0; i < wuyouStd.length; i++) {
    const r = dataStartRow + i;
    const row = ws1.getRow(r);
    const isAlt = i % 2 === 1;
    const fill = isAlt ? altFill : undefined;

    const c1 = ws1.getCell(r, 1); c1.value = wuyouStd[i][0]; c1.font = defaultFont; c1.border = BORDER_ALL; if (fill) c1.fill = fill;
    const c2 = ws1.getCell(r, 2); c2.value = wuyouStd[i][1]; c2.font = defaultFont; c2.numFmt = '#,##0.00'; c2.border = BORDER_ALL; if (fill) c2.fill = fill;
    const c3 = ws1.getCell(r, 3); c3.value = wuyouStd[i][2]; c3.font = defaultFont; c3.numFmt = '#,##0.00'; c3.border = BORDER_ALL; if (fill) c3.fill = fill;
    // 利润率公式: (售价*汇率 - 成本 - (重量/1000)*公布价 - 挂号费) / (售价*汇率)
    const c4 = ws1.getCell(r, 4);
    c4.value = { formula: `($R$6*$R$8-$R$4-(($R$5/1000)*B${r}+C${r}))/($R$6*$R$8)` };
    c4.font = defaultFont; c4.numFmt = '0.00%'; c4.border = BORDER_ALL; if (fill) c4.fill = fill;
  }

  // Fill 超级经济Global (columns 5-8) — RMB based
  for (let i = 0; i < globalEco.length; i++) {
    const r = dataStartRow + i;
    const isAlt = i % 2 === 1;
    const fill = isAlt ? altFill : undefined;

    const c5 = ws1.getCell(r, 5); c5.value = globalEco[i][0]; c5.font = defaultFont; c5.border = BORDER_ALL; if (fill) c5.fill = fill;
    const c6 = ws1.getCell(r, 6); c6.value = globalEco[i][1]; c6.font = defaultFont; c6.numFmt = '#,##0.00'; c6.border = BORDER_ALL; if (fill) c6.fill = fill;
    const c7 = ws1.getCell(r, 7); c7.value = globalEco[i][2]; c7.font = defaultFont; c7.numFmt = '#,##0.00'; c7.border = BORDER_ALL; if (fill) c7.fill = fill;
    const c8 = ws1.getCell(r, 8);
    c8.value = { formula: `($R$6*$R$8-$R$4-(($R$5/1000)*F${r}+G${r}))/($R$6*$R$8)` };
    c8.font = defaultFont; c8.numFmt = '0.00%'; c8.border = BORDER_ALL; if (fill) c8.fill = fill;
  }

  // Fill 超级经济 (columns 9-12) — USD based
  for (let i = 0; i < superEco.length; i++) {
    const r = dataStartRow + i;
    const isAlt = i % 2 === 1;
    const fill = isAlt ? altFill : undefined;

    const c9 = ws1.getCell(r, 9); c9.value = superEco[i][0]; c9.font = defaultFont; c9.border = BORDER_ALL; if (fill) c9.fill = fill;
    const c10 = ws1.getCell(r, 10); c10.value = superEco[i][1]; c10.font = defaultFont; c10.numFmt = '#,##0.00'; c10.border = BORDER_ALL; if (fill) c10.fill = fill;
    const c11 = ws1.getCell(r, 11); c11.value = superEco[i][2]; c11.font = defaultFont; c11.numFmt = '#,##0.00'; c11.border = BORDER_ALL; if (fill) c11.fill = fill;
    // USD: 运费=(重量/1000)*公布价+挂号费 (USD), 利润率=(售价 - 成本/汇率 - 运费USD)/售价
    const c12 = ws1.getCell(r, 12);
    c12.value = { formula: `($R$6-$R$4/$R$8-(($R$5/1000)*J${r}+K${r}))/$R$6` };
    c12.font = defaultFont; c12.numFmt = '0.00%'; c12.border = BORDER_ALL; if (fill) c12.fill = fill;
  }

  // Fill 无忧特惠 (columns 13-16) — USD based
  for (let i = 0; i < wuyouSaver.length; i++) {
    const r = dataStartRow + i;
    const isAlt = i % 2 === 1;
    const fill = isAlt ? altFill : undefined;

    const c13 = ws1.getCell(r, 13); c13.value = wuyouSaver[i][0]; c13.font = defaultFont; c13.border = BORDER_ALL; if (fill) c13.fill = fill;
    const c14 = ws1.getCell(r, 14); c14.value = wuyouSaver[i][1]; c14.font = defaultFont; c14.numFmt = '#,##0.00'; c14.border = BORDER_ALL; if (fill) c14.fill = fill;
    const c15 = ws1.getCell(r, 15); c15.value = wuyouSaver[i][2]; c15.font = defaultFont; c15.numFmt = '#,##0.00'; c15.border = BORDER_ALL; if (fill) c15.fill = fill;
    const c16 = ws1.getCell(r, 16);
    c16.value = { formula: `($R$6-$R$4/$R$8-(($R$5/1000)*N${r}+O${r}))/$R$6` };
    c16.font = defaultFont; c16.numFmt = '0.00%'; c16.border = BORDER_ALL; if (fill) c16.fill = fill;
  }

  // Set column widths
  [14, 10, 9, 9, 14, 10, 9, 9, 14, 10, 9, 9, 14, 10, 9, 9, 14, 12].forEach((w, i) => {
    ws1.getColumn(i + 1).width = w;
  });

  // ==================== SHEET 2: 区域差价定价规则 ====================
  const ws2 = wb.addWorksheet('区域差价定价规则', { views: [{ state: 'frozen', xSplit: 0, ySplit: 2 }] });

  // Title
  ws2.mergeCells('A1:L1');
  const t2 = ws2.getCell('A1');
  t2.value = '区域差价定价规则 (2026最新运费版)';
  t2.font = titleFont;
  t2.alignment = { horizontal: 'center', vertical: 'middle' };
  ws2.getRow(1).height = 30;

  // Headers
  const h2 = ['国家', '使用物流方式', '运费(KG单价)', '挂号费', '产品成本', '产品重量', '产品运费', '产品利润', '标价', '25%折标价', '30%折标价', '利润率'];
  h2.forEach((h, i) => {
    const c = ws2.getCell(2, i + 1);
    c.value = h;
    c.fill = headerFill;
    c.font = headerFont;
    c.alignment = { horizontal: 'center', vertical: 'middle' };
    c.border = BORDER_ALL;
  });
  ws2.getRow(2).height = 22;

  // Parameter cells: row 3 has the base params (editable)
  const paramCellsRow = 3;
  // Labels
  ws2.getCell(paramCellsRow, 1).value = '▼ 可修改参数 →';
  ws2.getCell(paramCellsRow, 1).font = { ...boldFont, color: { argb: 'C00000' } };
  ws2.getCell(paramCellsRow, 1).alignment = { horizontal: 'right' };
  ws2.getCell(paramCellsRow, 5).value = 13.5;
  ws2.getCell(paramCellsRow, 5).fill = inputFill;
  ws2.getCell(paramCellsRow, 5).font = { ...boldFont, color: { argb: '0000FF' } };
  ws2.getCell(paramCellsRow, 5).border = BORDER_ALL_MED;
  ws2.getCell(paramCellsRow, 6).value = 50;
  ws2.getCell(paramCellsRow, 6).fill = inputFill;
  ws2.getCell(paramCellsRow, 6).font = { ...boldFont, color: { argb: '0000FF' } };
  ws2.getCell(paramCellsRow, 6).border = BORDER_ALL_MED;
  ws2.getCell(paramCellsRow, 6).note = '产品重量(克)';
  ws2.getCell(paramCellsRow, 7).value = 7.55;
  ws2.getCell(paramCellsRow, 7).fill = inputFill;
  ws2.getCell(paramCellsRow, 7).font = { ...boldFont, color: { argb: '0000FF' } };
  ws2.getCell(paramCellsRow, 7).border = BORDER_ALL_MED;
  ws2.getCell(paramCellsRow, 7).note = '目标利润(RMB)';

  // Fill region data
  for (let i = 0; i < regionData.length; i++) {
    const r = paramCellsRow + 1 + i;
    const d = regionData[i];
    const isAlt = i % 2 === 1;
    const fill = isAlt ? altFill : undefined;

    ws2.getCell(r, 1).value = d[0]; ws2.getCell(r, 1).font = boldFont; ws2.getCell(r, 1).border = BORDER_ALL; if (fill) ws2.getCell(r, 1).fill = fill;
    ws2.getCell(r, 2).value = d[1]; ws2.getCell(r, 2).font = defaultFont; ws2.getCell(r, 2).border = BORDER_ALL; if (fill) ws2.getCell(r, 2).fill = fill;
    ws2.getCell(r, 3).value = d[2]; ws2.getCell(r, 3).font = defaultFont; ws2.getCell(r, 3).numFmt = '#,##0.00'; ws2.getCell(r, 3).border = BORDER_ALL; if (fill) ws2.getCell(r, 3).fill = fill;
    ws2.getCell(r, 4).value = d[3]; ws2.getCell(r, 4).font = defaultFont; ws2.getCell(r, 4).numFmt = '#,##0.00'; ws2.getCell(r, 4).border = BORDER_ALL; if (fill) ws2.getCell(r, 4).fill = fill;

    // 产品成本
    ws2.getCell(r, 5).value = { formula: `$E$3` }; ws2.getCell(r, 5).font = defaultFont; ws2.getCell(r, 5).border = BORDER_ALL; if (fill) ws2.getCell(r, 5).fill = fill;
    // 产品重量
    ws2.getCell(r, 6).value = { formula: `$F$3` }; ws2.getCell(r, 6).font = defaultFont; ws2.getCell(r, 6).border = BORDER_ALL; if (fill) ws2.getCell(r, 6).fill = fill;
    // 产品运费 = (重量/1000)*KG单价 + 挂号费
    ws2.getCell(r, 7).value = { formula: `(F${r}/1000)*C${r}+D${r}` };
    ws2.getCell(r, 7).font = defaultFont; ws2.getCell(r, 7).numFmt = '#,##0.00'; ws2.getCell(r, 7).border = BORDER_ALL; if (fill) ws2.getCell(r, 7).fill = fill;
    // 产品利润 = $G$3 (汇率) — placeholder
    ws2.getCell(r, 8).value = { formula: `$G$3` }; ws2.getCell(r, 8).font = defaultFont; ws2.getCell(r, 8).numFmt = '#,##0.00'; ws2.getCell(r, 8).border = BORDER_ALL; if (fill) ws2.getCell(r, 8).fill = fill;
    // 标价(USD) = (成本+运费+利润)/汇率/7.25  — use formula
    ws2.getCell(r, 9).value = { formula: `(E${r}+G${r}+H${r})/7.25` };
    ws2.getCell(r, 9).font = defaultFont; ws2.getCell(r, 9).numFmt = '"$"#,##0.00'; ws2.getCell(r, 9).border = BORDER_ALL; if (fill) ws2.getCell(r, 9).fill = fill;
    // 25%折标价
    ws2.getCell(r, 10).value = { formula: `I${r}/0.75` };
    ws2.getCell(r, 10).font = defaultFont; ws2.getCell(r, 10).numFmt = '"$"#,##0.00'; ws2.getCell(r, 10).border = BORDER_ALL; if (fill) ws2.getCell(r, 10).fill = fill;
    // 30%折标价
    ws2.getCell(r, 11).value = { formula: `I${r}/0.7` };
    ws2.getCell(r, 11).font = defaultFont; ws2.getCell(r, 11).numFmt = '"$"#,##0.00'; ws2.getCell(r, 11).border = BORDER_ALL; if (fill) ws2.getCell(r, 11).fill = fill;
    // 利润率
    ws2.getCell(r, 12).value = { formula: `H${r}/(I${r}*7.25)` };
    ws2.getCell(r, 12).font = defaultFont; ws2.getCell(r, 12).numFmt = '0.00%'; ws2.getCell(r, 12).border = BORDER_ALL; if (fill) ws2.getCell(r, 12).fill = fill;
  }

  // Column widths for sheet 2
  [16, 12, 12, 10, 10, 10, 10, 10, 10, 10, 10, 10].forEach((w, i) => {
    ws2.getColumn(i + 1).width = w;
  });

  // ==================== SHEET 3: 快速计算 ====================
  const ws3 = wb.addWorksheet('快速计算');
  ws3.getCell('A1').value = '拿货价'; ws3.getCell('B1').value = '运费'; ws3.getCell('C1').value = '成本';
  ws3.getCell('D1').value = '售价(USD)'; ws3.getCell('E1').value = '0.75标价'; ws3.getCell('F1').value = '0.85标价';
  ['A1','B1','C1','D1','E1','F1'].forEach(ref => {
    const c = ws3.getCell(ref);
    c.fill = headerFill; c.font = headerFont; c.alignment = { horizontal: 'center' }; c.border = BORDER_ALL;
  });

  ws3.getCell('A2').value = 18.5; ws3.getCell('A2').fill = inputFill; ws3.getCell('A2').font = { ...boldFont, color: { argb: '0000FF' } };
  ws3.getCell('B2').value = 0; ws3.getCell('B2').fill = inputFill; ws3.getCell('B2').font = { ...boldFont, color: { argb: '0000FF' } };
  ws3.getCell('C2').value = { formula: 'A2+B2' }; ws3.getCell('C2').numFmt = '#,##0.00';
  ws3.getCell('D2').value = { formula: 'C2/7.25/(1-0.13-0.2)' }; ws3.getCell('D2').numFmt = '"$"#,##0.00';
  ws3.getCell('E2').value = { formula: 'D2/0.75' }; ws3.getCell('E2').numFmt = '"$"#,##0.00';
  ws3.getCell('F2').value = { formula: 'D2/0.85' }; ws3.getCell('F2').numFmt = '"$"#,##0.00';

  [2,3,4,5,6].forEach(i => { ws3.getColumn(i).width = 12; });
  ws3.getColumn(1).width = 10;

  // ==================== SAVE ====================
  const outPath = 'C:\\Users\\Administrator\\Desktop\\2019维格运费利润计算表_最新运费更新版.xlsx';
  await wb.xlsx.writeFile(outPath);
  console.log('File saved to: ' + outPath);
}

main().catch(e => { console.error(e); process.exit(1); });
