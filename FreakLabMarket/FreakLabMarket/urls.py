"""
URL configuration for FreakLabMarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf.urls.static import static
from FreakLabMarket import settings

# from django.views.static import serve
# from django.urls import re_path

urlpatterns = [
    path('f78c4914f23acccb045f826c919609d443e81e21becae9cb44fad1b6aafbb8c4/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='goods')),
    path('user/', include('users.urls', namespace='users')),
]

# urlpatterns += [
#     re_path(
#         r"^media/(?P<path>.*)$",
#         serve,
#         {"document_root": settings.MEDIA_ROOT},
#     ),
# ]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)