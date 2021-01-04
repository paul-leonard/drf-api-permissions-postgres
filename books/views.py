from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer
from .permissions import isAuthorOrReadOnly

class BookList(ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookDetail(RetrieveUpdateDestroyAPIView):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Book.objects.all()
  serializer_class = BookSerializer
