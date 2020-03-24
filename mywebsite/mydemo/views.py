from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from .models import Movie, Book, Technology, Blog

def movie(request):
    try:
        res = Movie.objects.all()
        r = {}
        r['querydata'] = []
        for i in res:
            query = {}
            query['id'] = i.id
            query['moviename'] = i.moviename
            query['moviescore'] = i.moviescore
            query['viewingtime'] = i.viewingtime
            query['remarks'] = i.remarks
            query['impressions'] = i.impressions
            r['querydata'].append(query)
    except Exception as e:
        print(e)
    return JsonResponse(r)

def book(request):
    try:
        res = Book.objects.all()
        r = {}
        r['querydata'] = []
        for i in res:
            query = {}
            query['id'] = i.id
            query['bookname'] = i.bookname
            query['bookscore'] = i.bookscore
            query['booktimestart'] = i.booktimestart
            query['booktimeend'] = i.booktimeend
            query['remarks'] = i.remarks
            query['impressions'] = i.impressions
            r['querydata'].append(query)
    except Exception as e:
        print(e)
    return JsonResponse(r)

def technology(request):
    try:
        res = Technology.objects.all()
        r = {}
        r['querydata'] = []
        for i in res:
            query = {}
            query['id'] = i.id
            query['technologyname'] = i.technologyname
            query['technologyscore'] = i.technologyscore
            r['querydata'].append(query)
    except Exception as e:
        print(e)
    return JsonResponse(r)

def blog(request):
    try:
        res = Blog.objects.all()
        r = {}
        r['querydata'] = []
        for i in res:
            query = {}
            query['id'] = i.id
            query['blogtype'] = i.blogtype
            query['blogtime'] = i.blogtime
            query['remarks'] = i.remarks
            query['impressions'] = i.impressions
            r['querydata'].append(query)
    except Exception as e:
        print(e)
    return JsonResponse(r)
