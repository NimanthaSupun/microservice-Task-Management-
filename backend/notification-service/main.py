import redis
import os
import time
import json

# todo: connect to the redis
REDIS_URL = os.getenv("REDIS_URL","redis://localhost:6379")

#todo: We extract the host from the URL (e.g., 'redis')
#todo: For simplicity in this example, we can use redis.from_url
r = redis.from_url(REDIS_URL)


def process_notification():
    print("Notification service started, waiting for message....")

  # We use a 'pubsub' model or a simple 'list' (Queue)
    # Let's use a list for a reliable queue (RPOP/BLPOP)
    while True:
        # BLPOP 'blocks' until a message is available in the 'notifications' queue
        message = r.blpop("task_notifications",timeout=0)

        if message:
            # message is a tuple(queue_name,data)
            task_data = json.loads(message[1])
            print(f"[notify] sending notification for task: {task_data['title']}")
            # Here you would normally send an email/SMS
            time.sleep(2) # simulate task
            print(f"[DONE] notification sent!")

if __name__ == "__main__":
    process_notification()

    

