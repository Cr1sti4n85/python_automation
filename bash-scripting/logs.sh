#!/bin/bash

for logfile in /var/log/syslog; do
    echo "Processing $logfile"
    sudo cut -d' ' -f3- $logfile | sort | uniq -c | sort -nr | head -10
done