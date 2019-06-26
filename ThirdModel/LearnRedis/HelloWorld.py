import redis
r = redis.Redis(host='10.45.18.128',port=6379,db=0)
r.set('hello','world')
print(r.get('hello'))
