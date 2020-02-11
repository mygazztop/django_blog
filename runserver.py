import subprocess
import webbrowser
import os

os.chdir('C:\\Users\\user\\PycharmProjects\\django_blog')

if 'No changes detected' in str(subprocess.check_output('python manage.py makemigrations', shell=True)):
    webbrowser.open_new('http://127.0.0.1:8000/')
    subprocess.call('python manage.py runserver', shell=True)
else:
    print('You have to migrate: python manage.py migrate')
