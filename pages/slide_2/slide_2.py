"""
A page of the application.
Page content is imported from the slide_2.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""
from taipy.gui import Html, State
import pandas as pd
import csv
from openai import OpenAI
content = {}

def loadCsvFile(state):
    print(pd.read_csv(state.content))

#Begin shenanigans
prompt = "YOU ARE ONLY TO RETURN AN INTEGER AS AN ANSWER. THIS IS URGENT. ONLY AN INTEGER. Hello ChatGPT, your task is to analyze a financial statement and categorize it into one of 13 predefined categories. The categories are: 0: Housing, 1: Utilities, 2: Groceries, 3: Dining Out, 4: Transportation, 5: Healthcare, 6: Insurance, 7: Personal Spending, 8: Savings and Investments, 9: Debt Payments, 10: Subscriptions and Memberships, 11: Miscellaneous. UberEats and PostMates are dining out delivery services. Please respond only with the number of the category that best fits the expense. If you are more than kinda unsure which category it is, assume it belongs in misc. The name of the expense is: "

client = OpenAI(api_key='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')


categoryDict = {
  0: "Housing",
  1: "Utilities",
  2: "Groceries",
  3: "Dining Out",
  4: "Transportation",
  5: "Healthcare",
  6: "Insurance",
  7: "Personal Spending",
  8: "Savings and Investments",
  9: "Debt Payments",
  10: "Subscriptions and Memberships",
  11: "Miscellaneous"
}

totalPrices = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
totalRevenue = 4765

foodDelivery = [0,0.0]

def fillInDataFromCsv(fileName): #monthlyexpense is the planned
    file_name = fileName

    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        data_array = list(csvreader)

    for entry in data_array:
        nameOfPayment, price = entry[0], float(entry[1])

        if(price > 0): #Positive monetary value, 'income'
            # totalRevenue += price
            continue

        if ("ubereats" in nameOfPayment.lower()) or ("doordash" in nameOfPayment.lower()) or ("grubhub" in nameOfPayment.lower()) or ("gopuff" in nameOfPayment.lower()):
            foodDelivery[0]+=1
            foodDelivery[1]-= price

        categoryPrompt = prompt + nameOfPayment + " ONLY RETURN AN INTEGER. ONLY AN INTEGER."

        #Loop prompting ChatGPT until we receive 0-11 for category
        validCategory = False
        while(not validCategory):
            completion = client.chat.completions.create(model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": categoryPrompt}
            ])

            try:
                number = int(completion.choices[0].message.content.split(":")[0].strip())
            except ValueError:
                continue
            if(number>=0 and number <=11):
                validCategory = True


        # print("Current state of categoryDict:", categoryDict)

        # print(nameOfPayment + " was assigned to " + categoryDict[number])
        totalPrices[number] -= float(price)

fillInDataFromCsv("monthlyexpense.csv")
State.revenueTotal = totalRevenue
State.foodDelivery = foodDelivery
State.debtPaidTotal = totalPrices[9]


State.housing = totalPrices[0]
State.utilities = totalPrices[1]
State.groceries = totalPrices[2]
State.diningOut = totalPrices[3]
State.transportation = totalPrices[4]
State.healthcare = totalPrices[5]
State.insurance = totalPrices[6]
State.personalSpending = totalPrices[7]
State.savingsAndInvestments = totalPrices[8]
State.subscriptionsAndMemberships = totalPrices[10]
State.miscellaneous = totalPrices[11]
State.totalExpenses = sum(totalPrices)

highestIndex = 0
for i in range(len(totalPrices)):
    if totalPrices[i] > totalPrices[highestIndex]:
        highestIndex = i
State.highestCategory = [categoryDict[highestIndex],totalPrices[highestIndex]]
State.pricePrices = totalPrices




slide_2 = Html("""
<div style="width: 100%; height: 100%; position: relative; background: white">
    <div style="width: 1909px; height: 1231px; left: -235px; top: 0px; position: absolute; background: #2C909D">
        <div style="width: 981px; height: 154px; left: 471px; top: 108px; position: absolute; color: white; font-size: 128px; font-family: Sansita; font-weight: 700; word-wrap: break-word">Budget Wrapped</div>
        <div style="left: 591px; top: 303px; position: absolute; color: black; font-size: 48px; font-family: Sansita; font-weight: 700; word-wrap: break-word">Please upload your bank statement </div>
    </div>
    <div style="width: 464px; height: 442px; left: 492px; top: 395px; position: absolute; background: #2C909D; box-shadow: 0px 0px 48px rgba(24.54, 38.78, 89.25, 0.06)">
        <div style="width: 464px; height: 442px; left: 0px; top: 0px; position: absolute; background: #2C909D; border-radius: 24px"></div>
        <div style="padding-left: 5px; padding-right: 5px; padding-top: 4px; padding-bottom: 4px; left: 110px; top: 16px; position: absolute; background: #2C909D; box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.10) inset; border-radius: 40px; justify-content: flex-start; align-items: flex-start; gap: 4px; display: inline-flex">
            <div style="width: 134px; padding-left: 20px; padding-right: 20px; padding-top: 7px; padding-bottom: 7px; background: black; border-radius: 40px; justify-content: flex-end; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #2C909D; font-size: 16px; font-family: Inter; font-weight: 600; line-height: 14px; word-wrap: break-word">New Upload</div>
            </div>
            <div style="width: 95px; padding-left: 20px; padding-right: 20px; padding-top: 7px; padding-bottom: 7px; background: #2C909D; border-radius: 40px; justify-content: flex-end; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: black; font-size: 16px; font-family: Inter; font-weight: 600; line-height: 14px; word-wrap: break-word">Recent</div>
            </div>
        </div>
        <div style="width: 36px; height: 36px; left: 412px; top: 16px; position: absolute">
            <div style="width: 16px; height: 13.33px; left: 10px; top: 11px; position: absolute">
                <div style="width: 16px; height: 1.07px; left: 0px; top: 2.13px; position: absolute; background: black; border-radius: 8px"></div>
                <div style="width: 16px; height: 1.07px; left: 0px; top: 10.13px; position: absolute; background: black; border-radius: 8px"></div>
                <div style="width: 5.33px; height: 5.33px; left: 8px; top: 8px; position: absolute; background: #2C909D; border-radius: 9999px; border: 1.60px black solid"></div>
                <div style="width: 5.33px; height: 5.33px; left: 3.42px; top: 0px; position: absolute; background: #2C909D; border-radius: 9999px; border: 1.60px black solid"></div>
            </div>
            <div style="width: 36px; height: 36px; left: 0px; top: 0px; position: absolute; border-radius: 9999px; border: 1px #EBEFF2 solid"></div>
        </div>
        <div style="width: 464px; height: 374px; padding: 32px; left: 0px; top: 68px; position: absolute; background: #2C909D; border-top-left-radius: 24px; border-top-right-radius: 24px; flex-direction: column; justify-content: center; align-items: center; gap: 10px; display: inline-flex">
            <div style="align-self: stretch; flex: 1 1 0; border-radius: 24px; border: 2px #E2E6EA dotted; flex-direction: column; justify-content: center; align-items: center; display: flex">
                <div style="opacity: 0.50; text-align: center; color: #242634; font-size: 14px; font-family: SF Pro Display; font-weight: 400; word-wrap: break-word">Click to browse or drag and drop your files</div>
                <taipy:file_selector on_action="loadCsvFile" extensions=".csv,.xlsx" drop_message="Drop Message">{content}</taipy:file_selector>
            </div>
        </div>
        <div style="width: 464px; height: 1px; left: 0px; top: 68px; position: absolute; background: #EBEFF2"></div>
    </div>

</div>
""")
