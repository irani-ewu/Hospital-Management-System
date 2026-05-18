class PatientProfile:
    def __init__(self,pid,name,age,bg,symptoms):
        self.pid=pid
        self.name=name
        self.age=age
        self.bg=bg
        self.__symptoms=symptoms
    
    def get_symptoms(self):
        return self.__symptoms
        
    def show_details(self,pid):
        file = open(f"'{self.pid}'no. patient's data","a+")
        file.write(f"PID:'{self.pid}'\nName:'{self.name}'\nAge:'{self.age}'\nBG:'{self.bg}'\nSymptoms:'{self.get_symptoms()}'")
        file.close()
        print(f"\nPID:'{self.pid}'\nName:'{self.name}'\nAge:'{self.age}'\nBG:'{self.bg}'\nSymptoms:'{self.get_symptoms()}'")
    
    