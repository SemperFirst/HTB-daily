服务器开了ssh端口 postgresql端口关闭

ss -tln

l: Display only listening sockets.
-t: Display TCP sockets.
-n: Do not try to resolve service names.

### **核心区别对比**

| **特性** | **`-L` (本地转发)** | **`-R` (远程转发)** |
| --- | --- | --- |
| **发起方** | 本地机器 | 远程机器 |
| **监听端** | 本地开启端口 | 远程服务器开启端口 |
| **适用场景** | 访问远程内网服务 | 暴露本地服务给外部 |
| **数据终点** | 跳板机后方的目标服务 | SSH客户端所在机器的服务 |
| **典型命令** | **`ssh -L 本地端口:目标:端口`** | **`ssh -R 远程端口:目标:端口`** |

- D 动态转发 + proxychains

### **配置步骤**

1. **编辑配置文件**：复制下载
    
    bash
    
    ```
    sudo nano /etc/proxychains4.conf
    ```
    
2. **关键修改项**：
    - 取消注释 **`strict_chain`**（严格链模式）
    - 注释掉 **`dynamic_chain`** 和 **`random_chain`**
    - 在 **`[ProxyList]`** 底部添加代理设置：复制下载
        
        ini
        
        ```
        socks5  127.0.0.1 1234
        ```
        

### **3. 执行命令**

```
proxychains psql -h 10.10.10.100 -p 5432 -U christine
```
