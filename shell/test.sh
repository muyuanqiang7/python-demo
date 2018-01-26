#!/usr/bin/env bash
# test command
# Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。
num1=100
num2=200
if test $num1 -eq $num2; then
    printf "num1 等于 num2\n"
else
    printf "num1 不等于 num2\n"
fi

# 代码中的 [] 执行基本的算数运算
result=$[num1+num2]
printf "result is: $result\n"

str1="Google"
str2="Apple"
if test $str1 == $str2; then
    echo "str1 == str2"
else 
    echo "str1 != str2"
fi

if test [-z $num1]; then
    echo "字符串长度为0"
else
    echo "字符串长度不为0"
fi
# 文件测试 查看variable.sh
