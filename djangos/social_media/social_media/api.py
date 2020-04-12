from groups.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from social_media.serializer import UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = UserSerializer