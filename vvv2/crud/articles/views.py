from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    # articles =  Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')


def detail(request,pk):
    article=Article.objects.get(pk=pk)
    context = {
        'article':article
    }

    return render(request,'articles/detail.html',context)


def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.title=title
        article.content=content
        article.save()

        return redirect('articles:detail' ,pk=article.pk)
        # context = {
        #     'title': title,
        #     'content': content        
        # }
        # return render(request, 'articles/create.html', context)

    else:
        return render(request,'articles/create.html')


def update(request,pk):
    article=Article.objects.get(pk=pk)
    if request.method =='POST':        
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')

        article.save()
        return redirect('articles:detail',pk=article.pk )
    else:

        context= {
            'article':article
        }
        return render(request,'articles/update.html',context)




def delete(request,pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
    


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request.GET.get('msg1'))
    msg1 = request.GET.get('msg1')
    msg2 = request.GET.get('msg2')
    context = {
        'msg1': msg1,
        'msg2': msg2,
    }
    return render(request, 'articles/catch.html', context)