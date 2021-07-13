## Overview

This Flask application calculates the distance to moscow ring road by geodesic measurement by finding the given address with geocoder. These calculated data are written to the database.

After running this application, you can calculate the distance by going to the 'http://localhost:5000' page and giving the address.

The api I used to create this application is Yandex's geocoder api. The coordinates of the address searched with Yandex geocoder api are found and the geodesic distance is calculated in the measure_dist.py file I created. The found data is written to address.db and to the 'mkad_distance_searches.log' file.

## Requierements

pull down the source code from this Github repository:

```sh
$ git clone https://github.com/alperenkeser/Geocoder_Flask_Application
```

Create a new virtual environment:

```sh
# Windows
$ python -m venv .venv
```

```sh
# macOS/Linux
$ python3 -m venv .venv
```

Activate the virtual enviroment

```sh
# Windows
$ .venv\Scripts\activate
```

```sh
# macOS/Linux
source .venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Run server to serve the Moscow Ring Road Distance Finder Flask application:

```sh
(venv) $ flask run
```

Navigate to 'http://localhost:5000' to view the website!

## Testing

Before the run tests you should run server.

Run all tests:

```sh
(venv) $ python test.py
```


