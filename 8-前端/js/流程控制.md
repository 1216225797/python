# js流程控制

> 流程控制用于基于不同的条件来执行不同的动作。

### if语句

>if... else ...

>if ... else if ... else...

> 可以单分支,双分支,也可以多分支,需要注意 else if中间必须要有空格

```
if (condition){
    //当条件为 true 时执行的代码
}else{
    //当条件不为 true 时执行的代码
}
```

### switch语句

> 多分支语句： switch（）{。 case ：。。。。}
>
> switch 语句用于基于不同的条件来执行不同的动作。

```
 switch(n){
    case 1:
        //执行代码块 1
        break;
    case 2:
        //执行代码块 2
        break;
    default:
        //与 case 1 和 case 2 不同时执行的代码
}
```

# js循环

> 程序中进行有规律的重复性操作，需要用到循环语句。

> break 和 continue 语句对循环中的代码执行提供了更严格的控制。

### **for循环**

```
for(var i=0;i<len;i++){
    ......
}
```

### **while循环**

```
var i=0;

while(i<8){

    ......

    i++;

}
```

### for-in 语句

> for-in 语句是严格的迭代语句，用于枚举对象的属性。

```
var a = [10,20,30,40,50];
//迭代的是数组的下标。
for(i in a){
   document.write(a[i]);
}
//输出： 1020304050
```

# js元素获取与操作

> 可以使用内置对象document上的getElementById方法来获取页面上设置了id属性的元素，获取到的是一个html对象，然后将它赋值给一个变量，比如：

```
<script type="text/javascript">

    var oDiv = document.getElementById('div1');

</script>

....

<div id="div1">这是一个div元素</div>
```

> 上面的语句，如果把javascript写在元素的上面，就会出错，因为页面上从上往下加载执行的，javascript去页面上获取元素div1的时候，元素div1还没有加载，解决方法有两种：

**第一种方法：将javascript放到页面最下边**

```
....


<div id="div1">这是一个div元素</div>

....

<script type="text/javascript">

    var oDiv = document.getElementById('div1');

</script>
</body>
```

**第二种方法：将javascript语句放到window.onload触发的函数里面,获取元素的语句会在页面加载完后才执行，就不会出错了。**

```
<script type="text/javascript">

    window.onload = function(){
        var oDiv = document.getElementById('div1');
    }

</script>

....

<div id="div1">这是一个div元素</div>
```

## 样式操作

> 标签对象.style.css属性名="值" //改变标签对象的样式。
>
> 示例：id.style.color="red";
>
> 注意：属性名相当于变量名,所以css属性名中含有双拼词的(font-size)的减号要去掉，将后面的首字母大写。fontSize

## 文本操作

> 标签对象.innerHTML="内容"；//在标签对象内放置指定内容
>
> 获取一般用 innerText

## 表单中值的操作

> 标签对象.value； //获取标签对象的value值
>
> 标签对象.value=”值“；//设置标签对象的value值