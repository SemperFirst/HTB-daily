Rank: Easy
PHP JWT 
if (!count($json_data) == 2) {
    return $this->respond("Please provide username and password", 404);
}    

Flawed Logic Breakdown逻辑缺陷

count($json_data) returns an integer representing the number of keys in the JSON input (e.g., 2 if username and password are sent).
count($json_data) 返回一个整数，表示 JSON 输入中的键的数量（例如，如果发送了用户名和密码，则为 2）。
The negation operator (!) is applied before the comparison:
比较之前应用否定运算符（！） ：
If count($json_data) is 2:
如果 count($json_data) 为 2：
!2 becomes false!2 变为 false
false == 2 returns false — meaning the check fails to trigger even when username or password is missing
false == 2 返回 false — 意味着即使缺少用户名或密码，检查也无法触发

POC：
json数据删除password字段

修复：
if (count($json_data) != 2) {
    return $this->respond("Please provide username and password", 404);
} 
