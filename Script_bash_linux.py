"""#!/bin/bash - обязательно писать вначале скрипта."""

# Пример 1
# #!/bin/bash
# echo "Hello this is message from script"
# echo "Let's show file in the folder"
# ls
# ls -l
# echo "Done"

# Пример 2
# #!/bin/bash
# mycomputer="Asus x550c"  ---> Присваивание переменной без пробелов.
# myOS=`uname -a`  ---> Чтоб присвоить переменной команду Linux нужно поставить вот эти скобки ` `
# echo "This script name is $0"  ---> $0 равен названию файла скрипта.
# echo "Privet $1"  ---> Если во время запуска скрипта после названия написать имя или что ешё $1 примит его как параметр
# echo "Hello $2" ---> Тоже самое и с $2 если $1 уже имеет параметр то следущее слово $2 примет как параметр и так далее.
# num1=50
# num2=45
# summa=$((num1+num2)) ---> Обязательно в двойных скобках.
# echo "num1 + num2 = $summa" ---> $ ставим перед переменной которую хотим использовать.
# myhost=`hostname`
# mygwt="8.8.8.8"
# ping -c 4 $myhost
# ping -c 4 $mygwt
# echo -n "This is done..." ---> -n значит продолжить следуший текст на этой же строке.
# echo "Really done"

# Пример 3(if,elif,else)(case)
# #!/bin/bash
# if [ "$1" == "Vasea" ]; then
#       echo "Privet $1"
# elif [ "$1" == "Trump" ]; then
#       echo "Hello $1"
# else  echo "Bye Bye $1"
# fi ---> Так заканчивается
#
# read -p "Please Enter something:" x ---> Так мы просим пользователя ввести параметр для x
# echo "Starting CASE selection..."
#
# case $x in
#         1) echo "This is one";;
#     [2-9]) echo "Two-Nine";;
#   "Petya") echo "Privet $x";;
#         *) echo "Parameter Unknown sorry!"
# esac ---> Так заканчивается

# Пример 4(while)(for in)
# #!/bin/bash
# COUNTER=0
# while [ $COUNTER -lt 10 ]; do
#           echo "Current counter is $COUNTER"
#           COUNTER=$(($COUNTER+1))
#           #let COUNTER=COUNTER+1
#           #let COUNTER+=1
# done
#
# for myfile in `ls *.txt`; do
#             cat $myfile
# done
#
# for x in {1..10}; do
#           echo "X = $x"
# done
#
# for ((i=1; i<=10; i++ )); do
#           echo "Number I = $i"
# done

# Пример 5(Функции)
# #!/bin/bash
# summa=0
# myFunction()
#{
#       echo "This is text from Function!"
#       echo "Number1 = $1"
#       echo "Number2 = $2"
#       summa=$(($1+$2))
#}
# myFunction 50 25
# echo "SUMMA=$summa"