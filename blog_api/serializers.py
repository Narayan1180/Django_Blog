from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializers(serializers.Serializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    password=serializers.CharField()


    def validate(self,data):

        if User.objects.filter(username=data['username']).exists(): #checking duplicated users

            raise serializers.ValidationError('username is taken')
        
        return data
    

    def create(self,validated_data): #creating user 
        user = User.objects.create(first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   username=validated_data['username'])
        

        user.set_password(validated_data['password']) # this will automatically apply hash value

        user.save() # its required without it ,it will not stored in django db
        return user
    

class LoginSerializers(serializers.Serializer):  #use serializer when much customizations is needed
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):

        if not  User.objects.filter(username=data['username']).exists():

            raise serializers.ValidationError('username is taken')
        
        return data
    

    def get_jwt_token(self,data): # creating token for authenticated users

        user =authenticate(username=data['username'],password=data['password'])

        if not user:

            return {'messages':'Invalid Credentials','data':{}}
        
        refresh=RefreshToken.for_user(user) # authenticated user will get access token

        return {'message':'login success','data':{'token':'refresh','refresh':str(refresh),'access':str(refresh.access_token)}}



