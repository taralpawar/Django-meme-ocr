from django.shortcuts import render, redirect
from .models import OcrImage
# Create your views here.
import cv2
import easyocr
import numpy as np
reader = easyocr.Reader(['en'], gpu=True)


def recognise(request):
    if request.method == 'POST' and request.FILES:
        image = (request.FILES['image'])

        text = []
        ocrimg = OcrImage()
        ocrimg.upimage = image
        output = reader.readtext(image.read())
        for i in range(len(output)):
            text.append(output[i][1])
        cord = output[i][0]
        x_min, y_min = [min(idx) for idx in zip(*cord)]
        x_max, y_max = [max(idx) for idx in zip(*cord)]

        ocrimg.save()
        return render(request, 'memeocr/index.html', {'text': text, 'image': image})
    return render(request, 'memeocr/index.html')
