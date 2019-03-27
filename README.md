# Setup

- Clone the project and `cd` in it's directory

- Install all the requirements
```
pip3 -r requirements.txt
```

- Launch the http server to serve example files
```
cd sample_data
python3 -m http.server 8080
```

- Launch the application
```
cd ../alar_async_requests
python3 manage.py runserver
```

- Go to `localhost:8000`