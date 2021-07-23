from django.urls import include, path
from . import views
# Create your views here.
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', views.home.as_view()),
    path('home', login_required(views.home.as_view())),
    path('home/matching', login_required(views.matching.as_view())),
    path('home/message', login_required(views.message.as_view())),
    path('home/profile', login_required(views.profile.as_view())),
    # path('home/', views.home),
    # path('home', views.home.as_view()),
    # path('home/matching', views.matching.as_view()),
    # path('home/message', views.message.as_view()),
    # path('home/profile', views.profile.as_view()),
]
