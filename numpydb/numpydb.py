'''
Created on Sep 3, 2010

@author: John Salvatier
'''
import numpy as np

from datetime import datetime
import decimal
    
def execute(db, command):
    """ executes a command and turns the results into a numpy recarray (record array)"""
    cursor = db.cursor()
    cursor.execute(command)
    
    column_dtypes = [(col[0], _convert(col[1])) for col in cursor.description]
    
    return np.fromiter((tuple (row) for row in cursor), dtype=column_dtypes, count = cursor.rowcount)




def time_column(date, column_name):
    """ makes a string for calculating a time as (decimal) number of days since a date for a MySQL column. This is because the numpy.datetime datatype is not well developed."""
    return "TIME_TO_SEC(timediff(" + column_name + ",'" +  str(datetime.strptime(date, date_format)) + "'))/(60*60*24) as " + column_name

date_format = '%Y-%m-%d'


_type_conversions = {decimal.Decimal : float}
def _convert(type):
    try :
        return _type_conversions[type]
    except:
        return type