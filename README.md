# naxa-assignment

## Setup project

1. Install required dependencies on terminal: <br>`pip install -r requirements.txt`
2. Make migrations by running on terminal: <br>`python manage.py makemigrations`
3. Migrate database by running on terminal: <br>`python manage.py migrate`
4. Install packages using requirements.txt file preferrably in a virtual environment using command: <br>`pip install -r requirements.txt`
5. Install redis locally
6. Add following details to settings file from project folder
  - EMAIL_HOST_USER
  - EMAIL_HOST_PASSWORD
7. run server using this command in a terminal: <br>`python manage.py runserver`
8. Open a second terminal and start the celery worker by running the following command: <br>
   `celery -A naxa worker --pool=solo -l info`
9. Open a third terminal and start the celery beat by running the following command: 
   <br>`celery -A naxa beat --loglevel=info`
10. All Done 🎉🎉

## note
wasnt sure what kind of messaging was required. so implemented mail automation.<br>
didnt use postgis as i used sqlite db<br>
feel free to ask any questions
