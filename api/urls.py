from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, 'products')

urlpatterns = [
	path('', include(router.urls)),
]