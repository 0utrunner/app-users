class User:

    def __init__(self, name, email_address, dl, phone_number):
        self.name = name
        self.email_address = email_address
        self.dl = dl
        self.phone_number = phone_number

radd = User('Radd', 'Gr8BitHero@email.com', 9899100, '4042777373')
alta = User('Alta', 'redgirl9@email.com', 9293381, '4425998021')
shyren = User('Shyren', 'shyrenstars95@email.com', 1203948, '0809924421')

print(radd.name, radd.email_address)
print(alta.name, alta.dl)
print(shyren.name, shyren.email_address, shyren.phone_number)