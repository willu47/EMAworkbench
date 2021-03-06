
"""
Python model /Users/jhkwakkel/EMAworkbench/test/test_connectors/../models/Sales_Agent_Motivation_Dynamics.py
Translated using PySD version 0.7.2
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'Motivation Adjustment': 'motivation_adjustment',
    'Months of Expenses per Sale': 'months_of_expenses_per_sale',
    'Total Cumulative Sales': 'total_cumulative_sales',
    'Motivation': 'motivation',
    'Time': 'time',
    'Motivation Adjustment Time': 'motivation_adjustment_time',
    'Total Effort Available': 'total_effort_available',
    'INITIAL TIME': 'initial_time',
    'Success Rate': 'success_rate',
    'Sales': 'sales',
    'Accumulating Income': 'accumulating_income',
    'FINAL TIME': 'final_time',
    'Effort Required to Make a Sale': 'effort_required_to_make_a_sale',
    'Tenure': 'tenure',
    'Still Employed': 'still_employed',
    'Impact of Motivation on Effort': 'impact_of_motivation_on_effort',
    'Startup Subsidy Length': 'startup_subsidy_length',
    'Motivation Threshold': 'motivation_threshold',
    'Accumulating Sales': 'accumulating_sales',
    'SAVEPER': 'saveper',
    'Total Cumulative Income': 'total_cumulative_income',
    'Sales Effort Available': 'sales_effort_available',
    'Effort': 'effort',
    'TIME STEP': 'time_step',
    'TIME': 'time',
    'Accumulating Tenure': 'accumulating_tenure',
    'Fraction of Effort for Sales': 'fraction_of_effort_for_sales',
    'Income': 'income',
    'Startup Subsidy': 'startup_subsidy'}


@cache('step')
def accumulating_sales():
    """
    Accumulating Sales
    ------------------
    (accumulating_sales)
    Persons/Month

    """
    return sales()


@cache('run')
def startup_subsidy_length():
    """
    Startup Subsidy Length
    ----------------------
    (startup_subsidy_length)
    Month

    """
    return 6


@cache('run')
def motivation_threshold():
    """
    Motivation Threshold
    --------------------
    (motivation_threshold)


    """
    return 0.1


@cache('step')
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Month
    The initial time for the simulation.
    """
    return 0


@cache('run')
def startup_subsidy():
    """
    Startup Subsidy
    ---------------
    (startup_subsidy)
    Dmnl
    Months of expenses per month
    """
    return 0.5


integ_total_cumulative_sales = functions.Integ(lambda: accumulating_sales(), lambda: 0)


@cache('run')
def success_rate():
    """
    Success Rate
    ------------
    (success_rate)
    Dmnl

    """
    return 0.2


@cache('step')
def effort():
    """
    Effort
    ------
    (effort)
    Hours/Month

    """
    return sales_effort_available() * impact_of_motivation_on_effort(motivation())


@cache('run')
def months_of_expenses_per_sale():
    """
    Months of Expenses per Sale
    ---------------------------
    (months_of_expenses_per_sale)
    Month/Person

    """
    return 12 / 50


@cache('step')
def accumulating_tenure():
    """
    Accumulating Tenure
    -------------------
    (accumulating_tenure)
    Months/Month

    """
    return still_employed()


def impact_of_motivation_on_effort(x):
    """
    Impact of Motivation on Effort
    ------------------------------
    (impact_of_motivation_on_effort)
    Dmnl

    """
    return functions.lookup(x, [0, 0.285132, 0.448065, 0.570265, 0.733198, 0.95723, 1.4664, 3.19756, 4.03259], [
                            0, 0.0616114, 0.232228, 0.492891, 0.772512, 0.862559, 0.914692, 0.952607, 0.957346])


@cache('step')
def motivation_adjustment():
    """
    Motivation Adjustment
    ---------------------
    (motivation_adjustment)
    1/Month

    """
    return (income() - motivation()) / motivation_adjustment_time()


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Month [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('step')
def motivation():
    """
    Motivation
    ----------
    (motivation)
    Dmnl

    """
    return integ_motivation()


@cache('step')
def total_cumulative_income():
    """
    Total Cumulative Income
    -----------------------
    (total_cumulative_income)
    Month
    Express income in units of 'months of expenses'
    """
    return integ_total_cumulative_income()


@cache('step')
def still_employed():
    """
    Still Employed
    --------------
    (still_employed)
    Dmnl

    """
    return functions.if_then_else(motivation() > motivation_threshold(), 1, 0)


@cache('step')
def tenure():
    """
    Tenure
    ------
    (tenure)
    Month

    """
    return integ_tenure()


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Month [0,?]
    The time step for the simulation.
    """
    return 0.0625


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Month
    The final time for the simulation.
    """
    return 200


@cache('step')
def total_cumulative_sales():
    """
    Total Cumulative Sales
    ----------------------
    (total_cumulative_sales)
    Persons

    """
    return integ_total_cumulative_sales()


@cache('run')
def effort_required_to_make_a_sale():
    """
    Effort Required to Make a Sale
    ------------------------------
    (effort_required_to_make_a_sale)
    Hours/Person

    """
    return 4


@cache('step')
def sales_effort_available():
    """
    Sales Effort Available
    ----------------------
    (sales_effort_available)
    Hours/Month

    """
    return functions.if_then_else(
        still_employed() > 0,
        total_effort_available() *
        fraction_of_effort_for_sales(),
        0)


@cache('run')
def fraction_of_effort_for_sales():
    """
    Fraction of Effort for Sales
    ----------------------------
    (fraction_of_effort_for_sales)
    Dmnl

    """
    return 0.25


@cache('run')
def total_effort_available():
    """
    Total Effort Available
    ----------------------
    (total_effort_available)
    Hours/Month

    """
    return 200


@cache('step')
def income():
    """
    Income
    ------
    (income)
    Dmnl
    Technically in units of months of expenses earned per month
    """
    return months_of_expenses_per_sale() * sales() + functions.if_then_else(time() <
                                                                            startup_subsidy_length(), startup_subsidy(), 0)


integ_motivation = functions.Integ(lambda: motivation_adjustment(), lambda: 1)


integ_tenure = functions.Integ(lambda: accumulating_tenure(), lambda: 0)


integ_total_cumulative_income = functions.Integ(lambda: accumulating_income(), lambda: 0)


@cache('step')
def sales():
    """
    Sales
    -----
    (sales)
    Persons/Month

    """
    return effort() / effort_required_to_make_a_sale() * success_rate()


@cache('run')
def motivation_adjustment_time():
    """
    Motivation Adjustment Time
    --------------------------
    (motivation_adjustment_time)
    Month

    """
    return 3


@cache('step')
def accumulating_income():
    """
    Accumulating Income
    -------------------
    (accumulating_income)
    Month/Month

    """
    return income()


def time():
    return _t


functions.time = time
functions._stage = lambda: _stage
