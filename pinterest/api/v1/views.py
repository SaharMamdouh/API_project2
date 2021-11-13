from rest_framework.decorators import api_view
from rest_framework.response import Response
from pinterest.models import Movie
from rest_framework import status
from .serializers import MainSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser , BasePermission


#creating a custom permission
class UserCanDeleteMovie(BasePermission):

    def has_permission(self,request,view):
        if request.user.groups.filter(name="can_delete").exists(): #lw el user da 3ndo group esmo can delete yb2a lih delete permission
            return True
        return False


@api_view(['GET'])
def list_movie(request):
    movies=Movie.objects.all()
    Serialzed_data = MainSerializer(instance=movies,many=True)
    return Response(data=Serialzed_data.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_movie(request):
    if request.method == 'POST':
        serializer = MainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"]) # tells django that this is a type of rest view
@permission_classes([UserCanDeleteMovie])
def delete_movie(request, id):

    movie = Movie.objects.get(id = id)

    movie.delete()

    movies = Movie.objects.all()

    serializer = MainSerializer(instance=movies, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT','PATCH'])
def update_movie(request, id):
    movie=Movie.objects.get(id = id)
    if request.method == 'PUT':
        serializer = MainSerializer(instance=movie, data=request.data)
    elif request.method == 'PATCH':
        serializer = MainSerializer(instance=movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
