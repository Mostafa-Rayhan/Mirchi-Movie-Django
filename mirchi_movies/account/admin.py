from django.contrib import admin
from .models import Collections, TopPicks, BestFilms, BannerSlider, Trending, Recommended, NewReleases, OnDemand, Video


# Register your models here.

admin.site.register(Collections)
admin.site.register(TopPicks)
admin.site.register(BestFilms)
admin.site.register(BannerSlider)
admin.site.register(Trending)
admin.site.register(Recommended)
admin.site.register(NewReleases)
admin.site.register(OnDemand)
admin.site.register(Video)

