# Library Management System
*It is a simple library management system where admin can manage books along with auther and students can apply for the book*

# Tech Used
- Python flask
- Mysql

# To run application in development mode
- Make sure you have python installed in your system.
- Make sure you have mysql running.
- Copy .env.example to .env and fill up required values
- Generate a virtual enviroment to segregate the application dependencies with following command
```
  python -m venv env
```
- Activate virutal command with following command
```
  source env/Scripts/activate
```
- Now install all the application dependencies
```
  pip install -r requirement.txt
```
- Install python-dateutil
```
  pip install python-dateutil
```
- Migrate database with following command
```
  flask db upgrade
```
- To seed the database
```
  flask seed run
```
- Finally run application
```
  flask run
```

# To run application with docker
- Make sure your system has docker and docker-compose installed
- Then generate an image of our application with following command
```
  docker build -t lms-app .
```
- After image built succesfully, run docker-compose command to containarize our application
```
  docker-compose up 
```

# Navigate to localhost:8080/login
```
  Email: john.doe@gmail.com
  Password: admin123
```


### To generate migration files
```
flask db init
flask db migrate -m "Initial migration"
```

# Flask environment variables
| Name | Description |
| ----------- | ----------- |
| FLASK_APP | Name of the application i.e app |
| FLASK_ENV | Run time environment |
| FLASK_RUN_PORT | Port of the application |
| FLASK_RUN_HOST | Host of the application |
| FLASK_DEBUG | Boolean value to enable/disable debug mode |

# Application environment variables
| Name | Description |
| ----------- | ----------- |
| SECRET_KEY | Secret key of the application |
| DATABASE_URI | Database uri for connection |

# Additional links
- https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/