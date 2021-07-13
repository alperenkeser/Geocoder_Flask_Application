from flask import Blueprint, request, render_template, redirect
import logging

from database import geocode_table, db
from geocoder import Geocoder
from key import API_KEY
from measure_dist import Geodesic_dist  

geo_search = Blueprint('geo_search',__name__)

# Loggin configuration
logging.basicConfig(filename='mkad_distance_searches.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@geo_search.route('/', methods=['POST', 'GET'])
def index():
    geocoder = Geocoder(API_KEY)

    if request.method == 'POST':
        # The searched address is taken from this line.
        address_content = request.form['search_address']      

        # The coordinates of the address searched with the geocoder are found.
        cordinates = geocoder.cordinates(address=address_content)

        # The distance between the Moscow Ring Road and the address is found.
        distace_to_mkad = Geodesic_dist(cordinates).km

        #The obtained data is prepared to be written to the database.
        new_content = geocode_table(name=address_content,
                                    longitude=cordinates[0],
                                    latitude=cordinates[1],
                                    distance=distace_to_mkad)

        # The obtained data is written to the log file.
        logging.info(" Adress: {}".format(address_content))
        logging.info(" Cordinates: {}".format(cordinates))
        
        if(distace_to_mkad == 0):
            logging.info(" This location already in MKAD")
        else:
            logging.info(" Distace to MKAD: {}".format(distace_to_mkad))

        # The prepared data is written to the database.
        try:
            db.session.add(new_content)
            db.session.commit()
            return redirect('/')
        except:
            logging.error(' There was an issue searching your address')
            return 'There was an issue searching your address'

    else:
        #It renders the index.html page.
        addresses = geocode_table.query.order_by(geocode_table.date_created).all()
        return render_template('index.html',addresses=addresses)