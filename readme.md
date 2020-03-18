# <center> 小学数学题出题工具 </center>

> 疫情期间，为了帮助小孩子学习数学，作为程序员老爹为了不手写出题准备写个小工具。不过在动手之前还是上GitHub上查了一下，发现有着相同经历的人已经走在了前面。既然有轮子了就拿来用好了，不过当前开源的作者用的界面库不是我熟悉的，而且在Mac OS Mojave上显示有问题。因为我比较熟悉Qt，加上想学习一下PyQt的使用，特拿此项目用PyQt重新做下界面，顺便学习一下。如果有正在学习PyQt的可以加入一起学习。
>
> 核心算法没有更改，只是在调用方面稍作了修改，其中有一些bug需要解决。
>
> 感谢原作者。https://github.com/bosichong/PrimarySchoolMathematics.git



## 一、 环境

- Python 3.6+

## 二、 编译执行

- 安装依赖库

```
pip install -r requirements.txt
```

- 执行

```
python main.py
```



## 三、 待解决问题

1. 题目重复问题
2. 在去重之后，无法获取足够的题目数，导致程序卡死