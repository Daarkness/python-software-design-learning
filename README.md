python 软件设计

## 低耦合高内聚

    代码可以多么容易的被改变或者扩展
    两个通用指标
    1 低耦合
        代码之间的依赖程度是否够低
    2  高内聚
        某一类或者某一些功能在一起的程度


### 一 依赖反转

```
高层次的模块不应该依赖于低层次的模块 ，两者都应该依赖于抽象接口
抽象接口不应该依赖于具体实现。而具体实现则应该依赖于抽象接口

```

**python 中可以使用抽象子类的方式实现**

 [改造前代码](./01_dependency_inversion/before.py)   --> [改造后代码](01_dependency_inversion/after.py)

### 二 策略模式

```
一个类的行为或其算法可以在运行时更改。这种类型的设计模式属于行为型模式。
在策略模式中，我们创建表示各种策略的对象和一个行为随着策略对象改变而改变的 context 对象。策略对象改变 context 对象的执行算法。 意图：定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。
```

 [改造前代码](./02_strategy_pattern/before.py)   --> [改造后代码](./02_strategy_pattern/after.py)


### 三 观察者模式
```
观察者模式又叫发布-订阅（Publish-Subscribe）模式 其中的订阅表示这些观察者对象需要向目标对象进行注册，这样目标对象才知道有哪些对象在观察它。发布指的是当目标对象的状态改变时，它就向它所有的观察者对象发布状态更改的消息，以让这些观察者对象知晓。
一个目标对象的观察者对象数量是不固定的，可以随时增加新的观察者对象或取消已有的观察者对象。观察者模式的主要优点就是极大地降低了目标对象和观察者对象间的耦合，二者可以独自地改变和复用，让对系统增加功能或删除功能都很方便。

```
 [改造前代码](./03_observer_pattern/obs_before.py)   --> [改造后代码](./03_observer_pattern/obs_after.py)


### 四 模版方法
```
一个抽象类中，有一个主方法，再定义1…n个方法，可以是抽象的，也可以是实际的方法，定义一个类，继承该抽象类，重写抽象方法，通过调用抽象类，实现对子类的调用。
 

```
 [改造前代码](./04_05_template_pattern/before.py)   --> [改造后代码](./04_05_template_pattern/after.py)


### 五 桥接模式
```
在软件开发时，如果某个类存在两个独立变化的维度，可以运用桥接模式将这两个维度分离出来，使两者可以独立扩展，让系统更加符合“单一职责原则”。
```
 [改造前代码](./04_05_template_pattern/after.py)   --> [改造后代码](./04_05_template_pattern/after_with_bridge.py))


### 六 MVC
```
MVC主要作用是降低了视图与业务逻辑间的双向偶合。
MVC不是一种设计模式，MVC是一种架构模式。是软件体系架构的内容
只在于节藕view和业务之间双向耦合
```
 [改造前代码](./06_mvc/before.py)   --> [改造后代码](./06_mvc/after.py))



### 七 面向对象五大原则
```
1 单一职责原则（Single Responsibility Principle） 每一个类应该专注于做一件事情。
2 开闭原则（Open Close Principle）面向扩展开放，面向修改关闭。
3 里氏替换原则（Liskov Substitution Principle）超类存在的地方，子类是可以替换的。
4 借口隔离（Interface Segregation Principle）应当为客户端提供尽可能小的单独的接口，而不是提供大的总的接口。
5 依赖倒置原则（Dependence Inversion Principle） 实现尽量依赖抽象，不依赖具体实现。

```
- 单一职责原则:[改造前代码](./07_principle/single-responsibility-before.py)   --> [改造后代码](./07_principle/single-responsibility-after.py)
- 开闭原则:[改造前代码](./07_principle/open-closed-before.py)   --> [改造后代码](./07_principle/open-closed-after.py)
- 里氏替换原则: [改造前代码](./07_principle/liskov-substitution-before.py)   --> [改造后代码](./07_principle/liskov-substitution-after.py)
- 接口隔离原则: [改造前代码](./07_principle/interface-segregation-before.py)   --> [改造后代码](./07_principle/interface-segregation-after.py) 
    -->[使用组合改造后代码](./07_principle/interface-segregation-after-comp.py) 
- 依赖倒置原则: [改造前代码]()   --> [改造后代码]()

### 八 依赖反转对比依赖注入
```
依赖反转：抽象接口不应该依赖于具体实现。而具体实现则应该依赖于抽象接口
    是一个原则，设计原则的一部分 解耦合具体的类
依赖注入：如果一个类使用某种类型的对象，并不是让该类负责创建对象，把创建这个类的责任转移给另外一个类
    优点：让代码变得容易测试
```
- 依赖注入:
    ```
    在使用以来注入之前，我们没有办法pay方法编写测试用例
    ```
    [改造前代码](./08_dependency_inversion_dependency_injection/before.py) [改造前测试代码](./08_dependency_inversion_dependency_injection/before_test.py)-->
    [改造后代码](./08_dependency_inversion_dependency_injection/dependency_injection.py) [改造后测试代码](./08_dependency_inversion_dependency_injection/dependency_injection_test.py)

- 依赖反转
    [改造前代码](./08_dependency_inversion_dependency_injection/dependency_injection.py) [改造钱测试代码](./08_dependency_inversion_dependency_injection/dependency_injection_test.py) -->
    [改造后代码](./08_dependency_inversion_dependency_injection/dependency_inversion.py) [改造后测试代码](./08_dependency_inversion_dependency_injection/dependency_inversion_test.py)


### 九 继承还是组合？
```
    当你想提升代码内聚性，可以使用继承，不需要将所有的功能放到一个大的class里面
    但是继承是最大的一种耦合方式
    而组合往往更好，组合的方式可以更灵活，更少的耦合。
```
[改造前代码](./09_composition_inheritance/before.py)  -->[使用继承改造后代码](./09_composition_inheritance/with_inheritance.py)-->
    [使用组合改造后代码](./09_composition_inheritance/with_composition.py)







---
### 关于python相关

### 一 异常处理
```
python 所有的异常都是Exception的子类，整体呈树结构

tips:
    1 不要随意抛出没有意义的异常 如随意抛出  ValueError。
    2 python可以使用finally做额外的工作 如 关闭文件句柄。也可以使用上下文管理器。
    3 在正确的层级处理异常，而不是把异常一直往上层抛出。
    4 python 在运行代码和解释代码都使用异常来报告错误 如果你捕获的是Exception 那么你代码的问题也会被掩盖。只处理你知道该怎么做的错误。 
```
[错误处理](./python_exception_handing/error_handling.py) 

#### python异常处理高级应用

[基于异常处理的重试装饰器](./python_exception_handing/retry-decorator.py) 
[基于异常处理的记录装饰器](./python_exception_handing/logging-decorator.py) 

####  链式错误处理 
[code:链式错误处理](./python_exception_handing/example.py) 



 

### 