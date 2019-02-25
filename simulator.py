from farm import Farm
import sys


class Simulator:

    def main_menu(self):
        while True:
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print("field")
        print("harvest")
        print("status")
        print("relax")
        print("exit")

    def call_option(self, user_selected):
        if user_selected == "field":
            self.add_new_field()
        elif user_selected == "harvest":
            self.harvest()
        elif user_selected == "status":
            self.status()
        elif user_selected == "relax":
            self.relax()
        elif user_selected == "exit":
            sys.exit()

    def add_new_field(self):

        print("What kind of field is it: corn or wheat?")
        type = input()
        print("How large is the field in hectares?")
        size = int(input())

        Farm.add(type, size)
        print("Added a {} field of {} hectares!".format(type, size))

    def harvest(self):
        Farm.harvest()

    def status(self):
        Farm.total_harvest()

    def relax(self):
        Farm.relax_message()


a_farm_app = Simulator()
a_farm_app.main_menu()
