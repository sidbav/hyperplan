#/bin/bash
#robot=${1:-fetch}
#shift
#problem=${1:-box_pick}
#shift
#opt=${1:-speed}
#shift
#testing=${1:-}
#shift
#name=${problem}-${opt}
#if [ "$testing" == "--test" ]; then
#    suffix="-test"
#fi

DATE=`date +"%F-%T"`

SRC_MOUNT=${HOME}/Documents/hyperplan/examples
TARGET_MOUNT=/ws_hyperplan/data

# docker run \
   #--rm \
   #--name hyperplan \
   #--mount type=bind,source="${SRC_MOUNT}",target="${TARGET_MOUNT}" \
   #hyperplan ${testing} "$@" \
   #/ws_hyperplan/data/cubicles.cfg /ws_hyperplan/data/Twistycool.cfg \
   #>> ${HOME}/Documents/hyperplan/logs/hyperplan-${DATE}.log

echo docker run \
   --rm \
   --name hyperplan \
   --mount type=bind,source="${SRC_MOUNT}",target="${TARGET_MOUNT}" \
   hyperplan ${testing} "$@"

docker run \
   --rm \
   --name hyperplan \
   --mount type=bind,source="${SRC_MOUNT}",target="${TARGET_MOUNT}" \
   hyperplan ${testing} "$@" \
   >> ${HOME}/Documents/hyperplan/logs/hyperplan-${DATE}.log
