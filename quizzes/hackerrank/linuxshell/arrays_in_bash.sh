#!/bin/bash
## author: jinchoiseoul@gmail.com


################################################################################################
#### Read in an Array                                                                       ####
#### Given a list of countries, each on a new line, your task is to read them into an array ####
#### and then display the entire array, with a space between each of the countries' names.  ####
################################################################################################
## method 0
#declare -a countries=(`cat`)
#echo ${countries[@]}
#
## method 1
#countries=($(cat))
#echo ${countries[@]}
#
## method 2
#echo $(< /dev/stdin)
#
## method 3
#countries=($(< /dev/stdin))
#echo ${countries[@]}
#
## method 4
#i=0
#while read line
#do
#	countries[$i]=$line
#	((i+=1))
#done
#
#echo ${countries[@]}
#
#
###################################################################
##### Slice an Array                                           ####
##### Display only the elements lying between position 3 and 7 ####
##### both inclusive. Indexing starts from 0                   ####
###################################################################
#declare -a countries=(`cat`)
#echo ${countries[@]:3:5} # Note that it is NOT ${countries[@]:3:7}
