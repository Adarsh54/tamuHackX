import taipy as tp
from taipy.gui import Gui

from taipy import Core, Rest
from pages import *


pages = {
    "/": root_page,
    "slide_1": slide_1,
	"slide_2": slide_2,
	"slide_3": slide_3
}


if __name__ == "__main__":
    rest = Rest()
    core = Core()
    core.run()
    # #############################################################################
    # PLACEHOLDER: Create and submit your scenario here                           #
    #                                                                             #
    # Example:                                                                    #
    # from configuration import scenario_config                                   #
    # scenario = tp.create_scenario(scenario_config)                              #
    # scenario.submit()                                                           #
    # Comment, remove or replace the previous lines with your own use case        #
    # #############################################################################

    gui = Gui(pages=pages)
    tp.run(gui, rest, title="tamuHackX")
