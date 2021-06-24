class Converter:
    def __init__(self,weight,unit):
        self.weight=weight
        self.unit=unit

    def kg_to_pound(self):
        pound=self.weight*2.20462
        result=str(pound)+" Pound"
        return result

    def pound_to_kg(self):
        kg=self.weight*0.45
        result=str(kg)+" KG"
        return result
        
weight=float(input("Enter weight :"))
unit=input("Enter unit :")

c=Converter(weight,unit)

if((unit.lower())=="kilogram"):
    print(c.kg_to_pound())
elif((unit.lower())=="pound"):
    print(c.pound_to_kg())
