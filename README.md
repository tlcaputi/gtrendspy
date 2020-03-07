# theo_timeline: Pull and merge data from the Google Trends for Health API

This code has no license. Theodore Caputi (Copyright 2020) retains all rights over all code stored in this repo.


## Functionality
---

The main function of the package is `theo_timeline`. An example script would be:

```
import gtrends

gtrends.functions.theo_timeline(
    terms = ['corona', 'corona + symptoms'],
    names = ['corona', 'symptoms'],
    start = '2018-01-01',
    end = '2020-02-01',
    timeframe_list = ['month'],
    geo_country_list = ['US', 'CA'],
    geo_dma_list = [None],
    geo_region_list = [None],
    worldwide = False,
    timestep_years = 1,
    batch_size = 2,
    us_states = False,
    outpath = "C:/Users/tcapu/Google Drive/modules/gtrends",
    creds = "C:/Users/tcapu/Google Drive/modules/gtrends/info.py"
)
```

## Getting Started
---

(1) Request an SSH Deploy Key for this project from tcaputi@gmail.com.

(2) Install the package using the following command:

`pip install --upgrade git+ssh://git@github.com/tlcaputi/gtrends#egg=gtrends`

(3) Create an info file with your own parameters (SERVER, API_VERSION, DISCOVERY_URL_SUFFIX, DISCOVERY_URL, API_KEY)

(4) Begin using the package!
