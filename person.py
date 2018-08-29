class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone
    

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number):
        Person.__init__(self, name, address, telephone)

        self.__customer_number = customer_number

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def get_customer_number(self):
        return self.__customer_number

    def show_mailing_list(customer):
        mailing_list = input('Would you like to be on the mailing list? '\
                             'Enter y for yes: ')
        if mailing_list == 'y':
            print('Be on the look out for upcoming promotions! ')

        else:
            print('You have not subscribed to the mailing list.' )

        
