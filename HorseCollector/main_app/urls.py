from django.urls import path
from . import views # Import views to connect routes to view functions


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('horses/', views.horse_index, name='horse-index'),
    path('horses/<int:horse_id>/', views.horse_detail, name='horse-detail'),
        # new route used to create a cat
   
    path('horses/create/', views.HorseCreate.as_view(), name='horse-create'),
    path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horse-update'),
    path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horse-delete'),
    # path('horses/<int:horse_id>/add_feeding/', views.add_feeding, name='add-feeding'),
    # path('horses/<int:horse_id>/add_photo/', views.add_photo, name='add-photo'),
    # path('horses/<int:horse_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc-accessory'),
    # path('accessories/', views.AccessoryList.as_view(), name='accessory-list'), # New route for listing accessories
    # path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory-detail'), # New route for accessory detail 
]