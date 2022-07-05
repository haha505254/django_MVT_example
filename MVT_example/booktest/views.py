from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo
# Create your views here.
def index(request):
    return render(request,'booktest/index.html')

def show_books(request):
    #通過Model查詢圖書數據
    books = BookInfo.objects.all()
    return render(request,'booktest/show_books.html',locals())

def detail(request,bid):
    
    books = BookInfo.objects.get(id=bid)
    heros = books.heroinfo_set.all()
    return render(request,'booktest/detail.html',locals())
