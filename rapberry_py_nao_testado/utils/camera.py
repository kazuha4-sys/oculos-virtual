import pygame
import pygame.camera

def initialize_camera(resolution):
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], resolution)
    cam.start()
    return cam

def capture_image(cam):
    image = cam.get_image()
    return pygame.surfarray.array3d(image)
