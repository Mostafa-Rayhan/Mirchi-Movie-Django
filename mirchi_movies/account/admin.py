from django.contrib import admin
from .models import Collections, TopPicks, BestFilms, BannerSlider


# Register your models here.

admin.site.register(Collections)
admin.site.register(TopPicks)
admin.site.register(BestFilms)
admin.site.register(BannerSlider)

