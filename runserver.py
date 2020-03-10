import subprocess
import webbrowser
import os

os.chdir('C:\\Users\\user\\PycharmProjects\\django_blog')

try:
    migr_result = str(subprocess.check_output('python manage.py makemigrations', shell=True))
except:
    migr_result = 'err'
if 'No changes detected' in migr_result:
    webbrowser.open_new('http://127.0.0.1:8000/')
    subprocess.call('python manage.py runserver', shell=True)
elif 'err' in migr_result:
    print('You have to makemigrations: python manage.py makemigrations')
    print('You have to migrate: python manage.py migrate')
else:
    print('You have to migrate: python manage.py migrate')


'''
cd /home/mygazztop/mygazztop.pythonanywhere.com/
git pull
https://www.pythonanywhere.com/user/mygazztop/webapps/#tab_id_mygazztop_pythonanywhere_com
git reset --hard
'''
# touch /var/www/mygazztop.pythonanywhere.com _wsgi.py
