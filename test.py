class ROI:
    def __init__(self):
        self.current_total = 0
        self.total = 0

    def __str__(self):
        return str(self.total)

    def calculate_income(self):
    
        rental_income = float(input('Please enter rental amount: '))
        laundry = float(input('Please enter laundry amount: '))
        storage = float(input('Please enter storage amount: '))
        misc = float(input('Please enter miscellaneous amount: '))
        income = rental_income + laundry + storage + misc
        print(income)



