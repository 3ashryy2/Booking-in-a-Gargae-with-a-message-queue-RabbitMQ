from django.apps import AppConfig
import pika

class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'

    def ready(self):
        self.create_rabbitmq_queue('garage_responses')

    @staticmethod
    def create_rabbitmq_queue(queue_name):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)
        connection.close()




