from django.urls import path
from .views import (
  BookList,
  BookDetail,
)

urlpatterns = [
  path('api/v1/', BookList.as_view(), name='book_list_api'),
  path('api/v1/<int:pk>', BookDetail.as_view(), name='book_detail_api'),
]