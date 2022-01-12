# eTraining


![GitHub repo size](https://img.shields.io/github/repo-size/Filaraya/eTraining)
![GitHub contributors](https://img.shields.io/github/contributors/Filaraya/eTraining)
![GitHub stars](https://img.shields.io/github/stars/Filaraya/eTraining?style=social)
![GitHub forks](https://img.shields.io/github/forks/Filaraya/eTraining?style=social)


eTraining is a web application that allows the employees to do attend companies capacity building via online.

eTraining web application has features to Create, Read, Update and Delete (CRUD) materials like text, image, video and Files. The Admin (the company owner) manages all the CRUD operations in the web application. The user (employee or consultant) can create an account and able to attend the virtual training and materials.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* create virtualenv and install requirements 
```
python3
pip install -r requirements.txt 
```
## Installing eTraining

Create database tables, user for admin panel and run project.
```
python manage.py makemigrations
python manage.py migrate`
python manage.py createsuperuser`
python manage.py runserver
```

## Contact

If you want to contact me you can reach me at <faraya1@live.maryville.edu>.

## Deployment
The project has deployed on PythonAnywhere. this is the link URL 
http://fili.pythonanywhere.com/
