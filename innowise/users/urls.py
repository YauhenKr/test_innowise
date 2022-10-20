from django.urls import path

from users.views import UserBookingsHistoryAPIView


urlpatterns = [
    path('', UserBookingsHistoryAPIView.as_view(), name='list-of-users')
]