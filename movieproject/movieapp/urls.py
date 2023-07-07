
from django.urls import path
from . import views
app_name='movie_app'
urlpatterns = [

    path('', views.index,name='index'),
    path('movie/<int:movie_id>/', views.detail,name='detail'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('update_movie/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
]