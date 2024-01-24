from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, Receptionist,Booking
from django.views import View
from django.shortcuts import render,redirect
from .serializers import RoomSerializer, ReceptionistSerializer
from rest_framework.authtoken.models import Token
from .forms import BookingForm
from django.contrib.auth import authenticate

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class ViewRoomsView(APIView):
    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return render(request, 'view_rooms.html', {'rooms': serializer.data})
        #return Response(serializer.data, status=status.HTTP_200_OK)

class BookRoomView(View):
    template_name = 'book_room.html'

    def get(self, request, *args, **kwargs):
        room_id = kwargs.get('room_id')
        room = Room.objects.get(pk=room_id)
        form = BookingForm()
        return render(request, self.template_name, {'room': room, 'form': form})

    def post(self, request, *args, **kwargs):
        room_id = request.POST.get('room_id')
        room = Room.objects.get(pk=room_id)
        form = BookingForm(request.POST)

        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            guest_name = form.cleaned_data['guest_name']
            room.is_available = False
            room.save()

            booking = Booking.objects.create(room=room, check_in_date=check_in_date, check_out_date=check_out_date, guest_name=guest_name)

            return redirect('home')  # Redirect to the homepage after booking

        
        return render(request, self.template_name, {'room': room, 'form': form})

class ReceptionistRegistrationView(generics.CreateAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer
    permission_classes = [permissions.AllowAny]

class ReceptionistLoginView(APIView):
    #permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=receptionist)
            return Response({'token': token.key, 'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)