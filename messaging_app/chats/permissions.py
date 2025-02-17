from rest_framework.permissions import BasePermission
from .models import Conversation  # Import the Conversation model

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of a conversation
    to send, view, update, and delete messages.
    """
    message = "You are not a participant in this conversation."

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant of the conversation
        return request.user in obj.conversation.participants.all()
