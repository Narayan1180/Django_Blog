"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# blog/urls.py
from django.urls import path
from .views import blog_posts, PostListCreateView,BlogDetailView

urlpatterns = [
    path('', blog_posts, name='blog_posts'),
    path('api_posts/', PostListCreateView.as_view(), name='api_posts'),
    path('update_posts/<int:pk>', BlogDetailView.as_view(), name='update_posts'),
    # Add other URL patterns as needed
]

