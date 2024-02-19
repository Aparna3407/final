from django.urls import path
from . import views
app_name='displayapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('add',views.add_movie,name='add_movie'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]


