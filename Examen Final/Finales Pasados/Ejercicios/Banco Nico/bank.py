import conts
from clients import Client
import file
import time

class Bank:

    def __init__(self):
        self.queue_list = []
        self.queue_list_2 = []
        self.treated_list = []
        self.treated_list_2 = []

    def clients_append(self, client):
        if len(self.queue_list) <= len(self.queue_list_2):
            if client.state == 0:
                self.queue_list.append(str(client))
                print(self.queue_list)
                return self.queue_list
            else:
                print(conts.ERR)
        else:
            if client.state == 0:
                self.queue_list_2.append(str(client))
                print(self.queue_list_2)
                return self.queue_list_2
            else:
                print(conts.ERR)

    def load_data(self):
        print(conts.JUMP_LINE)
        inp = int(input(conts.INP_DB))
        if inp == 1:
            if len(self.queue_list) != 0:
                file.file_operator(self.queue_list)
                print(conts.LOAD_DATA)
            else:
                print(conts.JUMP_LINE)
                print(conts.EMPTY_Q_2)
        elif inp == 2:
            if len(self.queue_list_2) != 0:
                file.file_operator_2(self.queue_list_2)
                print(conts.LOAD_DATA)
            else:
                print(conts.JUMP_LINE)
                print(conts.EMPTY_Q_2)
        else:
            print(conts.ERR) 

    def show_queue(self):
        print(conts.JUMP_LINE)
        inp = int(input(conts.INP))
        if inp == 1:
            print(conts.JUMP_LINE)
            print(self.queue_list)
        elif inp == 2:
            print(conts.JUMP_LINE)
            print(self.queue_list_2)
        else:
            print(conts.ERR)
        return

    def show_cls_treated(self):
        print(conts.JUMP_LINE)
        cl_att_list = self.treated_list + self.treated_list_2
        if len(cl_att_list) != 0:
            file.file_clients_treated()
        else:
            print(conts.EMPTY_T)

    def treat_client(self):
        print(conts.JUMP_LINE)
        inp = int(input(conts.INP_Q))
        if inp == 1:
            if len(self.queue_list) != 0:
                for client in range(len(self.queue_list)):
                    print(f"Atendiendo cliente {self.queue_list[client]}")
                    time.sleep(1)
                    self.treated_list.append(self.queue_list[client])
                self.queue_list.clear()
                file.file_clear(self.queue_list)
                file.file_treated(self.treated_list)
                print(conts.JUMP_LINE)
                print(conts.CLIENT_ATTENDED)
            else:
                print(conts.JUMP_LINE)
                print(conts.EMPTY_Q)
        elif inp == 2:
            if len(self.queue_list_2) != 0:
                for client in range(len(self.queue_list_2)):
                    print(f"Atendiendo cliente {self.queue_list_2[client]}")
                    time.sleep(1)
                    self.treated_list_2.append(self.queue_list_2[client])
                self.queue_list_2.clear()
                file.file_clear_2(self.queue_list_2)
                file.file_treated(self.treated_list_2)
                print(conts.JUMP_LINE)
                print(conts.CLIENT_ATTENDED)
            else:
                print(conts.EMPTY_Q)
        else:
            print(conts.ERR)

    