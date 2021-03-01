
#!/bin/bash
mysql --silent -e "use DATABASENAME;select * INTO OUTFILE 'results.csv' FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' FROM TABLENAME;"
echo "Query results are in /var/lib/mysql/DATABASENAME"
sed -i 1i"HERE ADD THE TABLE COLUMN NAMES COMMA SEPARATED" /var/lib/mysql/DATABASENAME/results.csv
mv /var/lib/mysql/DATABASE/results.csv ~/results-$(date +"%Y-%m-%d").csv
echo "Archive moved to user's home folder"
echo "Mailing it to the users"
echo "Results are attached. Please check and let admins know if you find any issue" | mailx -s "Results dump" -a ~/results-$(date +"%Y-%m-%d").csv user@user.com
rm -rf ~/results-$(date +"%Y-%m-%d").csv
echo "Finished"
