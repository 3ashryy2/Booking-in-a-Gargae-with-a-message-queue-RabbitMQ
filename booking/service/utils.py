import pika
import json
import requests

def send_booking_request(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='booking_requests', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='booking_requests',
        body=json.dumps(data),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()


def send_notification(token, title, body, data):
    url = "http://notification_service_host:port/send-notification"  # Adjust with actual host and port
    payload = {
        "token": token,
        "title": title,
        "body": body,
        "data": data
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()  # Return JSON response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}  # Return error details