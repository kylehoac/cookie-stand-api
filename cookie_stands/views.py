from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie
from .permissions import IsPurchaserOrReadOnly
from .serializers import CookieSerializer


class CookieList(ListCreateAPIView):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer


class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPurchaserOrReadOnly,)
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer
