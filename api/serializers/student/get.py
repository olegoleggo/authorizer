from rest_framework import serializers
from Core.models import Student


class StudentIdSerializers(serializers.Serializer):
    univercity = serializers.CharField()
    id = serializers.IntegerField()
    userName = serializers.DictField(child=serializers.CharField())
    studyGroup = serializers.DictField(child=serializers.CharField())
    birthDay = serializers.DateField()
    validUntil = serializers.DateField()
    photo = serializers.ImageField()
    qr = serializers.ImageField()
