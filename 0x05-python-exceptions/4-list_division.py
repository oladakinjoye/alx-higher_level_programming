#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp_answer = 0
    for i in range(0, list_length):
        try:
            temp_answer = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp_answer = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_answer = 0
            print("division by 0")
        except IndexError:
            temp_answer = 0
            print("out of range")
        finally:
            pass
        new_list.append(temp_answer)
    return new_list
