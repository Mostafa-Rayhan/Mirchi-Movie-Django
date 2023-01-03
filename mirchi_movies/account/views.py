from django.shortcuts import render

from .models import Collections, TopPicks, BestFilms, BannerSlider

# Create your views here.

def index(request):
    # hero = Collections.objects.all()
    img_list = Collections.objects.all()
    pic = TopPicks.objects.all()
    film = BestFilms.objects.all()
    banner = BannerSlider.objects.all()

    context = {
        'lists': img_list,
        'pics': pic,
        'films': film,
        'banners': banner
    }
    return render(request, 'index.html', context)
