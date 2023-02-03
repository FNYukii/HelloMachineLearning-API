import hug
from tensorflow import keras
import joblib
import numpy as np
import cv2

# 対応表をロード
flowers = joblib.load("flowers.pkl")

# 画像の読み込みと変換
def process_image(file):
	img = np.asarray(bytearray(file), dtype=np.uint8)
	img2 = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	img3 = cv2.resize(img2, dsize=(224, 224))
	img3 = img3[np.newaxis, ...]
	img3 = img3/255.0
	return img3

@hug.get("/")
def api_root(cors: hug.directives.cors="*"):
	return "Development of Web API!"

@hug.post("/image-classifier")
def api_image_classifier(file, cors: hug.directives.cors="*"):

    # モデルを作成
    model = keras.models.load_model("ImageClassifierModel.h5")

    # 画像を変換して読み込み
    image = process_image(file)

    # モデルで予測を実行
    result = model.predict(image)

    # 結果を文字列にして返す
    return flowers[result[0].argmax()]
