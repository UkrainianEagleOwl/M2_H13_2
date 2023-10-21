

from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main,name="root"),
    path('<int:page>', views.main,name="root_paginate"),
    path('author/<int:author_id>', views.author_detail, name='author'),
    path('new_author/', views.new_author, name='new_author'),
    path('new_quote/', views.new_quote, name='new_quote'),
]