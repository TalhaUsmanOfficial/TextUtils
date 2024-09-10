"""
URL configuration for textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

# ! Code For Video 06-Ex-01 Personal Navigator.py
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.index, name="index"),
#     path("about/", views.about, name="about"),
# ]

# ! Code For Video 07-Laying Pipeline.py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("analyze/", views.analyze, name="analyze"),
    # path("capitalizefirst/", views.cap_first, name="cap_first"),
    # path("newlineremove/", views.new_line_remove, name="new_line_remove"),
    # path("spaceremover/", views.space_remover, name="space_remover"),
    # path("charcounter/", views.char_counter, name="char_counter"),
]
