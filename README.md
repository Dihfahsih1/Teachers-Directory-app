# Teachers-Directory-app
Currently hosted on Heroku:[https://teacherdirectoryapp.herokuapp.com/](https://teacherdirectoryapp.herokuapp.com/)

 How to run this app
 
 1) You can download the project folder in a zipped format, extract it to a desired location, navigate to that project location on your computer.

 2) Create the virtual environment where your project dependencies shall get install using this command
        python3 -m venv name_of_venv

        source name_of_venv/bin/activate to activate the virtual environment

3)  Run the following command to install all the required dependencies for the project
 		
		pip install -r requirements.txt
		
4) In the root folder of your application, run the following command to create the tables into the default sqlite database
		
		python manage.py makemigrations

5) Run also the following command to apply the above migrations to the database 

		python manage.py migrate
		
6) Create the super user of the app by running the following command

        python manage.py createsuperuser

        Enter the username, email and the password.
		
7) Use the following command to start the application

        python manage.py runserver

8) In your browser type in the following to access the app

        http://localhost:8000/

        enter the username and the password you created above.

9) To manage the app as the superadmin use the following link in your web browser

        http://localhost:8000/admin

10) Finally you can customize the app the way you want by editing the files using any text editor of your choice.

 