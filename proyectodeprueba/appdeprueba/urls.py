from django.urls import path
# from . import views
from .views import HomeView, PostDetailed

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailed.as_view(), name = 'post-details'),
]
