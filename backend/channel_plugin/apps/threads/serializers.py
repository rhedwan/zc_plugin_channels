from rest_framework import serializers

from .models import Thread


class ThreadSerializer(serializers.Serializer):

    user_id = serializers.CharField(max_length=10, required=True)
    content = serializers.CharField()
    timestamp = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        instance = dict(instance)
        channelmessage_id = self.context.get("channelmessage_id")
        thread = Thread(**instance, channelmessage_id=channelmessage_id)
        data = {"thread": thread}
        return data


class ThreadUpdateSerializer(serializers.Serializer):

    user_id = serializers.CharField(read_only=True)
    channelmessage_id = serializers.CharField(read_only=True)
    content = serializers.CharField()
    emojis = serializers.ListField(serializers.CharField(), allow_empty=True)
    edited = serializers.BooleanField(default=False)
    timestamp = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        instance = dict(instance)
        thread = Thread(**instance)
        data = {"thread": thread}
        return data
