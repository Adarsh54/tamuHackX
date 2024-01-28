import taipy as tp
from taipy.gui import Gui, State

from taipy import Core, Rest
from pages import *
"""
This file is designed to contain the various Python functions used to configure tasks.

The functions will be imported by the __init__.py file in this folder.
"""
import os
import csv
from openai import OpenAI


pages = {
    "/": root_page,
    "LOGIN": slide_1,
	"UPLOAD": slide_2,
    "REVENUE": slide_3,
	"DINING": slide_4,
    "DEBT": slide_5,
    "SUMMARY": slide_6,
    "BOT": slide_7
}











if __name__ == "__main__":
    rest = Rest()
    core = Core()
    core.run()
    # fillInDataFromCsv("monthlyexpense.csv")
    # print(getRevenueInfo())
    # #############################################################################
    # PLACEHOLDER: Create and submit your scenario here                           #
    #                                                                             #
    # Example:                                                                    #
    # from configuration import scenario_config                                   #
    # scenario = tp.create_scenario(scenario_config)                              #
    # scenario.submit()                                                           #
    # Comment, remove or replace the previous lines with your own use case        #
    # #############################################################################

    gui = Gui(pages=pages, css_file="main.css")
    tp.run(gui, rest, title="tamuHackX")
