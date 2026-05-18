# Hospital Management System (Python OOP)

This is a text-based (CLI) Python project that simulates how a hospital admin manages patients and doctors. I built this project to practice writing clean code using Object-Oriented Programming (OOP) and handling text files.

## 🚀 What it Does
*   **Add Patients:** Enter a patient's name, ID, and symptoms. The app automatically creates a text file to save their data.
*   **Add Staff:** Register Doctors (with degrees and specialities) or Nurses (with shifts). Their information is also saved to text files.
*   **Consultation (Interaction):** You type in a Patient ID and a Doctor ID. The system matches them up. If the doctor's speciality matches the patient's symptoms (e.g., a Cardiologist for Chest Pain), the doctor can write a prescription and save it to a new file.

## 🧠 The 4 OOP Pillars I Used
*   **Inheritance:** Created a main `StaffProfile` class. Code duplication is completely minimized by utilizing a base `StaffProfile` parent class that is seamlessly extended by `Doctor` and `Nurse` subclasses using `super().__init__()`.
*   **Encapsulation:** Made patient symptoms private (`__symptoms`) so they cannot be accidentally changed from outside the class.
*   **Polymorphism:** Created a `show_details()` method inside the Patient, Doctor, and Nurse classes. It uses the exact same name but behaves differently for each one.
*   **Object Interaction:** Passed the entire `Patient` object into the `Doctor` class method so they can "talk" to each other and check symptoms.

## 🛠️ How to Run It 
1. Download all the `.py` files into one folder.
2. Open your terminal/command prompt in that folder and run:
   ```bash
   python main.py
