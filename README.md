# django

rm db.sqlite
rm project/migrations
python2.7 manage.py migrate
python2.7 manage.py syncdb
