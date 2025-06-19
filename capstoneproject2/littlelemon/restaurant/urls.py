#define URL route for index() view
from django.urls import path, include
from . import views
from .views import  bookingview
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
 

    path('booking/', bookingview.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemView.as_view(), name='menu-items-list-create'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-items-detail'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
  
]
