from django.urls import path # type: ignore
from .import views

urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.index, name='index'),
]