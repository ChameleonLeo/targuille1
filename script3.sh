#!/bin/bash/

PIDS="`ps -e | grep java -i | awk {'print $1'}`"

mkdir /tmp/investigation

for PID in $PIDS
do
	lsof -p $PID > "/tmp/investigation/access_$PID.txt"
done

