from django.shortcuts               import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib                 import messages
from .forms                         import ArticleForm
from .models                        import Article, Comment

# Create your views here.


def articles(request):

    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        context = {
            "articles" : articles
                  }
        return render(request, "articles.html", context)

    articles = Article.objects.all()
    context = {
        "articles":articles
              }
    return render(request, "articles.html", context)


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles" : articles
              }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla oluşturuldu...")
        return redirect("index")

    context = {
        "form" : form
              }
    return render(request, "addarticle.html", context)


def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)

    comments  = article.comments.all()

    context = {
        "article"  : article,
        "comments" : comments
              }
    return render(request, "detail.html", context)


@login_required(login_url="user:login")
def editarticle(request, id):

    article = get_object_or_404(Article, id = id)
    form    = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi...")
        return redirect("index")

    context = {
        "form" : form
              }
    return render(request, "edit.html", context)


@login_required(login_url="user:login")
def deletearticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Makale başarıyla silindi...")
    return redirect("article:dashboard")


def addcomment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author  = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        new_comment         = Comment(comment_author=comment_author, comment_content=comment_content)
        new_comment.article = article
        new_comment.save()

    return redirect(reverse("article:detail", kwargs={"id":id}))

