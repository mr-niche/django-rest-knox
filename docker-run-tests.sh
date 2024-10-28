#!/usr/bin/env bash
MOUNT_FOLDER=/app

docker build -t local-drk-tox-image .

docker run --rm -it \
  -v "$(pwd)/tests":"$MOUNT_FOLDER/tests" \
  -v "$(pwd)/knox":"$MOUNT_FOLDER/knox" \
  -v "$(pwd)/knox_project":"$MOUNT_FOLDER/knox_project" \
  -v "$(pwd)/tox.ini":"$MOUNT_FOLDER/tox.ini" \
  -v "$(pwd)/setup.py":"$MOUNT_FOLDER/setup.py" \
  -v "$(pwd)/README.md":"$MOUNT_FOLDER/README.md" \
  -v "$(pwd)/manage.py":"$MOUNT_FOLDER/manage.py" \
  -w "$MOUNT_FOLDER" local-drk-tox-image tox
