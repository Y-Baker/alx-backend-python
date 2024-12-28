from models import User, Conversation, Message
from rest_framework import serializers
from django.utils.timezone import now

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    member_since = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'user_id', 'full_name', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'member_since', 'created_at']
        read_only_fields = ['user_id', 'member_since', 'created_at']

    def get_member_since(self, obj):
        return (now() - obj.created_at).days
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"



class conversationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="conversation-detail")
    participants = UserSerializer(many=True)
    created_since = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['url', 'conversation_id', 'title', 'participants', 'created_since', 'created_at']
        read_only_fields = ['conversation_id', 'created_since', 'created_at']
    
    def get_created_since(self, obj):
        return (now() - obj.created_at).days


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="message-detail")
    sender = UserSerializer()
    conversation = conversationSerializer()
    sent_since = serializers.SerializerMethodField()
    read_since = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['url', 'message_id', 'message_body', 'sender', 'sent_at', 'read_at', 'conversation', 'sent_since', 'read_since']
        read_only_fields = ['message_id', 'sent_at', 'read_at', 'sent_since', 'read_since']

    def get_sent_since(self, obj):
        return (now() - obj.sent_at).seconds
    
    def get_read_since(self, obj):
        if obj.read_at:
            return (obj.read_at - obj.sent_at).seconds
        return None