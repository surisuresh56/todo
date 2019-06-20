# TO-DO list Django app

A python and Django project which will create the To-Do lsit website and perform certain task i.e Adding the Task and Deleting the Task.
Also its having admin page where user can view the data and delete the data.Also if he need any data he can export the data.We also created the API to create/Delete/Update/View To-do list.

# Getting Started

# Installing
Create the Virtual environment and install the python version

<pre>VIRTUALENV_DIR=/tmp/projectenv
virtualenv "${VIRTUALENV_DIR}" -p python3.6
source "${VIRTUALENV_DIR}"/bin/activate</pre>

Clone the repository to a directory of your choice.

<pre>git clone https://github.com/surisuresh56/todo.git</pre>

Ensure all Python dependencies are installed via pip.

<pre>python pip install -U -r requirements.txt</pre>

Go to project directory using below command.

<pre>cd todo/todo_list_app</pre>

# Running the django app

<pre>python manage.py runserver server_ip/hostname:8000</pre>

# Checking the Django app functionality in browser

In browser give the url  http://localhost:8000/ ,it will open the app and you test the functionality for front end.
For API give the url http://localhost:8000/todo ,it will show you the details and you can perform CRUD operation and do the testing.

# Creating the admin user and login in Admin Interface

<pre>python manage.py createsuperuser
Username (leave blank to use 'skamanna'):test
Email address: test@gmail.com
Password: test@123
Password (again): test@123
Superuser created successfully.
</pre>
Use below url to login in admin and give the user name and password.It will logged in admin interface.Then do the testing for admin funcionaility.
<pre>
http://localhost:8000/admin
</pre>

