from django.urls import path

from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
]