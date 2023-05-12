from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import status
from .serialize import *
from .models import Links


@api_view(['POST'])
def create_short_link(request):
    """Создание ссылки"""
    serializer = SerializeCreateLink(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
def get_post_links(request):
    """Получение всех ссылок"""
    try:
        links = Links.objects.all()
        serializer = SerializeListLink(links, many=True)
        return Response(data=serializer.data)
    except Links.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"DB entry does not exist"})


@api_view(['GET'])
def get_detail_link(request):
    """Получение данных по исходной ссылке"""
    try:
        link = Links.objects.get(source_link=request.data['source_link'])
        serializer = SerializeListLink(link, many=False)
        return Response(serializer.data)
    except Links.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"DB entry does not exist"})


@api_view(['DELETE'])
def delete_link(request, pk=None):
    """Удаление записи"""
    if pk is None:
        pk = int(request.data['id'])
    else:
        raise Exception("Не указан id записи")
    link = Links.objects.get(pk=pk)
    link.delete()
    return Response(status=status.HTTP_200_OK)


def redirect_on_page(request, short_name_url):
    """Переход по ключу"""
    link = Links.objects.get(update_link=short_name_url)
    return redirect(link.source_link)
