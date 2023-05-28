class Length:
    cm = 40000

    @staticmethod
    def cm_to_inches(cm):
        return cm / 2.54

    @staticmethod
    def km_to_miles(km):
        return km / 1.609


cm = float(input("Enter len in cm"))
print(Length.cm_to_inches(cm))
km = float(input("Enter len in km"))
print(Length.km_to_miles(km))


class Weight:


    @staticmethod
    def kg_to_pounds(kg):
        return cm / 2.54

    @staticmethod
    def km_to_miles(km):
        return km / 1.609
