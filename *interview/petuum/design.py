

# 如题, 想问一道petuum的面经题, 一台机器向另一台机器传100G的文件, 硬盘,内存,网络速度均为1GB/s, 内存是10个G,
# 问最短需要多少时间? 说一下我自己的想法: 虽然内存有10g,但是传输受到1g传输速度的限制, 100g 分成100个包,
# 第一个包到达的时间是4s,剩下99个包每隔一秒到达,所以总时间是99+4 s, 但是看地理一些人说是无限接近100s,不太明白为什么.