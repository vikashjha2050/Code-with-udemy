from groups.models import Group
from rest_framework import viewsets, views, status, generics
from rest_framework.response import Response
from social_media.serializer import GroupSerializer
from django.http import Http404


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class GroupViews(views.APIView):

	def get_object(self, pk):
		try:
			group = Group.objects.get(pk=pk)
		except Group.DoesNotExist:
			raise Http404
		return group

	def get(self, request, pk, format=None):
		print(request.query_params, '******get data********')
		group = self.get_object(pk)
		serializer = GroupSerializer(group)
		return Response(serializer.data)

	def post(self, request, pk, format=None):
		serializer = GroupSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		print(serializer.errors, 'errors*****************')
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		group = self.get_object(pk)
		group.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, pk):
		group = self.get_object(pk)
		serializer = GroupSerializer(group, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		print(serializer.errors, 'errors*****************')
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupGenericApi(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
		