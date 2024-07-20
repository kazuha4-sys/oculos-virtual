import cv2
import numpy as np
import joblib

def load_model(model_path):
    return joblib.load(model_path)

def predict_symbol(model, img):
    img = cv2.resize(img, (64, 64))
    img = img.reshape(1, -1)
    return model.predict(img)[0]
