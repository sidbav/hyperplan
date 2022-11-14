DATE=`date +"%F-%T"`
SRC_MOUNT=${HOME}/Documents/hyperplan/examples
TARGET_MOUNT=/ws_hyperplan/data

docker run \
   --rm \
   --name hyperplan \
   --mount type=bind,source="${SRC_MOUNT}",target="${TARGET_MOUNT}" \
   hyperplan ${testing} "$@" \
   >> ./logs/hyperplan-${DATE}.log