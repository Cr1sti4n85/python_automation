#!/bin/bash

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done

m=0
command=$1 #we get the first argument from the command line, which is random-exit.py in this case.
#if the received command is not successful (exit status != 0) and the number of retries is 
#less than or equal to 5, we will retry the command.
while ! $command && [ $m -le 5 ]; do    
    sleep $m
    ((m+=1))
    echo "Retry #$m"
done;