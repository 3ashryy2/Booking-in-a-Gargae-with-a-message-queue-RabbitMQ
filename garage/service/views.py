from rest_framework import viewsets, status as http_status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BookingRequest
from rest_framework.exceptions import NotFound, ValidationError
from .serializers import BookingRequestSerializer
from .utils import send_garage_response

class BookingRequestViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing booking requests.
    """
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer


    @action(detail=True, methods=['post'], url_path='decide')
    def decide(self, request, pk=None):
        try:
            booking_request = self.get_object()
        except BookingRequest.DoesNotExist:
            raise NotFound(detail="Booking request not found.")

        status = request.data.get('status', None)
        if status not in ['confirmed', 'rejected']:
            raise ValidationError(detail="Invalid status provided.")

        booking_request.status = status
        booking_request.save()

        response_data = {
            'booking_id': booking_request.booking_id,
            'status': status
        }
        send_garage_response(response_data)
        return Response({'status': 'Booking request updated.'}, status=http_status.HTTP_200_OK)
