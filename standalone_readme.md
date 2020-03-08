## Using the package

(1) Use this SSH key:

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDgeaTOl5ywdENPnUBbaWQyvVBEsUIS4ACsqPDFiEkgnIsEwTYS/yssy/qhokYLgAzLPGL9JupnayU++lhfZ6PVLqXDi9AqtH9CsgaFcmNd6BNyuAla5hjYqPDFwFyt6I4zMneNjCwDTsR/KiC0bZ2hwfaKm607lxmW9fdldjfsM4MYrh3UZ7fRYCF5uscgp5cbK0Bn39CMqyVL2jH1a9JyIGgKlxG5+GJuAl5WJuVjJTWd3p+OtrMkX5H1oMjKwI5ANZu2h95En0dMmpGRPRt8qunE4DNEit5tY9EfQeuShaZT8Ml3hVm69QevsjHkKIU4IMCSWYEoqy2Kve6GtKGxdiCewM/Hy+kchqRBzvaGCt1WaSQlV6jDdEJ9Hd2fAd//ThLzVb0/nKj+85KxGgsAZvROre3osCJO+RQ/33VlRUvk72sG0EVCAL03yBHBVQtK85I3XUqyHX4mRMV5aZz2S+ezoihyCIH0kNGNLA3dSEYUJ32CoOlEFW38kDaHZzYPfTdPmBWaYgRitrAila+qc+iPqqnkzTr1ITDvOP5GgXhDeOGOiD46pyQJrOsXyAuJ5t/fAXcSv2Fgq73eqvPsEYA188AJrhR6rzSZupRi5OqK3ry27+AZ1vu4+9j0tKLinDpP0YanlamrAuv+X+9r+C+XwwFgFp5S+v+HL/RwDw== tcaputi@gmail.com

(2) Install the package from pip

`pip install --upgrade git+ssh://git@github.com/tlcaputi/gtrends#egg=gtrends`

(3) Create a `creds` file with your access parameters (SERVER, API_VERSION, DISCOVERY_URL_SUFFIX, DISCOVERY_URL, API_KEY)

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
