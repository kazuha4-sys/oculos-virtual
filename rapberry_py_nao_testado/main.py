import cv2
import yaml
import pygame
from utils.camera import initialize_camera, capture_image
from utils.display import initialize_display, update_display
from utils.symbol_recognition.py import load_model, predict_symbol

with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

cam = initialize_camera(tuple(config['camera']['resolution']))
screen = initialize_display(config['display']['width'], config['display']['height'])

model = load_model(config['model']['path'])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame = capture_image(cam)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    translated_text = ''
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        symbol_image = gray[y:y+h, x:x+w]
        letter = predict_symbol(model, symbol_image)
        translated_text += letter
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, letter, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    update_display(screen, frame)

pygame.quit()
