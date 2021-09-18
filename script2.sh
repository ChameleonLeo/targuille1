#!/bin/bash/

for i in {0..10}
do
	openssl rand -hex 500 > "test_`date "+%F"`_$i.txt"
done

# for editing crontab use command "crontab -e"
# to schedule this script every 6 hours add to crontab the following string:
# 0 */6 * * * /path/to/script/script2.sh
