"""
A page of the application.
Page content is imported from the slide_6.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, State


data =  {
    "Categories of Spending": ["Housing","Utilities","Groceries","Dining Out", "Transportation","Healthcare", "Insurance", "Personal Spending", "Savings and Investments", "Debt Payments", "Subscriptions and Memberships", "Miscellaneous"],
    "Amount ($)": [State.housing, State.utilities, State.groceries, State.diningOut, State.transportation, State.healthcare, State.insurance, State.personalSpending, State.savingsAndInvestments, State.debtPaidTotal, State.subscriptionsAndMemberships, State.miscellaneous]
}


slide_6 = Markdown("pages/slide_6/slide_6.md")
