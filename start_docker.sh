#!/bin/bash

source .env

docker run -it --rm \
  -v "${HYPERPLAN_SRC_DIR}":/ws_hyperplan/src/hyperplan \
  --mount type=bind,source="${HYPERPLAN_FETCH_DATA_DIR}",target=/ws_hyperplan/data/hyperplan-fetch \
  hyperplan /bin/bash
