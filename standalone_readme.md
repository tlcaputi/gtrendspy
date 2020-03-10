## Using the package

(1) Add your SSH key to the repo

(2) Install the package from pip

`pip install --upgrade git+ssh://git@github.com/tlcaputi/gtrends#egg=gtrends`

(3) Create a `creds` file setting your own parameters (SERVER, API_VERSION, DISCOVERY_URL_SUFFIX, DISCOVERY_URL, API_KEY)

(4) Use the package with a script following this example, which would pull monthly data for the search terms `cat` and `cat + food` and save them into CSV files `cat_month.csv` and `food_month.csv`:

```
from gtrends import timeline

timeline.theo_timeline(
    terms = ['cat', 'cat + food'],
    names = ['cat', 'food'],
    start = '2018-01-01',
    end = '2020-02-01',
    timeframe_list = ['month'],
    geo_country_list = ['US', 'CA'],
    worldwide = False,
    us_states = False,
    timestep_years = 1,
    batch_size = 2,
    outpath = "/path/to/output/dir",
    creds = "/path/to/creds.txt"
)

```
