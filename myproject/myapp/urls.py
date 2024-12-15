from django.urls import path
from myapp import views

app_name="web"
urlpatterns = [
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('insert/',views.ins,name='insert'),
]
