from rest_framework import viewsets, status as rest_status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from .utils import send_booking_request


class BookingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


    def perform_create(self, serializer):
        instance = serializer.save()
        booking_data = {
            'booking_id': instance.id,
            'garage_id': instance.garage_id,
            'start_date': instance.start_date.isoformat(),
            'end_date': instance.end_date.isoformat()
        }
        send_booking_request(booking_data)
        return Response(serializer.data, status=rest_status.HTTP_201_CREATED)

    @action(detail=True, methods=['post','put'], url_path='update_status')
    def update_status(self, request, pk=None):
        booking = self.get_object()
        new_status = request.data.get('status')
        if new_status not in Booking.STATUS_CHOICES:
            return Response({'error': 'Invalid status'}, status=rest_status.HTTP_400_BAD_REQUEST)

        booking.status = new_status
        booking.save()
        return Response({'status': 'updated'}, status=rest_status.HTTP_200_OK)