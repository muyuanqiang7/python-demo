#!/usr/bin/env bash
# echo command
# Shell 的 echo 指令与 PHP 的 echo 指令类似，都是用于字符串的输出。命令格式：
echo "It is a test"
# 处理转义字符
echo "\"It is a test\""
# read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
#read name
#echo "$name It's a test"
# 显示换行
echo  "OK! \n" #
echo -e "OK! \n" # -e 开启转义

# 显示不换行
echo -e " OK! \c"
echo "It is a test"

# 显示结果定向至文件 文件不存在时会自动创建
# 覆盖文件
current_date=`date +%Y%m%d%H%M%S`
file_name="${current_date}myfile.txt"
echo $file_name
#echo "it's a test " > ./$file_name
# 往文件追加
append_directory="./app"
append_file="appenfile.txt"
append_path="$append_directory/$append_file"
#mkdir -p $append_file
#mkfile() { mkdir -p -- "$1" && touch -- "$1"/"$2" }
#mkfile ${append_directory} ${append_file}
#创建目录并且创建文件
#mkdir -p $append_directory && touch $append_path
#echo "and append something into the file" > $append_path

# 原样输出字符串,不进行转义或取变量(用单引号)
echo '$name\"'

# 显示命令执行结果
echo `date +%Y%m%d`

# echo 命令输出字符串总结
#       |      能否引用变量        |       能否引用转移符        |  能否引用文本格式符(如：换行符、制表符)
#
#单引号  |           否           |             否             |                             否
#
#双引号  |           能           |             能             |                             能
#
#无引号  |           能           |             能             |                             否