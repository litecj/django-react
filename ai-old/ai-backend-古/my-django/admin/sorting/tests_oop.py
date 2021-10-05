import unittest
from admin.sorting.models_oop import Grade, Calculator, Contacts

class TestCalculator(unittest.TestCase):
    cal = Calculator()
    cal.num1 = 8
    cal.num2 = 5

    def test_add(self):
        self.assertEqual(self.cal.add(), 13)

    def test_sub(self):
        self.assertEqual(self.cal.subtract(), 3)

    def test_multi(self):
        self.assertEqual(self.cal.multiple(), 40)

    def test_div(self):
        self.assertEqual(self.cal.divide(), 1.6)

    def test_mod(self):
        self.assertEqual(self.cal.remain(), 3)


class TestGrade(unittest.TestCase):

    def test_grade(self):
        grade = Grade('Jun', 92, 88, 90)
        # grade.name = "Jun"
        # grade.kor = 92
        # grade.eng = 88
        # grade.math = 90
        self.assertEqual(grade.name, 'Jun')
        self.assertEqual(grade.return_grade(), 'A')
        # print(f'{grade.name} grade is {grade.return_grade()}')
        # self.assertEqual(grade.return_grade(), 'c')


class TestContacts(unittest.TestCase):

    def test_get_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom','010-1234-5897','tom@test.com','Seoul'))
        ls.append(Contacts.set_contact('Hera', '010-6574-8956', 'hera@test.com', 'Busan'))
        ls.append(Contacts.set_contact('Sujaun', '010-4561-2342', 'suuu@test.com', 'Beijing'))
        ls.append(Contacts.set_contact('Hei', '010-4257-5897', 'hei@test.com', 'Seoul'))
        ls = Contacts.get_contacts(ls)
        # ls1 = Contacts.del_contact('Tom')
        self.assertEqual(ls[2].name,'Sujaun')

    def test_del_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom', '010-1234-5897', 'tom@test.com', 'Seoul'))
        ls.append(Contacts.set_contact('Hera', '010-6574-8956', 'hera@test.com', 'Busan'))
        ls.append(Contacts.set_contact('Sujaun', '010-4561-2342', 'suuu@test.com', 'Beijing'))
        ls.append(Contacts.set_contact('Hei', '010-4257-5897', 'hei@test.com', 'Seoul'))
        ls = Contacts.del_contact(ls, 'Tom')
        print([i.to_string() for i in ls])
        self.assertEqual(ls[0].name, 'Hera')
        self.assertEqual(len(ls), 3)

if __name__ == '__main__':
    unittest.main()
