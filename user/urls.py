from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path('<int:id>/', UserDetailView.as_view(), name='user-detail'),
]
