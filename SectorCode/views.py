from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, SectorCodeSerializer
from . import services
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SectorCodeAPI(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = SectorCodeSerializer
    def list(self, request):
        data = services.get_books()
        return Response(data)

    def post(self, request):
        data = services.get_books(request.data['name'])
        return Response(data)
