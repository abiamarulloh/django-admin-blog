from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryList, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('', include(router.urls)),
]