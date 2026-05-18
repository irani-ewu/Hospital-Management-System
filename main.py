from patient import *
from staffs import *
from treatment import *

# To hold the objects created during the data entry
allPatients=[] # Can hold P1 (patient1)
allStaffs=[] # Can hold S1 (doctor1)

while True:
    print("This is a Admin View. Where to proceed?\n 1.Patient Profile\n 2.Staff Profile\n 3.Consultation")

    try:
        Press=int(input("Press:\n"))
    except ValueError:
        print("Enter only numerical value")

    if (Press==1):
        print("\n||Enter the patient's detail here||\n")
        
        try:
            pid=int(input("Enter the patient id:\n"))
        except ValueError:
            print("Enter only numerical value")
            
        name=input("Enter the patient's name:\n")
        
        try:
            age=int(input("Enter the patient's age:\n"))
        except ValueError:
            print("Enter only numerical value")
            
        bg=input("Enter the patient's blood group:\n")
        symptoms=input("Enter the patient's current symptoms:\n")
        
        # Now create a object of a patient
        P1=PatientProfile(pid,name,age,bg,symptoms)
        allPatients.append(P1)
        P1.show_details(pid)
        
    elif(Press==2):
        
        print("||Enter the staff's detail here||\n")
        
        sid=input("Enter the staff's id:\n")
        na_me=input("Enter the staff's name:\n")
        
        try:
            a_ge=int(input("Enter the staff's age:\n"))
        except ValueError:
            print("Enter only numerical value")
        
        print("Is Staff a Doctor or Nurse?\n")
        
        Staff = input("Staff:")
        
        if(Staff=="Doctor"):
            degrees=input("\nEnter the doctor's degrees:\n")
            specialization=input("Enter the doctor's expertise:\n")
            S1=Doctor(sid,na_me,a_ge,degrees,specialization)
            allStaffs.append(S1)
            S1.show_details(sid)
        elif(Staff=="Nurse"):
            shift=input("Enter the nurse's shift:\n")
            S2=Nurse(sid,na_me,a_ge,shift)
            S2.show_details(sid)

    elif(Press==3):
        print("\n----------Consultation Interface----------\n")
        
        try:
            check_pid=int(input("\nEnter the patient's id for consultation:\n"))
        except ValueError:
            print("\nEnter only numerical value\n")
            
        check_sid=input("Enter the Doctor's id for consultation:\n") 
        
        found_patient = None
        found_staff = None
        
        for patient in allPatients:
            if patient.pid==check_pid:
                found_patient=patient
                break
            
        for staff in allStaffs: # Here staff means only the doctor
            if staff.sid==check_sid:
                found_staff=staff
                break
        
        if found_patient is not None and found_staff is not None:
            found_staff.write_prescription(found_patient)
        else:
            print("\nInvalid Patient ID or Doctor ID/ Staff is not a Doctor\n")
            
        