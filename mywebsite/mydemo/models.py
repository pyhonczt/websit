from django.db import models

class Movie(models.Model):
    moviename = models.CharField(max_length=24, verbose_name='电影名称')
    moviescore = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='评分')
    viewingtime = models.DateField(verbose_name='观影日期')
    remarks = models.CharField(max_length=24, verbose_name='评语')
    impressions = models.TextField(verbose_name='观后感')

class Book(models.Model):
    bookname = models.CharField(max_length=24, verbose_name='书名')
    bookscore = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='理解多少')
    booktimestart = models.DateField(verbose_name='开始日期')
    booktimeend = models.DateField(verbose_name='结束日期')
    remarks = models.CharField(max_length=24, verbose_name='评语')
    impressions = models.TextField(verbose_name='观后感')

class Technology(models.Model):
    technologyname = models.CharField(max_length=24, verbose_name='技术名称')
    technologyscore = models.IntegerField(verbose_name='学习程度')

class Blog(models.Model):
    blogtype = models.CharField(max_length=24, verbose_name='技术领域')
    blogtime = models.DateField(verbose_name='日期')
    remarks = models.CharField(max_length=50, verbose_name='简介')
    impressions = models.TextField(verbose_name='详细文档')
