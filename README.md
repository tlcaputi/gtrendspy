# Pull and merge data from the Google Trends for Health API

This code has no license. Theodore L Caputi (Copyright 2020) retains all rights over all code in this package. Unauthorized use, including reuse, modification, and distribution, is forbidden.


## Usage

To use the [gtrends package for Python3](https://www.github.com/tlcaputi/gtrends), you'll need to request an API Key from Google. You can do that easily [here](https://docs.google.com/forms/d/e/1FAIpQLSenHdGiGl1YF-7rVDDmmulN8R-ra9MnGLLs7gIIaAX9VHPdPg/viewform).

The main function of the package is `theo_timeline`, a function that pulls and merges data from the Google Trends API and saves a single CSV file for each term (dates on the index and geographies as the columns). Note that multiple files will be created if multiple timeframes are requested. An example script would be:

```{python}

from gtrendspy import timeline

timeline.theo_timeline(
    terms = ['cat', 'cat + food'],
    names = ['cat', 'food'],
    start = '2018-01-01',
    end = '2020-02-01',
    timeframe_list = ['month'],
    geo_country_list = ['US', 'CA'],
    worldwide = False,
    timestep_years = 1,
    batch_size = 2,
    us_states = False,
    outpath = "/path/to/output/directory",
    creds = "/path/to/info.py"
)

```

This script would pull monthly data for the search terms `cat` and `cat + food` for both the US and Canada between 1 Jan 2018 and 1 Feb 2020, and then reformat that data into two CSV files (`cat_month.csv` and `food_month.csv`, respectively). Each of these CSV files would be formatted such that the first column (timestamp) gives the month and the second and third columns (US and CA) give search queries for the US and Canada, respectively.

This package is intended to be used in conjunction with the [gtrendR package for R](https://www.github.com/tlcaputi/gtrendR).

## Getting Started

Note: This package assumes use of Python 3.X and pip3. It works on Linux and Windows OS.

### Install from pip

(1) pip install from Github

```console
pip install gtrendspy
```

(2) pip install requirements.txt

```console
pip install -r requirements.txt
```

(3) Create a `creds` file setting your own parameters (DISCOVERY_URL, API_KEY)

(4) Begin using the package! The merged output will be in the directory you named as `outpath`.



### Tarball

(1) Request tarball (gtrends.tar.gz) from tcaputi@gmail.com

(2) Run the command:

```console
pip install --upgrade /path/to/gtrends.tar.gz
```

(3) Install dependencies using the command:

```console
pip install -r /path/to/gtrends/requirements.txt
```

(4) Create a `creds` file setting your own parameters (DISCOVERY_URL, API_KEY)

(5) Begin using the package! The merged output will be in the directory you named as `outpath`.
