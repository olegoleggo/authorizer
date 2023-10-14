from django.urls import path
from api.views.student import StudentInfo

urlpatterns = [
    path('get/', StudentInfo.as_view())
]

