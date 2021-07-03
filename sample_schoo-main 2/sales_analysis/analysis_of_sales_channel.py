import os
import pandas as pd

# Windows の方は
# folder_path = '.\\excel\\'
folder_path = './excel/'


def get_sales_data(path):
    # フォルダの中のファイルをすべて取り出す
    excel_files = os.listdir(path)
    # Excelファイルの中のデータを取り出すためのリストを定義
    list_sales_data = []
    # Excelファイルの売上データを取り出す
    for excel_file in excel_files:
        if '売上' in excel_file:
            sales_data = pd.read_excel(path + excel_file)
            list_sales_data.append(sales_data)
    # 取り出した売上データを連結する
    sales_summary = pd.concat(list_sales_data, ignore_index=True)
    return sales_summary


def get_channel_data(path):
    # 取引先流入元データをpandasで読み込む
    sales_channel = pd.read_excel(path + '取引先流入元.xlsx')
    return sales_channel


# 売上データと流入元データを取得
sales = get_sales_data(folder_path)
channel = get_channel_data(folder_path)

# 流入元データと、売上サマリーデータを結合する
sales_summary = pd.merge(channel, sales, on='取引先名')

# 流入元ごとの売上データを集計
sales_by_channel = sales_summary.groupby('流入元').sum()

# 流入元ごとの売上データを出力
print(sales_by_channel)

# Excelに集計したデータを出力
with pd.ExcelWriter('summary.xlsx') as writer:
    sales_summary.to_excel(writer, sheet_name='売上サマリー')
    sales_by_channel.to_excel(writer, sheet_name='流入元ごとの売上')

target_symbol = 'Gold'
start = '2019-1-1'
end = '2019-12-31'

if __name__=='__main__' :
  plot_chart( df_data ,target_symbol ,start ,end )


start_date = '2007-1-1'
dict_target_symbols = {
                       ##
                       # 市場：何を買い、何を売るか
                       #

                       # 為替
                        'j6.f':'Japanese Yen'      # 日本円
                       ,'e6.f':'Euro'              # ユーロ
                       ,'b6.f':'British Pound'     # 英ポンド
                       ,'s6.f':'Swiss Franc'       # スイスフラン
                       ,'d6.f':'Canadian Dollar'   # カナダドル
                       ,'a6.f':'Austrarian Dollar' # 豪ドル
                       ,'m6.f':'Mexican Peso'      # メキシコペソ
                       # 貴金属
                       ,'gc.f':'Gold'              # 金
                       ,'si.f':'Silver'            # 銀
                       ,'hg.f':'High Grade Copper' # 銅
                       # 燃料
                       ,'cl.f':'Crude Oil'         # WTI原油
                       ,'ho.f':'ULSD NY Harbor'    # 灯油 ULSD
                       ,'rb.f':'Gasoline RBOB'     # 無鉛ガソリン
                       ,'ng.f':'Nature Gas'        # 天然ガス
                       # 農畜産物
                       ,'zc.f':'Corn'              # とうもろこし
                       ,'zs.f':'Soybean'           # 大豆
                       ,'zw.f':'Wheat'             # 小麦
                       ,'sb.f':'Sugar'             # 砂糖
                       ,'ct.f':'Cotton'            # 綿
                       ,'cc.f':'Cocoa'             # ココア
                       ,'kc.f':'Coffee'            # コーヒー
                       ,'gf.f':'Feeder Cattle'     # 飼養牛
                       ,'le.f':'Live Cattle'       # 牛
                       ,'lh.f':'Lean Hogs'         # 豚
                       # 債権・金利
                       ,'ge.f':'Eurodollar'        # ユーロドル金利先物
                       ,'zf.f':'5 Year T Note'     # 財務省中期債権
                       ,'zn.f':'10 Year T Note'    # 同長期債権
                       # 全27銘柄
                       }                  

if __name__=='__main__' :
  df_data = set_price_data( start_date ,dict_target_symbols )

target_symbol = 'Gold'
start = '2019-1-1'
end = '2019-12-31'

if __name__=='__main__' :
  plot_chart( df_data ,target_symbol ,start ,end )
  
  