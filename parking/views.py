from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import uuid
import pygame
import pygame.camera

# Create your views here.
def see(request):
    photo_path = make_photo()
    context = {
        "photo": photo_path
    }
    return render(request, "parking/see.html", context)

def make_photo():
    filename = f"{str(uuid.uuid4())}.jpg"
    pygame.camera.init()
    pygame.camera.list_cameras() #Camera detected or not
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,f"parking/static/parking/{filename}")
    cam.stop()
    return filename