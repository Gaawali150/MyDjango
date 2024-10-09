from django.shortcuts import render
from .form import ImageForm
from .models import Image

def home(request):
    # Initialize the form
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()  # Reset the form after saving
    img = Image.objects.all()
    

    return render(request, 'imageUpload/home.html', {'img':img, 'form': form})
