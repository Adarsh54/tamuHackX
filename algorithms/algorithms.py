"""
This file is designed to contain the various Python functions used to configure tasks.

The functions will be imported by the __init__.py file in this folder.
"""
import os
import csv
from openai import OpenAI




client = OpenAI(api_key='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')


prompt = "YOU ARE ONLY TO RETURN AN INTEGER AS AN ANSWER. THIS IS URGENT. ONLY AN INTEGER. Hello ChatGPT, your task is to analyze a financial statement and categorize it into one of 13 predefined categories. The categories are: 0: Housing, 1: Utilities, 2: Groceries, 3: Dining Out, 4: Transportation, 5: Healthcare, 6: Insurance, 7: Personal Spending, 8: Savings and Investments, 9: Debt Payments, 10: Subscriptions and Memberships, 11: Miscellaneous. UberEats and PostMates are dining out delivery services. Please respond only with the number of the category that best fits the expense. If you are more than kinda unsure which category it is, assume it belongs in misc. The name of the expense is: "


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
totalRevenue = 0

foodDelivery = [0,0.0]

def fillInDataFromCsv(fileName): #monthlyexpense is the planned
    file_name = fileName

    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        data_array = list(csvreader)

    for entry in data_array:
        nameOfPayment, price = entry[0], float(entry[1])

        if(price > 0): #Positive monetary value, 'income'
            totalRevenue += price
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

def getRevenueInfo():
    return totalPrices[9]
    # return "This month you paid $" + str(totalPrices[9]) + " in debt off! Good work, keep chipping away!"

def getFoodDeliveryInfo():
    return foodDelivery

def getTopSpendingCategoryInfo():
    highestIndex = 0
    for i in range(len(totalPrices)):
        if totalPrices[i] > totalPrices[highestIndex]:
            highestIndex = i
    return [categoryDict[highestIndex],totalPrices[highestIndex]]

def getDebtInfo():
    return totalPrices[9]

def getDiningInfo():
    return totalPrices[3]


# ##################################################################################################################
# PLACEHOLDER: Put your Python functions here                                                                      #
#                                                                                                                  #
# Example:                                                                                                         #
# def place_holder_algorithm():                                                                                    #
#     pass                                                                                                         #
# Comment, remove or replace the previous lines with your own use case                                             #
# ##################################################################################################################
