import os


# Redis configuration
REDIS_HOST = os.environ.get('OPENSHIFT_REDIS_DB_HOST') \
    if os.environ.get('OPENSHIFT_REDIS_DB_HOST') else '127.0.0.1'
REDIS_PORT = os.environ.get('OPENSHIFT_REDIS_DB_PORT') \
    if os.environ.get('OPENSHIFT_REDIS_DB_PORT') else '6379'
REDIS_PASSWORD = os.environ.get('OPENSHIFT_REDIS_DB_PASSWORD') \
    if os.environ.get('OPENSHIFT_REDIS_DB_PASSWORD') else None

# Vibe API
# API = 'https://vibeapp.co/api/v1/initial_data/'
API = 'https://z1.vibeapp.co/api/v1/profile_lookup/'
API_STAT = 'https://vibeapp.co/api/v1/api_stats/'
#API_KEY = 'b2acf1eadef73f4aeda890e0571f3e06'
API_KEY = '1506031333144200697baf0680018ab63e17d327076ef437f5'

LOCAL_DEV = False if os.environ.get('OPENSHIFT_REDIS_DB_PASSWORD') else True

FLUSH_VERSION = 2
FLUSH_REDIS = 'FLUSH_REDIS'
