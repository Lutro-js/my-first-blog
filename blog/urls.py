from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'), #サイトにアクセスしたら「views.post_list」が正しい行き先だということをDjangoに伝える。「name='post_list'」はビューを識別するために使われるURLの名前
]