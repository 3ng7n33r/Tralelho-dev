
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/3ng7n33r/Tralelho-dev/tree/mob)
# Tralelho

Tralelho is a tanslation service for medical professionals

## Translators needed
This project needs translators. If you speak a language other than English, French or German and would like to contribute, please don't hesitate to [contact me](mailto:tralelho@maxemailian.anonaddy.com). A translation service integration has been set up to make translating this project as simple as possible.

## Installation

After cloning the repo, some steps have to be taken for a proper setup.
Pre-requisites:
<ul>
<li>Python</li>
<li>pip</li>
<li>virtualenv (optional but recommended)</li>
</ul> 
It is recommended to set up a virtual environment.

    $ virtualenv ~/tralelho


Once set up and enabled we install the necessary python packages from the requirements.txt file:

    $ pip3 install -r requirements.txt
    
Now the database has to be migrated:

    $ python manage.py migrate
    
and the fixtures will populate the database. The order is important here:

    $ python manage.py loaddata languages.json
    $ python manage.py loaddata countries.json
   
 And the project should be ready to go. You can take a look at the website with:

     python manage.py runserver

## Contributing
Please have a look in the Issues section.
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPL3](https://choosealicense.com/licenses/gpl-3.0/)
