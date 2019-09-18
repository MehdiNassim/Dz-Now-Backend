# from django.shortcuts import render
# from rest_framework import viewsets, mixins
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.exceptions import ParseError
# from rest_framework.schemas import ManualSchema
# from rest_framework.compat import coreapi, coreschema
from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import FileUploadParser
# from rest_framework import status
# from rest_framework import filters
# import time
from django.views.decorators.csrf import csrf_exempt
# import json
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from google.oauth2 import id_token
from google.auth.transport import requests

# import datetime
# from django.db.models.expressions import RawSQL
# from django.db.models import Count

from . import serializers
from . import models
from . import permissions

CLIENT_ID = "252296444280-4f8cvbso5p7k6qf7mo0flqsraldrt2ir.apps.googleusercontent.com"


@csrf_exempt
def login_user_google(access_token):
    try:
        user_info = id_token.verify_oauth2_token(access_token, requests.Request(), CLIENT_ID)

        if user_info['aud'] not in [CLIENT_ID]:
            raise ValueError('Could not verify audience.')

        if user_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return JsonResponse({'error': 'Invalid data'}, safe=False)
    except ValueError:
        return JsonResponse({'error': 'Invalid token'}, safe=False)
    try:
        user = models.UserProfile.objects.get(google_id=user_info['sub'])

    except models.UserProfile.DoesNotExist:
        password = '123456'
        user = models.UserProfile(
            email=user_info['email'],
            first_name=user_info['given_name'],
            last_name=user_info['family_name'],
            google_id=user_info['sub'],
        )
        user.set_password(password)
        user.save()
    try:
        token = Token.objects.get(user=user).key
    except:
        token = Token.objects.create(user=user).key
    if token:
        return JsonResponse(
            {
                'token': token,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
    else:
        return JsonResponse({'error': 'Invalid data'})


class AuthSocial(APIView):
    def post(self, request):
        try:
            access_token = request.data['accessToken']
            return login_user_google(access_token)
        except:
            return JsonResponse({'error': 'Error in request'})
