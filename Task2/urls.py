from django.urls import path
#from . import views
from .views import HomePageView,ViewRoomsView,BookRoomView, ReceptionistRegistrationView, ReceptionistLoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('view-rooms/', ViewRoomsView.as_view(), name='view-rooms'),
    path('book-room/<int:room_id>/', BookRoomView.as_view(), name='book-room'),
    path('receptionist/register/', ReceptionistRegistrationView.as_view(), name='receptionist-register'),
    path('receptionist/login/', ReceptionistLoginView.as_view(), name='receptionist-login'),
]