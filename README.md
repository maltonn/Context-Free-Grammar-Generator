# 文脈自由文法ジェネレータ
## grammer.txtの書き方
例：
```
S -> aXa
X -> bXb
X -> _
```
左辺：変数（＝非終端記号）1文字
右辺：変数と終端記号からなる文字列

### 変数と非終端記号の区別
本プログラムでは左辺に出てくる記号を変数 / そうでない記号を非終端記号と定義

### ε規則
_をεとして扱う
すなわち
X -> ε は　X -> _

