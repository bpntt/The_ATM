from ast import main
import csv
import atm_exeptions
import logging
#import atm_exeptions
#from atm_exeptions import  low_topup_error, low_balance_error, low_withdraw_error, user_not_found
logging.basicConfig(filename='ex_log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class machine:
    def __init__(self) -> None:
        pass

    def top_up(balance):
        topup = int(input("Enter the deposit amount:\n"))
        try:
            balance = balance + topup
            print(f"balace is: {balance}")
        except topup < 50:
            #atm_exeptions.low_topup_error()
            logging.error("Withdraw cannot be less then 50")
            machine.top_up(balance)

        return balance

    def top_up_modifed(balance):
        topup = int(input("Enter the deposit amount:\n"))
        if topup < 50:
            #atm_exeptions.low_topup_error()
            logging.error("Topup cannot be less then 50")
            machine.top_up_modifed()
        else:
                balance = balance + topup - topup*0.03
                print(f"balace is: {balance}")

        return balance

    def withdraw_cash(balance):
        count_of_withdraw = int(input("Withdraw money:\n"))
        total_withdraw = count_of_withdraw + machine.tax_calculator(count_of_withdraw) 
        if count_of_withdraw < 50:
            #atm_exeptions.low_withdraw_error()
            logging.error("Withdraw cannot be less then 50")
            print(f"balace is: {balance}")
            machine.withdraw_cash(balance)
        elif total_withdraw > balance:
            #atm_exeptions.low_balance_error()
            logging.error("Balace have no enought money")
            print(f"balace is: {balance}")
        elif count_of_withdraw < balance:
            if total_withdraw < balance:
                if balance < 5000000:
                    balance = balance - total_withdraw
                    print(f"balace is: {balance}")
                else:
                    balance = (balance - total_withdraw) - total_withdraw*0.1
                    print(f"balace is: {balance}")

            return balance
        
    def withdraw_cash_modifed(balance):
        count_of_withdraw = int(input("Withdraw money:\n"))
        total_withdraw = count_of_withdraw + machine.tax_calculator(count_of_withdraw) 
        if count_of_withdraw < 50:
            #atm_exeptions.low_withdraw_error()
            print(f"balace is: {balance}")
            machine.withdraw_cash_modifed(balance)
        elif total_withdraw > balance:
            #atm_exeptions.low_balance_error()
            logging.error("Balace have no enought money")
            print(f"balace is: {balance}")
        elif count_of_withdraw < balance:
            if total_withdraw < balance:
                if balance < 5000000:
                    balance = (balance - total_withdraw) - total_withdraw*0.03
                    print(f"balace is: {balance}")
                else:
                    balance = (balance - total_withdraw) - total_withdraw*0.1 - total_withdraw*0.03
                    print(f"balace is: {balance}")

            return balance

    def tax_calculator(count):
        tax = count*0.015
        if tax < 30:
            tax = 30
        elif tax > 600:
            tax= 600
        return tax

    def tax_calculator_modifed(count):
        tax = count*0.015
        luxuary_tax = count*0.1
        if tax < 30:
            tax = 30
        elif tax > 600:
            tax= 600
        print(f"tax amound {tax} + 'luxury tax' {luxuary_tax}. Final tax: {tax + luxuary_tax}\n")
    def tax_politics():
        question = input("Questions about the commission for cash withdrawal:\n About the commission for cash withdrawal or top up(1)\n Tax calculator(2)\n")
        while True:
            if question == "1":
                print("The Bank charges a cash withdrawal fee of 1.5 percent of the withdrawal amount. Non less then 30 and non more then 600\n")
                print("You have 3 free top ups or withdraws only. After this 3 procent commission will be charged\n")
                answer = input("Is there more than 5000000 on your account?\n Yes(1)\n No(2)\n")
                if answer =="1":
                        print("If you account has more than 5 million, the bank withdraws a commission equal to 1.5 percent + 10 percent of the withdrawal amount.\n")
                        break
                elif answer =="2": 
                    print("You have no other tax\n")
                    break
            elif question == "2":
                answer = input("Is there more than 5000000 on your account?\n Yes(1)\n No(2)\n")
                if answer =="2":
                    tax = int(input("Input you potentional withdraw:\n"))
                    tax_final =machine.tax_calculator(tax)
                    print(f"You tax: {tax_final}")
                    break
                    
                elif answer == "1":
                    tax =int(input("Input you potentional withdraw:\n"))
                    machine.tax_calculator_modifed(tax)
                    break
                    

    def balance_check(balance):
        print(f"\n{balance} \n")

    def notification():
        print("After the following action, an additional 3 procent commission will be charged\n")
    
    def self_introdaction():
        name= input("Write you name:\n")
        f_name = input("Write you family name:\n")
        return name, f_name 
    
    def create_an_account(name_in,f_name_in):
        print(name_in,f_name_in)
        with open("account_list.csv", mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter="|", lineterminator="\r")
            file_writer.writerow([{name_in}, {f_name_in}, int(0)])
            print(f"account has been created! name = {name_in}, family name = {f_name_in}, balace = 0")


            
    
    def hello_window():
        income = input("Welcome to the Atm! Do you have an account: 1(Y) / 2(N) \n:")
        print(income)
        name, f_name = machine.self_introdaction()
        print(name,f_name)
        match income:
            case "1":
                with open ("account_list.csv", "r") as file:
                    read = csv.reader(file)
                    print(read)
                    for row in read: 
                        if name and f_name in row:
                            print(f"{name = }, {f_name =}, balace = {row[2]}")
                            return int(row[2])
                        else: 
                            #atm_exeptions.user_not_found()
                            logging.error("User not found")
                            answer = input("Do you want to create an account? \n1(Y)/2(N)")
                            match answer:
                                case "1" |"Y"|"y":
                                    machine.create_an_account(name,f_name)
                                case "2"|"N"|"n":
                                    print("Good bye!")
                                    machine.hello_window()
            case "2"|"N"|"n":
                machine.create_an_account(name,f_name)
                with open ("account_list.csv", "r") as file:
                    read = csv.reader(file)
                    for row in read: 
                        if name and f_name in row:
                            print(f"{name = }, {f_name =}, balace = {row[2]}")
                            return int(row[2])

    #def changer (input_code):
    #    match input_code:
    #        case "1":
    #            with open
    


    def main(self):
        account_balance = machine.hello_window()

        count_of_movments = 0
        while True:
            if count_of_movments == 2:
                    machine.notification()
            choice = input("What do you wnat to do:\n Check account balace (1)\n Withdraw (2)\n Top Up account (3)\n About tax politics(4)\n Change the account (5)\n Stop(6):\n ")
            try: 
                match choice:
                    
                    case "1":
                        machine.balance_check(account_balance)
                    case"2":
                        if count_of_movments<3:
                            account_balance = machine.withdraw_cash(account_balance)
                            count_of_movments+=1
                        else:
                            account_balance = machine.withdraw_cash_modifed(account_balance)
                            count_of_movments+=1
                    case "3":
                        if count_of_movments<3:
                            account_balance = machine.top_up(account_balance)
                            count_of_movments+=1
                        else:
                            account_balance = machine.top_up_modifed(account_balance)
                            count_of_movments+=1
                    case"4":
                        machine.tax_politics()
                    case "5":
                        machine.Start()
                    case "6":
                        break
            except:
                    print(f"{choice} Is incorrect input\n")

ex_1 = machine()
ex_1.main()

