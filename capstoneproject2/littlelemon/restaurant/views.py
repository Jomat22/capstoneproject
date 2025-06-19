from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import booking, menu, MenuItem
from .serializers import menuSerializer, bookingSerializer, MenuItemSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated




@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
       queryset = MenuItem.objects.all()
       serializer_class = MenuItemSerializer




class bookingview(APIView):
  
  def get(self,request):
    items = booking.objects.all()
    serializer = bookingSerializer
    return Response(serializer.data)
  
  def post(self,request):
    serializer = menuSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response({"status":"success", "data":serializer.data})
    

class MenuItemsView(generics.ListCreateAPIView):
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer



class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing booking instances.
    Provides CRUD operations for the Booking model.
    """
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]
