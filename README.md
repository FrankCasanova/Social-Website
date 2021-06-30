# Social-Website
A social web site
------------------PROJECT IN DEVELOPMENT--------------------

I hope can deploy this soon, but is some tedious

This project is just for training concepts like OAuth and complex functions with Redis

------------------------
I want dockerize all
fix some bugs
TDD has not been aplied, I want to cover all project 
and then create a deploy versión
----------------------- 

for WSL:
sudo service postgresql restart
sudo service redis-server start
source venv/bin/activate

for test with certificate host use:

python manage.py runserver_plus --cert-file cert.crt

main page:
https://mysite.com:8000/account/


-A follow system using many-to-many relationships with an 
intermediary model.

-Activity stream using generic relations and 
optimized QuerySets to retrieve related objects.

-Django signals, a signal receiver function to denormalize 
related object counts.

-Application configuration classes, to load signal handlers.

-I used Redis in this project to store item views, 
and built an image ranking with Redis.

------------------PROJECT IN DEVELOPMENT--------------------

