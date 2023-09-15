from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"), 
    path('menu/', views.MenuItemsView.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(),name='menu-detail'),
    path('book/', views.Book.as_view(), name='book'),
    path('bookings/', views.bookings, name='bookings'),
    path('api-token-auth/', obtain_auth_token),
]
