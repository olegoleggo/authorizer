from django.db import models


class Links(models.Model):
    """Модель для хранения исходной ссылки и сокращённой ссылки"""
    source_link = models.CharField(max_length=528)
    update_link = models.CharField(max_length=100, unique=True)
