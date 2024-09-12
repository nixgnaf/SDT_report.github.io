#!/bin/bash

count=0

echo > output.log

while true
do
./command.sh &>> output.log
if [[ $? -ne 0 ]]; then
    break
fi
((count++))
done

echo "the command failed after running $count times."

