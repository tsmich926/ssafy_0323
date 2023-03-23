from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:pk>/', views.detail,name='detail'),
    # path('create/', view.create, name='create'),
    # get 방식으로 빈 페이지를 사용자에게 보여주는 주소
    # path('new/', views.new, name='new'),   
    # new 를 받아서 데이타를 입력한 후 server에게 전달하는 주소
    path('create/', views.create, name='create'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]