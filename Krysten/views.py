from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Krysten.models import Person, Texts, Music
def about_me(request):
    krysten = Person.objects.all()[0]
    print(krysten.description)
    print(krysten.image_url.url)
    return render(request, 'home.html', {"krysten": krysten, "image_url": krysten.image_url.url})

@login_required
def upload(request):
    krysten = Person.objects.all()[0]

    return render(request, 'upload.html', {"krysten": krysten})

@login_required
def update_description(request):
    if request.method == "POST":
        print(request.POST.get("description", None))
        print(type(request.POST.get("new_image", None)))
        print(request.FILES)

        return render(request, 'home.html', {})
    krysten = Person.objects.all()[0]
    krysten.description = request.POST.get("description", None)

def display_writing(request):
    writings = Texts.objects.all()
    return render(request, "writings.html", {"writings": writings})

def display_music(request):
    music = Music.objects.all()
    return render(request, "music.html", {"songs": music})
# Create your views here.
