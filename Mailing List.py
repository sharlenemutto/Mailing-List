#Program collects customer information
#and allows customer to be added to a mailing list

import person

def main():
    name = input('Please enter your name: ')
    address = input('Please enter your address: ')
    telephone = input('Please enter your telephone number: ')
    customer_number = input('Please enter your customer number: ')

    customer = person.Customer(name, address, telephone, customer_number)

    customer.show_mailing_list()

    
    print('Name: ', customer.get_name())
    print('Address: ', customer.get_address())
    print('Telephone: ', customer.get_telephone())
    print('Customer Number: ', customer.get_customer_number())

    correct_information = input('Please verify your information.'\
                                "Enter 'n' if the information is not correct: ")
    correct_information.lower()
    
    while correct_information == 'n':
        name = input('Please enter your name: ')
        address = input('Please enter your address: ')
        telephone = input('Please enter your telephone number: ')
        customer_number = input('Please enter your customer number: ')

        customer = person.Customer(name, address, telephone, customer_number)

        print('Name: ', customer.get_name())
        print('Address: ', customer.get_address())
        print('Telephone: ', customer.get_telephone())
        print('Customer Number: ', customer.get_customer_number())

        correct_information = input('Please verify your information.'\
                                    "Enter 'n' if the information is not correct: ")

main()

    
