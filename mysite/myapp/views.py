import base64
from io import BytesIO
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate
from qrcode.image.pure import PyPNGImage
import qrcode
# Create your views here.
def home(request):
    if request.method == "POST":
        print("i am homepage")
        name = request.POST.get('name')
        print(name)
        
        image = qrcode.make(name,version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=4,
                     border=2,
                     image_factory=PyPNGImage
                     )
        stream = BytesIO()
        image.save(stream,kind="PNG")
        bytes_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(bytes_data).decode('utf-8')





        
        

        
        return render(request,'myapp/home.html',{"qr_image_base64":qr_image_base64,"name":name})
    if request.method == "GET":
        return render(request,'myapp/home.html')




