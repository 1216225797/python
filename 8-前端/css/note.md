# CSS
```angular2html
为了让网页元素的样式更加丰富，
也为了让网页的内容和样式能拆分开，
CSS由此思想而诞生，
CSS是 Cascading Style Sheets 的首字母缩写，
意思是层叠样式表。
有了CSS，html中大部分表现样式的标签就废弃不用了，
html只负责文档的结构和内容，表现形式完全交给CSS，html文档变得更加简洁。
```

## Css基本语法及页面引用

### css基本语法
> css的定义方法是：
> 选择器 { 属性:值; 属性:值; 属性:值;}
>选择器是将样式和页面元素关联起来的名称，属性是希望设置的样式属性每个属性有一个或多个值。

示例:
```angular2html
div{ width:100px; height:100px; color:red }
```

### css页面引入方法
1、外联式：通过link标签，链接到外部样式表到页面中。
```angular2html
<link rel="stylesheet" type="text/css" href="css/main.css">
```
2、嵌入式：通过style标签，在网页上创建嵌入的样式表。
```angular2html
<style type="text/css">

    div{ width:100px; height:100px; color:red }
    ......

</style>
```
3、内联式：通过标签的style属性，在标签上直接写样式。

```angular2html
<div style="width:100px; height:100px; color:red ">
......
</div>
```

## CSS选择器
常用的选择器有如下几种：

**1、标签选择器**

> 标签选择器，此种选择器影响范围大，建议尽量应用在层级选择器中。

举例:
```angular2html
*{margin:0;padding:0}
div{color:red}   


<div>....</div>   <!-- 对应以上两条样式 -->
<div class="box">....</div>   <!-- 对应以上两条样式 -->
```

**2、id选择器**
>通过id名来选择元素，元素的id名称不能重复，所以一个样式设置项只能对应于页面上一个元素，不能复用，
> id名一般给程序使用，所以不推荐使用id作为选择器。

举例:
```angular2html
#box{color:red} 

<div id="box">....</div>   <!-- 对应以上一条样式，其它元素不允许应用此样式 -->
```
**3、类选择器**

> 通过类名来选择元素，一个类可应用于多个元素，
> 一个元素上也可以使用多个类，应用灵活，可复用，是css中应用最多的一种选择器。

举例:
```angular2html
.red{color:red}
.big{font-size:20px}
.mt10{margin-top:10px} 

<div class="red">....</div>
<h1 class="red big mt10">....</h1>
<p class="red mt10">....</p>
```

**4、层级选择器**

> 主要应用在选择父元素下的子元素，或者子元素下面的子元素，可与标签元素结合使用，减少命名，
> 同时也可以通过层级，防止命名冲突。

举例:
```angular2html
.box span{color:red}
.box .red{color:pink}
.red{color:red}

<div class="box">
    <span>....</span>
    <a href="#" class="red">....</a>
</div>

<h3 class="red">....</h3>
```

**5、组选择器**

> 多个选择器，如果有同样的样式设置，可以使用组选择器。也成为 并列选择

举例:
```angular2html
.box1,.box2,.box3{width:100px;height:100px}
.box1{background:red}
.box2{background:pink}
.box2{background:gold}

<div class="box1">....</div>
<div class="box2">....</div>
<div class="box3">....</div>
```

**6、伪类及伪元素选择器**

> 常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，
> 伪元素选择器有before和after,它们可以通过样式在元素中插入内容。

```angular2html
.box1:hover{color:red}

<div class="box1">....</div>

a:hover {color: #FF00FF; text-decoration: underline} /* 鼠标在该元素上时 */


a:before{content:"Hello";}         /*在每个<a>元素之前插入内容*/
a:after{content:"world";}        /*在每个<a>元素之后插入内容*/
```