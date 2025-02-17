from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, MessageViewSet, ConversationViewSet
from .user_message_views import UserMessageView
# from drf_nested_routers import NestedDefaultRouter # type: ignore


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'conversations', ConversationViewSet)
# router.register(r'messages', MessageViewSet)

# conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
# conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# conversation_router.register(r'participants', UserViewSet, basename='conversation-participants')


urlpatterns = [
    # path('', include(router.urls)),
    # path('', include(conversation_router.urls)),
    path('user/messages/', UserMessageView.as_view()),
]
