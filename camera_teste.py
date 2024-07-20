import cv2

# Teste simples para verificar a função imread
def test_cv2_imread():
    img_path = 'WhatsApp Image 2024-07-19 at 19.19.36 (1).jpeg'  # Substitua pelo caminho para uma imagem válida
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Failed to load image.")
    else:
        print("Image loaded successfully.")
        print(f"Image shape: {img.shape}")

test_cv2_imread()
