#!/usr/bin/env bash
set -euox pipefail

cd yarn-journal
~/.local/bin/poetry run ./manage.py migrate

rm -rf ~/yarn-journal-static/static
~/.local/bin/poetry run ./manage.py collectstatic

sudo /bin/systemctl restart yarn_journal.service
