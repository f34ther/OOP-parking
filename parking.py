# we need: TakeTicket, payForParking, leaveGarage (methods)
# tickets(), parkingSpaces(list), currentTicket(dictionary)

class Garage():

    def __init__(self):
        self.tickets_limit = 10
        self.parking_limit = 10
        self.currentTicket = {
            'paid': False
        }

    def takeTicket(self):
        self.tickets_limit -= 1
        self.parking_limit -= 1
        print(f'Parking tickets available: {self.tickets_limit}')
        print(f'Parking spots available: {self.parking_limit}')
        return f'Tickets left: {self.tickets_limit}; Parking Spaces left: {self.parking_limit} '

    def payForParking(self):
        self.amount = input('Please enter $10 for parking payment: ')

        if self.amount < '10':
            self.amount
        elif self.amount > '10':
            # overpayment
            self.currentTicket['paid'] = True
            print(f'Here is your change: ${int(self.amount)-10}')
        else:
            self.currentTicket['paid'] = True
            print('You have paid for your ticket, you have 15 minutes to leave.')

    def leaveGarage(self):
        if self.currentTicket['paid'] == False:
            print('Please pay your ticket before exiting.')

        else:
            self.tickets_limit += 1
            self.parking_limit += 1
            print(f'Parking tickets available: {self.tickets_limit}')
            print(f'Parking spots available: {self.parking_limit}')
            print('Thank you, have a nice day!')


ticket = Garage()
ticket.takeTicket()
ticket.payForParking()
ticket.leaveGarage()
