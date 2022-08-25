# KietHub - Backend (Work in progress)

## How to run locally

### 1. Clone the repository

```
git clone https://github.com/g-paras/kiethub-backend
```

### 2. cd in project folder & install requirements

```
cd kiethub-backend
pip install -r requirements.txt
```

### 3. copy .env file

```
cp .env.example .env
```

### 3. create and run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 4. rum the django application

```
python manage.py runserver
```
