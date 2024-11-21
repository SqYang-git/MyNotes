# $\rm Texifer$
Updated CST 2024 Nov 21 15:19

下载后用Typora查看效果更佳

[TOC]

------

------

## 基本结构(示例)

```tex
\documentclass[12pt,a4paper]{ctexart}%磅数,纸张大小

\usepackage{geometry}%纸张格式
\geometry{a4paper,scale=0.85}

\usepackage{tikz}%矢量图

\linespread{1.5}%行间距

\usepackage{subfigure}%并排放置图形/表格
\usepackage{booktabs}%创建高质量表格

\usepackage{graphicx}%图片插入
\graphicspath{{graph/}}%给出图片相对路径,需保证"graph"文件夹存在
\usepackage{floatrow}%高级浮动体排列

%导言区

\title{\heiti }%填入文件名
\author{}%填入作者
\date{}%填入日期或\date

\begin{document}
	\maketitle
	\tableofcontents%实验报告不需
	\begin{flushleft}%左对齐环境
	
	
	%正文区
	
	\end{flushleft}
\end{document}
```

------

------

## 正文格式

1. 层级(缩进的良好习惯)

```tex
\part{}%part为文字编号"第一部分"
\chapter{}%chapter为文字编号"第一章"
\section{一级}%section为数字编号"1"
	内容1
	\subsection{二级}
		内容1.1
		\subsubsection{三级}
			内容1.1.1
```

2. 段落
   相邻两行视为同一段,另起一段应空一行或加`\\`
   段落结束可加`\par`
   段间空行可用`\vspace{1cm}\\`
3. 页面
   `\newpage`另起一页
4. 局部特殊字体
   直立`\textup{ }`
   意大利`\textit{ }`
   倾斜`\textsl{ }`
   小型大写`\textsc{ }`
   加宽加粗`\textbf{ }`

------

------

## 插入

1. 插入图片

```tex
\begin{figure}[H]
	\centering
	\includegraphics[width=0.8\linewidth]{1.png}%图形宽度为文本宽度的0.8倍,名称为"1.png"
	\caption{}%输入图片标题
	\label{fig:1}%给图形定义标签,可用"\ref{fig:1}"引用
\end{figure}
```

2. 矢量图$\rm MathCha$,$\rm Inkscape$

3. 表格$\rm Tables Generator$或

```tex
\begin{center}
	%表头
	\toprule
	序号&1&2&3&4&5&6&7&8&9\\
	\midrule
	质量($g$)&199.58&200.07&199.79&199.88&199.84&199.70&199.81&199.63&199.84\\
	\bottomrule
	\end{tabular}
\end{center}
```

4. 列表(无序`itemize`,有序`enumerate`,描述`description`)

```tex
\begin{enumerate}
	\item[(1)]第一点:
	\item[(2)]第二点:
	\item[(3)]第三点:
\end{enumerate}
```

5. 插入公式:行间`$ $`,单行居中`$$ $$`
