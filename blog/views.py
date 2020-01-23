from django.shortcuts import render, HttpResponse
from article.models import Article
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        "number1":10,
        "number2":5
    }
    return render(request,"index.html",context)
    
def about(request):
    return render(request,"about.html")

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()
    context = {
        "articles":articles
        }
    return render(request, "articles.html",context=context)