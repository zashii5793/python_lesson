import openpyxl
openpyxl.path.abspath()

https://techacademy.jp/magazine/18986

# base.pyのあるディレクトリの絶対パスを取得
current_dir = pathlib.Path(__file__).resolve().parent
# モジュールのあるパスを追加
sys.path.append( str(current_dir) + '/../' )

#Macでは、optionキーを押しながら、¥キーを押す。(Mac mini 等で Windows用のキーボードを接続している場合は Alt キー)

wb = openpyxl.load_workbook(".\list.xlsx")

for sheet in wb:
    for row in sheet:
        for cell in row:
            print(cell.value)