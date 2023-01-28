OPTION=$1
MESSAGE_COLOR='\033[1;34m \033[47m'
MESSAGE_COLOR_2='\033[1;35m \033[47m'
NC='\033[0m'

export ENVIRONMENT=localhost

if [ "$OPTION" == "worker" ]; then
    echo "${MESSAGE_COLOR}=============> Start worker <============${NC}"
    #cd .. && celery -A communicator_api.tasks worker -B -l info --heartbeat-interval 5
    # cd .. && celery -A communicator_api.tasks worker -B -l info -c 4 -Ofair -Q —-without-gossip
    cd .. && celery -A communicator_api.tasks worker --concurrency=4 --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair
    # cd .. && celery -A communicator_api.tasks worker -l info -Ofair -P eventlet -c 1000 --without-gossip --without-mingle --without-heartbeat
elif [ "$OPTION" == "stop" ]; then
    echo "${MESSAGE_COLOR}==============> Stop celery <============${NC}"
    cd .. && celery -A communicator_api.tasks control shutdown
else
    echo "${MESSAGE_COLOR}===========> Option not found <==========${NC}"
fi