#!/bin/bash
echo "Hello World"
your_name="muyuanqiang7"
echo ${your_name}
echo $your_name
echo ${#your_name}
# 提取子串
echo ${your_name:1:4}
# 查找字符串
str="Shell is a great language"
echo ${str}
#echo `expr index "$str" "S"`
array_name=("bob" "Mike" "Lily")
echo ${array_name[0]}
echo ${#array_name[@]}
echo ${#array_name[*]}
echo ${#array_name[1]}
for item in ${array_name[@]}; do
    echo ${item}
done

var="http://www.baidu.com"
echo ${var#*//}