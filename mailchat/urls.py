from django.urls import path
from . import views as mviews

urlpatterns = [
    path('', mviews.index, name='mail'),
    path('verify', mviews.verify),
    path('verify/', mviews.verify)
]
