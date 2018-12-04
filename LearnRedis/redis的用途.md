#1、全页面缓存
首先是整页缓存。
如果你正在使用服务器端呈现的内容，则不需要为每个单独的请求重新渲染每个页面。
使用如Redis这样的缓存，你可以缓存经常请求的内容，从而大大减少请求最多的页面的延迟，并且大多数框架针对Redis缓存页面都有hooks。

简单命令


/ Set the page that will last 1 minute
SET key "<html>...</html>" EX 60
// Get the page
GET key
#2、排行榜
Redis令人耀眼的地方之一就是排行榜。
由于Redis在内存中，因此可以非常快速和高效地处理递增和递减。
将此与每个请求运行SQL查询比较，性能收益巨大！
这与Redis的排序集相结合意味着你可以以毫秒为单位抓取列表中评分最高的项目，而且实现起来非常容易。

简单命令


// Add an item to the sorted set
ZADD sortedSet 1 "one"
// Get all items from the sorted set
ZRANGE sortedSet 0 -1
// Get all items from the sorted set with their score
ZRANGE sortedSet 0 -1 WITHSCORES

#3、会话Session存储
我所见的Redis最常见的用途是会话存储。
与其他会话存储（如Memcache）不同，Redis可以保留数据，以便在缓存停止的情况下，
在重新启动时，所有数据仍然存在。
即便不是需要严格持续的任务，此功能仍可以为你的用户省去大量的麻烦。没有人会乐于见到他们的会话被无缘无故随机删掉。

简单命令


	// Set session that will last 1 minute
	SET randomHash "{userId}" EX 60
	// Get userId
	GET randomHash
	
#4、队列
使用Redis可以做的一个不太常见，但非常有用的事情是排队。
无论是电子邮件队列还是其他应用程序使用的数据，你都可以在Redis中创建一个高效的队列。
任何熟悉堆栈以及会push和pop项目的开发人员都可以轻松自然地使用此功能。

简单命令


	// Add a Message
	HSET messages <id> <message>
	ZADD due <due_timestamp> <id>
	// Recieving Message
	ZRANGEBYSCORE due -inf <current_timestamp> LIMIT 0 1
	HGET messages <message_id>
	// Delete Message
	ZREM due <message_id>
	HDEL messages <message_id>

#5、pub/sub
Redis在真实世界的最终用法即我将在这篇文章中提出的pub / sub。这是Redis内置的最强大的功能之一；得到的可能是无限的。
你可以创建一个实时聊天系统，在社交网络上触发好友请求的通知等等。这个功能是Redis提供的最被低估的功能之一，但功能非常强大，而且使用简单。

简单命令

	// Add a message to a channel
	PUBLISH channel message
	// Recieve messages from a channel
	SUBSCRIBE channel
结论

我希望你会喜欢这些Redis在真实世界的使用。
虽然这篇文章只抓住了Redis能为你做的事情的表面，但是我希望你能从中获得应如何充分利用Redis的启发。
