import openpyxl

#Macでは、optionキーを押しながら、¥キーを押す。(Mac mini 等で Windows用のキーボードを接続している場合は Alt キー)

wb = openpyxl.load_workbook(".\list.xlsx")

for sheet in wb:
    for row in sheet:
        for cell in row:
            print(cell.value)