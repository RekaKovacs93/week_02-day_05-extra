import math

class CompoundInterest:
    def __init__(self, principal_amount, rate, num_of_years, per_month):
        self.principal_amount = principal_amount
        self.rate = rate
        self.num_of_years = num_of_years
        self.final_amount = 0
        self.per_month = 0

    def calculate(self):
        first = 1 + (self.rate / 12)
        second = 12 * self.num_of_years
        self.final_amount += round((first ** second) * self.principal_amount , 2)
        return self.final_amount
    
    # def calculate_with_monthly_payment(self):
    #     # A = P * ((1 + r/n)^(n*t) - 1)/(r/n)
    #     first = 1 + (self.rate / 12)
    #     second = 12 * self.num_of_years
    #     third = first ** second
    #     fourth = (third - 1) / (self.rate / 12)
    #     self.final_amount += round(fourth * self.principal_amount , 2)
    #     return self.final_amount
        

# def calculate_compound_interest_with_contributions():
#     principal = float(input("Enter the starting amount: "))
#     rate = float(input("Enter the annual interest rate (as a decimal): "))
#     years = int(input("Enter the number of years: "))
#     n = 12 # compounded monthly
#     contribution = float(input("Enter the monthly contribution: "))
#     A = principal
#     for i in range(years * n):
#         A = A * (1 + rate/n) + contribution * ((1 + rate/n) ** (i+1) - (1 + rate/n))
#     return round(A, 2)

