### Complex-Network

## 在第一部分首先构造一个复杂网络模型
#思路：
攻击、图生成模块全部迁移到服务器上来
每一次针对图攻击之后才对图进行异步更新，避免反复刷新造成性能下降以及效果崩溃
删除的结点在图中换颜色？

折线图实时更新
折线图数据放大1000倍，因为无法显示小数

解决问题一：
迁移到服务器

解决问题二：
Category
对于前端的图：不删除结点，改变category

解决问题三：
折线图显示正确？

解决问题四：
攻击模式的选择：放到服务器上做借助前后端交互