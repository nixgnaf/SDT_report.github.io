#!/bin/bash

#usage: $0 < FILENAME

MINLEN=45

while read line
do
 echo "$line" 

 len=${#line}
 if [ "$len" -lt "$MINLEN" ]
  then echo
 fi
done

