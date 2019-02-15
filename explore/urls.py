from django.urls import path, re_path
from explore import views


app_name= 'explore'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    # path('explore/', views.post_list, name='explore'),
    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),

    ]
