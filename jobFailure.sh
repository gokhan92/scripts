#!/bin/bash
#This script will detect the failed jobs for the processes and send an email with details in case of failure

kinit -kt ~hdfs/hdfs.keytab keytabRealm
JOB_LIST="/partition1/Jobs/jobList.txt"
yarn application -list -appStates FINISHED | grep FAILED | grep root.users | grep userName | awk '{print $1}'> $JOB_LIST
jobs_len=$(cat $JOB_LIST | wc -l)
if [ $jobs_len -gt 0 ]
then
#yarn application -list -appStates RUNNING | awk '{print $1}'> $JOB_LIST
 echo -e "\nHi Name of the  Team,\n\nPlease check the listed jobs above.Please contact admin team to troubleshoot. \n\nThanks,\nAdmin team." >> $JOB_LIST
 mail -s "Jobs Failure" user@users.com  < /partition1/Jobs/jobList.txt
fi
