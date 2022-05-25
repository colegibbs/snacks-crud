from django.urls import path
from .views import SnackListView, SnackDeatilView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
  path('', SnackListView.as_view(), name="snack_list")
  
]