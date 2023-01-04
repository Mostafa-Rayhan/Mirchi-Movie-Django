from django.db import models

# Create your models here.

# class HeroSection(models.Model):
#     name = models.CharField(max_length=300)
#     image = models.ImageField(upload_to='media/hero')
#
#     def __str__(self):
#         return self.name

class Collections(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/collections')

    def __str__(self):
        return self.name


class TopPicks(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/topPicks')

    def __str__(self):
        return self.name

class BestFilms(models.Model):
    film_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/bestFilm')
    film_type = models.CharField(max_length=300)
    views = models.IntegerField(max_length=20)
    comments = models.IntegerField(max_length=20)

    def __str__(self):
        return self.film_name

class BannerSlider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/banner')

    def __str__(self):
        return self.name

class Trending(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/trending')

    def __str__(self):
        return self.name

class Recommended(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/recommended')

    def __str__(self):
        return self.name

class NewReleases(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/newReleases')

    def __str__(self):
        return self.name

class OnDemand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/onDemand')

    def __str__(self):
        return self.name
