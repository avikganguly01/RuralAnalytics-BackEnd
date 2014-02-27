#!/bin/bash
 

if  type mysql > /dev/null;
then
	EXPECTED_ARGS=5
	E_BADARGS=65
	MYSQL=`which mysql`
	 
	Q1="CREATE DATABASE IF NOT EXISTS $3;"
	Q2="GRANT ALL ON $3.* TO '$4'@'localhost' IDENTIFIED BY '$5';"
	Q3="FLUSH PRIVILEGES;"
	SQL="${Q1}${Q2}${Q3}"
 
	if [ $# -ne $EXPECTED_ARGS ]
	then
	  echo "Usage: $0 user pass dbname dbuser dbpass"
	  exit $E_BADARGS
	fi
 
	$MYSQL -u$1 -p$2 -e "$SQL"
else
	echo "No working MySQL installation found"
fi
