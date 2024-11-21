## Cheet Sheet

------

### 一、杂的知识点

**debug**
RTE:数组越界/除0;TLE/MLE:程序错误(例如递归未设置边界)/复杂度过高(list$\to$dict;使用高效算法)

**浅拷贝** 声明二维数组时,浅拷贝会导致所有行引用同一个列表,从而修改一个元素时牵连影响.建议列表推导式创建列表.

```python
matrix[0][0] = 1
print(matrix)  # 输出: [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
m = 3; n = 4  # 列表推导式
matrix = [[0 for _ in range(n)] for _ in range(m)]
print(matrix)  # 输出: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

`map(func, *iterables)`:将函数应⽤于传⼊的每个可迭代对象的各个元素

**列表操作** `len()`;`.append()`;`.extend()`;`.insert()`;`.sort()`
`.pop()`从列表中移除元素,并返回指定元素的值`list1.pop()`,可以`print`出来.

**字符串操作** `.replace()`;`.split()`;`.strip()`移除首位指定字符,默认为空格/换行;`.join()`(将序列中元素以指定字符串连接)

**组合数据类型操作** 
`seen=set()`创建无序列不重复元素集合,可用于进行关系测试.
e.g."无重复序列的最长字符串"`seen.add(s[r])`,`seen.remove(s[l])`.
`dict()`创建字典

**解包输出** 例如对矩阵`list[[]]`,输出则对每一行`line`用`print(*line)`

**F-string** `f"{sum1:.2f}"`

`list`结果分行输出:`print("\n".join(list))`(也可用于加空格输出)

生成列表/元组/字符串的枚举对象`enumerate`,输出几组`index, item`.欲对`item`排列,需转化为新列表:

```python
indexed_list1 = list(enumerate(list1))
indexed_list1.sort(key=lambda x: x[1], reverse = True)  # False升序,True降序

skills.sort(key=lambda x: (x[0], -x[1]))
```

对要求以空行为判定输入结束的依据的,加`input()`即可

------

### 二、dp



------

### 三、greedy



------

### 四、math

绝对值`abs()`;幂函数`pow(x, y)`:$x^y$.二进制`bin`(binary),从编号为`2`(第三个字符)开始才是结果

除后取整:向下`num // n`,向上`(num + n - 1) // n  `

`math.ceil(number)`向上取整,`math.floor(number)`向下取整,`math.trunc(number)`截断取整(去掉小数位数)

$\rm Euler$筛法(以列表查找的形式为例,截至`10 ** 6`)

```python
is_prime = [True] * 1000001
for i in range(2, int(1000000 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1000001, i):
            is_prime[j] = False
```

------

### 五、sortings



------

### 六、recursion



------

### 七、two pointers



------

### 八、matrix

滑动窗口求极值:创建大窗口--根据输入对对应点周围"检查窗口"可作用的范围赋值(注意大窗口边界)---初始化极值及其数量--遍历,同则加数量,大则赋值给极值,重置数量

> 易错点:未将输入值`-=1`转化为以0开始记数的表格里的位置;数组越界;直径/半径

------

### 九、searching

图(包括矩阵,迷宫,树)搜索包括:
DFS:枚举所有完整路径以遍历所有情况;优先使用递归实现,岔道口即递归式,死胡同即递归边界(本质还是栈)

> 注意加保护圈,或调用判断函数

BFS:
```python
from collections import deque  
# double-ended queue,一种list-like的容器,适用于需频繁从队列两端进行操作,支持append,popleft,extend等
def bfs(start, end):
    queue = deque([(0, start)])  # 定义队列queue,起点元组(step, start)入队,目前步长step = 0
    in_queue = {start}   # 记录已入队节点(而非已被访问的节点)
    while queue:  # 如果queue非空
        step, front = queue.popleft() # 取出队首元素
        if front == end:
            return step # 返回需要的结果，如：步长、路径等信息

        # 将 front 的下一层结点中未曾入队的结点全部入队q，并加入集合in_queue设置为已入队
```

1. 定义队列`queue`,起点`(0, start)`入队,目前步长为`0`
2. `while`循环,条件是队列`queue`非空
3. `while`循环中,取出队首元素`front`
4. 将`front`的下一层结点中未曾入队的结点入队,标记他们的层号为`step`的层号加`1`并加入`in_queue`
5. 返回第二步继续循环

> `in_queue`用来判断节点是否已经入队,而不是节点是否已经被访问.
> 若设置成是否被访问,可能由于其他节点可以到达正在队列中的某节点(未被访问)而将其反复入队,大大增加算量.

