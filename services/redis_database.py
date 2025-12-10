import os

from pygments.lexers import q
from redis import Redis


REDIS_HOST=os.getenv("REDIS_HOST")
REDIS_PORT=int(os.getenv("REDIS_PORT"))
REDIS_DB=int(os.getenv("REDIS_DB"))

r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

ttl_seconds = 2*24*60*60  # TTL = 2 дня


