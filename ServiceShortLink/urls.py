
from django.contrib import admin
from django.urls import path, include
from shortlink.views import redirect_on_page


urlpatterns = [
    path('api/v1/links/', include('shortlink.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('<str:short_name_url>', redirect_on_page),
    path('admin/', admin.site.urls),


]
