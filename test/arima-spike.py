#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pull and merge data from the Google Trends API

Copyright (c) 2020 Theodore L Caputi

"""

__author__ = "Theodore L Caputi"
__copyright__ = "Copyright 2020, Theodore L Caputi"
__credits__ = ""
__license__ = "No License"
__version__ = "1.0.0"
__maintainer__ = "Theodore L Caputi"
__email__ = "tcaputi@mit.edu"
__status__ = "Development"



# One Geography
from pyper import *
import pandas as pd
import numpy as np
import datetime
import tempfile



def run_arima(fn, interrupt, geo):

    df = pd.read_csv(fn)
    r.df = df
    r.interrupt = interrupt
    r.geo = geo


    r(
        '''
        library(imputeTS)
        US_df <- run_arima(
          df = df,
          interrupt = interrupt,
          geo = geo
        )
        '''
    )

    return(r.US_df)




def arima_plot(obj, US_df, xlab, ylab, beginplot, endplot, lbreak, linelabel, interrupt, lwd, save, width, height, outfn):

    r.US_df = US_df
    r.xlab = xlab
    r.ylab = ylab
    r.beginplot = beginplot
    r.endplot = endplot
    r.lbreak = lbreak
    r.linelabel = linelabel
    r.interrupt = interrupt
    r.lwd = lwd
    r.save = save
    r.width = width
    r.height = height
    r.outfn = outfn

    r(
    '''
    {} <- arima_plot(
      US_df,
      title = NULL,
      xlab = "Date",
      ylab = "Query Fraction\n(Per 10 Million Searches)",
      beginplot = "2019-09-01",
      endplot = "2020-01-15",
      lbreak = "1 month",
      linelabel = "Tobacco 21\nSigned",
      interrupt = ymd("2019-12-19"),
      lwd = 1,
      save = T,
      width = 6,
      height = 3,
      outfn = './output/panB.pdf'
    )

    '''.format(obj)
    )




def line_plot(obj, US_df, beginplot, endplot, interrupt, linelabel, xlab, ylab, lbreak, lwd, save, height, width, outfn):
    r.US_df = US_df
    r.beginplot = beginplot
    r.endplot = endplot
    r.interrupt = interrupt
    r.linelabel = linelabel
    r.xlab = xlab
    r.ylab = ylab
    r.lbreak = lbreak
    r.lwd = lwd
    r.save = save
    r.height = height
    r.width = width
    r.outfn = outfn

    r(
    '''
    {} <- line_plot(
      US_df,
      beginplot = T,
      endplot = T,
      interrupt = "2019-12-19",
      linelabel = "Tobacco 21\nSigned",
      title = NULL,
      xlab = "Date",
      ylab = "Query Fraction\n(Per 10 Million Searches)",
      lbreak = "3 year",
      lwd = 0.3,
      save = T,
      height = 3,
      width = 6,
      outfn = './output/panA_py.png'
    )
    '''.format(obj)
    )


def savefig(title, objects, labels, ncol, nrow, rel_height, out, base_width, base_height):

    r.ncol = ncol
    r.nrow = nrow
    r.rel_height = rel_height
    r.out = out
    r.base_width = base_width
    r.base_height = base_height


    txt ='''
    rtitle <- ggdraw() +
      draw_label(
        '{}',
        fontface = 'bold',
        hjust = 0.5
      ) +
      theme(
        plot.margin = margin(0, 0, 0, 7)
      )
    '''.format(title)
    print(txt)
    r(txt)


    txt ='''
    tmpfig <- plot_grid({}, labels={}, ncol=ncol, nrow=nrow, rel_height=rel_height)
    '''.format(', '.join(objects), 'c("' + '","'.join(labels) + '")')
    print(txt)
    r(txt)


    txt ='''
    outfig <- plot_grid(rtitle, tmpfig, ncol = 1, rel_heights = c(0.1, 1))
    save_plot(out, outfig, base_width=base_width, base_height=base_height)
    '''
    print(txt)
    r(txt)


def state_pct_change(obj, fn, interrupt, preperiod, endperiod, scaletitle, linecol, lowcol, midcol, highcol, save, width, height, outfn):


    df = pd.read_csv(fn)
    df.columns = [re.sub("US_", "", x) for x in df.columns.tolist()]
    r.df = df

    r.interrupt = interrupt
    r.preperiod = preperiod
    r.endperiod = endperiod
    r.scaletitle = scaletitle
    r.linecol = linecol
    r.lowcol = lowcol
    r.midcol = midcol
    r.highcol = highcol
    r.save = save
    r.width = width
    r.height = height
    r.outfn = outfn

    r(
    '''
    {} <- state_pct_change(
      df,
      interrupt = interrupt,
      preperiod = preperiod,
      endperiod = endperiod,
      scaletitle = scaletitle,
      linecol = linecol,
      lowcol = lowcol,
      midcol = midcol,
      highcol = highcol,
      save = save,
      width = width,
      height = height,
      outfn = outfn,
    )
    '''.format(obj)
    )


def state_arima(r_name, fn, interrupt):

    df = pd.read_csv(fn)
    df.columns = [re.sub("US_", "", x) for x in df.columns.tolist()]
    r.data = df
    r.interrupt = interrupt

    r(
    '''
    {} <- state_arima(
      data = data,
      interrupt = interrupt
    )
    '''.format(r_name)
    )

    return(r.state_list)


def open_r_df_from_list(df_from_list):
    '''
    This is a work-around to allow you to open data frames from lists that you
    access from a list returned by R. It creates a tempfile, saves the data frame
    as a CSV to the tempfile, then reads the tempfile back into Python.
    '''

    tmpfile = tempfile.NamedTemporaryFile(mode='w', delete = False)

    if 'timestamp' in df_from_list.columns.tolist():
        timestamps = df_from_list['timestamp'].str.decode("utf-8")
        if any([True if x else False for x in timestamps]):
            df_from_list['timestamp'] = timestamps

    if 'state' in df_from_list.columns.tolist():
        states = df_from_list['state'].str.decode("utf-8")
        if any([True if x else False for x in states]):
            df_from_list['state'] = states

    pd.DataFrame(df_from_list).to_csv(tmpfile.name, index = False)
    df = pd.read_csv(tmpfile.name)

    return(df)


def state_arima_spaghetti(obj, state_list, interrupt, xlab = None, ylab  = None,
                            linelabel  = None, lbreak  = None, lwd = None,
                            beginplot = None, endplot = None, xfmt = None,
                            states_with_labels = None, states_to_exclude = None,
                            save = None, width = None, height = None, outfn = None
                            ):


    df = open_r_df_from_list(state_list['spaghetti'])
    r.data = df
    r('names(data) <- gsub("X[.]|[.]", "", names(data))')

    r.interrupt = state_list['interrupt']
    r.xlab = xlab
    r.ylab = ylab
    r.linelabel = linelabel
    r.lbreak = lbreak
    r.lwd = lwd
    r.beginplot = beginplot
    r.endplot = endplot
    r.save = save
    r.width = width
    r.height = height
    r.outfn = outfn


    r(
    '''
    {} <- state_arima_spaghetti(
      state_arima_list = data,
      interrupt = interrupt,
      xlab = xlab,
      ylab = ylab,
      linelabel = linelabel,
      lbreak = lbreak,
      lwd = lwd,
      beginplot = beginplot,
      endplot = endplot,
      xfmt = {},
      states_with_labels = {},
      states_to_exclude = {},
      save = save,
      width = width,
      height = height,
      outfn = outfn,
    )
    '''.format(obj, xfmt, 'c("' + '","'.join(states_with_labels) + '")', 'c("' + '","'.join(states_to_exclude) + '")')
    )


def state_arima_pctdiff(obj, state_list, save, width, height, outfn):

    df = open_r_df_from_list(state_list['summary'])
    df.columns = [re.sub("US_", "", x) for x in df.columns.tolist()]

    r.df = df
    r('names(df) <- gsub("X[.]|[.]", "", names(df))')
    r.save = save
    r.width = width
    r.height = height
    r.outfn = outfn

    r(
    '''
    {} <- state_arima_pctdiff(
      df,
      save = save,
      width = width,
      height = height,
      outfn = outfn,
    )
    '''.format(obj)
    )






r = R(use_pandas = True)
r("library('gtrendR')")


ROOTPATH = "C:/Users/tcapu/Google Drive/PublicHealthStudies/tob21searches"
r("setwd('{}')".format(ROOTPATH))


US_df = run_arima(
            fn = "{}/lt/buycigs_day.csv".format(ROOTPATH),
            interrupt = "2019-12-19",
            geo="US"
)


line_plot(
    "panA",
    US_df,
    beginplot = True,
    endplot = True,
    interrupt = "2019-12-19",
    linelabel = "Tobacco 21\nSigned",
    xlab = "Date",
    ylab = "Query Fraction\n(Per 10 Million Searches)",
    lbreak = "3 year",
    lwd = 0.3,
    save = True,
    height = 3,
    width = 6,
    outfn = './output/panA_py.png'
)


arima_plot(
    "panB",
    US_df,
    beginplot = True,
    endplot = True,
    interrupt = "2019-12-19",
    linelabel = "Tobacco 21\nSigned",
    xlab = "Date",
    ylab = "Query Fraction\n(Per 10 Million Searches)",
    lbreak = "3 year",
    lwd = 0.3,
    save = True,
    height = 3,
    width = 6,
    outfn = './output/panB_py.png'
)


savefig(
    title = "Google Searches for Buying Tobacco Online",
    objects = ['panA', 'panB'],
    labels = ['A', 'B'],
    ncol = 1,
    nrow = 2,
    rel_height = [1, 1.1],
    out = "./output/Fig1_py3.png",
    base_width = 6,
    base_height = 6
)



ROOTPATH = "C:/Users/tcapu/Google Drive/PublicHealthStudies/buyguns"
r("setwd('{}')".format(ROOTPATH))


state_list = state_arima(
    r_name = "rstatelist",
    fn = "{}/input/buyguns_week.csv".format(ROOTPATH),
    interrupt = "2020-03-01"
)


state_pct_change(
  obj="panC",
  fn = "{}/input/buyguns_week.csv".format(ROOTPATH),
  interrupt = "2020-03-01",
  preperiod = 90,
  endperiod = "2020-03-23",
  scaletitle = "% Increase\nin Searches",
  linecol = "gray",
  lowcol = "red",
  midcol = "white",
  highcol = "dodgerblue4",
  save = True,
  width = 6,
  height = 3,
  outfn = './output/panC.png'
)

state_arima_spaghetti(
  obj="panD",
  state_list = r.rstatelist,
  interrupt = "2020-03-01",
  xlab = "Date",
  ylab = "Actual Versus Model-Fitted\nSearch Queries (% Diff.)",
  linelabel = "COVID-19\nOutbreak",
  lbreak = "1 week",
  lwd = 0.4,
  beginplot = "2020-02-23",
  endplot = "2020-03-16",
  xfmt = 'date_format("%d %b")',
  states_with_labels = ['CA', 'NY', 'US'],
  states_to_exclude = ['IA'],
  save = True,
  width = 6,
  height = 4,
  outfn = "./output/panD.png"
)



state_arima_pctdiff(
  obj="panE",
  state_list = r.rstatelist,
  save = True,
  width = 6,
  height = 3,
  outfn = './output/panE.png'
)


savefig(
    title = "Google Searches for Purchasing Guns",
    objects = ['panC', 'panD', 'panE'],
    labels = ['C', 'D', 'E'],
    ncol = 1,
    nrow = 3,
    rel_height = [1.1, 1, 1.1],
    out = "./output/Fig2_py3.png",
    base_width = 7,
    base_height = 12
)
