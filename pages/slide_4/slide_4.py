"""
A page of the application.
Page content is imported from the slide_4.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, State

# percentages=[(1852,50.83), (1856,45.29), ..., (2016,46.09), (2020,51.31)]
# data = pandas.DataFrame(percentages, columns= ["Year", "%"])

# path = {}
totalRevenue = State.revenueTotal
print(str(totalRevenue) + " was the total revenue you made!")


# def loadCsvFile(state):
#     print(pd.read_csv(state.path))

slide_4 = Markdown("pages/slide_4/slide_4.md")
