"""
A page of the application.
Page content is imported from the slide_4.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, State
import pandas as pd

your_total = State.diningOut
percentages=[("US Average Amount of Money Spent on Food per Month",166.00), ("How Much Money You Spent on Food this Month",your_total)]
data = pd.DataFrame(percentages, columns= ["Food Spending", "Money Spent ($)"])

slide_4 = Markdown("pages/slide_4/slide_4.md")
