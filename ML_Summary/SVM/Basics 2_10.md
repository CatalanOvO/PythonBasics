十大SVM核心公式



#### 1. Linear SVM

1. **介绍**

   - 用于分类线性可分的数据，通过构建一个决策超平面将不同类的数据点分开

2. **特点：**

   - 适用于数据线性可分的情况
   - 构造最优决策边界，最大化类间距离

3. **公式：**

   假设训练数据 $(x_{i},y_{i}),i=1,\cdots,n,\space x_{i} \in\mathbb{R}^{d},y_{i} \in \{ -1,1 \}$

   - 决策函数：$f(x)=w \cdot x+b$
   - 目标函数： $\mathop{min}\limits_{w,b} \space \frac{1}{2} ||w|| ^{2}$
   - 约束条件： $y_{i}(w \cdot x_{i}+b) \geq 1, \forall i$

4. **推导：**

   通过拉格朗日乘数法：

   - 拉格朗日函数：$L(w,b,\alpha)=\frac{1}{2}||w||^{2}-\sum\limits_{i=1}^{n}\alpha_{i} [y_{i}(w_{i}\cdot x_{i}+b) -1]$

   - 对偶问题： $\mathop{max}\limits_{\alpha}\sum\limits_{i=1}^{n}\alpha_{i}- \frac{1}{2}\sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} \alpha_i \alpha_{j}y_{i}y_{j}x_{i}x_{j}, \space subject \space to \sum\limits_{i=1}^{n}\alpha_{i}y_{i}=0$ 

   - 最优 $w$ 和 $b$： $w=\sum\limits_{i=1}^{n}\alpha_{i}y_{i}x_{i}$

     ​			$b = y_{k} - w \cdot x_{k}, \space for \space any \space support \space vector x_{k}$



#### 2.Non-linear SVM

1. 介绍：

   - 处理非线性可分的数据，通过核函数将数据映射到高维空间

2. 特点：

   - 适用于复杂的非线性数据

   - 依赖核函数将低维数据映射到高维

3. 公式：

   使用核函数 $\kappa(x_{i},x_{j})$

   - 决策函数：$f(x)=\sum\limits_{i=1}^{n}\alpha_{i}y_{i}\kappa(x_{i},x)+b$
   - 目标函数：$\mathop{max}\limits_{i=1}^{n} \sum\limits_{i=1}^{n} \alpha_{i}- \frac{1}{2}\sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} \alpha_i \alpha_{j}y_{i}y_{j} \kappa(x_{i},x_{j})$
   - 约束条件： $\sum\limits_{i=1}^{n}\alpha_{i}y_{i}=0, \space 0 \leq \alpha_i \leq C, \space \forall i$

4. 推导：

   通过核技巧替代直接计算：

   - 拉格朗日对偶形式中，将内积替换为核函数$\kappa(x_i,y_i)$
   - 决策边界在高维特征空间内求得，降低直接计算的复杂性