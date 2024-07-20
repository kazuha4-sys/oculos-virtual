import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

def preprocess_image(img):
    img = cv2.resize(img, (64, 64))  # Redimensionar para o tamanho esperado pelo modelo
    img = cv2.GaussianBlur(img, (5, 5), 0)  # Aplicar desfoque para suavizar a imagem
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)  # Binarizar a imagem
    img = img.astype(np.float32) / 255.0  # Normalizar a imagem
    return img

def load_images(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        label_path = os.path.join(data_dir, label)
        if os.path.isdir(label_path):
            for file in os.listdir(label_path):
                if file.endswith('.png'):
                    img_path = os.path.join(label_path, file)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        img = preprocess_image(img)
                        images.append(img)
                        labels.append(label)
                    else:
                        print(f"Warning: Failed to load image {img_path}")
    if not images:
        raise ValueError("No images found in the symbols directory.")
    return np.array(images), np.array(labels)

def predict_symbol(model, img):
    img = preprocess_image(img)
    img = img.reshape(1, -1)
    return model.predict(img)[0]

def initialize_camera():
    cap = cv2.VideoCapture(0)  # 0 é o índice para a câmera padrão
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return cap

def capture_image(cap):
    ret, frame = cap.read()
    if not ret:
        raise IOError("Failed to capture image")
    return frame

def load_model(model_path):
    return joblib.load(model_path)

def detect_symbols(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filtrar contornos pequenos
    min_contour_area = 500  # Ajuste conforme necessário
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
    
    return gray, contours

data_dir = 'symbols'
if not os.path.exists(data_dir):
    raise FileNotFoundError(f"The directory {data_dir} does not exist. Please create it and add your symbol images.")

images, labels = load_images(data_dir)
if len(images) == 0 or len(labels) == 0:
    raise ValueError("No images or labels found. Please check the symbols directory.")

n_samples = len(images)
data = images.reshape((n_samples, -1))

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)
joblib.dump(model, 'model.pkl')

cap = initialize_camera()
model = load_model('model.pkl')

while True:
    frame = capture_image(cap)
    gray, contours = detect_symbols(frame)

    translated_text = ''
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        symbol_image = gray[y:y+h, x:x+w]
        letter = predict_symbol(model, symbol_image)
        translated_text += letter

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, letter, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Symbol Translator', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

