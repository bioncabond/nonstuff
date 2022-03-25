from rest_framework import generics
from .serializer import NonstuffSerializer
from .models import Nonstuff
# from .permissions import IsOwnerOrReadOnly

class NonstuffList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Nonstuff.objects.all()
    serializer_class = NonstuffSerializer

class NonstuffDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Nonstuff.objects.all()
    serializer_class = NonstuffSerializer