
import mapquest_connect
import urllib.parse

class Steps:
    def output(self, json_result):
        '''Print locations for maneuvers.'''
        route = json_result['route']
        legs = route['legs']
        print('DIRECTIONS')
        for item in legs:
            maneuvers = item['maneuvers']
            for steps in maneuvers:
                print(steps['narrative'])
        



class TotalDistance:
    def output(self, json_result):
        '''Print total distance.'''
        route = json_result['route']
        len_distance = route['distance']
        distance = int(round(len_distance))
        print('TOTAL DISTANCE: {} miles'.format(distance))
        
            
        


class TotalTime:
    def output(self, json_result):
        '''Print the total time in minutes.'''
        route = json_result['route']
        raw_time = float(route['time'])
        min_sec = raw_time/60
        minutes = int(round(min_sec))
        print('TOTAL TIME: {} minutes'.format(minutes))
        
        
            
        
class LatLong:
    def output(self, json_result):
        '''Runs the entire sequence to receive and return latitude and longitude coordinates.'''
        coords = self.coords_list(json_result)
        self.print_pair(coords)
        
        
    def coords_list(self, json_result) -> list:
        '''Display the latitutude/longitude coordinates.'''
        coords_list = []
        route = json_result['route']
        locations = route['locations']
        latlong = locations
        for item in latlong:
            coordinates = item['latLng']
            coords_list.append(coordinates['lat'])
            coords_list.append(coordinates['lng'])

        return coords_list

    def print_pair(self, coords_list):
        '''Takes pairs in the list of coordinates and prints the latitude
        and longitude in the appropriate format.'''
        pair = self.pair(coords_list)
        print('LATLONGS')
        for item in pair:
            if item[0] < 0:
                coord = str(item[0])
                south_coord = coord.strip('-')
                float_coord = float(south_coord)
                north_south = '{:.2f}S'.format(float_coord)
            elif item[0] >= 0:
                north_south = '{:.2f}N'.format(item[0])

            if item[1] < 0:
                coord = str(item[1])
                west_coord = coord.strip('-')
                float_coord = float(west_coord)
                east_west = '{:.2f}W'.format(float_coord)
            elif item[1] >= 0:
                east_west = '{:.2f}E'.format(item[1])
                
            print('{} {}'.format(north_south, east_west))
                         
                         
    def pair(self, coordinates: list) -> list:
        '''Pairs each longitude and latitude coordinate in the coordinates list
           into individual lists in order to format and print the strings accordingly.'''
        values = []
        for val in range(0, len(coordinates), 2):
            values.append(coordinates[val:val+2])
        return values

    
    
                     
class Elevation:
    def output(self, json_result):
        '''Runs the entire sequence to receive and return elevation readings.'''
        l = LatLong()
        coords_list = l.coords_list(json_result)
        pairs = l.pair(coords_list)
        elevation_results = self.get_elevation(pairs)
        self.return_elevations(elevation_results)

        

    def height(self, json_result: 'json'):
        '''Gets elevation reading from the JSON formatted response.'''
        coords = []
        elevation_profile = json_result['elevationProfile']
        for item in elevation_profile:
            coords.append(item['height'])
        return coords



    def get_elevation(self, coordinates: list):
        '''Takes all elevation values and puts them into a list.'''

        values = []
        for c in coordinates:
            get_url = mapquest_connect.elevation_url(c)
            result = mapquest_connect.results(get_url)
            elevation = Elevation().height(result)
            values.append(elevation)

        return values


        



    def return_elevations(self, elevations: list):
        '''Prints all elevation values in appropriately converted values (feet)'''
        print('ELEVATION(S)')
        convert = 3.28084
        for item in elevations:
            conversion = item[0]*convert
            elevation = int(round(conversion))
            print(str(elevation)+" ft")
            
            
        
        

