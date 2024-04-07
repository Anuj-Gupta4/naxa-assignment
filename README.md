# naxa-assignment

## Setup project

1. install required dependencies on terminal: <br>`pip install -r requirements.txt`
2. make migrations by running on terminal: <br>`python manage.py makemigrations`
3. migrate database by running on terminal: <br>`python manage.py migrate`
4. install packages using requirements.txt file preferrably in a virtual environment using command: <br>`pip install -r requirements.txt`
5. install redis locally
6. add following details to settings file from project folder
  - EMAIL_HOST_USER
  - EMAIL_HOST_PASSWORD
7. run server using this command in a terminal: <br>`python manage.py runserver`
8. Open a second terminal and start the celery worker by running the following command: <br>
   `celery -A naxa worker --pool=solo -l info`
9. Open a third terminal and start the celery beat by running the following command: 
   <br>`celery -A naxa beat --loglevel=info`
10. All Done 🎉🎉
