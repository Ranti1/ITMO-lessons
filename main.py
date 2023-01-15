def repeat(func):
    def wrapper():
        for i in range(3):
            print(f"{i + 1}. {func()}")

    return wrapper()


def square(*args):
    try:
        summ = 0
        for num in args:
            summ += num ** 2
        return summ
    except TypeError:
        summ = 0
        for num in args:
            summ += int(num) ** 2
        return summ
    except ValueError:
        return TypeError()


print(square(1, "2", "3"))


class Item:
    def __init__(self, name="", priorities="", time="", user_notes=""):
        self.name = name
        self.priorities = priorities
        self.time = time
        self.user_notes = user_notes

    def change_name(self):
        self.name = input("Enter a new name for your case: ")
        return self.name

    def change_priorities(self):
        self.priorities = input("What is the priority of your case (please enter a number): ")
        return self.priorities

    def change_time(self):
        self.time = input("What time do you need to do your business (enter time in format 00:00): ")
        return self.time

    def change_notes(self):
        self.user_notes = input("Enter your notes: ")
        return self.user_notes

    def output_data(self):
        print(f"Case: {self.name}\nPriorities: {self.priorities}\nTime: {self.time}\nNotes: {self.user_notes}")


class ItemList(Item):
    def make_new_cases(self):
        """The function creates X new cases"""
        number = int(input("Enter a number of your cases: "))
        self.list = []
        for i in range(number):
            small_list = {}
            small_list["Name"] = self.change_name()
            small_list["Priorities"] = self.change_priorities()
            small_list["Time"] = self.change_time()
            small_list["Notes"] = self.change_notes()
            self.list.append(small_list)
            print("----------------------\n")

    def get_all_cases(self):
        """The function prints all cases to the console"""
        for dicti in self.list:
            for key, value in dicti.items():
                print(f"{key} : {value}")
            print("----------------------")

    def get_cases_by_time(self):
        """The function displays the case for a certain time"""
        time = input("Enter the time of the business you need(enter time in format 00:00): ")
        for dict in self.list:
            if dict.get("Time") == time:
                for key, value in dict.items():
                    print(f"{key} : {value}")
                print("----------------------")
            else:
                print("Time entered incorrectly or/and such case does not exist")

    def get_important_cases(self):
        """The function displays only important cases"""
        nums = input("Enter the numbers of the important cases you want to do, separated by a space: ").split(" ")
        for i in nums:
            for dict in self.list:
                if dict.get("Priorities") == i:
                    for key, value in dict.items():
                        print(f"{key} : {value}")
                    print("----------------------")
                else:
                    print("Priorities entered incorrectly or/and such case does not exist")

    def delete_case(self):
        """The function delete certain case"""
        name = input("Enter the name of the case you want to delete: ")
        for dict in self.list:
            if dict.get("Name") == name:
                del dict
                print("Successfully removed")
                break
            else:
                print("Case's name entered incorrectly or/and such case does not exist")
                break

    def change_attribute(self):
        """The function changes one parameter of one case"""
        name, key, new_value = map(str, input(
            "Enter the name of the case, the parameter you want to change and the new value "
            "separated by a space: ").split(" "))
        for dict in self.list:
            if dict.get("Name") == name:
                dict[key] = new_value
                print("Successfully changed")
                break
            else:
                print("Nothing to change")


test = ItemList()
test.make_new_cases()
test.get_all_cases()
test.delete_case()
test.get_all_cases()
