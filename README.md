# myDATA3_todolist_backend

cd myDATA3_todolist_backend
source env/bin/activate
pip install -r requirements.txt
python manage.py loaddata data.json
python manage.py runserver
