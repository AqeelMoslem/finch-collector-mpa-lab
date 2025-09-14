from django.urls import path
from . import views # Import views to connect routes to view functions


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('horses/', views.horse_index, name='horse-index'),
    path('horses/<int:horse_id>/', views.horse_detail, name='horse-detail'),
    path('horses/create/', views.HorseCreate.as_view(), name='horse-create'),
    path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horse-update'),
    path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horse-delete'),
    path('horses/<int:horse_id>/add_feeding/', views.add_feeding, name='add-feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    path('horses/<int:horse_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    path('horses/<int:horse_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),
    path('accounts/signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),


   
]