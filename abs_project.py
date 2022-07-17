from abc import ABC, abstractmethod
import pickle


class Frame(ABC):
    def __init__(self, file_name):
        self.__file_name = None
        self.file_name = file_name

    @abstractmethod
    def output(self):
        pass


class AddressBookFrame(Frame):
    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        parse = file_name.split('.')
        self.__file_name = '.'.join([parse.pop(0), 'bak'])

    def output(self):
        with open(self.__file_name, "r") as fh:
            unpacked = fh.read()
            print(unpacked)


class NoteBookFrame(Frame):
    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        parse = file_name.split('.')
        self.__file_name = '.'.join([parse.pop(0), 'bin'])

    def output(self):
        with open(self.__file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            print(unpacked)


class HelperFrame(Frame):
    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        self.__file_name = file_name.split('.')[0]

    def output(self):
        with open(self.__file_name, "r") as fh:
            unpacked = fh.read()
            print(unpacked)


if __name__ == '__main__':

    name = 'contacts'
    contact_output = AddressBookFrame(name)
    contact_output.output()
    
    name = 'test'
    notes_output = NoteBookFrame(name)
    notes_output.output()

    name = 'notebook_helper.dkk'
    help_output = HelperFrame(name)
    help_output.output()
