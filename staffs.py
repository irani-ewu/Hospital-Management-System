from patient import *
from treatment import *

class StaffProfile:
    def __init__(self,sid,name,age):
        self.sid=sid
        self.name=name
        self.age=age
    

class Doctor(StaffProfile):   
    def __init__(self,sid,name,age,degrees,specialization):
        super().__init__(sid,name,age)
        self.degrees=degrees
        self.specialization=specialization

    def show_details(self,sid):
        file = open(f"'{self.sid}'no. staff's data","a+")
        file.write(f"SID:'{self.sid}'\nName:'{self.name}'\nAge:'{self.age}'\nDegrees:'{self.degrees}'\nSpecialization:'{self.specialization}'")
        file.close()
        print(f"SID:'{self.sid}'\nName:'{self.name}'\nAge:'{self.age}'\nDegrees:'{self.degrees}'\nSpecialization:'{self.specialization}'")
    
    def write_prescription(self,patient_obj):
        symptoms = patient_obj.get_symptoms()
        required_specialist = Treatment.get(symptoms)
        
        if(self.specialization==required_specialist):
            print(f"'{self.name}' will treat patient '{patient_obj.pid}','{patient_obj.name}'")

            file = open(f"'{self.sid}'no. Dr. prescription for '{patient_obj.pid}'","a+")
            file.write(f"Diagnosis of '{symptoms}\n'")
            
            Suggestion = input("Doctor please write here:\n")
            file.write(Suggestion)
            
            file.close()
            print("\nPrescription Saved\n")
        else:
            print(f"Sorry This Doctor do not diagnosis this symptom: '{symptoms}'")

    
class Nurse(StaffProfile):   
    def __init__(self,sid,name,age,shift):
        super().__init__(sid,name,age)
        self.shift=shift
    
    def show_details(self,sid):
        file = open(f"'{self.sid}'no. staff's data","a+")
        file.write(f"SID:'{self.sid}'\nName:'{self.name}'\nAge:'{self.age}'\nShift:'{self.shift}'\n")
        file.close()
        print(f"SID:'{self.sid}'\nName:'{self.name}'\nAge:'{self.age}'\nShift:'{self.shift}'\n")
    