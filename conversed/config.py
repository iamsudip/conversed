import os

REDIS_HOST = os.environ.get('OPENSHIFT_REDIS_DB_HOST') \
    if os.environ.get('OPENSHIFT_REDIS_DB_HOST') else '127.0.0.1'
REDIS_PORT = os.environ.get('OPENSHIFT_REDIS_DB_PORT') \
    if os.environ.get('OPENSHIFT_REDIS_DB_PORT') else '6379'
REDIS_PASSWORD = os.environ.get('OPENSHIFT_REDIS_DB_PASSWORD') \
    if os.environ.get('OPENSHIFT_REDIS_DB_PASSWORD') else None