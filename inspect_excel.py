import pandas as pd
import sys

def preview_excel(path, label):
    try:
        print(f'--- {label} ---')
        xl = pd.ExcelFile(path)
        print(f'Sheets: {xl.sheet_names}')
        for sheet in xl.sheet_names[:1]: # just preview first sheet for now
            print(f'\nSheet: {sheet}')
            df = pd.read_excel(path, sheet_name=sheet)
            print(df.head(10).to_string())
            print(f'\nColumns in {sheet}: {df.columns.tolist()}')
    except Exception as e:
        print(f'Error reading {path}: {e}')

template_path = r'C:\Users\Administrator\Desktop\2019维格运费利润计算表.xlsx'
shipping_path = r'C:\Users\Administrator\Desktop\速卖通最新运费单.xlsx'

preview_excel(template_path, 'Template')
preview_excel(shipping_path, 'Shipping Rates')
