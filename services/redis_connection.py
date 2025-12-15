import os

from redis import Redis

# Подключение к базе данных
REDIS_HOST=os.getenv("REDIS_HOST")
REDIS_PORT=os.getenv("REDIS_PORT")
REDIS_DB=os.getenv("REDIS_DB")

r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)





