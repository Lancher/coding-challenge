# 1. lc 酒吧
# 98. Validate Binary Search Tree


# 2. time-stamped hash table, follow-up multi-tread 一个写一个读怎么办
#

# 3. hash-table 原理问了两遍。。。

# 4. 蠡口依山舞. From 1point 3acres bbs

# 5. 带引号的tokenization


# 6. next element of a given node in bst with parent ptr, follow-up 只给root怎么做

#
# 第一轮， 国人小哥，入职10个月。 最近高频题 有一堆棋子 坐标int[]x, int[]y, 如果两个棋子x或者y相同，就可以选择拿掉一个
#                按照这个规则一直拿，请问能拿的最多数量。
#
#                我当时准备面经的时候这题还不是高频，所以 一开始就想到用greedy 找到取棋子的顺序， 其实是topological 顺序。
#                但是国人小哥觉得这题没必要， 给了我一个反例（其实后来我发现top肯定可以， 但是不好和他反驳）
#                在他提示下， 画了两个连通图 问我最后剩几个， 我发现这题就是找联通块个数，就是剩下的棋子数
#                用Union Find写了， 但是发现原input 我这样写是O（N^2) 小哥说有什么优化方法。
#                想到了用hashmap记录adjacent list，也就是对input进行处理先。
#                没写代码这部分， 时间差不多到了。 小哥说dfs对于这题其实更简单，不懂为什么大家都喜欢用union find。
#               但是因为input的原因 真的第一时间想拿来dfs感觉也挺难处理的。   整体小哥觉得非常满意

# 第二轮， 国人小姐姐。 也非常nice。 考得是num of island 变种。 求出各个联通块1的数量之后， 将这些数字排成一排找到其中median
#               我分析了下说先dfs找联通块
#               然后quickSelect 找mid number
#               dfs找联通块的时候 因为要记录当前联通块数量， 我说用个global var，她说最好不要， 提示了下 发现可以dfs return 一个int来pop结果
#               之后正准备要写QuickSelect，结果被告知可以有这个api。。。。
#               所以留出10分钟聊天 也没第二题了

# 中午吃饭。 国人小哥， 友好。 chicken leg不错


# 第三轮，  不太典型的阿三。 上来问了我一堆restful （我有相关实习经验） 的知识。 考了我http code， 但是我真的不会。
#                 我只知道基本的， 但是他问我 201， 203， 205 还有 401和403差别。 还有how to partially update something （patch）. From 1point 3acres bbs
#                 这里没怎么回答上， 不知道会不会扣分
#                 题目： 说了半天local min 和如何找， 然后扩展到三维上， 给一个点请问找到附近的local min  我问是否方向360°，说简化前后左右。
#                             又是一个dfs 从当前点找四个方向比自己低的点走， 不需要记录visited, 因为总是从高往低。 直到自己四周都比自己高，就返回自己
#                             因为boundary默认是无穷高，所以必然有（和面试官check过）
#                             run了test case， handle了corner case。 面试官满意。


# 第四轮，  亚裔10年大哥，微软7gg3. 年轻看不出来10年经验了。  上来后似乎临时给我出题。 出了四题。
#                1. 面经删除binary tree的invali 边。 traverse + set秒之
#                2.求binary tree 最底下一层level的sum。  bfs level order traverse 秒之
#                3.写一个binary search 要找第一个比x（可能不存在） 大的数的index。 bug free +test case 秒之。
#                4. 面经题。 一个单词 "sprint" 可以选择删除任何一个char 但是删除之后的单词必须得在dict里面。
#                      请问这个单词是否可以删到最后只剩一个char （一个char默认可以删完）。
#                      本以为考trie。 结果说给了  boolean isWord(String str)  也就是说字典已经给了
#                     dfs backtrack + memo 解决。
#                这轮状态挺好，题目也不难，面试官挺满意。


# Round 1 : 给一个无序数组， 一个参数 k。 返回boolean表示能不能把数组分成长为k的顺子。followup :
# 简单判断输入无懈情况 (len % k == 0) followup ： 顺子长度限制改为只要 l >= 3 就行。这题和蠡口原题区别是输入数组是无序的。
# 复用了第一问的一些代码，我用treemap做的。写完代码比划比划test case就到时间了。
# TODO: [寫過了] 好像有更好的結髮

# Round 2 : 一个完全二叉树， 节点从浅到深，从左到右标号 1, 2, 3, 4, ... implement一个method
# TreeNode getIndexedNode(TreeNode root, int ind) 返回标号为ind的节点，没有就返回null。给了个空间O(1)的解法，
# 面试官一开始没懂讲了半天。 followup：implement int getSize(TreeNode root)。用第一问实现的method，
# 二分最深一层最右的叶子节点搞定。


# Round 3：每个entry有duration的Map。高频面经不多说了，面试官表示key和value可以是不同的类型，
# 于是我用泛型写。followup：这个design有什么问题，答曰有的entry过期了还存着浪费空间， 加个clean(),
# 用heap做。写完代码又问unit test 哪里最难，没答上，大哥表示应该dependency inject 一个 fake clock。



# Round 4 : 换了包装的House Rob。就是给一个数组，求subset最大和并要求选的元素不能相邻。
# 一维dp做，写了一半跟面试官说可以constant space。 写完面试官说你把constant space的也写了吧。
# 然后第二题：问我听没听说过ASCII Map， 我表示完全没有，然后出了一道数岛（汗）。
# followup ： 有一个method可以把一块水变成陆地，然后返回岛的个数。假装思考了一会说了两句废话然后跟他讲了并查集的做法。



# TODO: 第二轮是个CBC，还是面经的高频，在树里面A已经选中一个节点，你需要选出另外一个最佳点。follow up是先手的话选哪里。
# 第一问很简单，第二问也秒写了，不过一开始的写法比较弱智，我直接用了hashmap做记录，没直接返回结果，
# 导致空间复杂度是O（n^2)之后写完了code才优化。之后又聊了聊bfs和dfs的区别，以及实际上的空间
# 使用。包括stack和heap的实际空间大小。感觉这轮其实可以是strong的，但是可能小哥不满意follow up直接给的复杂度太高，
# 只给了positive


