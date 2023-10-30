from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer
from .utils import custom_response
# Create your views here.


class PostListView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        post_serializer = PostSerializer(queryset, many=True)
        return Response(post_serializer.data)


class PostCreateView(APIView):

    def post(self, request, *args, **kwargs):

        post_serializer = PostSerializer(data=request.data)

        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=HTTP_201_CREATED)

        return Response(post_serializer.errors, status=HTTP_400_BAD_REQUEST)


class PostDetailViewAPI(APIView):

    def get(self, request, pk, *args, **kwargs):

        try:
            post = Post.objects.get(pk=pk)

        except post.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)
    
            # Updated Item 


    def put(self, request, pk, *args, **kwargs):

        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        post_serializer = PostSerializer(post, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response({"success": True, "message": "Succcessfully Updated Item"}, post_serializer.data)
        return Response(post_serializer.errors, status=HTTP_400_BAD_REQUEST)
    


    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"success": False, "message": "Item Not Found"}, status=HTTP_404_NOT_FOUND)
        post.delete()
        return Response({"success": True, "message": "Succcessfully Deleted Item"}, status=HTTP_204_NO_CONTENT)
