# k5trismegistus-sezemi-2015-readable-code
## environment
Python 3.4.3

## how to use
レシピのデータは文字コードがUTF-8であるcsv形式で作成します。
レシピの格納されているファイルを引数として与えると、ファイルに含まれているレシピデータを出力します。
レシピデータにはidと名前が必要です。
１行について１レシピ分のデータを格納します。
id, 名前
という形式で追記していってください。

'''
python cookingpapa.py recipe.csv

=> 0: オムライス
'''