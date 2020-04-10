import pprint
from apiclient.discovery import build
import pandas as pd

SERVER = 'https://www.googleapis.com'

API_VERSION = 'v1beta'
DISCOVERY_URL_SUFFIX = '/discovery/v1/apis/trends/' + API_VERSION + '/rest'
DISCOVERY_URL = SERVER + DISCOVERY_URL_SUFFIX
API_KEY = 'AIzaSyCmAh_lLmd9oM5HDFhD65yGvPqq5gognSc' # Theo's Key


service = build('trends', 'v1beta',
                  developerKey=API_KEY,
                  discoveryServiceUrl=DISCOVERY_URL)

# Top queries, no restrictions.
top_queries = service.getTopQueries(term='apple')
response = top_queries.execute()
pprint.pprint(response)

topterms = [x.get('title') for x in response['item']]
topterms[0:10]
