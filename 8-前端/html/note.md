# 前端课程课件
## 课程介绍

```angular2html
1.HTML           (常用标签          网页的基本结构)
2.CSS            (常用样式          网页的显示效果)
3.JavaScript     (用户交互效果       动态效果)
4.jQuery         (JavaScript库     简化原生js操作)
5.Ajax           (异步数据交互       在页面不刷新的情况下进行数据交互)
6.BootStrap      (前段UI框架        快速搭建静态页面并支持不同设备)
```

## HTML概述

### 一、什么是HTML

HTML 是用来描述网页的一种语言。

> 超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。

> HTML 不是一种编程语言，而是一种标记语言

> 标记语言是一套标记标签 (markup tag)

> HTML 文档包含了HTML 标签及文本内容

>HTML文档也叫做 web 页面

### 二、HTML是干嘛的

> 可以使用 HTML 来建立自己的 WEB 站点，HTML 运行在浏览器上，由浏览器来解析。

### 三、建立HTML文件

- .html
- .htm

### 四、HTML注释

```angular2html
<!--注释内容-->
```

### 五、HTML网页的基本结构

```angular2html
<!DOCTYPE html>      声明为 HTML5 文档
<html>               元素是 HTML 页面的根元素
<head>               元素包含了文档的元（meta）数据
<body>               元素包含了可见的页面内容

```

#### 通用声明 （了解）
HTML5
```angular2html
<!DOCTYPE html>
```

HTML4.01
```angular2html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
```

XHTML1.0
```angular2html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```



### 六、HTML标签结构
HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由尖括号包围的关键词
- HTML 标签通常是成对出现的
- 标签对中的第一个标签是开始标签，第二个标签是结束标签

```angular2html
<开始标签>内容</结束标签>
```

### 七、HTML元素

"HTML 标签" 和 "HTML 元素" 通常都是描述同样的意思.
 一个 HTML 元素包含了开始标签与结束标签

### 八、HTML属性

- HTML 元素可以设置属性
- 属性一般添加在开始标签
- 属性一般以名称/值对的形式出现，比如：name="value"。

**注意：**
- 属性值必须用双引号引起来
- 标签都用小写字母
- 双标签必须要写闭合标签

## HTML常用标签
### 一、HTML常用的块级标签（块级元素）
> 独占一行
#### 有语义的HTML块级元素
> 有默认样式
##### 标题（Heading） 
> 通过H1～H6 标签来定义的.

##### 段落 
>通过标签 p 来定义的.

##### 列表

无序列表 ul,li
> 是一个项目的列表,列项目使用粗体圆点（典型的小黑圆圈）进行标记

有序列表 ol,li
> 也是一个项目的列表，列表项目使用数字进行标记。

自定义列表 dl,dt,dd（了解）

**注意：**
列表项内部可以使用段落、换行符、图片、链接以及其他列表等等。

##### 表格 table,tr,td

table常用属性

- border        边框
- cellpadding   内容距离表框的距离
- cellspacing   单元格和单元格之间的距离
- rowspan       垂直合并（跨行显示）
- colspan       水平合并（跨列显示）
- align        内容水平对齐方式
- valign        内容垂直对齐方式

#### 无意义的块级元素 div

```angular2html
<div> 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示换行。
一般与 CSS 一同使用
<div> 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。
```

### 二、HTML常用的行级标签（行内元素）
不独占一行
### 有语义的行内元素

#### HTML链接 a标签

```angular2html
<a href="链接地址">链接文本</a>
```

target属性，定义被链接的文档在何处显示  _blank 新窗口打开

#### HTML图像

```angular2html
<img src="图片地址" alt="">
```

#### 文本标签
- b标签 i标签 strong标签 em标签

### 无语义的行内元素

- span标签 配合css使用

### 三、常用的实体字符

```angular2html
&gt;&lt;&copy;
```
### 四、表单标签
表单是一个包含表单元素的区域。通过form来定义表单区域
> 通过type属性定义不同类型的表单控件
- text 普通文本输入框
- password 密码输入框
- radio    单选按钮
- checked  多选按钮
- select   下拉框
- file     文件上传选框
- textarea 文本域
- submit   提交按钮
- reset    重置按钮
- hidden   隐藏域，要和表单一起提交的信息

常用属性：
```angular2html
name 属性：表单项名，用于存储内容值
value属性：输入的值
disabled属性：禁用属性
readonly属性：禁用属性
checked属性：选择框指定默认选项
placeholder：提示
```
**注意：**
```angular2html
form 有两个必须存在的属性 action提交地址 metchod提交方式
post:通过request body传参，参数不可见，参数没有大小限制
get:通url进行传参，参数可见，不安全，大小有限制，

如果表单中含有文件上传 
    method提交方式必须为post 
    form中必须有enctype属性
    enctype="multipart/form-data"
```



 
    



