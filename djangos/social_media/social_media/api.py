from groups.models import Group
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from social_media.serializer import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class GroupViews(views.APIView):

	def get(self, request):
	   queryset = Group.objects.all()
	   serializer = GroupSerializer(queryset, many=True)
	   return Response(serializer.data)

	def post(self, request):
		serializer = GroupSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)