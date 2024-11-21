# SciDavis笔记

[TOC]

------

## 批量导入数据

```txt
#第一行不可记录数据,可以记录变量名称,用Space或TAB
时间	水平	竖直
0.0	0.0	0.0
0.1	1.0	1.0
0.2	2.0	4.0
```

导入:View--Results Log--Import ASCII File(s)--选取.txt文件--在Separator中选择TAB--点击Open导入

------

## 表格的编辑和运算

新建列表:File--New-- New Table

| 1[X] | 2[Y] | #数据名[用于哪个轴]<br />#改变数轴:右键--$\text{Set Column(s) As}$ |
| :--: | :--: | :----------------------------------------------------------: |
|      |      |                                                              |
|      |      |                                                              |

删除表格并自动补齐:选中--右键--Remove Rows
清除表格中的数据:选中--右键--Clear Rows
添加列:右键空白区域--Add Column
添加行:右键末行--Add Rows
插入行:右键前一行--Insert Empty Rows

设置数据格式:Type
Type:Numeric(数据),Text(文本)
Format:Demical(小数型),Scientific(科学技术法型),Automatic自动判断
Decimal Digits:小数位数
(更改后需Apply)

表格运算:选中列--Formula--选择col("变量名")--Add--选择运算方式/手动输入--Add

------

## 数据拟合

**直线拟合**
作拟合图:选中数据--Plot--Scatter散点图--选中图像--Analysis--Quick Fit --Fit Linear
显示拟合结果:View--Results Log

**多项式曲线拟合**
作拟合图:选中数据--Plot--Scatter散点图--选中图像--Analysis--Quick Fit --Fit Polynomial--Order输入最高次数(1-9)

**普通曲线拟合**
作拟合图:选中数据--Plot--Scatter散点图--选中图像--Analysis--Quick Fit --Fit Wizard--Basic选择要做的计算或在框内手动输入解析式--Parameters输入未知系数--Fit$\times2$

------

## 坐标轴编辑

**编辑坐标轴**:双击
Scale:
From最小To最大
Minor Ticks分度值标签(大格中小格数目)
Axis:
勾选Show显示坐标轴
选中左侧位置列表可修改各处图注Title及其文字格式Font
后面从左到右为下标,上标,四类特殊符号,加粗,斜体,下划线
Type选择标注数据类型(一般Numeric),坐标轴数字格式Font,调整坐标轴颜色Color,调整坐标轴刻度显示位置Major/Minor Ticks(分别为大/小格,None不显示,可用于制作图框,In在图内,Out在图外)
勾选Show Labels显示标签内容,Format标签数据类型,Angle调整标注旋转角度,Color更改标注颜色

**编辑曲线**:双击
Symbol:
Style选择点的形状,Size更改点的大小
Line:
Line Type线型
Axes:
选择数据对应的坐标轴

**双Y轴曲线**:在Axes中,两数据分别对应Left和Right--Axis中,显示Right

------

## 添加误差棒

准备好对应的误差数据记录,选中
点击图像窗口--Graph--Add Error Bars--Add Error Bars To选择对象
Existing column选择误差对应的原数据
窗口底测选择误差棒方向,点击Add添加
Percent of data改为输入相对误差

------

## 图像标注

选中--Graph
Add Text添加文本--Active Layer
Draw Arrow箭头标注--左键添加箭头(仅仅是箭头)--右键编辑,Delete删除
Draw Line画线--点击,右键,Properties编辑线段格式,加箭头
