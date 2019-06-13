#! /bin/bash
#
#$Author: ee364b08 $
#$Date: 2016-01-26 20:43:37 -0500 (Tue, 26 Jan 2016) $
#$Revision: 87015 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b08/Lab02/hangman.bash $
#$Id: hangman.bash 87015 2016-01-27 01:43:37Z ee364b08 $


#Declarations#
arr=(banana parsimonious sesquipedalian)
word=0
guess=0
flag=0
ans=0
flag2=1

i=$(echo $(($RANDOM % 3)))
word=${arr[$i]}


if (($i==0))
then
    size=${#word}
    echo "Your word is $size characters long"
    guess=(. . . . . .)
elif (($i==1))
then
    size=${#word}
    echo "Your word is $size characters long"
    guess=(. . . . . . . . . . . .)
else
    size=${#word}
    echo "Your word is $size characters long"
    guess=(. . . . . . . . . . . . . .)
fi

while ((flag < size))
do
    echo "Word is: ${guess[*]}"
    read -p "Make a guess: " letter
    
    echo $word | grep $letter > /dev/null
    if (( $? == 0 ))
    then
        echo ${guess[*]} | grep $letter > /dev/null
        if (($? != 0))
        then
            echo "Good going!"
            echo
            for ((i=0; i<$size; i++))
            do
                if [[ $letter = ${word:$i:1} ]]
                then
                    ((flag=flag+1))
                    guess[$i]=${word:$i:1}
                fi
            done
        else
            echo "Sorry, try again."
            echo  " "  
        fi
    else
      echo "Sorry, try again."
      echo  " "  
    fi

done

echo
echo "Word is: ${guess[*]}! Congratulations!"

exit 0
