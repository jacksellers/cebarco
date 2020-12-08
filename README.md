# cebarco

### Installation
```
git clone https://github.com/jacksellers/cebarco.git
cd cebarco
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cd app
> app/keys.py
nano app/keys.py
```
Paste the secret key (SECRET_KEY = '...')
```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
