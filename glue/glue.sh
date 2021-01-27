PARENT_ID="$$"
echo $PARENT_ID

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

CMD="\033[38;5;69m"
ERROR="\033[38;5;161m"
RESET="\033[0m"

RUN_LOCATION="$(pwd)/rt"
rm -rf "$RUN_LOCATION"
mkdir -p "$RUN_LOCATION"

get_pipe() {
    COMP_NAME=$1
    echo "$RUN_LOCATION/pipe-${COMP_NAME}.fifo"
}

start_component() {
    EXECUTOR=$1
    COMP_NAME=$2

    echo "Starting $COMP_NAME $args"

    pipe=$(get_pipe "$COMP_NAME")
    mkfifo "$pipe"

    echo "$CMD$EXECUTOR$RESET"
    ( cd "components/$COMP_NAME" ; $EXECUTOR < "$pipe" | process_component $COMP_NAME ) &
    : > "$pipe" # Open the pipe
}

process_component() {
    COMP_NAME=$1
    echo "Processing $COMP_NAME"
    while true
    do
        RECEIVER=""
        while [ -z "$RECEIVER" ] ; do
            read RECEIVER
        done
        read MSG
        echo "$CMD$COMP_NAME is sending '$MSG' to '$RECEIVER'$RESET"

        pipe=$(get_pipe "$RECEIVER")
        if [ ! -p "$pipe" ] ; then
            echo "${ERROR}Tried to communicate with component $RECEIVER ($pipe)$RESET"
            kill $PARENT_ID
            exit
        fi
        echo "$COMP_NAME" > "$pipe"
        echo "$MSG" > "$pipe"
    done
}

start_component "python3 run.py /dev/ttys003" INTR
start_component "python3 run.py" RLAY
start_component "python3 run.py" CONS

while true ; do sleep 1 ; done
