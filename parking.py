# we need: TakeTicket, payForParking, leaveGarage (methods)
# tickets(), parkingSpaces(list), currentTicket(dictionary)

class Garage():
    tickets_limit = range(1, 11)
    parking_limit = range(1, 11)
    currentTicket = {
        'paid': False
    }

    def __init__(self, y_new_ticket):
        self.y_new_ticket = y_new_ticket

    def takeTicket(self):
        tickets_limit -= range(1)
        parking_limit -= range(1)
        return f'Tickets left: {len(tickets_limit)}; Parking Spaces left: {len(parking_limit)} '

    def payForParking(self):
        amount = input()

        if amount == input():
            print(f'Amount due: ${amount}')
        else:
            currentTicket.paid = True
            print('You have paid for your ticket, you have 15 minutes to leave.')

    def leaveGarage(self):
        if currentTicket.paid == True:
            tickets_limit += range(1)
            parking_limit += range(1)
            print('Thank you, have a nice day!')
        else:
            print('Please pay your ticket before exiting.')


ticket1 = Garage(1)

ticket1.leaveGarage()
