import redis


def get_redis_connection(redis_host,redis_port,redis_password,redis_database = 0):
	pool = redis.ConnectionPool(host=redis_host, port=redis_port,password=redis_password)
	redis_connection = redis.Redis(connection_pool=pool)
	return redis_connection

def set_key(key,val):
	connection = get_redis_connection()
	connection.set(key,val)

def get_key(key):
	connection = get_redis_connection()
	return connection.get(key)