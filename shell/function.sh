#!/usr/bin/env bash
# linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。
#函数定义
#[ function ] funname [()]

#{

#    action;

#    [return int;]

#}

echoFunc(){
    echo "this is first function in shell"
}
#echo "-----------函数开始执行---------"
#echoFunc
#echo "-----------函数执行完毕---------"


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

#paramFunc 1 2 3 4 5 6 7 $param
# $10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。
# $#	传递到脚本的参数个数
# $*	以一个单字符串显示所有向脚本传递的参数
# $$	脚本运行的当前进程ID号
# $!	后台运行的最后一个进程的ID号
# $@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
# $-	显示Shell使用的当前选项，与set命令功能相同。
# $?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。


## shell输入/输出重定向
# 标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据。
# 标准输出文件(stdout)：stdout 的文件描述符为1，Unix程序默认向stdout输出数据。
# 标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。
# 默认情况下，command > file 将 stdout 重定向到 file，command < file 将stdin 重定向到 file。
# 表示标准错误文件(stderr)。

# 如果希望将 stdout 和 stderr 合并后重定向到 file，可以这样写：

# $ command > file 2>&1
# 或者
# $ command >> file 2>&1
#

# /dev/null 文件
# 如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null：

# $ command > /dev/null
# /dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。
# 但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

# 如果希望屏蔽 stdout 和 stderr，可以这样写：

# $ command > /dev/null 2>&1

# 0 是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。

who > ./users

read text < ./users
echo $text