#'STEP 4-FINAL STEP-START'
import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help="State the type of calculation you want here, choose "
                                             "either 'annuity or 'diff'")
parser.add_argument("--principal", type=int, help="enter credit principal here")
parser.add_argument("--periods", type=int, help="enter number of periods here")
parser.add_argument("--interest", type=float, help="enter your annual interest rate here")
parser.add_argument("--payment", type=float, help="enter your monthly payment here")
args = parser.parse_args()
success_flag = False


def differentiated_calc():
    principal = args.principal
    months = args.periods
    nominal_interest = args.interest / (100 * 12)
    monthly_payments = []
    for m in range(1, months + 1):
        dm = principal / months + nominal_interest * (principal - (principal * (m - 1)) / months)
        monthly_payments.append(math.ceil(dm))
        print("Month {}: paid out {}".format(m, math.ceil(dm)))
    else:
        print("\nOverpayment = {}".format(round(sum(monthly_payments) - principal)))


def duration_calc():
    principal = args.principal
    monthly_payment = args.payment
    interest = args.interest / 100
    nominal_interest = interest / 12
    duration_calc = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest * principal),
                                       1 + nominal_interest))
    duration_years = int(duration_calc / 12)
    duration_months = duration_calc % 12
    if duration_years == 0:
        print("You need {} months to repay this credit!".format(duration_months))
    elif duration_months == 0:
        print("You need {} years to repay this credit!".format(duration_years))
    else:
        print("You need {} years and {} months to repay this credit!".format(duration_years, duration_months))
    print("Overpayment = {}".format(math.ceil(monthly_payment * duration_calc - principal)))

def principal_calculation():
    annuity = args.payment
    months = args.periods
    interest = args.interest / 100
    nominal_interest = interest / 12
    principal = annuity / (nominal_interest / (1 - pow(1 + nominal_interest, -months)))
    print("Your credit principal = {}!".format((math.floor(principal))))
    print("Overpayment = {}".format(math.ceil(annuity * months - principal)))


def annuity_calculation():
    principal = args.principal
    months = args.periods
    interest = args.interest / 100
    nominal_interest = interest / 12
    annuity = math.ceil(principal * (nominal_interest / (1 - pow(1 + nominal_interest, -months))))
    print("Your annuity payment = {}!".format(annuity))
    print("\nOverpayment = {}".format(annuity * months - principal))


def check_args():
    global success_flag
    d = vars(args)
    count = 0
    for each in d.values():
        if each is None:
            count += 1
        elif type(each) is not str:
            if each < 0:
                print("Principal, payment, interest rate and months need to be positive. Please check your values")
                return
    if count >= 2:
        print("Incorrect number of parameters: please specify correct number of parameters")
        return
    elif args.type != "diff" and args.type != "annuity":
        print("Incorrect parameters: please input either 'annuity' or 'diff' for type")
    elif args.type == "diff" and args.payment:
        print("For differentiated payment plan, 'payment' argument is invalid, since it changes each month")
        return
    elif args.interest is None:
        print("Incorrect parameters: please specify annual interest rate")
        return
    success_flag = True


check_args()
if success_flag:
    if args.type == "annuity" and args.payment is None:
        annuity_calculation()
    if args.type == "annuity" and args.principal is None:
        principal_calculation()
    if args.type == "annuity" and args.periods is None:
        duration_calc()
    if args.type == "diff" and args.payment is None:
        differentiated_calc()
