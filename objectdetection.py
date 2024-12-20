# -*- coding: utf-8 -*-
"""ObjectDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1An4EsBURprFpq_3-JWm7_C7HAnM1O1rU

# Yoloを試してみる
"""

# ultralyticsパッケージをPyPIからインストールする
!pip install ultralytics

# ultralyticsライブラリからYOLOクラスをインポートする
from ultralytics import YOLO

# 事前に学習されたYOLOモデルを読み込む（トレーニングに推奨）
model = YOLO("yolov8n.pt")

# coco8.yaml'データセットを使用してモデルを10エポックでトレーニングする
results = model.train(data="coco8.yaml", epochs=10)

# モデルの評価を実行し、結果を取得する
results=model.val()

# 物体検出したい画像を追加
from google.colab import files
uploaded = files.upload()

# 画像'./IMG_5089.JPEG'をモデルに入力して結果を取得する
results = model("./IMG_5089.JPEG")

# PILライブラリからImageクラスをインポートする
from PIL import Image

# 結果を画像で保存する
for i, r in enumerate(results):
    # Plot results image
    im_bgr = r.plot()  # BGR-order numpy array
    im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

    # Show results to screen (in supported environments)
    r.show()

    # Save results to disk
    r.save(filename=f"results{i}.jpg")

"""# オリジナルデータを学習させてみる"""

# ultralyticsパッケージをPyPIからインストールする
!pip install ultralytics

# ultralyticsライブラリからYOLOクラスをインポートする
from ultralytics import YOLO

# 事前に学習されたYOLOモデルを読み込む（トレーニングに推奨）
model = YOLO("yolov8n.pt")

# データセットをアップロード(zip形式)
from google.colab import files
uploaded = files.upload()

# データセットを解凍
!unzip datasets.zip

# zip形式のデータセットを削除
!rm datasets.zip

# yamlファイルをアップロード
from google.colab import files
uploaded = files.upload()

# coco8.yaml'データセットを使用してモデルを10エポックでトレーニングする
results = model.train(data="dataset.yaml", epochs=100)

# モデルの評価を実行し、結果を取得する
results=model.val()

# 物体検出したい画像を追加
from google.colab import files
uploaded = files.upload()

# 画像'./IMG_5089.JPEG'をモデルに入力して結果を取得する
results = model("./IMG_5084.jpg")

# PILライブラリからImageクラスをインポートする
from PIL import Image

# 結果を画像で保存する
for i, r in enumerate(results):
    # Plot results image
    im_bgr = r.plot()  # BGR-order numpy array
    im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

    # Show results to screen (in supported environments)
    r.show()

    # Save results to disk
    r.save(filename=f"results{i}.jpg")

pip install notebook

from notebook.auth import passwd
print(passwd())