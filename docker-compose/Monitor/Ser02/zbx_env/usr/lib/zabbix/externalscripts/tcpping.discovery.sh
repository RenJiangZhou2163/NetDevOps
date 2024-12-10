#!/bin/bash

# 输入参数，即模板宏的值
input=$1

# 初始化JSON对象
json="{\"data\":["

# 分割输入参数，提取DNS名称和IP地址
IFS=';' read -ra ADDR <<< "$input"
for i in "${ADDR[@]}"; do
    IFS=':' read -ra DNS <<< "$i"
    json+="{\"{#TCPPING_SERVER}\":\"${DNS[0]}\",\"{#TCPPING_PORT}\":\"${DNS[1]}\"},"
done

# 删除最后一个逗号，并添加结束括号
json=${json%?}
json+="]}"

# 输出JSON对象
echo $json
