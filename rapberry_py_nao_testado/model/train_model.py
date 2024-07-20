import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

def load_images(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, label)):
            for file in os.listdir(os.path.join(data_dir, label)):
                if file.endswith('.png'):
                    img_path = os.path.join(data_dir, label, file)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    img = cv2.resize(img, (64, 64))
                    images.append(img)
                    labels.append(label)
    return np.array(images), np.array(labels)

data_dir = '../symbols'
images, labels = load_images(data_dir)

n_samples = len(images)
data = images.reshape((n_samples, -1))

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
