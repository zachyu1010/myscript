#!/bin/bash

#curl --remote-name http://zachary_yu:knePOI123@eip.kneron.com:8080/redmine/attachments/download/3580/12401.tgz
#curl --remote-name http://1f1841f68935200e12329f87b6241269e069b628@eip.kneron.com:8080/redmine/attachments/download/3580/12401.tgz
#set -x

CURL_CONFIGS="--keepalive-time 10 --silent --show-error --fail --insecure --location -b cookies.txt -c cookies.txt"
#CURL_CONFIGS="--insecure --location -b cookies.txt -c cookies.txt"
CURL_CONFIGS2="--show-error --fail --insecure --location -b cookies.txt -c cookies.txt"

LOGIN_PAGE=http://eip.kneron.com:8080/redmine/login
USER=zachary_yu
PASS=knePOI123
DOWNLOAD_FILE=http://eip.kneron.com:8080/redmine/attachments/download/3580/12401.tgz


cleanup()
{
    rm -f cookies.txt
}

# Initial cleanup
cleanup

# Fetch CSRF authenticity token
CSRF1=$(curl $CURL_CONFIGS $DOWNLOAD_FILE | grep "name=\"authenticity_token" | sed 's/.*value="\(.*\)".*/\1/')

if [[ $? -ne 0  ]]
then
    echo "Error getting csrf token"
    echo $CSRF1
    cleanup
    exit 1
fi

#echo $CSRF1

# Login
HTML=$(curl $CURL_CONFIGS -d "login=Login&username=${USER}&password=${PASS}&authenticity_token=${CSRF1}" ${LOGIN_PAGE})
 
#echo $HTML

if [[ $? -ne 0  ]]
then
    echo "Error logging in"
    cleanup
    exit 1
fi

# Download file
curl $CURL_CONFIGS2 $DOWNLOAD_FILE --remote-name

if [[ $? -ne 0  ]]
then
    echo "Error downloading backup file" | tee -a ${LOGFILE}
    cleanup
    exit 1
fi

cleanup
