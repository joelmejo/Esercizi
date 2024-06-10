from dottore import *
from paziente import *
# ### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.

# - Definire i seguenti metodi:

#     init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve
#        verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor().
#        In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha
#        il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare
#        il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad
#        esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".

#     getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato
#        moltiplicando la parcella del dottore per il numero di pazienti.

#     getFatture(): deve ritornare il valore dell'attributo fatture, dopo aver assegnato ad esso il numero
#        dei pazienti che ha il dottore.

#     addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore,
#        aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().
#        Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"

#     removePatient(): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in
#        input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e
#        il salario, richiamando il metodo get Fatture() e getSalary().
#        Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".

class Fattura:
    def __init__(self, patients: list[Paziente], doctor: Dottore) -> None:
        if doctor.isAValidDoctor():
            self.patients = patients
            self.doctor = doctor
            self.invoices: int = len(patients)
            self.salary: int = 0
        else:
            self.patients = None
            self.doctor = None
            self.invoices = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self) -> int:
        return self.doctor.getParcel() * len(self.patients)
    
    def getFatture(self) -> int:
        return len(self.patients)
    
    def addPatient(self, newPatient: Paziente) -> None:
        self.patients.append(newPatient)
        self.invoices = self.getFatture()
        self.salary = self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.getName()} è stato aggiunto il paziente {newPatient.getIdCode()}")

    def removePatient(self, id_code: str) -> None:
        for patient in self.patients:
            if patient.getIdCode() == id_code:
                self.patients.remove(patient)
                self.invoices = self.getFatture()
                self.salary = self.getSalary()
                print(f"Alla lista del Dottor {self.doctor.getName()} è stato rimosso il paziente {id_code}")
                break