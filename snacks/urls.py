from django.urls import path
from .views import SnackListView, SnackDeatilView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
  path('', SnackListView.as_view(), name="snack_list")
  path('<int:pk>/', SnackDeatilView.as_view(), name="snack_detail")
  path('')
]