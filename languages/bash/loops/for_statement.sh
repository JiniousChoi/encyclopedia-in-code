#!/bin/bash
# reference https://www.cyberciti.biz/faq/bash-for-loop/

for i in 'Jin Choi' 'Brad Pitt'
do
   echo "Welcome $i !"
done

for i in {1..5}
do
   echo "First Five Natural Number: $i"
done

for i in {2..10..2}
do
   echo "First Five Even Number: $i"
done

# Three-expression bash for loops syntax
for (( c=3; c>=0; c-- ))
do  
   echo "Countdown: $c"
done

# infinite loop
for (( ; ; ))
do
   echo "infinite loops [ hit CTRL+C to stop]"
   sleep 0.2
done

###############################
### Not meant to be excuted ###
###############################

# backup files given as parameters
function backup_files() {
    FILES="$@"
    for f in $FILES
    do
        # if .bak backup file exists, skip doing backup
        if [ -f ${f}.bak ]; then
            echo "Skiping $f file..."
            continue  # read next file and skip the cp command
        fi
        # we are here means no backup file exists, just use cp command to copy file
        /bin/cp $f $f.bak
    done
}
