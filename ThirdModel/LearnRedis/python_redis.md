
http://www.cnblogs.com/melonjiang/p/5342383.html
Python—redis


#如果是用apt-get或者yum install安装的redis，可以直接通过下面的命令停止/启动/重启redis

/etc/init.d/redis-server stop 
/etc/init.d/redis-server start 
/etc/init.d/redis-server restart

#如果是通过源码安装的redis，则可以通过redis的客户端程序redis-cli的shutdown命令来重启redis

1.redis关闭 
redis-cli -h 127.0.0.1 -p 6379 shutdown

2.redis启动 
redis-server
./redis-server /path/to/redis.conf

#安装redis python客户端

pip install redis
查看安装是否成功
pip list