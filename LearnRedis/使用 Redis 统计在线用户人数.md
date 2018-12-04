https://blog.csdn.net/zwjyyy1203/article/details/80342874


方案 1 ：使用有序集合
每当一个用户上线时， 我们就执行 ZADD 命令， 将这个用户以及它的在线时间添加到指定的有序集合中：

ZADD "online_users" <user_id> <current_timestamp>
通过使用 ZSCORE 命令检查指定的用户 ID 在有序集合中是否有相关联的分值， 我们可以知道该用户是否在线：

ZSCORE "online_users" <user_id>
而通过执行 ZCARD 命令， 我们可以知道总共有多用户在线：

ZCARD "online_users"
使用有序集合储存在线用户的强大之处在于， 它是本文介绍的所有方案当中， 能够执行最多聚合操作的一个方案， 原因在于， 这一方案既可以通过有序集合的成员（也即是用户的 ID）进行聚合操作， 也可以根据有序集合的分值（也即是用户的登录时间）进行聚合操作。

首先， 通过 ZINTERSTORE 和 ZUNIONSTORE 命令， 我们可以对多个记录了在线用户的有序集合进行聚合计算：

# 计算出 7 天之内都有上线的用户，并将它储存到 7_days_both_online_users 有序集合当中
ZINTERSTORE 7_days_both_online_users 7 "day_1_online_users" "day_2_online_users" ... "day_7_online_users"

# 计算出 7 天之内总共有多少人上线了
ZUNIONSTORE 7_days_total_online_users 7 "day_1_online_users" ... "day_7_online_users"
此外， 通过 ZCOUNT 命令， 我们可以统计出在指定的时间段之内有多少用户在线， 而 ZRANGEBYSCORE 命令则可以让我们获取到这些用户的名单：

# 统计指定时间段内上线的用户数量
ZCOUNT "online_users" <start_timestamp> <end_timestamp>

# 获取指定时间段内上线的用户名单
ZRANGEBYSCORE "online_users" <start_timestamp> <end_timestamp> WITHSCORES
通过这一方法， 我们可以知道网站在不同时间段的上线人数以及上线用户名单， 比如说， 我们可以用这个方法来分别获知网站在早晨、上午、中午、下午和夜晚的上线人数。