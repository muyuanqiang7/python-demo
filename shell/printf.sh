#!/usr/bin/env bash
# printf command
# printf 命令模仿 C 程序库（library）里的 printf() 程序。
#
# printf 由 POSIX 标准所定义，因此使用 printf 的脚本比使用 echo 移植性好。
#
# printf 使用引用文本或空格分隔的参数，外面可以在 printf 中使用格式化字符串，还可以制定字符串的宽度、
# 左右对齐方式等。默认 printf 不会像 echo 自动添加换行符，我们可以手动添加 \n。
# printf 命令的语法：
# printf  format-string  [arguments...]

printf "Hello, Shell\n"
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876

# %s %c %d %f都是格式替代符
#
# %-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，
# 如果不足则自动以空格填充，超过也会将内容全部显示出来。
#
# %-4.2f 指格式化为小数，其中.2指保留2位小数。
printf "%d %s\n" 1 "abd"
printf '%-10d %-10s\n' 123 'abc'

printf '%10s\n' abc
# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def

printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j

# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
printf "%s and %d \n"
# printf的转义序列