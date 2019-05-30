# JavaScript 基本数据类型

typeof函数获取一个变量的类型：

```angularjs
* boolean - 如果变量是 Boolean 类型的
* number - 如果变量是 Number 类型的 (整数、浮点数)
* string - 如果变量是 String 类型的 （采用""、 ''）
* object - 如果变量是一种引用类型或 Null 类型的 
        如：new Array()/ new String()...
* function -- 函数类型
* undefined - 如果变量是 Undefined 类型的
```

# js数据类型转换
使用：Number（）、parseInt() 和parseFloat（） 做类型转换
```angularjs
Number()强转一个数值(包含整数和浮点数)。

*parseInt()强转整数，

*parseFloat（）强转浮点数
```

函数isNaN()检测参数是否不是一个数字。
```angularjs
isNaN()  is not a number
```

可用的 3 种强制类型转换如下：

```angularjs
Boolean(value) - 把给定的值转换成 Boolean 型；

Number(value) - 把给定的值转换成数字（可以是整数或浮点数）；

String(value) - 把给定的值转换成字符串；
```

# js运算符

算术运算符

```angularjs
 + - * / ++ --
```
字符串连接
```angularjs
 +
```
赋值运算
```angularjs
 =    +=   -=   %=
```
比较运算符
```angularjs
<  >    >=    <=    ==    ===   !=   !==
```
逻辑运算符
```angularjs
 &&  ||  !
```
位运算
```angularjs
 ^    &    |   <<   >>
```
其它运算符
```angularjs
?   :    三元运算符
```