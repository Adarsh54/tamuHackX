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
revenueTotal = State.revenueTotal
#Your total estimated revenue for this month is $(revenueTotal), keep on raking it in!


# def loadCsvFile(state):
#     print(pd.read_csv(state.path))

# slide_3 = Markdown("pages/slide_3/slide_3.md")
html_content = f"""
<div style="width: 100%; height: 100%; position: relative; background: white">
    <div style="width: 1909px; height: 1231px; left: -235px; top: 0px; position: absolute; background: #ffb5b5">
        <div style="width: 981px; height: 154px; left: 471px; top: 108px; position: absolute; color: black; font-size: 60px; font-family: Sansita; font-weight: 700; word-wrap: break-word">Your total revenue for this month is:<br></br><span style="color: #00A86B;">${revenueTotal}</span>, keep on raking it in! <br></br>Your expenses for this month were:<br></br><span style="color: #990F02;">${int(State.totalExpenses)}</span>, try to keep an eye on your spending. </div>
    </div>

</div>
"""

slide_3 = Html(html_content)
