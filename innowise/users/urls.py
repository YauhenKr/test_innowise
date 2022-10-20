from django.urls import path

from .views import *

urlpatterns = [
    path('', UserWhereaboutsView.as_view(), name='list-of-users')
]