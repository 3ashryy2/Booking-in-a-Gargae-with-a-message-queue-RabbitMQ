from django.core.management.base import BaseCommand
import pika
import json
from service.models import BookingRequest
from service.utils import send_notification

class Command(BaseCommand):
    help = 'Consumes booking requests from the Booking microservice'

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='booking_requests', durable=True)

        def callback(ch, method, properties, body):
            data = json.loads(body)
            # Assuming data contains 'booking_id', 'garage_id','start_date', and 'end_date', 'status'
            send_notification(data['client_token'], "Booking Request", f"Your booking request from {data['start_date']} to {data['end_date ']} has been received.", {'booking_id': data['booking_id']})
            BookingRequest.objects.create(**data)
            print("Booking request received and created:", data)

        channel.basic_consume(queue='booking_requests', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
