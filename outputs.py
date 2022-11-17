import sys
from PIL import Image
import pyocr
import pyocr.builders
import glob
import os
import re
import datetime 
# tesseract 
tools = pyocr.get_available_tools()
tool = tools[0]


def image_to_text(file_path):
    txt = tool.image_to_string(
        Image.open(file_path),  # OCRする画像
        lang="jpn",  # 学習済み言語データ
        builder=pyocr.builders.DigitBuilder(tesseract_layout=6),  # 期待される出力のタイプを指定 # DigitBuilder(tesseract_layout=6)
    )

    return txt


def main():
    file_paths = glob.glob("images/*")
    to_dir = "outputs"

    for file_path in file_paths:
        txt = image_to_text(file_path)

        # パスからファイル名のみ(拡張子なし)を取得
        filename = os.path.splitext(os.path.basename(file_path))[0]

        # 出力先のパスを生成
        to_path = os.path.join(to_dir, filename + ".txt")

        # 出力先を生成したパスに変更
        with open(to_path, mode="w") as f:
            f.writelines(txt)


def calorie():
    file_paths = glob.glob("outputs/*")
    nums = []

    for n in file_paths:
        with open(n, mode="r") as f:
            X = f.read()
            num = int(X)
            nums.append(num)
    Addition = sum(nums)
    now = datetime.datetime.now()
    today = now.strftime('%Y/%m/%d ')
    print(f"{today}の摂取カロリーは{Addition}kcalです。")


# image_to_text()

main()

calorie()

