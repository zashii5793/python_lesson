import shutil

try:
    shutil.copytree('./before','./after')
except FileExistsError as e:
    print('すでにafterフォルダが存在しています')
    