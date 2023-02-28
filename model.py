import cv2
import numpy as np
import tensorflow as tf


def prepare_model(path='./Xception.h5'):
    model = tf.keras.models.load_model(path)
    return model


def preprocess(image):
    res = []
    for img in image:
        img = cv2.resize(img, (32, 32))
        img = np.array(img, dtype=np.float)
        img /= 255,
        res.append(img)
    return np.array(res).reshape(2, 32, 32, 3)


def pipeline_predict(model, images):
    images = preprocess(images)
    res = model.predict_on_batch(images)
    res = np.argmax(res, axis=1)
    if sum(res) == 0:
        return 0
    return 1


if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    # model = prepare_model("C:\Python39\pythonProject2\Xception.h5")
    # while True:
    #     start = time.time()
    #     _, img = camera.read()
    #     images = [img, img]
    #     res = pipeline_predict(model, images)
    #     print(res)
