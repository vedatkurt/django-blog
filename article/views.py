from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "article/index.html")

def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Article saved successfully!")
        return redirect("article:dashboard")

    return render(request, "article/add.html", {"form":form})

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Article updated successfully!")
        return redirect("index")

    return render(request, "article/update.html",{"form":form})

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)

    article.delete()

    messages.success(request,"Article deleted successfully!")
    
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
        }

    return redirect("article:dashboard")
    return render(request, "dashboard.html", context=context)

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
        }
    return render(request, "article/dashboard.html",context=context)

@login_required(login_url = "user:login")
def detail(request,id):
    article = get_object_or_404(Article,id=id)

    comments = article.comments.all()

    context = {
        "article":article,
        "comments":comments,
        }
    return render(request, "article/detail.html",context=context)

@login_required(login_url = "user:login")
def addComment(request,id):
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content = comment_content)
        newComment.article = article

        newComment.save()
    
    return redirect("/article/detail/" + str(id))