from .serializers import UserProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET'])
#@authentication_classes([TokenAuthentication]) already defined in setting in default authentication type
def logout(request):
    request.user.auth_token.delete()
    return Response({"message":"logout done successfully"})

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    data = {'data':'', 'status':''}
    saved_serializer=UserProfile(data=request.data)
    if saved_serializer.is_valid():
        saved_serializer.save()
        data['data'] = {'user':
             { 'email': saved_serializer.data.get('email'),
                'username': saved_serializer.data.get('username')

        },
        'message': 'created'
        }
        data['status'] = status.HTTP_201_CREATED
    else:
        data['data'] = saved_serializer.data
        data['status'] = status.HTTP_201_CREATED

    return Response(**data)

