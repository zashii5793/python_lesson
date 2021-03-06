import tkinter as tk
import numpy as np
import sys

# ボタンを押したときの処理 --- (*1)
def calc_bmi():
    # BMIを計算
    h = float(textHeight.get()) / 100
    w = float(textWeight.get())
    bmi = w / h ** 2
    rw = h ** 2 * 22
    per = int(w / rw * 100) - 100
    # 結果をラベルに表示
    s = "肥満 {0}% (bmi={1})".format(per, bmi)
    labelResult['text'] = s


def calc_go():

    labelResult['text'] = sum(range(1,101))
  

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("肥満判定")
win.geometry("500x250")

# 部品を作成 --- (*3)
labelHeight = tk.Label(win, text=u'身長(cm):')
labelHeight.pack()

textHeight = tk.Entry(win)
textHeight.insert(tk.END, '160')
textHeight.pack()

labelWeight = tk.Label(win, text=u'体重(kg):')
labelWeight.pack()

textWeight = tk.Entry(win)
textWeight.insert(tk.END, '70')
textWeight.pack()

labelResult = tk.Label(win, text=u'---')
labelResult.pack()

labeltest = tk.Label(win, text=u'test')
labeltest.pack()

calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_bmi
calcButton.pack()

testButton = tk.Button(win, text=u'Go')
testButton["command"] = calc_go
testButton.pack()

# ウィンドウを動かす
win.mainloop()

n = 0
for i in range(21):
    print(i)
