# Css颜色,文本字体

## css颜色表示法
1.颜色名表示，比如：red 红色，gold 金色

2.16进制数值表示，比如：#ff0000 表示红色，这种可以简写成 #f00

3.RGB颜色: 红(R)、绿(G)、蓝(B)三个颜色通道的变化 background-color: rgb(200,100,0);

4.RGBA颜色: 红(R)、绿(G)、蓝(B)、透明度(A) background-color: rgba(0,0,0,0.5);

```angular2html
16进制  0-9 a-f
rgb的值 0-255
```

## css文本设置
常用的应用文本的css样式：

```angular2html
color 设置文字的颜色，如： color:red;
font-size 设置文字的大小，如：font-size:12px;
font-family 设置文字的字体，如：font-family:'微软雅黑';
font-style 设置字体是否倾斜，如：font-style:'normal'; 设置不倾斜，font-style:'italic';设置文字倾斜
font-weight 设置文字是否加粗，如：font-weight:bold; 设置加粗 font-weight:normal 设置不加粗

line-height 设置文字的行高，如：line-height:24px;
text-decoration 设置文字的下划线，如：text-decoration:none; 将文字下划线去掉
text-indent 设置文字首行缩进，如：text-indent:24px; 设置文字首行缩进24px
text-align 设置文字水平对齐方式，如text-align:center 设置文字水平居中
```

## css边框属性
```angular2html
border:宽度 样式 颜色;
border-color;
border-style; 边框样式：solid实线，dotted点状线，dashed虚线
border-width:
border-left-color;
border-left-style;
border-left-width:
CSS3的样式
border-radius：圆角处理
box-shadow: x轴偏移 y轴偏移 模糊度 扩散程度 颜色 inset内阴影 设置或检索对象阴影
```

## 背景属性
```angular2html
*background-color: 背景颜色
*background-image: 背景图片
*background-repeat：是否重复，如何重复?(平铺)
*background-position：定位

css3的属性                
*background-size: 背景大小，如 background-size:100px 140px;
```

## 元素溢出
当子元素的尺寸超过父元素的尺寸时，需要设置父元素显示溢出的子元素的方式，设置的方法是通过overflow属性来设置。

**overflow的设置项：**
```angular2html
1.visible 默认值。内容不会被修剪，会呈现在元素框之外。
2.hidden 内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷的功能。
3.scroll 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
4.auto 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
```



