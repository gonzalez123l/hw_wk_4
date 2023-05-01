class roi():
    
    def __init__(self):
        self.income = 0
        self.expense = 0
        self.cashflow = 0
        self.investment_total = 0
        self.roi_amount = 0

    def income_total(self):
        self.income = float(input("enter your total monthly income:"))

    def monthly_expenses(self):
        insurance = float(input("How much do you spend on insurance each month?"))
        mortgage = float(input("How much is your mortgage?"))
        utility = float(input("How much are your utilities?"))
        proprty_management = float(input("How much do you spend on proprty management?"))
        repairs = float(input("How much do you spend on repairs?:"))
        cleaning = float(input("How much do you spend on cleaning fees?"))
        miscellaneous = float(input("Do you have any miscellaneous expenses such as HOA, lawn or others?"))

        self.expense = insurance + mortgage + utility + proprty_management + repairs + cleaning + miscellaneous

    def cashflow_total(self):
        self.cashflow = self.income - self.expense
        print(f"Based on the numbers provided this is your estimated monthly cashflow amount {self.cashflow}")

    def calculate_investment(self):
        closing = float(input("How much was your closing cost?"))
        lump_sum = float(input("How much was your down payment total?"))
        other_expense = float(input("How much did you expend on other expenses like repairs or advertising costs?"))

        self.investment_total = closing + lump_sum + other_expense
        self.roi_amount = (self.cashflow*12) / self.investment_total
        roi_percentage = self.roi_amount *100
        print(f"Based on the answer you provided your return on investment will be approximately {roi_percentage}%")
# I keep getting a high ROI which I don't believe is entirely accurate so I don't believe that the formulas used to calulate totals is correct.

ROI = roi()
ROI.income_total()
ROI.monthly_expenses()
ROI.cashflow_total()
ROI.calculate_investment()
