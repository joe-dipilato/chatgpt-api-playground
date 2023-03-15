#!/bin/bash

FILE=$1
ACTION=${2:-"./${FILE}"}
LASTTIME=0

if [ ! -f "${FILE}" ]; then
    echo "ERROR: ${FILE} doesn't exist"
    exit 1
fi

while sleep 1; do
    FILETIME=$(stat "${FILE}" --format=%Y) # Linux
    # FILETIME=$(stat -f %c "${FILE}") # Mac
    if [ "$LASTTIME" -ne "${FILETIME}" ]; then
        echo
        LASTTIME=${FILETIME}
        ${ACTION}
    fi
    echo -n "."
done

