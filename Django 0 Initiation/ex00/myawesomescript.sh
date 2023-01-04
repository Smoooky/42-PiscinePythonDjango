#!/bin/sh
#Location:
if [ $# -eq 0 ]
  then
    URL='bit.ly/3X45o6j'
  else
    URL=$1
fi
curl --head --silent  ${URL} | grep Location | cut -d " " -f 2
