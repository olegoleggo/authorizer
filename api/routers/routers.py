from django.urls import path, include


urlpatterns = [
    path('student/', include('api.routers.student'))
]