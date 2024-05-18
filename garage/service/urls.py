# garage_service/garages/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingRequestViewSet

router = DefaultRouter()
router.register(r'booking-requests', BookingRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
