from django.urls import path
from shortlink.views import *

urlpatterns = [
    path('create/', create_short_link),
    path('delete/', delete_link),
    path('get/', get_post_links),
]
