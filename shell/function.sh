#!/usr/bin/env bash
# linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。
#函数定义
#[ function ] funname [()]

#{

#    action;

#    [return int;]

#}

echoFunc(){
    echo "this is first funcrion in shell"
}
echo "-----------函数开始执行---------"
echoFunc
echo "-----------函数执行完毕---------"


returnFunc(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read num1
    echo "输入第二个数字: "
    read num2
    echo "两个数字分别为 $num1 和 $num2 !"
    return $(($num1+$num2))
}

#returnFunc
# 函数返回值在调用该函数后通过 $? 来获得
#echo "输入的两个数字之和为 $? !"

param=10
# 函数参数传递
paramFunc(){
    echo "第一个参数 $1"
    echo "第二个参数 $2"
    echo "第三个参数 $3"
    echo "第四个参数 $4"
    echo "第五个参数 $5"
    echo "第六个参数 $6"
    echo "第七个参数 $7"
    echo "第八个参数 $8"
}

paramFunc 1 2 3 4 5 6 7 $param
# $10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。
# $#	传递到脚本的参数个数
# $*	以一个单字符串显示所有向脚本传递的参数
# $$	脚本运行的当前进程ID号
# $!	后台运行的最后一个进程的ID号
# $@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
# $-	显示Shell使用的当前选项，与set命令功能相同。
# $?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。


## shell输入/输出重定向

