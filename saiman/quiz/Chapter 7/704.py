class Length:

    @staticmethod
    def cm_to_inches(cm):
        return cm / 2.54

    @staticmethod
    def km_to_miles(km):
        return km / 1.609


class Weight:

    @staticmethod
    def kg_to_pounds(kg):
        return kg * 2.205

    @staticmethod
    def gram_to_ounce(gm):
        return gm / 28.35


class Time:

    @staticmethod
    def s_to_hr(s):
        return s / 3600

    @staticmethod
    def ms_to_s(ms):
        return ms / 1000


cm = float(input("Enter len in cm"))
print(Length.cm_to_inches(cm))
km = float(input("Enter len in km"))
print(Length.km_to_miles(km))

kg = float(input("Enter weight in kg"))
print(Weight.kg_to_pounds(kg))
gm = float(input("Enter weight in gram"))
print(Weight.gram_to_ounce(gm))

s = float(input("Enter time in sec"))
print(Time.s_to_hr(s))
ms = float(input("Enter time  in milliseconds"))
print(Time.ms_to_s(ms))
