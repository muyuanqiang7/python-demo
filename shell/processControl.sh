#!/usr/bin/env bash
# shell 流程控制
# 和Java、PHP等语言不一样，sh的流程控制不可为空
#   if condition
#   then
#        command1
#        command2
#        ...
#        commandN
#   fi

# if-else
#    if condition
#    then
#        command1
#        command2
#        ...
#        commandN
#    else
#        command
#    fi

a=10
b=20
if [ $a == $b ]; then
    echo "a==b"
elif [ $a -gt $b ]; then
    echo "a > b"
elif [ $a -lt $b ]; then
    echo "a < b"
else
    echo "没有符合的条件"
fi

num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi

# for循环
#   for var in item1 item2 ... itemN
#   do
#       command1
#       command2
#       ...
#       commandN
#   done

for loop in 1 2 3 4 5;do
    echo "current value is: $loop"
done
# while
#   while condition
#   do
#       command
#   done
# 使用中使用了 Bash let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量
int=1
while (( $int<=5 )); do
    echo "current int is $int"
    let "int++"
done

# until
# until循环执行一系列命令直至条件为真时停止。

# until循环与while循环在处理方式上刚好相反。

# 一般while循环优于until循环，但在某些时候—也只是极少数情况下，until循环更加有用。


# case
# Shell case语句为多选择语句。可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。case语句格式如
#    case 值 in
#    模式1)
#        command1
#        command2
#        ...
#        commandN
#        ;;
#    模式2）
#        command1
#        command2
#        ...
#        commandN
#        ;;
#    esac
echo "请输入1-4之间的数字"
echo "你输入的数字是:"
read num

case $num in
    1)
        echo "你输入了1"
        ;;
    2)
        echo "你输入了2"
        ;;
    3)
        echo "你输入了3"
        ;;
    4)
        echo "你输入了4"
        ;;
    *)
        echo "你没有输入1-4之间的数字"
        ;;
esac

while :
do
    echo "请输入1-5之间的数字"
    echo "你输入的数字是:"
    read number
    case $number in
        1|2|3|4|5)
            echo "你输入的数字是 $number"
            ;;
         *)
            echo "你输入了非1-5之间的数字, error: $number"
            break
            ;;
    esac
done