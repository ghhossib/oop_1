# Ассоциация - наследование при котором один класс является полем другого класса (Целое состоит из частей)
# ассоциация - Агрегация в UML (Унифицированый язык моделирования ) - линия  с незакрашенным ромбом(часть объекта удалена-целое остается)
class Salary:
    def __init__(self, pay):
        self.pay = pay # оплата за месяц
        # метод вывода зарплаты за год
    @property
    def getSummOfYear(self):
        return int(self.pay*12)

class Worker:
    def __init__(self, pay,bonus,name):
        self.pay = pay 
        self.bonus = bonus
        self.name = name 
# метод - выводит зарплату сотрудника за год с премией
    def getSummOfYearForWorker(self):
        return f"Зарплата вместе с премией у сотрудника {self.name} составляет {self.bonus + self.pay.getSummOfYear}"

# класс композиции 
class Tax:
    def __init__(self,pay,bonus, tax, name_tax):
        self.pay = pay
        self.bonus = bonus
        self.name_tax = name_tax
        self.tax = tax
        self.salary = Salary = (self.pay) #атрибут self.salary явялется объектом класса Salary

    #метод вывода налога 
    @property
    def getTaxOfYear(self):
        return int(self.bonus + self.salary.getSummOfYear) * self.name_tax / 100

    #метод 
    def getInformationOfTax(self):
        return f"Сумма налога {self.name_tax} за год составила {self.getTaxOfYear} рублей"
        
        
        
            

# объект - зарплата за месяц 
salary_of_month = Salary(20000)
print(salary_of_month.getSummOfYear)
# объект - работник 
sasha = Worker(salary_of_month,20000,'Саша')
print(sasha.getSummOfYearForWorker())
tax = Tax(salary_of_month, sasha.bonus,13,'подоходный для физ.лиц')
print(tax.getInformationOfTax)
            
