#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    * The starting flight will name a source of NONE
    * The ending flight will have a destination of NONE
    Plan:
        0. I can create a dict and add the source of each ticket as a key
           and its destination as the value.
        1. Then I can find the starting flight by with flight_dict["NONE"]
           save it to a reference variable
        2. loop for range in length of tickets
        3. each iteration adding next_flight to a list of routes
           and updating next_flight
        4. return route
    """
    # Your code here
    flight_dict = {t.source:t.destination for t in tickets}
    next_flight = "NONE"
    routes = []
    for _ in range(length):
        routes.append(flight_dict[next_flight])
        next_flight = flight_dict[next_flight]


    return routes
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#                     "SLC", "PIT", "ORD", "NONE"]
print(reconstruct_trip(tickets, 10))