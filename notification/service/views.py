# Noftification/service/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer  # Ensure you have a serializer for validation
from .utils import send_fcm_message

class SendNotificationAPIView(APIView):
    """
    API view to send notifications via FCM HTTP v1 API.
    """
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            title = serializer.validated_data.get('title')
            body = serializer.validated_data.get('body')
            data = serializer.validated_data.get('data')
            response = send_fcm_message(token, title, body,data)
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
