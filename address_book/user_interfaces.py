from abc import ABC, abstractmethod

from colorama import Fore
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import prompt

from commands import COMMANDS, COMMAND_DESCRIPTIONS


class UserViewer(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_commands(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def get_data_input(self, prompt):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_error(self, message):
        pass


class ConsoleUserViewer(UserViewer):
    def display_contacts(self, contacts):
        formatted_contacts = self.format_contacts(contacts)
        print(formatted_contacts)

    def format_contacts(self, contacts):
        all_contacts = []
        header = '{:<20} {:<30} {:<20} {:<20}'.format('Name', 'Phone', 'Birthday', 'Email')
        separator = '-' * len(header)
        all_contacts.append(header)
        all_contacts.append(separator)
        if contacts:
            for record in contacts:
                phones = ', '.join([f'{phone.value}' for phone in record.phones])
                birthday_str = record.birthday.value if record.birthday else '-'
                email_str = record.email.value if record.email else '-'
                record_str = '{:<20} {:<30} {:<20} {:<20}'.format(
                    record.name.value,
                    phones,
                    birthday_str,
                    email_str
                )
                all_contacts.append(record_str)
        else:
            all_contacts.append("The address book is empty.")

        return '\n'.join(all_contacts)

    def display_commands(self):
        print(Fore.GREEN, "Available commands:")
        separator = '|----------------------|--------------------------------------------|'
        print(separator, f'\n|  Commands            |  Description {" ":30}|\n', separator, sep='')
        for description, commands in COMMAND_DESCRIPTIONS.items():
            print(f"| {Fore.WHITE} {', '.join(commands):<20}{Fore.GREEN}| {description:<43}|")
        print(separator, '\n')

    def get_user_input(self):
        completer = NestedCompleter.from_nested_dict({command[0]: None for command in COMMANDS.values()})
        user_input = prompt('>>>', completer=completer, lexer=None).strip().lower()
        return user_input

    def get_data_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)

    def display_error(self, message):
        print(message)
