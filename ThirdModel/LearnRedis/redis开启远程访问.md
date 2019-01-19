https://www.cnblogs.com/liusxg/p/5712493.html

redis默认只允许本地访问，要使redis可以远程访问可以修改redis.conf
 
打开redis.conf文件在NETWORK部分有说明
 
	################################## NETWORK #####################################
	 
	# By default, if no "bind" configuration directive is specified, Redis listens
	# for connections from all the network interfaces available on the server.
	# It is possible to listen to just one or multiple selected interfaces using
	# the "bind" configuration directive, followed by one or more IP addresses.
	#
	# Examples:
	#
	# bind 192.168.1.100 10.0.0.1
	# bind 127.0.0.1 ::1
	#
	# ~~~ WARNING ~~~ If the computer running Redis is directly exposed to the
	# internet, binding to all the interfaces is dangerous and will expose the
	# instance to everybody on the internet. So by default we uncomment the
	# following bind directive, that will force Redis to listen only into
	# the IPv4 lookback interface address (this means Redis will be able to
	# accept connections only from clients running into the same computer it
	# is running).
	#
	# IF YOU ARE SURE YOU WANT YOUR INSTANCE TO LISTEN TO ALL THE INTERFACES
	# JUST COMMENT THE FOLLOWING LINE.
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	bind 127.0.0.1
 
##解决办法：注释掉bind 127.0.0.1可以使所有的ip访问redis
若是想指定多个ip访问，但并不是全部的ip访问，可以bind
 
注意
下面还有个说明
 
	# Protected mode is a layer of security protection, in order to avoid that
	# Redis instances left open on the internet are accessed and exploited.
	#
	# When protected mode is on and if:
	#
	# 1) The server is not binding explicitly to a set of addresses using the
	#    "bind" directive.
	# 2) No password is configured.
	#
	# The server only accepts connections from clients connecting from the
	# IPv4 and IPv6 loopback addresses 127.0.0.1 and ::1, and from Unix domain
	# sockets.
	#
	# By default protected mode is enabled. You should disable it only if
	# you are sure you want clients from other hosts to connect to Redis
	# even if no authentication is configured, nor a specific set of interfaces
	# are explicitly listed using the "bind" directive.
	protected-mode yes
 
 
在redis3.2之后，redis增加了protected-mode，在这个模式下，即使注释掉了bind 127.0.0.1，再访问redisd时候还是报错，如下
 
	(error) DENIED Redis is running in protected mode because protected mode is enabled, no bind address was specified, no authentication password is requested to clients. In this mode connections are only accepted from the loopback interface. If you want to connect from external computers to Redis you may adopt one of the following solutions: 1) Just disable protected mode sending the command 'CONFIG SET protected-mode no' from the loopback interface by connecting to Redis from the same host the server is running, however MAKE SURE Redis is not publicly accessible from internet if you do so. Use CONFIG REWRITE to make this change permanent. 2) Alternatively you can just disable the protected mode by editing the Redis configuration file, and setting the protected mode option to 'no', and then restarting the server. 3) If you started the server manually just for testing, restart it with the '--protected-mode no' option. 4) Setup a bind address or an authentication password. NOTE: You only need to do one of the above things in order for the server to start accepting connections from the outside.
 
##修改办法：protected-mode no