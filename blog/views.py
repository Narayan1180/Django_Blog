
from django.shortcuts import render,HttpResponse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
import requests

# Django view for rendering HTML
def blog_posts(request):
    # Fetch blog posts from the Django REST API
    api_url = 'http://localhost:8000/api_posts/'  # Adjust the API endpoint
    response = requests.get(api_url)
    
    if response.status_code == 200:
        try:
            posts = response.json()
            return render(request, 'blog_posts.html', {'posts': posts})
        except requests.exceptions.JSONDecodeError as e:
            return HttpResponse( {'error_message': f'Error decoding JSON: {e}'})
    else:
        return HttpResponse( {'error_message': "error"})

# Django REST API view
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

