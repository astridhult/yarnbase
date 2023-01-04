#!/usr/bin/env bash
set -euox pipefail

SRC=.
DST=astridroald.nl:yarn-journal

rsync --rsh='ssh -p1248' -rzP --delete --filter=":- .gitignore" --exclude='.git' --exclude='.env' $SRC $DST
ssh -p 1248 astridroald.nl 'bash -s' < deploy-remote-steps.sh
