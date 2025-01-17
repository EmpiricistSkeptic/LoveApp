from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer, UserRegistrationSerializer, LoginSerializer
from .models import RelationshipDate, Profile


def main_page(request):
    return render(request, 'main.html')

def poems_page(request):
    return render(request, 'poems.html')


def letters_page(request):
    return render(request, 'letters.html')

def map_page(request):
    return render(request, 'map.html')


@api_view(['POST'])
def registerAccount(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created succssefuly"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginUser(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "Login successful"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logoutUser(request):
    try:
        token = request.user.auth_token
        if token:
            token.delete()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        return Response({"error": "No token provided"}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"error": "An error occured during logout"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'PUT'])
def userProfile(request):
    if request.method == 'GET':
        try:
            profile = request.user.profile
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            profile = request.user.profile
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)