#!/bin/bash

#usage: rfe old_extension new_extension

# refe gif jpg

E_BADARGS=65

case $# in

 0|1)
 echo "Usage: `basename $0` old_file_suffix new_file_suffix"
 exit $E_BADARGS
 ;;
esac

for filename in *.$1
do
 mv $filename ${filename%$1}$2
done

exit 0
