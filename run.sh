OPTION=$1
OPTION_2=$2
MESSAGE_COLOR="\033[1;32m \033[47m"
NC="\033[0m"

if [ "$OPTION" == "deploy" ]; then
    echo "${MESSAGE_COLOR}############## START DELPLOY LOCALHOST ##############${NC}"
    cd ./bash && sh deploy_dev.sh $OPTION_2
elif [ "$OPTION" == "celery" ]; then
    echo "${MESSAGE_COLOR}############## CELERY ##############${NC}"
    cd ./bash && sh celery.sh $OPTION_2
elif [ "$OPTION" == "test" ]; then
    echo "${MESSAGE_COLOR}############## START TEST CARTERA ##############${NC}"
    cd ./bash && sh run_tests.sh
    echo "${MESSAGE_COLOR}############### END TEST CARTERA ###############${NC}"
elif [ "$OPTION" == "build" ]; then
    echo "${MESSAGE_COLOR}############## START BUILD IMAGE ##############${NC}"
    cd ./bash && sh build.sh $OPTION_2
    echo "${MESSAGE_COLOR}############### END BUILD IMAGE ###############${NC}"
else
    echo "${MESSAGE_COLOR}############## OPTION NOT FOUND ##############${NC}"
fi
