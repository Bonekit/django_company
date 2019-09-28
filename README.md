# A Django.Company Application

<!-- TABLE OF CONTENTS -->
## Index

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project
[![product-screenshot]]()

Django.Company is not my first Django application, but the first I like to release on GitHub. I had a lot of fun and learned many new things about Django, for this application I tried to use the class-based-views and currently I’m not a friend of this kind of views. I find that the function-based-views are a lot easier to customize and to use.

With my application you can use the following features:
* User-Defaults (login, registration, logout)
* Messages (JavaScript included)
* CRUD: Companies
* Upload images (Logos)
* Company-ListView with Pagination


### Built With

* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Django]([https://djangoproject.com])
* [Bootswatch]([https://bootswatch.com])
* [Python](https://python.org)


<!-- GETTING STARTED -->
## Getting Started

**Please do not use my application for production with the current settings!**

### Installation

* Install Python 3.7.4
* Install virtualenv
```
pip install virtualenv
```
* Create the virtual environment for Django
```
mkdir django_example
cd django_example
virtualenv venv
```
* MacOS and Linux
`source venv/bin/activate`

* Windows
`venv/script/activate`

* Install Django
```
pip install django
pip install sqlparse
````
* Now: Clone the application
* Prepare the database

**If you like to use other databases then sqlite3, please google how to configure Postgres, MySQL in the Django settings**

```
python manage.py makemigrations
python manage.py migrate
```
* Collect all static files from the applications
```
python manage.py collectstatic
```
* Create a super user for the admin area
```
python manage.py createsuperuser
```
* Engines start
```
python manage.py runserver
```

<!-- USAGE EXAMPLES -->
## Usage

You can use this simple application to create companies with a few informations about them and add a logo. 
There is a list about all added companies, from there you can update, delete the companies and you can click on the brand to see more details about a specific company. 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Tobias Menzel - [@BonekitDEV](https://twitter.com/BonekitDEV)

Project Link: [https://github.com/Bonekit/django_company](https://github.com/Bonekit/django_company)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Django]([https://djangoproject.com])
* [Bootswatch]([https://bootswatch.com])
* [Python](https://python.org)
* [othneildrew]([https://github.com/othneildrew])

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: https://raw.githubusercontent.com/Bonekit/django_company/master/screenshot.png