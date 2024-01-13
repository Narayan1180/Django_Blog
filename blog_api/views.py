from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializers,LoginSerializers


# creating register and login page
class RegisterView(APIView):

    def post(self,request):

        try:

            data=request.data
            print(data)
            serializer = RegisterSerializers(data=data)
            if not serializer.is_valid():

                return Response({

                    'data':serializer.errors,
                    'message':'something went wrong',
    
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data':{},
                'message':'your account is created'
            },status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)



class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            print(data)
            serializer=LoginSerializers(data=data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({

                    'data':serializer.errors,
                    'message':'something went wrong',
    
                },status=status.HTTP_400_BAD_REQUEST)
            
            response=serializer.get_jwt_token(serializer.data)
            print(response)
            return Response(
                response,status=status.HTTP_200_OK  
            )
        
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

            




    



