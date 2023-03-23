from django.shortcuts import render, redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm



def detail(request, id):
    # blog = Blog.objects.get(id = id)
    article = get_object_or_404(Article, pk = id) # 수정
    return render(request, 'detail.html', { 'article': article })


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form =ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)

    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')



def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('articles:index', pk=article.pk)
    
    else:
        form = ArticleForm(instance = article)

        context = {'form': article}
        return render(request, 'articles/update.html', context)
