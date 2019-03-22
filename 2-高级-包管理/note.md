# 1.模块
- 一个模块就是一个包含python代码的文件，后缀名是.py就可以，模块就是个python文件
- 用模块的原因：
    - 程序太大,编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 根据模块的规范，最好在模块中编写以下内容：
        - 函数(单一功能)
        - 类(相似功能的组合，或者类似业务模块)
        - 测试代码
- 如何用模块
    - 模块直接导入
        - 加入模块名称直接以数字开头,需要借助importlib帮助
    - 语法：
    
            import module_name
            module_name.function_name
            module_name.class_name
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
    
    - from module_name import func_name, class_name
        - 按上述方法有选择的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
        
    - from module_name import *
        - 导入模块所以内容
- `if __name__ == "main"` 的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所以程序的入口都以此为入口
    
# 2.模块的搜索路径和存储
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
- 添加搜索路径(搜索路径是以列表类型存储)
    
        sys.path.append(dir)

- 模块的加载顺序
    1. 搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path路径


# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式是：
                
                package_name.func_name
                package_name.class_name.func_name()
    - import package_name as p
        - 具体方法跟作用方式，跟上述简单导入一致
        - 注意的是此种方法时默认对__init__.py内容的导入
       
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.fun()
                package.module.class.var
    
    - import package.module as pm
    
 
 - from ... import导入
    - from package import module
    - 此种导入方法不执行__init__的内容
            
            from pkg01 import p01
            p01.sayHello()
    - from package import *
        - 导入当前包__init__.py文件中所有的函数和类
        - 使用方法
        
                func_name()
                class_name.func_name()
                class_name.var
                
 - from package.module import *
    - 导入包中指定的模块的所有内容
    - 使用方法
    
            func_name()
            class_name.func_name()
            

 - 在开发环境中经常会用其他模块，可以在当前包中直接导入其他模块中的内容
    - import完整的包或者模块的路径
 - `__all__` 的用法
    - 在使用from package import * 的时候，* 可以导入的内容
    - `__init__.py`中如果文件为空，或者没有`__all__`,那么只可以把`__init__`中的内容导入
    - `__init__`如果设置了`__all__`的值，那么则按照`__all__`指定的子包或者模块进行加载，
    如此则不会载入`__init__` 中的内容
    - `__all__=['module1', 'module2', 'package1'.......]`
    
 # 命名空间
 - 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
 - 作用是防止命名冲突        
    
    