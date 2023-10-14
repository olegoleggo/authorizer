from rest_framework import serializers
from .models import Links,Student
import validators


class SerializeListLink(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SerializeCreateLink(serializers.ModelSerializer):
    """Валидация для создания ссылки"""
    def create(self, validated_data):
        if not validators.url(validated_data["source_link"]):
            raise serializers.ValidationError("sourсe_link is not link")
        return Links.objects.create(**validated_data)

    class Meta:
        model = Links
        fields = ['source_link', 'update_link']
