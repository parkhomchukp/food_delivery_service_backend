from django.urls import path

from .views import UserProfileListCreateView, UserProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('all-profiles/', UserProfileListCreateView.as_view(), name='all_profiles'),
    path('profile/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='profile')
]
