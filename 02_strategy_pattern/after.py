import string
import random
from typing import List
from abc import ABC,abstractmethod 


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):

    def create_ordering(self,list:List[SupportTicket]) -> list[SupportTicket]:
        """
            策略子类必须实现的方法
        """


class FIFOTickerOrdering(TicketOrderingStrategy):

    def create_ordering(self, list: List[SupportTicket]) -> list[SupportTicket]:
        # 先入先出的策略
        return list.copy()

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        # 将SupportTicket数组随机排列后返回   
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        
        # 这里将原本的判断代码解耦为执行初始化传入的策略
        # 如果有新的需求，增加对应的策略即可
        ticket_list = self.processing_strategy.create_ordering(self.tickets)
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done.")
            return 
        for ticket in ticket_list:
            self.process_ticket(ticket)


    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
# 如果需要修改，修改传入的策略即可
# 如果需要新增，新增策略即可，不影响流程的代码
app = CustomerSupport(RandomOrderingStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()