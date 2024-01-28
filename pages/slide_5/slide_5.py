"""
A page of the application.
Page content is imported from the slide_3.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, State, Html
content = {}


# percentages=[(1852,50.83), (1856,45.29), ..., (2016,46.09), (2020,51.31)]
# data = pandas.DataFrame(percentages, columns= ["Year", "%"])

# path = {}
#stuff = getRevenueInfo()
debtPaid = int(State.debtPaidTotal)
#Your total estimated revenue for this month is $(revenueTotal), keep on raking it in!




# def loadCsvFile(state):
#     print(pd.read_csv(state.path))

# slide_3 = Markdown("pages/slide_3/slide_3.md")


# Assuming the debt_paid value contains the relevant information


html_content = f"""
<div style="width: 100%; height: 100%; position: relative; background: white">
    <div style="width: 1909px; height: 1231px; left: -235px; top: 0px; position: absolute; background: #0096c7">
        <div style="width: 981px; height: 154px; left: 471px; top: 100px; position: absolute; color: black; font-size: 50px; font-family: Sansita; font-weight: 700; word-wrap: break-word">
            <div style="font-size: 100px; font-weight: bold;">Let's Talk About Debt...</div>
            You paid back ${debtPaid} worth of debt. These small victories can lead to debt freedom in the long term, so keep it up!
        </div>
    </div>
</div>
"""

# Create an Html object with the formatted content

slide_5 = Html(html_content)
