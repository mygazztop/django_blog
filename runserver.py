import subprocess
import webbrowser
import os

os.chdir('C:\\Users\\user\\PycharmProjects\\django_blog')

if 'No changes detected' in str(subprocess.check_output('python manage.py makemigrations', shell=True)):
    webbrowser.open_new('http://127.0.0.1:8000/')
    subprocess.call('python manage.py runserver', shell=True)
else:
    print('You have to migrate: python manage.py migrate')


'''
cd /home/mygazztop/mygazztop.pythonanywhere.com/django_blog
git pull
touch /var/www/mygazztop.pythonanywhere.com _wsgi.py
https://www.pythonanywhere.com/user/mygazztop/webapps/#tab_id_mygazztop_pythonanywhere_com
'''