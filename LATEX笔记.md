#  $\rm LATEX$(主要$\rm Markdown$中)
Updated CST 2024 Nov 21 15:19

下载后用Typora查看效果更佳

[TOC]

------

------

## 公式插入

1. 行内公式:\$公式\$
   为展现出行间公式效果,式子前加`\displaystyle`
2. 行间公式
   \\[
   公式
   \\\]
3. 公式块:$$ Return

------

------

## 格式

1. 多行公式:
   多行环境:首行`\begin{align}`(尾同)
   换行:默认右对齐,令某处对齐时前加&
2. 大括号(分情况):
   首行`\begin{cases}`(尾同)
   `\\`换行;令条件对齐加`&`
3. 方阵:首行`\begin{matrix}`(尾同)(用`&`对齐)
   `matrix`无括号;`bmatrix`方括号;`pmatrix`圆括号;`vmatrix`竖线
4. 省略号:`\cdots`($\cdots$),`\vdots`($\vdots$),`\ddots`($\ddots$)
5. 括号与定界符:
   `()`,`[]`正常敲出;`{}`在$LATEX$中无法正常输出,前加`\`即可
   `\lceil`($\lceil$),`\rceil`($\rceil$),`\lfloor`($\lfloor$),`\rfloor`($\rfloor$)
   Ps:可通过在左括号前加`\left`来达到高度自适应,右同;对于某处求导等情况,其竖线无对应左括号,可引入`\left.` 为"虚拟括号"
6. 空格:
   `\,`小`\space`中`\quad`大(q的个数决定间隔大小)

------

------

## 字体

1. 书法`\mathcal`
   手迹`\mathscr `
2. 粗体`\bf`
   如转置矩阵:`\bf A^{\rm T}`($\bf A^{\rm T}$)
3. 斜体→变量
   直立体(罗马体)→文本:`\rm{ }`或`\text{ }`
   Ps:`\text{ }`支持空格;`\text `只对后面的第一个符号起作用(减少`\rm` 作用范围可用`{ }`括住指令与作用部分),于是:
    Suggestion:用`\text{ }`敲出直立体
4. 粗斜体(矢量):`\boldsymbol`

------

------

## 特殊符号

1. 希腊字母(大写则首字母大写):
   `\alpha`($\alpha$/$\Alpha$),`\beta`($\beta$/$\Beta$),`\gamma`($\gamma$/$\Gamma$),`\delta`($\delta$/$\Delta$),`\epsilon`($\epsilon$/$\Epsilon$),`\zeta`($\zeta$/$\Zeta$),`\eta`($\eta$/$\Eta$),`\theta`($\theta$/$\Theta$),`\iota`($\iota$/$\Iota$),`\kappa`($\kappa$/$\Kappa$),`\lambda`($\lambda$/$\Lambda$),`\mu`($\mu$/$\Mu$),`\nu`($\nu$/$\Nu$),`\xi`($\xi$/$\Xi$),`\omicron`($\omicron$/$\Omicron$),`\pi`($\pi$/$\Pi$),`\rho`($\rho$/$\Rho$),`\sigma`($\sigma$/$\Sigma$),`\tau`($\tau$/$\Tau$),`\upsilon`($\upsilon$/$\Upsilon$),`\phi`($\phi$/$\Phi$),`\chi`($\chi$/$\Chi$),`\psi`($\psi$/$\Psi$),`\omega`($\omega$/$\Omega$)
   Ps:变体希腊字母:`\var `($\varGamma$,$\varDelta$,$\vartheta$,$\varTheta$,$\varLambda$,$\varXi$,$\varpi$,$\varPi$,$\varsigma$,$\varSigma$,$\varUpsilon$,$\varphi$,$\varPhi$,$\varPsi$,$\varOmega$均支持)
2. 数集:`\varnothing`($\varnothing$),`\R`($\R$,$\Q\N\Z$同)
   Ps:也可使用`\mathbb`来输入其他的双线字符
3. 其它:`\infty`($\infty$),`\partial`($\partial$),`\propto`($\propto$),`\degree`($\degree$)
4. `\textbackslash`($\textbackslash$)

------

------

## 运算符号

1. 普通运算符:`+`,`-`,`\times`($\times$),`\cdot`($\cdot$),`\div`($\div$),`\pm`($\pm$),`\mp`($\mp$)
   等式:`=`,`<`,`>`,`\ge`($\ge$),`\le`($\le$),`\gg`($\gg$),`\ll`($\ll$),`\ne`($\ne$),`\approx`($\approx$),`\equiv`($\equiv$)
2. 分数:`\frac{ }{ }`
   嵌套分式:通过使用`\dfrac`使嵌套部分表观字号更大(latex不可用)
3. 根式:`\sqrt[n]{ }`($\sqrt[n]{x}$)
4. 关系运算符:
   `\cap`($\cap$),`\cup`($\cup$),`\in`($\in$),`\notin`($\notin$),`\subseteq`($\subseteq$),`\subsetneq`($\subsetneq$),`\forall`($\forall$),`\exists`($\exists$),`\nexists`($\nexists$),`\because`($\because$),`\therefore`($\therefore$)
5. `\sin`(三角,双曲同),`\log_a x`,`\lim_{x\to0}`,`\max`,`\min`
6. 大型运算符:
   求和`\sum_{i=a}^b`(处于分式中时可用`\limits`强行放至求和号下方)
   求积:`\prod_{i=a}^{b}`
   积分:`\int_{a}^{b}`(`i`的个数决定积分重数),环路`\oint`
   ($\,\text dx$的格式应为`\,\text dx`从而使`d`直立且前有间隔)
7. `\circ`($\circ$),`\otimes`($\otimes$)

------

------

## 符号修饰

1. 上标:`^{text}`;下标:`_{text}`
   向量:`\vec`;`\overrightarrow{ }`更多字符
   横线:`\bar`;`\overline{ }`更多字符
   算符:`\hat`;`\overhat{ }`更多字符
    埃:`\mathring`
   复数:`\tilde`
   导数:`\dot`(`d`的个数决定阶数)
2. 箭头:(双线则首字母大写)(更长则前加`long`)
   `\leftarrow`($\leftarrow$,右上下同)
   `\leftrightarrow`($\leftrightarrow$,上下同)
   `\nearrow`($\nearrow$,`se`,`sw`,`nw`同)
   `\hookleftarrow`($\hookleftarrow$,右同),`\mapsto`($\mapsto$)
   `\leftharpoonup`($\leftharpoonup$,右下同),`\rightleftharpoons`($\rightleftharpoons$)
3. 箭头上加字符`\stackrel{}{\longrightarrow}`
