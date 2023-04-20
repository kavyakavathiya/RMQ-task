from task_queue.tasks import add

result = add.delay(2, 2)
print(result.wait())
