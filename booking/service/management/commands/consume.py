from django.core.management.base import BaseCommand
import pika
import json
from service.models import Booking
from service.utils import send_notification


class Command(BaseCommand):
    help = 'Consumes responses from the Garage microservice'

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='garage_responses', durable=True)

        def callback(ch, method, properties, body):
            data = json.loads(body)
            # Assuming data contains 'booking_id' and 'status'
            send_notification(data['client_token'], "Booking Update", f"Your booking request has been {data['status']}.", {'booking_id': data['booking_id']})
            Booking.objects.filter(id=data['booking_id']).update(status=data['status'])
            print("Booking updated:", data)

        channel.basic_consume(queue='garage_responses', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
