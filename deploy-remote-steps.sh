cd yarn-journal
rm -rf ~/yarn-journal-static/static
~/.local/bin/poetry run ./manage.py collectstatic
sudo /bin/systemctl restart yarn_journal.service
