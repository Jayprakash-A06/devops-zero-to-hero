#!/bin/bash

# Using Backticks
current_date=`date`
echo "Current date: $current_date"
# Using $(...)
current_time=$(date +%H:%M:%S)
echo "Current time: $current_time"
