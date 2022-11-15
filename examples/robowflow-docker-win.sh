DATE=`date +"%F-%T"`
SRC_MOUNT=/mnt/e/Code/hyperplan/examples
echo ${SRC_MOUNT}
TARGET_MOUNT=/ws_hyperplan/data

docker run \
   --rm \
   --name hyperplan \
   --mount type=bind,source="${SRC_MOUNT}",target="${TARGET_MOUNT}" \
   hyperplan ${testing} "$@" \
   >> ./logs/hyperplan-${DATE}.log