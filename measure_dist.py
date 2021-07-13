"""
    Measeure geodesic distance between MKAD and given location

    Example:
        Cordinates should be tuple(float,float) type 
        (example: (55.898947, 37.632206))
        
        Kilometer
        >>> distace_to_mkad = Geodesic_dist(cordinates).km
        or meter
        >>> distace_to_mkad = Geodesic_dist(cordinates).m

"""

from typing import Tuple
import math

EARTH_RADIUS = 6371e3 # meters

MKAD_AREA=((55.571826, 37.368775), (55.911123, 37.843427))
MKAD_LOC=(55.898947, 37.632206)

class Geodesic_dist:
    meters:float
    def __init__(self, loc:Tuple):
        self.meters = 0

        # Checking whether it is within the Moscow Ring Road area.
        if self.is_in_area(loc,MKAD_AREA) == False:
            # Measure geodesic distance from given coordinates to MKAD
            self.meters = self.measure(loc,MKAD_LOC)
        else:
            self.meters= 0

    # Geodesic measurement function with two coordinates
    def measure(self,loc1:Tuple,loc2:Tuple) -> float:
        lat1,long1 = loc1[0],loc1[1]
        lat2,long2 = loc2[0],loc2[1]
        
        # lati,longi in radians
        lati1 = lat1 * math.pi/180 
        lati2 = lat2 * math.pi/180
        dif_lati = (lat2 - lat1) * math.pi/180
        dif_longi = (long2 - long1) * math.pi/180

        a = math.sin(dif_lati/2) * math.sin(dif_lati/2) + \
            math.cos(lati1) * math.cos(lati2) * \
            math.sin(dif_longi/2) * math.sin(dif_longi/2)
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        dist = EARTH_RADIUS * c

        return dist
    
    # Function to check whether the given coordinate is in given area.
    def is_in_area(self,loc:Tuple,area) -> bool:
        loc_lati,loc_long = loc[0],loc[1]

        area_low_lati,area_low_long  = area[0][0],area[0][1]
        area_up_lati,area_up_long  = area[1][0],area[1][1]

        return (area_low_lati<=loc_lati and loc_lati<=area_up_lati and 
                area_low_long<=loc_long and loc_long<=area_up_long)
    
    @property
    def meter(self):
        return self.meters

    @property
    def m(self):
        return self.meter
            
    @property
    def kilometer(self):
        return self.meters / 1000
        
    @property
    def km(self):
        return self.kilometer