#!/usr/bin/env bash
echo "传递参数"

echo "执行文件名为 $0"
echo "第一个参数为 $1"
echo "第二个参数为 $2"

array_name=(A B "C" D)
echo ${array_name[*]}
echo ${array_name[@]}

var=`expr 2 + 2`
echo $var
ach_gs=2.1
ach_gs_max=3
x=$(echo "scale = 3; $ach_gs * 100 / $ach_gs_max" | bc)
echo $x

a=20
b=10

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"
# 关系运算符
if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi
if true; then
    echo "if-fi"
fi

if [ $a -eq $b ]; then
    echo "a==b"
fi

if [ $a -ne $b ]; then
    echo "a != b"
fi

if [ $a -gt $b ]; then
    echo "a > b"
fi
if [ $a -lt $b ]; then
    echo "a < b"
fi
if [ $a -ge $b ]; then
    echo "a >= b"
fi
if [ $a -le $b ]; then
    echo "a <= b"
fi
# 布尔运算符
# !	    非运算，表达式为 true 则返回 false，否则返回 true。
# -o	或运算，有一个表达式为 true 则返回 true。
# -a	与运算，两个表达式都为 true 才返回 true。
if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a != $b: a 等于 b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a 小于 100 且 $b 大于 15 : 返回 true"
else
   echo "$a 小于 100 且 $b 大于 15 : 返回 false"
fi
if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a 小于 100 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 100 或 $b 大于 100 : 返回 false"
fi
if [ $a -lt 5 -o $b -gt 100 ]
then
   echo "$a 小于 5 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 5 或 $b 大于 100 : 返回 false"
fi
# 逻辑运算符
# && 与
# || 或
if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi
# 取反
if [[ !($a -lt 100 || $b -gt 100) ]]
then
   echo "返回 true---------------"
else
   echo "返回 false--------------"
fi
# 字符串运算符
a="abc"
b="efg"

if [ $a = $b ]
then
   echo "$a = $b : a 等于 b"
else
   echo "$a = $b: a 不等于 b"
fi
if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a != $b: a 等于 b"
fi
if [ -z $a ]
then
   echo "-z $a : 字符串长度为 0"
else
   echo "-z $a : 字符串长度不为 0"
fi
if [ -n $a ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
if [ $a ]
then
   echo "$a : 字符串不为空"
else
   echo "$a : 字符串为空"
fi

##文件测试运算符
# -b file	检测文件是否是块设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
# -c file	检测文件是否是字符设备文件，如果是，则返回 true。	[ -c $file ] 返回 false。
# -d file	检测文件是否是目录，如果是，则返回 true。	[ -d $file ] 返回 false。
# -f file	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
# -g file	检测文件是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
# -k file	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
# -p file	检测文件是否是有名管道，如果是，则返回 true。	[ -p $file ] 返回 false。
# -u file	检测文件是否设置了 SUID 位，如果是，则返回 true。	[ -u $file ] 返回 false。
# -r file	检测文件是否可读，如果是，则返回 true。	[ -r $file ] 返回 true。
# -w file	检测文件是否可写，如果是，则返回 true。	[ -w $file ] 返回 true。
# -x file	检测文件是否可执行，如果是，则返回 true。	[ -x $file ] 返回 true。
# -s file	检测文件是否为空（文件大小是否大于0），不为空返回 true。	[ -s $file ] 返回 true。
# -e file	检测文件（包括目录）是否存在，如果是，则返回 true。	[ -e $file ] 返回 true。
file="/Users/muyuanqiang/PycharmProjects/python-demo/shell/execute.sh"
if [ -d $file ]; then
    echo "文件为目录"
else
    echo "文件不是目录"
fi
