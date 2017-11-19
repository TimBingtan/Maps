
import urllib.request
import urllib.parse
import json

BASE_URL = 'http://open.mapquestapi.com/'

api_key = '''Kept hidden for security and privacy'''
secret = '''Kept hidden for security and privacy'''
# API cannot function without these values


def get_route(locations: list) -> str:
    '''Takes a list of locations and parses them into URL format.'''
    
    query_parameters = [('key', api_key), ('from', locations[0])]
    for i in range(1, len(locations)):
        query_parameters.append(('to',locations[i]))

    return BASE_URL + 'directions/v2/route?' + urllib.parse.urlencode(query_parameters)


def results(url: str) -> 'json':
    '''Receives and decodes URL response in JSON format.'''
    response = None
    
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    
    except:
        print()
        print('MAPQUEST ERROR')
        
    finally:
        if response != None:
            response.close()


def elevation_url(coordinates: list) -> str:
    '''Takes the query parameters of the elevation and parses into URL format.'''
    coords_list = []
    for item in coordinates:
        coords_list.append(item)
    str_coordinates = str(coords_list)
    strip_list = str_coordinates.strip('[]')
    latlong = strip_list.replace(' ', '')
    query_parameters = [
        ('key', api_key),  ('shapeFormat', 'raw')
        ]
    
    return BASE_URL + 'elevation/v1/profile?' + urllib.parse.urlencode(query_parameters) + '&latLngCollection=' + latlong


