from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
import requests
import json
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class =PostSerializer

#kakao api
url = "https://dapi.kakao.com/v2/search/web"
queryString = {"query":"덕성여자대학교"}
header = {"Authorization":"KakaoAK 14e325f9b8a8506687a9d4b59bf6455d"}
r = requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))

print("############## api2 ################")
url = "https://kapi.kakao.com/v1/api/talk/profile"
header = {"Authorization":"Bearer 14e325f9b8a8506687a9d4b59bf6455d"}
r = requests.get(url, headers=header)
print(json.loads(r.text))
