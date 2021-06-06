
#export PYTHONPATH="/Users/user/opt/anaconda3/lib/python3.8/site-packages/openpyxl:$PYTHONPATH"

import openpyxl
import os

#openpyxl.path.abspath()
#/Users/user/opt/anaconda3/lib/python3.8/site-packages/openpyxl
#https://techacademy.jp/magazine/18986

# base.pyのあるディレクトリの絶対パスを取得
#Macでは、optionキーを押しながら、¥キーを押す。(Mac mini 等で Windows用のキーボードを接続している場合は Alt キー)

wb = openpyxl.load_workbook(".\list.xlsx")

for sheet in wb:
    for row in sheet:
        for cell in row:
            print(cell.value)