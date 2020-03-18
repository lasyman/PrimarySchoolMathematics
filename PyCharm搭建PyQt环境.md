# <center> PyCharm搭建PyQt环境 </center>

> PyQt目前有PyQt4和PyQt5两个版本。本文使用最新的PyQt5



## 一、运行环境

Python 3.6+



## 二、安装PyQt5

安装PyQt5需要的库

```shell
pip install PyQt5
pip install pyqt5-tools
```

## 三、PyCharm配置PyQt5

1. 打开PyCharm的设置界面，找到Tools下面的External Tools，添加如下两个工具，具体添加如下2. 3：

![](http://pics.wanjiabc.cn/pyqt5_1.png)

2. 添加Qt Designer工具

   此工具主要为了绘制UI使用，如果你本机安装有Qt环境，直接打开Designer绘制也可以。

   ![](http://pics.wanjiabc.cn/pyqt5_2.png)

Program参数选择你pyqt5-tools安装的位置，此处我的路径如下:

`D:\Program Files\Python\Python36\Lib\site-packages\pyqt5_tools\designer.exe `

3. 添加PyUIC

   这个工具比较重要，是为了把Qt的ui文件转换为py文件的

   ![](http://pics.wanjiabc.cn/pyqt5_3.png)

Program: python的执行路径

`D:\Program Files\Python\Python36\python.exe`

Arguments:

`-m PyQt5.uic.pyuic  $FileName$ -o ui_$FileNameWithoutExtension$.py`

Working directory:

`$FileDir$`

## 四、使用PyUIC编译ui文件

点击要编译的ui文件，右键在External Tools选择PyUIC，则会转换ui文件为py文件，生成在ui所在目录，文件以ui_开头。如下图：

![](http://pics.wanjiabc.cn/pyqt5_4.png)