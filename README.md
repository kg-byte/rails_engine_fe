
<!-- ABOUT THE PROJECT -->
# Rails Engine
## About This Project
*Rails Engine FE* is a Django Application that consumes several endpoints rendered by *[Rails Engine Repository](https://github.com/kg-byte/rails-engine)*. The purpose of this project is to demonstrate Service Oriented Architecture where font-end and back-end team chose to build their applications using different programming languages. 

<p align="right">(<a href="#top">back to top</a>)</p>

## Features Implemented:

- [x] Consume the following V1 Endpoints to render data to user:
    - [x] All merchants with merchant names as links to their show page:
       - [x] Backend endpoint:```GET http://localhost:3000/api/v1/merchants```
       - [x] Frontend url(root): ```http://127.0.0.1:8000/```
      <img width="800" alt="image" src="https://user-images.githubusercontent.com/97060659/170410828-9c97abd6-7f5b-4eb0-bae0-dc9879995835.png">
    - [x] One merchant with items of thtat merchant with item names as links to item show page:
       - [x] Backend endpoint:```GET http://localhost:3000/api/v1/merchants/{{merchant_id}}```
       - [x] Frontend url: ```http://127.0.0.1:8000/{{merchant_id}}```
       <img width="800" alt="image" src="https://user-images.githubusercontent.com/97060659/170410937-f403b84d-64e6-4c7b-9d36-a33357810ba3.png">
    - [x] All items with item names as links to the item show page:
       - [x] Backend endpoint: ```GET http://localhost:3000/api/v1/items```
       - [x] Frontend url: ```http://127.0.0.1:8000/items```
      <img width="800" alt="image" src="https://user-images.githubusercontent.com/97060659/170411435-afc8fcfd-b6ad-454c-b9f3-033c39184693.png">
    - [x] Items show page with item details:
       - [x] Backend endpoint: ```GET http://localhost:3000/api/v1/items/{{item_id}```
       - [x] Frontend url: ```http://127.0.0.1:8000/items/{{item_id}}```
      <img width="800" alt="image" src="https://user-images.githubusercontent.com/97060659/170411563-8041975c-2f96-462b-8849-4ebb55e55b8d.png">
    - [x] Search Mercants by name via search bar on home page:
       - [x] Backend endpoint: ```GET http://localhost:3000/api/v1/merchants/find?name=iLl```
       - [x] Frontend url(landing page): ```http://127.0.0.1:8000/](http://127.0.0.1:8000/search?...search=group``` 
       <img width="800" alt="image" src="https://user-images.githubusercontent.com/97060659/170412820-56711eef-fc00-476f-a6c8-0beca2404fef.png">
    - [x] Edge case handled in search merchants by name: no user input for search:
       <img width="800" alt="image" src="https://user-images.githubusercontent.com/97060659/170412875-eeed7e3a-e843-4818-bca9-f868e8bb2a3e.png">

    
<p align="right">(<a href="#top">back to top</a>)</p>

## Installation

 As neither the front-end or the back-end service is held on a public server, please follow the following instructions to start both front-end/back-end servers to navigate the urls and run tests.
 
### Pre-requiste: Clone the backend [Rails Engine Repo](https://github.com/kg-byte/rails_engine_fe) and start server:

1. Fork and/or Clone the BE repo 
  ```
  git clone git@github.com:kg-byte/viewing_party.git
  ```
2. Install gems and dependencies
  ```
   bundle install
  ```
3. Set up db/seed file with the following content:
  ```
  cmd = "pg_restore --verbose --clean --no-acl --no-owner -h localhost -U $(whoami) -d rails-engine_development db/data/rails-engine-development.pgdump"
puts "Loading PostgreSQL Data dump into local database with command:"
puts cmd
system(cmd)
```
4. Run the following line and you may see lots of output including some warnings/errors from pg_restore that you can ignore. 
  ```
   db:{drop,create,migrate,seed}
  ```
5. Run the following line - Check to see that your schema.rb exists and has the proper tables/attributes that match the data
  ```
  rails db:schema:dump
  ```
7. Run run test suit 
  ```
  bundle exec rspec
  ```
8. Start the server to service API requests:
  ```
  rails s
  ```
  
<p align="right">(<a href="#top">back to top</a>)</p>

### Clone and set up Rails Engine FE (this repo):

1. Fork and/or Clone this repo 
  ```
  git clone git@github.com:kg-byte/rails_engine_fe.git
  ```
2. Set up and activate a virtual environment in the repository directory:
  ```
  python3 -m venv my_env
  source my_env/bin/activate
  ```
3. Install the `django`, `requests` and any other required modules:
  ```
  pip install django
  pip3 install requests
  ```
4. Start the server:
  ```
  python manage.py runserver
  ```
5. Run tests:
  ```
  python ./manage.py test
  ```
6. Visit the front-end urls mentioned above in features implemented, e.g., the homepage(merchannt index page):
  ```
  http://127.0.0.1:8000/
  ```
  
<p align="right">(<a href="#top">back to top</a>)</p>

## Built With

* [Django Framework](https://www.djangoproject.com/)


<p align="right">(<a href="#top">back to top</a>)</p>

## Versions

- [Python 3.9.13](https://www.python.org/downloads/release/python-3913/#:~:text=According%20to%20the%20release%20calendar,only%20form%20until%20October%202025.)

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributors
<p>
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
</p>

- Author: [Kim Guo](https://www.linkedin.com/in/kim-guo-5331b4158/)


<p>
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</p>

- Author: [Kim Guo](https://github.com/kg-byte)

<p align="right">(<a href="#top">back to top</a>)</p>


