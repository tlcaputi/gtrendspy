
from googleapiclient.discovery import build
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import tempfile
import shutil
import pandas as pd
import math
import functools
import numpy as np
import re
import sys
import statistics
from gtrendspy import timeline


def get_top_terms(
            term='',
            number=25,
            type='top',
            start = None,
            end = None,
            region = None,
            creds = None,
            service = None
            ):

    if service is None and creds is not None:
        # Set parameters
        global API_KEY
        global SERVER
        global API_VERSION
        global DISCOVERY_URL_SUFFIX
        global DISCOVERY_URL

        f = open(creds, 'r')
        for line in f:
            exec(line, globals())

        service = build('trends', 'v1beta',
                          developerKey=API_KEY,
                          discoveryServiceUrl=DISCOVERY_URL)


    if type=='top':
        top_queries = service.getTopQueries(
                term=term,
                restrictions_startDate=start,
                restrictions_endDate=end,
                restrictions_geo=region
                )
    elif type=='rising':
        top_queries = service.getRisingQueries(
                term=term,
                restrictions_startDate=start,
                restrictions_endDate=end,
                restrictions_geo=region
                )

    response = top_queries.execute()
    topterms = [x.get('title') for x in response['item']]
    return(topterms[0:number])



def theo_timeline_top(root_terms, num_terms_per_root, start, end, timeframe_list, timestep_years,
                  outpath, creds, geo_country_list = [None],
                  geo_dma_list  = [None], geo_region_list  = [None],
                  worldwide = False, batch_size = 30, us_states = False,
                  rm_US_ = True):

    # Set parameters
    global API_KEY
    global SERVER
    global API_VERSION
    global DISCOVERY_URL_SUFFIX
    global DISCOVERY_URL

    f = open(creds, 'r')
    for line in f:      exec(line, globals())

    service = build('trends', 'v1beta',
                        developerKey=API_KEY,
                        discoveryServiceUrl=DISCOVERY_URL)

    regions = geo_country_list + geo_dma_list + geo_region_list + region
    regions_notnone = [x for x in regions if x is not None]
    assert len(regions_notnone) in [0, 1]

    if len(regions_notnone) == 1:
        region = regions_notnone[0]
    else:
        region = None


    # Make the start and end date into datetime format
    start_month = datetime.strptime(start, '%Y-%m-%d').strftime('%Y-%m')
    end_month = datetime.strptime(end, '%Y-%m-%d').strftime('%Y-%m')

    all_terms = []
    for root_term in root_terms:
        top_terms = get_top_terms(
                term=root_term,
                number=num_terms_per_root,
                type='top',
                start = start_month,
                end = end_month,
                region = region,
                service = service)

        all_terms = all_terms + top_terms

    all_terms = list(set(all_terms))
    names = [re.sub(" ", "", x) for x in all_terms]

    timeline.theo_timeline(
        terms = all_terms,
        names = names,
        start = start,
        end = end,
        timeframe_list = timeframe_list,
        timestep_years = timestep_years,
        outpath = outpath,
        creds = creds,
        geo_country_list = geo_country_list,
        geo_dma_list  = geo_dma_list,
        geo_region_list  = geo_region_list,
        worldwide = worldwide,
        batch_size = batch_size,
        us_states = us_states,
        rm_US_ = rm_US_
    )


def main():

    theo_timeline_top(
            root_terms = ['apple', 'cats'],
            num_terms_per_root = 3,
            start = '2019-01-01',
            end = '2020-01-01',
            timeframe_list = ['month'],
            timestep_years = 1,
            outpath = "C:/Users/tcapu/Google Drive/modules/gtrendspy/test/output",
            creds = "C:/Users/tcapu/Google Drive/modules/gtrendspy/info_theo.py",
            region = ['US'],
            geo_country_list = [None],
            geo_dma_list  = [None],
            geo_region_list  = [None],
            worldwide = False,
            batch_size = 29,
            us_states = False,
            rm_US_ = True
            )

if __name__ == "main":
    main()
