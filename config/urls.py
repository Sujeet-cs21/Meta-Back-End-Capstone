from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant.views import BookingViewSet,MenuItemsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', include('restaurant.urls')),
    path('admin/', admin.site.urls),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('api.urls')),
    path('api/', include(router.urls)),
    path('api/token/login/', TokenObtainPairView.as_view(), name='token-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
