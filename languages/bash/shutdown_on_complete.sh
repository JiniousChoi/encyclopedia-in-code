#!/bin/bash
FILE=$1

prerequisite() {
    if [[ -z $FILE ]]; then
        echo "FILE should be passed as first param"
        exit 1;
    fi

    if [[ $USER != "root" ]]; then
        echo "root privilege required."
        exit 1;
    fi
}
prerequisite;


is_condition_satisfied () {
    if [[ ! -a $FILE ]]; then
        return 0;
    else
        return 1;
    fi
}

command_on_condition () {
    echo "now shutting down..."
    sleep 1; sudo shutdown -k now
}

intermission () {
    sleep 1;
}

logging () {
    echo "saving current time"
    date >> ~/shutdown.time
}

while true; do
    if is_condition_satisfied; then
        logging;
        command_on_condition;
        exit 0;
    else
        echo "file $FILE exists"
        echo "keep looping"
    fi
    intermission;
done

exit 0
