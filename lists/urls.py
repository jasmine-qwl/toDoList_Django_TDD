"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from lists import views
from django.conf.urls import url

urlpatterns = [
    url(r'^new$', views.new_list, name ='new_list'),
    url(r'^(\d+)/$', views.view_list, name = 'view_list'),
    url(r"^users/(.+)/$", views.my_lists, name = "my_lists"),
    url(r'^(\d+)/share$', views.share_list, name = 'share_list'),
    url(r'^(\d+)/delete$', views.delete_list, name = 'delete_list')
]
