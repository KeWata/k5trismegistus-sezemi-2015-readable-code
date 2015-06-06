# k5trismegistus-sezemi-2015-readable-code
## environment
Python 3.4.3

## how to use
レシピのデータは文字コードがUTF-8であるcsv形式で作成します。
レシピの格納されているファイルを引数として与えると、ファイルに含まれているレシピデータを出力します。
レシピデータは現時点で「レシピ名」しか扱えません。なので、recipe_nameの下にレシピ名を追記していってください。
1行について1レシピを扱うことができます。

'''
python cookingpapa.py recipe.csv

=> ['オムライス']
'''