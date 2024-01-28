"""
A page of the application.
Page content is imported from the slide_3.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown

# percentages=[(1852,50.83), (1856,45.29), ..., (2016,46.09), (2020,51.31)]
# data = pandas.DataFrame(percentages, columns= ["Year", "%"])

# path = {}

# def loadCsvFile(state):
#     print(pd.read_csv(state.path))

slide_3 = Markdown("pages/slide_3/slide_3.md")
