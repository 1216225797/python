# jQuery

> jQuery是一个是免费、开源的javascript库, 也是目前使用最广泛的javascript函数库。
>
> jQuery极大的方便你完成web前段的相关操作,例如节点操作,元素操作,事件绑定,ajax操作, 且解决了大多数的兼容性问题
>
> jQuery的版本分为1.x系列和2.x、3.x系列，1.x系列兼容低版本的浏览器，2.x、3.x系列放弃支持低版本浏览器，目前使用最多的是1.x系列的。
>
> [http://jquery.com/](http://jquery.com/)官方网站

jquery是一个函数库，一个js文件，页面用script标签引入这个js文件就可以使用。

```
<script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>
```

## jquery选择器

**jquery用法思想**
选择某个网页元素，然后对它进行某种操作

**jquery选择器**
jquery选择器可以快速地选择元素，选择规则和css样式相同

### 基础选择器

```
//通过id来获取元素 document.getElementById();
// $('#logo').css('border','solid 2px red');
//通过标签名来获取元素
// $('li').css('background','#369');
//通过class类名获取元素
// $('.w').css('background','#369');
//逗号 并列获取
// $('#logo,#menu').css('background','#369');
//空格 层级获取
// $('#images li').css('background','#369');
```

### 过滤获取

```
//获取第一个和最后一个元素
// $('ul li:first').css('background','#369');
// $('ul li:last').css('background','#369');
//获取指定索引的元素 索引从0开始 
// $('li:eq(7)').css('background','#369');
// $('li').eq(7).css('background','#369');
//获取包含指定文本的元素
// $('li:contains(国)').css('background','#369');
//通过包含指定属性来获取元素 通过属性来获取
// $('li[name=y]').css('background','#369');
```

### 父子关系获取

```
//获取所有的子元素
// $('#images').children().css('background','#369');
//获取第一个子元素
// $('ul li:first-child').css('background','#369');
//获取最后一个子元素
// $('ul li:last-child').css('background','#369');
//获取指定个数的子元素 个数从1开始
// $('ul li:nth-child(3)').css('background','#369');

//获取元素上一个同级元素
// $('#f').prev().css('background','#369');
//获取元素下一个同级元素
// $('#f').next().css('background','#369');
//获取同辈元素 (同辈元素不包含自己)
// $('#f').siblings().css('background','#369');


//获取父级元素
// $('#f').parent().css('background','#369');
//获取先辈级元素
// $('#f').parents('#all').css('border','solid 1px red');

//在父级元素中查找指定的子元素
$('#images').find('.w').css('background','#369');
```

# jQuery元素操作

通过jQuery可以操作控制元素的样式,文本,属性等

## jquery样式操作

**css操作行内样式**

```
// 获取div的样式
$("div").css("width");
$("div").css("color");


//设置div的样式
$("div").css("width","30px");
$("div").css("height","30px");
$("div").css({fontSize:"30px",color:"red"});

```

**特别注意**
选择器获取的多个元素，获取信息获取的是第一个，比如：$("div").css("width")，获取的是第一个div的width。

## 类名class操作

**操作样式类名**

```
$("#div1").addClass("divClass2") //为id为div1的对象追加样式divClass2
$("#div1").removeClass("divClass")  //移除id为div1的对象的class名为divClass的样式
$("#div1").removeClass("divClass divClass2") //移除多个样式
$("#div1").toggleClass("anotherClass") //重复切换anotherClass样式

```

## 文本操作

**1、html() 取出或设置html内容**

```
// 取出html内容

var $htm = $('#div1').html();

// 设置html内容

$('#div1').html('<span>添加文字</span>');

```

**2、text() 取出或设置text内容**

```
// 取出文本内容

var $htm = $('#div1').text();

// 设置文本内容

$('#div1').text('<span>添加文字</span>');

```

## 属性操作

**1、attr() 取出或设置某个属性的值**

```
// 取出图片的地址

var Src = $('#img1').attr('src');

// 设置图片的地址和alt属性

$('#img1').attr({ .src: "test.jpg", alt: "Test Image" });

//也可以用户设置class属性
$('#abc').attr('class','all')

//也可以自定义 属性
$('#abc').attr('love','iloveyou')

```

**2、removeattr()删除属性**

```
$('#abc').removeattr('class')

$('#abc').removeattr('love')
```