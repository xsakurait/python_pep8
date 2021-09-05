urlに#つける、urlフラグメント(フラグメント識別子)(アンカー)
#WEBページの特定の場所にアクセスしたとき、表示するためにurlに着けるもの（これはgoogleの検証で行きたい部分のaのhrefを見ないと指定できない）
# """
# 例<h1>あ</h1>
# <a href=#a_tag>'</a>
# """
#pythonのコーディング規約="PEP8"
#インデントは、tabを使用せずに半角スペース４つで統一

# NO a=1 # comment
#YES a=1  # comment(横に書くときは半角2マス開ける)
#ブロックコメント(１行コメント）も、#とスペース１つから始める
# comment

# def a()
(エラー)
'''
a
b
'''

# def a()
    '''
    a
    b 
    '''
#a=[1,2
    3](3は1のところに合わせる)

'''
def a(a=1,
      b=1)(引数は中身と区別させるため半角２マス分開ける)

def a():
    pass

(インデントがない=(トップレベル)所に書く関数やクラスに関しては半角２マス開ける)
def b():

    def __init__(self):
        pass

    def a(self,a):
        pass
'''

'''
import os
import sys(２行に分けて書く)
同一モジュールの場合は、まとめて書く
from datetime import datetime
from datetime import date
〇from datetime import datetime,date

(osなど標準ライブラリ集、Numpyなどのサードパーティーでグループ化して、最後にモジュールを持ってくる)
import os
import shutil
import sys

imprt numpy as np
import pandas as pd

from apps.your_app import your_module

手動で扱うのが手間な場合は、Jupyterであればisort formatterなどの拡張機能、.pyファイルであればisortライブラリなどを利用すると楽ができます。
基本的に（webなどのプロジェクトであれば）誤読を避けたりリネーム・パス移動などで影響を少なくするため、絶対パスを指定してimportします。
ワイルドカードを使ったimportは避けます。（from os import * といったような）
何が読み込まれいるのかが分かりづらいのと、複数のモジュール間で同じ名称のものがあった場合に片方が上書きされてしまい、事故の元になるためです。
余分なスペースは入れない
spam ( ham[ 1 ])
〇a = 1
=の位置を合わせるために余分なスペースを入れないようにする
x     = 1
sasas = 2
def a(a, img=0.0(=前後にスペース入れない))

命名規則
関数名や変数名 小文字のみで、単語間をアンダースコアで区切ります(スネークケース）
クラス名は先頭のみ大文字(パスカルケース）
定数名(すべて大文字、単語間を_で区切ります
モジュール名はすべて小文字で、単語間に_を入れる
パッケージ名(フォルダ名）_使ってはいけない
よやくごとへんすうめいかぶるときは、一番後ろに_つける
if is_null(True書かない)
例外はキャメルケース
import pandas
(目的違うので、１行開ける)
int num

void set(){}
(目的違うので１行開ける)
void draw(){}