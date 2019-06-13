#! /bin/bash

#----------------------------------
# $Author: ee364b08 $
# $Date: 2016-03-19 15:22:31 -0500 (Tue, 19 March 2016)) $
#----------------------------------

function part_a 
{               
    Arr=(a.txt b.txt c.txt d.txt)
    (( randomvr=$RANDOM%4 ))
    tail -n 6 ${Arr[$randomvr]} | head -n 3
    return                      
}                               

function part_b
{              
    if [[ -d $1 ]]
    then
        echo "$1 is a directory name"
    elif [[ -f $1 ]]
    then
        echo "$1 is a file name"
    else
        echo "$1 is not a file or directory name"
    fi
    return                     
}                              

function part_c
{
 #   exec 4< file.txt
 #   while read lineA <&4
 #   do
 #       read lineB <&4
 #   done
    return
}

function part_d
{
    file=temp.txt
    words=$(wc -w $file)
    lines=$(wc -w $file)
    wordscount=$(echo $words | cut -d " " -f 1)
    linescount=$(echo $words | cut -d " " -f 1)
    echo "temp.txt has $wordscount words and $linescount lines"
    return
}

function part_e
{
    python3.4 ece364.py > output.txt 2>&1 
    return
}

function part_f
{
    file=people.csv
    tail -n +2 $file | sort -t"," -k4,4 -k6,6 -k1,1 -k2,2 | tail -n 10
    return
}

function part_g
{
    str="multimillionaire"
    echo $str | tr 'a' '-' | tr 'e' '-' | tr 'i' '-' | tr 'o' '-' | tr 'u' '-'
    return
}


function part_h
{
    exec 2> /dev/null
    curdir=$(echo $('pwd'))
    changedir=$(echo $('pwd')"/src")
    cd $changedir
    for i in *.c
    do
        if gcc $i
        then
            echo "${i%.c}.c: success"
        else
            echo "${i%.c}.c: failure"
        fi
    done
    cd $curdir
    return
}

function part_i
{
    grep -c "PURDUE" info.txt
    return
}

function part_j
{
    ping -c 3 ecegrid.ecn.purdue.edu
    return
}

# To test your function, you can call it below like this:
#
 part_a

 part_b practical.bash
 
 part_d

 part_e

 part_f

 part_g

 part_h

 part_i

 part_j
