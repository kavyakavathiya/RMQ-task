from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import pika
import json

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = data.get('task') 
        # task = request.POST.get('task')
        print(task)
        new_task = Task(task=task)
        new_task.save()

        # publish task to RMQ queue
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='task_queue')
        channel.basic_publish(exchange='', routing_key='task_queue', body=json.dumps({'task': task}))
        connection.close()

        return JsonResponse({'status': 'success'})
    else:
        return HttpResponseNotFound('Not found')
