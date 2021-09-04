import redis
class Redis:
    client = ''
    def __init__(self):
        redis_url = 'redis://localhost:6379/0'
        self.client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
    def send_data(self, data: str):
        self.client.publish('logger',data)