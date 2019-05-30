# js定时器

通过使用 JavaScript，我们有能力作到在一个设定的时间间隔之后来执行代码，而不是在函数被调用后立即执行。我们称之为计时事件。

**定时器在javascript中的作用**

1、制作动画
2、异步操作

### 定时器类型及语法

> setInterval() - 间隔指定的毫秒数不停地执行指定的代码。

>  setTimeout() - 暂停指定的毫秒数后执行指定的代码 setInterval() 和 setTimeout() 是 Window对象的两个方法。

```
 定时器：
    setTimeout  只执行一次的定时器 
    clearTimeout 关闭只执行一次的定时器
    setInterval  反复执行的定时器
    clearInterval 关闭反复执行的定时器

  var time1 = setTimeout(myalert,2000);
  var time2 = setInterval(myalert,2000);
  /*
  clearTimeout(time1);
  clearInterval(time2);
  */
  function myalert(){
      alert('ok!');
  }
```

# js函数

*第一种是使用function语句定义函数

```
function abc(){
    alert('abc');
}
```

*第二种是在表达式中定义函数

```
var 函数名 = function\(参数1，参数2，…\){函数体};

//例如：

//定义

    var add = function\(a,b\){

        return a+b;

    }

    //调用函数

    document.write\(add\(50,20\)\);
```

### arguments

```
在函数代码中，使用特殊对象 arguments，开发者无需明确指出参数名，就能访问它们。
例如，在函数 sayHi() 中，第一个参数是 message。用 arguments[0] 
也可以访问这个值，即第一个参数的值（第一个参数位于位置 0，
第二个参数位于位置 1，依此类推）。
```

### 关于变量和参数问题：

```
函数外面定义的变量是全局变量，函数内可以直接使用。
在函数内部没有使用var定义的=变量则为全局变量，
*在函数内使用var关键字定义的变量是局部变量，即出了函数外边无法获取。
```