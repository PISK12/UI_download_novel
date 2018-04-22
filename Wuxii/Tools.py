import pickle

import requests


class Tools():
    @staticmethod
    def save_obj(obj, name):
        with open(name + ".pkl", "wb") as file:
            pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_obj(name):
        try:
            with open(name + ".pkl", "rb") as file:
                return pickle.load(file)
        except EOFError as e:
            return {}
        except FileNotFoundError as e:
            Tools.save_obj({}, name)
            return {}
        else:
            pass
        finally:
            pass

    @staticmethod
    def _which_number(max, text="give me number", min=0):
        number = min - 1
        max += min
        while min > number or number >= max:
            number = input(text + " ")
            if not number.isdigit():
                print("I cant see number")
            number = int(number)
        return number

    @staticmethod
    def _show_list_in_console(lista, start):
        maxChar = len(lista)
        maxChar = str(maxChar)
        maxChar = len(maxChar)
        for r, text in enumerate(lista, start):
            print(str(r).rjust(maxChar, "0") + ". " + text)

    @staticmethod
    def show_and_choose_number(lista, start=0):
        sort_list = sorted(lista)
        Tools._show_list_in_console(sort_list, start)
        number = Tools._which_number(max=len(sort_list), min=start)
        number -= start
        return lista[lista.index(sort_list[number])]

