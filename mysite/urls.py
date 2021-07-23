"""mysite URL Configuration

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
from django import contrib
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.decorators import login_required
# from mysite.matching import views
from django.views.generic import TemplateView

# ページを表示させるだけであれば以下の記述のみでOK。
index_view = TemplateView.as_view(template_name = 'registration/index.html')

urlpatterns = [
    # path('admin', admin.site.urls),
    # プロジェクトとアプリの階層を間違いえないようにする。
    path('', login_required(index_view), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('', include('matching.urls')),

    # login_required関数でURL先をログイン必須にすることができる。
    # path('', login_required(include('matching.urls'))),
]
