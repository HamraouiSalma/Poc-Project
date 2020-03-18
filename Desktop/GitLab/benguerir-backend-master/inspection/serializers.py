from rest_framework import serializers
from inspection.models import Inspection, Comment, STATUS


class InspectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    inspection_tag = serializers.CharField(max_length=255)  # style={'base_template': 'textarea.html'}
    content = serializers.CharField()
    status = serializers.ChoiceField(choices=STATUS, default=0)

    def create(self, validated_data):
        """
        Create and return a new `Inspection` instance, given the validated data.
        """
        return Inspection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Inspection` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.inspection_tag = validated_data.get('inspection_tag', instance.code)
        instance.content = validated_data.get('content', instance.language)
        instance.status = validated_data.get('status', instance.style)
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    body = serializers.CharField(max_length=255)  # style={'base_template': 'textarea.html'}
    content = serializers.CharField()
    status = serializers.ChoiceField(choices=STATUS, default=0)

    def create(self, validated_data):
        """
        Create and return a new `Inspection` instance, given the validated data.
        """
        return Inspection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Inspection` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.inspection_tag = validated_data.get('inspection_tag', instance.code)
        instance.content = validated_data.get('content', instance.language)
        instance.status = validated_data.get('status', instance.style)
        instance.save()
        return instance

