# cebarco

### Installation
```
git clone https://github.com/jacksellers/cebarco.git
cd cebarco
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cd app
> keys.py
nano keys.py
```
Paste the secret key and save the file
```
python manage.py migrate
python manage.py runserver
```
