"""funai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from image_app.views import generate_image, generate_graph
from django.views import static
from django.conf import settings

urlpatterns = [
    path('graphai/admin/', admin.site.urls),
    path('graphai/', generate_graph),
    path('graphai/generate_image/', generate_image, name='generate_image'),
    path('graphai/generate_graph/', generate_graph, name='generate_graph'),
    re_path(r'^graphai/static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')

]
