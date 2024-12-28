from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, MessageViewSet, ConversationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]