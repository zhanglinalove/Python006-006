#### 作业1:  



**作业说明:**

本次作业的实现方式，是参考了该文章http://www.cppcns.com/jiaoben/python/283521.html 模仿实现的



**实现前期遇到了很多问题:**

①设计的目标不明确

②Socket相关的方法非常不熟悉，不知道如何下手

③报错以后，不知道具体原因无法解决



**最终解决方案:**

①在网络上寻找答案，理解设计思路与方法

②模仿代码的书写方式

③理解之后，对于其中的不合理的地方，进行了调整

④报错实现找不出答案的时候，咨询了老师

⑤BrokenPipeError: [Errno 32] Broken pipe 的报错，主要是服务端、或者是客户端一端掉线了





#### 作业2:



作业实现功能:使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。



其余说明:

本次提交的作业，并没有实现，模拟知乎登录手机登录的功能。仅实现了作为游客，进行数据抓取的功能

后期仍然需要优化的2点:

①模拟知乎登录后，然后进行数据抓取【我的账号，仅支持，手机发送验证码的登录方式】

②爬取全部数据的时候，可采用多线程的方式

③代码后期需要进行调优





老师给的几点建议，使用

①要解决的是cookie问题，而知乎post用户密码是加密的可以采用调用知乎的js加密密码提交，也可以采用selenium模拟浏览器登陆成功一次拿到cookie再继续用requests做自动化操作，其他大家可以讨论

②关于JS加密密码提交方式，参考：知乎的js加密密码提交，老师能否再解释的仔细一点呢。

[老师提供的知乎JS加密方式登录的解决方案](https://www.zhihu.com/tardis/sogou/art/32898234?ab_signature=CiRBUEJneXFtV3ZROUxCZThtLXZ2M2VmcV9YZ0k3Znczclcwaz0SIDU1MWQ0YzllY2JjNDE3ZmMxYWJmMDk5NzU5NmE4ZWZiGhAIARIGNi42OS4xGgQzNDYw)