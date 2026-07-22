# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Product
# from .serializers import ProductSerializer

# class ProductListCreate(APIView):
#     # Write a get request for getting all products
#     def get(self,request):
#         products= Product.Objects.all()
#         # Here we will user serializer to convert python objet into json
#         serializer = ProductSerializer(
#             products,many=True
#         )
#         return Response(serializer.data)
    
#     # Write a post request for adding a new product
#     def post(self, request):
#         serializer = ProductSerializer(
#             data=request.data
#         )  # Request Data
#         if serializer.is_valid():  # Check data is valid or not
#             serializer.save()  # Saving in Database
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


from rest_framework import generics
#This is the most important thing in DRF for writing the API of your project
#It makes your code shorter because when we are writing APIs in normal django
# The code becomes messay
from rest_framework.permissions import AllowAny
#This module in DRF tells the django which can access the api
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    #This the post request in djando rest framework
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
