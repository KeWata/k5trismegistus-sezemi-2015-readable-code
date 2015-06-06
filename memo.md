# task1

## code
https://github.com/k5trismegistus/k5trismegistus-sezemi-2015-readable-code/blob/2aa619ac1bc90caebb895426f872c1322759f077/cookingpapa.py

## explaination
余計なことはせずにシンプルにする

## in short
考え過ぎない


# task3

## code
https://github.com/k5trismegistus/k5trismegistus-sezemi-2015-readable-code/blob/55fe391fb753daa8bdad3d5c4d0d1e44ee7ebbc4/cookingpapa.py

## explaination
今後、どのように仕様が変化していくかはわからない（というのが現実的な仮定）なので、
まだ仕様で言われたことだけを忠実にこなすシンプルなスクリプトにとどめている。
レシピデータを格納するクラスなどを今の段階で作ってしまうと、予想していたのと違う要求が来た場合に
大改修が必要になってしまう。

## in short
言われたことだけをこなす


# task4

## explaination
task3と同じ

# task5

## code
https://github.com/k5trismegistus/k5trismegistus-sezemi-2015-readable-code/blob/d26125ee67f2582da294da52e338e4c19d63cf57/cookingpapa.py

## explaination
レシピデータに複数のカラムが出てきましたが、まだ独自クラスは作らず辞書形式で格納しています。
キーとしてrecipe_idやrecipe_nameといった読めばわかる名前を使っています。
複数のレシピデータをあつかうのも、その各レシピデータの格納される辞書をリスト形式で実装しました。

## in short
あるものは使う

## 啓太
```python
load_recipe_data(csv_name)
```
関数名に動作を，変数名にどういったデータを格納するべきかが記述されている．
```python
for recipe in recipe_list:
```
なにをイテレートしているかが明確である．

```python
print_recipe_all(recipe_list)
```
プリントをするにしても，引数の一部なのか全部なのか，それが指定されているのがリーダブル!
```



### 以下変更点
```python
load_recipe_data_from_files
```
複数のファイルからデータを読み込む際に，現在の関数を複数回呼べるようにする関数．

