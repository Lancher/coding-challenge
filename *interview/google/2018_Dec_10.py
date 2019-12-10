
# LC 2 ;  follow up： try to use as fewer rounds as possible （two pointer）


# like LC 490: but the maze if infinitely large, want the minimum path length;
# followup: there are obstacles (two-way BFS)
# TODO: Two-Way BFS Word ladder

# like LC Meeting rooms: given 1 worker, several valid job intervals, and a new job interval to add,
# want to check whether it is still valid; follow up: given k workers, several valid job intervals,
# and a new job interval to add, want to check whether it is still valid
# tic tac toe: check winner; follow up: LC 794
# TODO: 794. Valid Tic-Tac-Toe State


# 第一题是给定Google园区地图和自行车分布位置，和你在的位置，如果找到离自己最近自行车。这个可以用DFS或者BFS搜索
# 然后就是如果是同时间给多个人找自行车该怎么做，我先想的是最简单的一个一个来，大叔举了个例子不同顺序的话可能给的不是
# 最优解，最后我又改成多个人同时BFS的方法
# TODO: https://www.youtube.com/watch?v=cQ5MsiGaDY8&t=390s


# 第二也是一个白人小哥。题感觉比较难，我现在还不知应该怎么做。题目是在第一象限里面，两个function--Setvalue（
# x，y，value）会设置一个点的值，x，y范围是0-INT-MAX. getsum（x1,y1,x2,y2)计算在这个矩形内部的所有点的和。
# 问你如何实现这两个函数。我一开始想说用pre-calculated-sum-in-retangle的方法，但是这个matrix又大又稀疏。
# 所以楼主也不知道怎么解。最后硬着头皮写了个基于Set<x>和hashmap<intx,set<y,val>>结构的方法。


# 第四个还是白人大哥，题目非常简单，可能是我没有明白他想考察什么。题目就是很简单的在一个buffer里面填充一个矩形出来。
# 我后来想想可能他想考函数的signiture的设计。


# 最后一个是一个华人小姐姐。出了一个word-complention，也就是使用Trie，完成insert和search+BFS/DFS。
# Leetcode auto complete


# - 第二轮的王位继承，getOrder函数的实现。一般大家好像是preorder traversel，但是看到有面试官要求O(1)实现，
# 不知道有没有朋友有O（1）的做法？
# void birth(String parent, String name) 父亲名字和孩子名字，生个娃
# void death(String name) 此人要死
# List<String> getOrder() 返回当前的继承顺序，string array/list
#
# 讨论得知，每个人的名字是唯一的，继承顺序符合如下规律:
# 假设王有大皇子二皇子三皇子，大皇子有长子次子三子，那么继承顺序是王->大皇子->大皇子长子->大皇子次子->大皇子三子->二皇子->三皇子
# 死掉的人不能出现在继承顺序里，但是如果上面例子中大皇子死了，只需把大皇子移除，原始继承顺序保持不变：王->大皇子长子->大皇子次子->大皇子三子->二皇子->三皇子
#
# 三个function会被反复调用，实现function细节。


# - 第三轮第二题，我的感觉是用map来计数？不是太有思路……
# 产品中要monitor service response time，假设已经收集了大量数据，给定percentile的定义：如果说20ms的响应时间是90
# percentile，代表收集的数据中90%的response time小于20ms，10%的response time大于20ms。同理，如果是说50 percentile，
# 就是50%小于，50%大于。分析如何处理数据从而得到percentile。（这里假设了已经收集了大量数据，
# 但是我们仍然就大量采集数据的系统环境进行了分析。最终还是回归到已经收集好的情况下）假设数据量大到memory无法存下，
# 怎么处理？不考察系统设计，只根据实际需求在数据和算法层面进行优化。


# void update(double price, int timestamp) 更新/修正/删除股票价格，其中timestamp大部分时间是递增的，
# 但是有时候发现过去的记录有错误，所以会对过去数据修正或invalidate。对过去数据修正是指input argument中的timestamp
# 是一个已经记录在案的timestamp，让price为function新提供的price；invalidat时候function argument中的price为-1，
# 删除timestamp对应的记录
# double max() 返回历史最大值
# double min() 返回历史最低值
# double current() 返回最近一次的记录。
# . From 1point 3acres bbs
# 针对各种情况进行实现和算法复杂度讨论。（大量更新？大量查询？invalidate很多很少？etc.）


# move() 朝着机器人面对方向移动一格
# turnLeft(int k) 逆时针转动k次
# turnRight(int k) 顺时针转动k次
# clean() 打扫机器人当前格子
# cleanRoom() 发动机器人清理整个房间，清扫任务的entry function。
#
# 难点主要在如何把move turn和clean的function扦插到具体的算法实现中。


