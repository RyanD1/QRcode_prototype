# -*- coding: utf-8 -*-
"""Excel File Parser

This module handles excel file verification and processing.
It first verifies whether the input file is a valid excel file.
It then verifies whether the given excel file is compitable to the 
given template format.

This module supports the following file formats: .xls, .xlsx.

This module requires the following packages: pandas, xlsm, openpyxl

Example:

Attributes:

Todo:

"""

import xlrd
from sys import getsizeof


def verifyExcel(file):
    """Verifies if input file is a valid excel file.

    Verifies the input file. Raise not valid file error if input file
    is not a valid excel file supported by this module.

    Args:
        file (str): Path of input file.

    Returns:
        xlrd.book.Book: The workbook object of valid input file.
            return None if file is not valid.
    """
    try:
        workbook = xlrd.open_workbook(file, on_demand=True)
        # print(workbook, type(workbook), getsizeof(workbook))

        # worksheet = workbook.sheet_by_index(0)
        # print(worksheet, type(worksheet), getsizeof(worksheet))
        # # cell(row, col)
        # val1 = worksheet.cell(0, 0).value
        # val2 = worksheet.cell(0, 1).value
        # val3 = worksheet.cell(0, 2).value
        # val4 = worksheet.cell(0, 3).value
        # print(val1, type(val1), getsizeof(workbook))
        # print(val2, type(val2), getsizeof(workbook))
        # print(val3, type(val3), getsizeof(workbook))
        # print(val4, type(val4), getsizeof(workbook))
        return workbook
    except xlrd.XLRDError:
        print("not valid excel file")
        return False
    except FileNotFoundError:
        print("file not found")
        return False


def verifyTemplate(workbook):
    """Verifies if input file is a valid excel file.

    Verifies the input file. Raise not valid file error if input file
    is not a valid excel file supported by this module.

    Args:
        file (str): Path of input file.

    Returns:
        bool: True for valid excel file, False otherwise.
    """

    return True


def parseExcel(file):
    return
