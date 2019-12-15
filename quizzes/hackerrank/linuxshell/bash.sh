#!/bin/bash
## author: jinchoiseoul@gmail.com

#####################
#### Let's Echo  ####
#####################
echo "Let's Echo"
echo 'hello'


########################################
#### Looping and Skipping           ####
#### print odd numbers from 1 to 99 ####
########################################
echo ""
echo "Looping and Skipping"
echo "method 1"
seq 1 2 99

echo ""
echo "method 2"
for i in $(seq 1 2 99)
do
    echo $i
done

echo ""
echo "method 3"
for i in {1..99..2}
do
    echo $i
done


################################################
#### A Personalized Echo                    ####
#### read stdin and assign it to a variable ####
################################################
echo ""
echo "A Personalized Echo"
echo -n "your name : "; read NAME
echo "Welcome $NAME"


####################################
#### Looping with Numbers       ####
#### print numbers from 1 to 50 ####
####################################
echo ""
echo "Looping with Numbers"
for i in {1..50}
do
    echo $i;
done


####################################################################
#### The World of Numbers                                       ####
#### given 2 ints, print sum, difference, product, and quotient ####
####################################################################
echo ""
echo "The World of Numbers"
echo -n "number a : "; read a
echo -n "number b : "; read b
echo $(($a + $b))
echo $(($a - $b))
echo $(($a * $b))
echo $(($a / $b))


###########################
#### Comparing Numbers ####
#### Identify  <, =, > ####
###########################
echo ""
echo 'Comparing Numbers';
echo -n 'number X : '; read X
echo -n 'number Y : '; read Y

if [[ $X -lt $Y ]]; then
    echo "X is less than Y"
elif [ $X -gt $Y ]; then
    echo "X is greater than Y"
elif test $X -eq $Y; then
	echo "X is equal to Y"
else
    echo "[Error] cannot reach here"
fi


###############################################
#### Getting Started with conditionals     ####
#### read in one character 'Y','y','N','n' ####
###############################################
echo ""
echo 'Getting Started with conditionals'
echo -n 'Y or n : '; read answer

case $answer in
    [yY] )
        echo "YES" ;;
    [nN] )
        echo "NO" ;;
    * )
        echo "Error" ;;
esac


######################################################################
#### More on Conditionals                                         ####
#### Identify if a triangle is Scalene, Isosceles, or Equilateral ####
######################################################################
echo ""
echo "More on Conditionals"
echo -n "a length : "; read a
echo -n "b length : "; read b
echo -n "c length : "; read c

if [[ $a == $b && $b == $c ]]
then
    echo 'EQUILATERAL';
elif [[ $a == $b || $b == $c || $c == $a ]]
then
    echo 'ISOSCELES';
else
    echo 'SCALENE';
fi


########################################################################
#### Arithmetic Operations                                          ####
#### Evaluate the arithmetic expression correct to 3 decimal places ####
########################################################################
echo ""
echo "Arithmetic Operations"
expr1="5+50*3/20 + (19*2)/7"
expr2="-105+50*3/20 + (19^2)/7"
expr3="(-105.5*7+50*3)/20 + (19^2)/7"
OLDIFS=$IFS
IFS=''
for expr0 in $expr1 $expr2 $expr3
do
    echo -n "$expr0 = "
    printf "%.3f\n" $(bc -l <<< $expr0); 
    # Note: <<< is for HERE STRINGS, a variant of here documents

    echo -n "$expr0 = "
	echo "b=eval('$expr0'.replace('^','**')); print(round(b,3))" | python3
done
IFS=$OLDIFS


##############################################################################
#### Compute the Average                                                  ####
#### compute average of N ints from stdin correct to three decimal places ####
##############################################################################
echo ""
echo "Compute the Average"
#method 1
echo -n 'how many numbers : '; read N
n_sum=0
for ((i=0;i<$N;i++))
do
    echo -n "number $(expr $i + 1): "; read line
    n_sum=$(($n_sum+$line))
done

printf "%.03f\n" `echo "$n_sum/$N" | bc -l`

#method 2
n_sum=0
N=0
while read line || [[ -n "$line" ]] # in case of last line lack of newline
do
    n_sum=$(($n_sum + $line))
#    N=$(($N + 1))
	 ((N++))
done < <(echo -e "1\n3\n5\n7\n8") # preserve stdin for stdin-reading commands inside loop
printf "%.03f\n" `echo "$n_sum/$N" | bc -l`

#method 3
n_sum=0
N=0
while read line <&7 # preserve stdin for stdin-reading commands inside loop
do
    n_sum=$(($n_sum + $line))
    ((N++))
done 7< <(printf "11\n23\n25\n17\n8")
printf "%.03f\n" `bc -l <<< $n_sum/$N`


##########################################################
#### Functions and Fractals - Recursive Trees - Bash! ####
##########################################################
echo ""
echo "Functions and Fractals"

declare -A m
StartLegLength=16
maxrows=63
maxcols=100
echo -n "iter : "; read iter


function Y {
  typeset -i row=$1 col=$2 len=$3 iter=$4
  typeset -i r=$row x=$len cl=$col cr=$col l=$((len/2))

  # leg
  while (( x-- > 0 ))
  do m[$((r--)),$col]=1
  done

  # fork
  x=$len
  while (( x-- > 0 ))
  do m[$r,$((--cl))]=1
     m[$r,$((++cr))]=1
     ((r--))
  done

  # subs
  if (( --iter > 0 ))
  then Y $r $cl $l $iter
       Y $r $cr $l $iter
  fi
}

# initialize
for (( row=0; row<maxrows; row++ ))
do  for (( col=0; col<maxcols; col++))
    do  m[$row,$col]=_
    done
done

# recurse
Y $(( maxrows-1 )) $(( (maxcols-1)/2 )) $StartLegLength $iter

# show the result
for (( r=0; r<maxrows; r++ ))
do  for (( c=0; c<maxcols; c++))
    do  printf "%s" ${m[$r,$c]}
    done
    printf "\n"
done
