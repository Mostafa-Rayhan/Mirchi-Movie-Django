from django.shortcuts import render

from .models import Collections, TopPicks, BestFilms, BannerSlider, Trending, Recommended, NewReleases, OnDemand, Video

# Create your views here.

def index(request):
    # hero = Collections.objects.all()
    img_list = Collections.objects.all()
    pic = TopPicks.objects.all()
    film = BestFilms.objects.all()
    banner = BannerSlider.objects.all()
    trending = Trending.objects.all()
    recommend = Recommended.objects.all()
    new = NewReleases.objects.all()
    demand = OnDemand.objects.all()
    vdo = Video.objects.all()


    context = {
        'lists': img_list,
        'pics': pic,
        'films': film,
        'banners': banner,
        'trendings': trending,
        'recommends': recommend,
        'news': new,
        'demands': demand,
        'vdos': vdo
    }
    return render(request, 'index.html', context)
