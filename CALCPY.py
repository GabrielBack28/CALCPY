version = ("0.8.0")

def show_message_welcome():
    print("Olá.")
    print("Bem vindo ao CALCPY. \n")

def format_input_numeric(value):
    value = value.replace(",", ".")
    return float(value)

def is_value_valid(value):
    if value <= 0:
        return False
    else:
        return True

def is_yes(value):
    return (value in ["Y", "y"])

def is_no(value):
    return (value in ["N", "n"])

def time_value(time, time_base_one, time_base_two):
    if time >= time_base_one:
        return float(0.15)
    elif time >= time_base_two:
        return float(0.175)
    else:
        return float(0.2)

def insert_value_applied():
    while True:
        try:
            value_applied = input("Digite o valor aplicado (reais): ")
            value_applied = format_input_numeric(value_applied)
            if is_value_valid(value_applied):
                return value_applied
            else:
                print("O valor aplicado deve ser maior do que 0!")
        except ValueError:
            print("Valor inválido! Tente novamente.")

def insert_time_applied():
    while True:
        try:
            time = input("Digite o tempo (meses): ")
            time = format_input_numeric(time)
            if is_value_valid(time):
                return time
            else:
                print("O tempo deve ser maior que 0!")
        except ValueError:
            print("Valor inválido! Tente novamente.")

def insert_monthly_application():
    valid_monthly_application = False
    while not valid_monthly_application:
        try:
            monthly_application = input("Digite a aplicação mensal (reais): ")
            monthly_application = format_input_numeric(monthly_application)
            if monthly_application < 0:
                print("A aplicação mensal deve ser maior ou igual a 0!")
            else:
                return monthly_application
                valid_monthly_application = True
        except ValueError:
            print("Valor inválido! Tente novamente.")

def executa():
    show_message_welcome()

    #----------loop para o app (final do app)----------
    app_valid = False
    while not app_valid:
        #-----valor aplicado-----
        value_applied = insert_value_applied()
        #-----tempo-----
        time = insert_time_applied()
        #-----aplicação mensal-----
        monthly_application = insert_monthly_application()


        #----------alterar dados----------
        change_valid_data = False
        while not change_valid_data:
            change_data = input("Você gostaria de alterar algum valor fixo? (Y/N)")
            if is_yes(change_data):

                #----------alterar taxa de juros----------
                valid_interest_rate = False
                while not valid_interest_rate:
                    interest_rate = input("Você gostaria de alterar o valor da taxa de juros? (Y/N)")
                    if is_yes(interest_rate):
                        try:
                            interest_rate = input("Digite o valor da taxa de juros: ")
                            interest_rate = format_input_numeric(interest_rate)

                            if interest_rate <= 0:
                                print("A taxa de juros deve ser maior que 0!")
                            else:
                                valid_interest_rate = True
                        except ValueError:
                            print("Valor inválido! Tente novamente.")
                    elif is_no(interest_rate):
                        interest_rate = float(0.5175)
                        valid_interest_rate = True
                    else:
                        print("O valor inserido não é válido! Tente novamente.")
                
                #----------alterar o Imposto de Renda----------
                IR_valid = False
                while not IR_valid:
                    IR = input("Você gostaria de alterar o valor do imposto de renda? (Y/N)")
                    if is_yes(IR):
                        try:
                            IR = input("Digite o valor do Imposto de Renda: ")
                            IR = format_input_numeric(IR)

                            if IR <= 0:
                                print("O Imposto de Renda deve ser maior que 0!")
                            else:
                                IR_valid = True
                        except ValueError:
                            print("O valor inserido não é válido! Tente novamente.")

                    elif is_no(IR):
                        IR = time_value(time, 25, 12)
                        IR_valid = True
                    else:
                        print("O valor inserido não é válido! Tente novamente.")
                    
                IR2 = time_value(time, 24, 12)

                #----------alterar a custodia da bolsa----------
                purse_custody_valid = False
                while not purse_custody_valid:
                    purse_custody = input("Você gostaria de alterar o valor da custódia da Bolsa? (Y/N)")
                    if is_yes(purse_custody):
                        try:
                            purse_custody = input("Digite o valor da custodia da bolsa: ")
                            purse_custody = format_input_numeric(purse_custody)

                            if purse_custody <= 0:
                                print("A Custodia da Bolsa deve ser maior que 0!")
                            else:
                                purse_custody_valid = True
                        except ValueError:
                            print("O valor inserido não é válido! Tente novamente.")
                    elif is_no(purse_custody):
                        purse_custody = float(0.00025)
                        purse_custody_valid = True
                    else:
                        print("O valor inserido não é válido! Tente novamente.")

                change_valid_data = True

            #----------valores fixos----------
            elif is_no(change_data):

                interest_rate = float(0.5175)

                IR = time_value(time, 25, 13)
                IR2 = time_value(time, 24, 12)

                purse_custody = float(0.00025)

                change_valid_data = True

            else:
                print("Valor inválido! Tente novamente.")


      #----------calculos----------
        value_for_calculation = ((interest_rate / 100) + 1)

        value_time = ((value_applied * (value_for_calculation ** time)) + ((monthly_application *((value_for_calculation ** time)-1))/(interest_rate/100)))

        final_value_month = (value_time * value_for_calculation)

        net_gain = ((final_value_month - value_time) - ((final_value_month - value_time) * IR))

        saved_value = (value_applied + (monthly_application * time))

        obtained_gain = ((final_value_month - saved_value) - ((final_value_month - saved_value) * IR2))

        final_gain = ((saved_value + obtained_gain) - ((saved_value + obtained_gain) * purse_custody))


        #----------resultados----------
        print("\nO valor em sua conta após ", "%.0f" % time, " mesês é: ", "%.2f" % value_time)

        print("O valor após o final do mês é de: ", "%.2f" % final_value_month)

        print("O valor do seu ganho líquido é de: ", "%.2f" % net_gain)

        print("O valor guardado no colchão é de: ", "%.2f" % saved_value)

        print("O valor da relação de ganhos é de: ", "%.2f" % obtained_gain)

        print("O valor do seu ganho final é de: ", "%.2f" % final_gain, "\n")


        #----------validar o loop----------
        validation_back = False
        while not validation_back:
            app = input("Você gostaria de voltar ao início do programa? (Y/N)")
            if is_yes(app):
                print("\n" * 3)
                validation_back = True
            elif is_no(app):
                validation_back = True
                app_valid = True
            else:
                print("O valor inserido não é válido! Tente novamente. \n")

if __name__ == '__main__':
    executa()
