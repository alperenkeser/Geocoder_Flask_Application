from exceptions import  InvalidKey, NothingFound, UnexpectedResponse

from typing import Tuple

import requests

class Geocoder:
    """
        Yandex Geocoder API:

        Yandex Geocoder API class is find address to cordinates,
        address to area cordinates and cordinates to address.

        Example:
            First you need to enter the api key.
            >>> from geocoder import Geocoder
            >>> geocoder = Geocder("your API_KEY")

            Finding cordinate -> finds coordinate from given address
            (it returns tuple(float(latitude), float(longitude)))
            >>> cordinates = geocoder.cordinates("your address")

            Finding area cordinates -> finds area lower and upper cordinates from given address
            (it returns lowerCordinate, upperCordinate)
            (each cordinate have tuple(float(latitude), float(longitude)))
            >>> area_cordinates = geocodcer.area_cordinates("your address")


            Finding address -> finds address from given cordinates
            (it returns string)
            >>> address = geocoder.address(your_latitude,your_longitude) 

    """
    api_key: str

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _request(self, address: str) -> dict:
        response = requests.get(
                    "https://geocode-maps.yandex.ru/1.x/",
                    params = dict(format="json", apikey=self.api_key, geocode=address, lang="en-US"),
        )

        if response.status_code == 200:
            return response.json()["response"]
        elif response.status_code == 403:
            raise InvalidKey()
        else:
            raise UnexpectedResponse(
                f"status_code={response.status_code}, body={response.content}"
            )
    
    def cordinates(self, address: str) -> Tuple[float]:
        
        data = self._request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        cordinates = data[0]["GeoObject"]["Point"]["pos"]
        
        long, lati = tuple(cordinates.split(" "))

        return float(lati), float(long)
        #return cordinates

    def area_cordinates(self,address: str) -> Tuple[tuple]:
        data = self._request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        lowerCorner = data[0]["GeoObject"]["boundedBy"]["Envelope"]["lowerCorner"]
        upperCorner = data[0]["GeoObject"]["boundedBy"]["Envelope"]["upperCorner"]

        lower_long, lower_lati = tuple(lowerCorner.split(" "))
        upper_long, upper_lati = tuple(upperCorner.split(" "))

        lowerCordinate = (float(lower_lati),float(lower_long))
        upperCordinate = (float(upper_lati),float(upper_long))

        return lowerCordinate,upperCordinate

    def address(self, lati: float, long: float) -> str:

        got = self._request(f"{long},{lati}")
        data = got["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{lati} {long}"')

        return data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]