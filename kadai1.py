# task1. 変数の使い方

name1: str = "シンジ"
name2: str = "カヲルくん"

print(name1 + "と" + name2 + "は仲良し！")


# task2. if文の使い方

name1: str = "シンジ"
name2: str = "使徒"

if name2 == "使徒":
    print(name2 + "です！")
else:
    print(name1 + "と" + name2 + "は仲良し！")


# task3. 配列の使い方

names: list = ["シンジ", "レイ", "カヲルくん"]

names.append("アスカ")


# task4. for文の使い方

for name in names:
    print(name)


# task5. 関数の使い方

def show_names() -> None:

    names: list = ["シンジ", "レイ", "カヲルくん"]
    names.append("アスカ")

    for name in names:
        print(name)

show_names()


# task6. 引数を使う関数の使い方

def show_names_arg(name :str) -> None:

    names: list = ["シンジ", "レイ", "カヲルくん", "アスカ"]
    names.append(name)

    for name in names:
        print(name)

show_names_arg("マリ")


# task7. 文字検索

name = input("名前を入力してください：")

if name in ["シンジ", "レイ", "カヲルくん", "アスカ"]:
    print(name + "はいます。")
else:
    print(name + "はいません。")
