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
    
    # Wait for Redis to be ready
    while True:
        try:
            r.ping()
            print("Successfully connected to Redis!")
            break
        except Exception as e:
            print(f"Waiting for Redis... ({e})")
            time.sleep(2)

    while True:
        try:
            message = r.blpop("task_notifications", timeout=0)
            if message:
                task_data = json.loads(message[1])
                print(f"[notify] sending notification for task: {task_data['title']}")
                time.sleep(2)
                print(f"[DONE] notification sent!")
        except Exception as e:
            print(f"Connection lost, retrying... ({e})")
            time.sleep(2)

if __name__ == "__main__":
    process_notification()

    

