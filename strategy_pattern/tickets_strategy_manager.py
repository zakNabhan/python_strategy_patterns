import string
import random
from typing import List

from abc import ABC, abstractmethod


class SupportTicket:
    #
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class TicketOrderingStragtegy:
    # Interface class
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStragtegy):
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return ticket_list.copy()


class FILOOOrderingStrategy(TicketOrderingStragtegy):
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = ticket_list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStragtegy):
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = ticket_list.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:
    # maintainers a list of tickets

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStragtegy):
        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(self.tickets) == 0:
            print("There are no tickets to process. well done!")
            return
        # create ordered list
        for ticket in ticket_list:
            self.process_ticket(ticket)
        '''
        if processing_stragtegy == "fifo":  # first in first out
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_stragtegy == "filo":  # first in last out
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_stragtegy == "random":  # random
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in self.tickets:
                self.process_ticket(ticket)
        '''

    def process_ticket(self, ticket: SupportTicket):
        print("=======================================")
        print(f"Processing ticket id:  {ticket.id}")
        print(f"Customer:  {ticket.customer}")
        print(f"Issue:  {ticket.issue}")


# test area


if __name__ == "__main__":
    # create the application
    app = CustomerSupport()

    # register a few tickets

    app.create_ticket("Zakaria Nabhan", "My Customer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can not upload any videos, please help")
    app.create_ticket("Arjan Egges ", "VScode does not resolve automatically MY bugs")

    # process the tickets
    # app.process_tickets("fifo")

    # create instance of class
    app.process_tickets(RandomOrderingStrategy())


