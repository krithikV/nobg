import os
import urllib.request
from django.conf import settings
from django.shortcuts import render
from rembg import remove
from PIL import Image
import base64
from io import BytesIO

def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
        my_string = base64.b64encode(image_file.read())
        """
        with open(image_path, 'wb') as file:
            file.write(image_file.read())
        """
        input = Image.open(BytesIO(base64.b64decode(my_string)))
        buffered = BytesIO()
        output = remove(input)
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        return render(request, 'remover/result_image.html', {'img_org_url': my_string.decode(),'image_url': img_str.decode()})

    return render(request, 'remover/upload_image.html')

def result_image(request):
    return render(request, 'remover/result_image.html')
