# TapTapCommentCrawler
此仓库包括了TapTap厂商评论和游戏评论的Python爬虫

其中
developer.py是爬取厂商评论
game.py是爬取游戏评论

<hr>

### 注意
1.两个爬虫的代码均为网上查找，然后我再稍作修改，比如developer.py本人就将导出为csv改成导出为json

2.game.py无法中断(也就是会将游戏的所有评论打印完，除了990页以上)如果中断可能不会保存下来(毕竟不能将写入放到循环里面嘛，不然有可能会重复写入或者造成卡顿qwq)

<hr>
2021.4.27
修复了game.py无法自定义页数的问题（虽然没有测试），如果有问题可以在Issues提出
<br>
<br>

### readme统计

<br>

![统计](https://count.getloli.com/get/@misaka10843?theme=elbooru)

