'''
    People Sort
    Given a list of people objects, create a function that sorts the list by an attribute name.
    The attribute to sort by will be given as a string.
    The Person class will only include these attributes in the following order:
        firstname
        lastname
        age
    Examples

    p1 = Person("Michael", "Smith", 40)
    p2 = Person("Alice", "Waters", 21)
    p3 = Person("Zoey", "Jones", 29)

    people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
    # Alice, Michael, Zoey

    people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
    # Jones, Smith, Waters

    people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
    # 21, 29, 40

    Notes

        Sort the list in ASCENDING order.
        All objects will be valid.

'''

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

def people_sort(people, attribute):
    # Define a lambda function to get the attribute value for sorting
    key_function = lambda person: getattr(person, attribute)

    # Use the sorted function to sort the list based on the specified attribute
    sorted_people = sorted(people, key=key_function)

    return sorted_people

# Example usage:
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

result_firstname = people_sort([p1, p2, p3], "firstname")
print(result_firstname)
# Output: [p2, p1, p3]

result_lastname = people_sort([p1, p2, p3], "lastname")
print(result_lastname)
# Output: [p3, p1, p2]

result_age = people_sort([p1, p2, p3], "age")
print(result_age)
# Output: [p2, p3, p1]
