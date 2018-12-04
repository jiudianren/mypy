#1��ȫҳ�滺��
��������ҳ���档
���������ʹ�÷������˳��ֵ����ݣ�����ҪΪÿ������������������Ⱦÿ��ҳ�档
ʹ����Redis�����Ļ��棬����Ի��澭����������ݣ��Ӷ���������������ҳ����ӳ٣����Ҵ����������Redis����ҳ�涼��hooks��

������


/ Set the page that will last 1 minute
SET key "<html>...</html>" EX 60
// Get the page
GET key
#2�����а�
Redis����ҫ�۵ĵط�֮һ�������а�
����Redis���ڴ��У���˿��Էǳ����ٺ͸�Ч�ش�������͵ݼ���
������ÿ����������SQL��ѯ�Ƚϣ���������޴�
����Redis������������ζ��������Ժ���Ϊ��λץȡ�б���������ߵ���Ŀ������ʵ�������ǳ����ס�

������


// Add an item to the sorted set
ZADD sortedSet 1 "one"
// Get all items from the sorted set
ZRANGE sortedSet 0 -1
// Get all items from the sorted set with their score
ZRANGE sortedSet 0 -1 WITHSCORES

#3���ỰSession�洢
��������Redis�������;�ǻỰ�洢��
�������Ự�洢����Memcache����ͬ��Redis���Ա������ݣ��Ա��ڻ���ֹͣ������£�
����������ʱ������������Ȼ���ڡ�
���㲻����Ҫ�ϸ���������񣬴˹����Կ���Ϊ����û�ʡȥ�������鷳��û���˻����ڼ������ǵĻỰ����Ե�޹����ɾ����

������


	// Set session that will last 1 minute
	SET randomHash "{userId}" EX 60
	// Get userId
	GET randomHash
	
#4������
ʹ��Redis��������һ����̫���������ǳ����õ��������Ŷӡ�
�����ǵ����ʼ����л�������Ӧ�ó���ʹ�õ����ݣ��㶼������Redis�д���һ����Ч�Ķ��С�
�κ���Ϥ��ջ�Լ���push��pop��Ŀ�Ŀ�����Ա������������Ȼ��ʹ�ô˹��ܡ�

������


	// Add a Message
	HSET messages <id> <message>
	ZADD due <due_timestamp> <id>
	// Recieving Message
	ZRANGEBYSCORE due -inf <current_timestamp> LIMIT 0 1
	HGET messages <message_id>
	// Delete Message
	ZREM due <message_id>
	HDEL messages <message_id>

#5��pub/sub
Redis����ʵ����������÷����ҽ�����ƪ�����������pub / sub������Redis���õ���ǿ��Ĺ���֮һ���õ��Ŀ��������޵ġ�
����Դ���һ��ʵʱ����ϵͳ�����罻�����ϴ������������֪ͨ�ȵȡ����������Redis�ṩ����͹��Ĺ���֮һ�������ܷǳ�ǿ�󣬶���ʹ�ü򵥡�

������

	// Add a message to a channel
	PUBLISH channel message
	// Recieve messages from a channel
	SUBSCRIBE channel
����

��ϣ�����ϲ����ЩRedis����ʵ�����ʹ�á�
��Ȼ��ƪ����ֻץס��Redis��Ϊ����������ı��棬������ϣ�����ܴ��л��Ӧ��γ������Redis��������
