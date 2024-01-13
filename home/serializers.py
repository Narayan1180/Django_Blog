
from rest_framework import serializers

from. models import Blog

class BlogSerializer(serializers.ModelSerializer): # use ModelSerializer if its not requeire much customizations
    class Meta:
        model=Blog

        exclude=['created_at','updated_at']

