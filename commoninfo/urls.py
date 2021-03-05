from django.urls import path
from . import views

urlpatterns =[
    path('commoninfo/add', views.addUserInfo),
    path('commoninfo/fetch', views.fetchUserInfo),
    path('commoninfo', views.commoninfo)
]
