import unittest
from persona import *
from dottore import *
from paziente import *
from fattura import *
# ### Creazione di Test Case con UnitTest

# Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento
#  delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire
#  l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici
#  delle classi.

# Istruzioni
# Creare un nuovo file Python denominato "test_persona.py".
# Importare il modulo unittest e tutte le classi definite.

# Test della Classe Persona
# - Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi first_name, last_name e age.
#   - Il funzionamento dei metodi setName, setLastName e setAge.

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona('Mario', 'Rossi')

    def test_attributi(self):
        self.assertEqual(self.persona.getName(), 'Mario')
        self.assertEqual(self.persona.getLastName(), 'Rossi')
        self.assertEqual(self.persona.getAge(), 0)

    def test_metodi(self):
        self.persona.setName('Marco')
        self.persona.setLastName('Bianchi')
        self.persona.setAge(50)
        self.assertEqual(self.persona.getName(), 'Marco')
        self.assertEqual(self.persona.getLastName(), 'Bianchi')
        self.assertEqual(self.persona.getAge(), 50)

# Test della Classe Dottore
# - Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Dottore.
#   - Il funzionamento del metodo isValidDoctor con diverse età.

class TestDottore(unittest.TestCase):
    def setUp(self) -> None:
        self.dottore = Dottore('Giuseppe', 'Verdi', 'Oncologia', 150.0)
        self.dottore.setAge(50)

    def test_attributi(self):
        self.assertEqual(self.dottore.getName(), 'Giuseppe')
        self.assertEqual(self.dottore.getLastName(), 'Verdi')
        self.assertEqual(self.dottore.getSpecialization(), 'Oncologia')
        self.assertEqual(self.dottore.getParcel(), 150.0)

    def test_metodi(self):
        self.dottore.setName('Mario')
        self.dottore.setLastName('Bianchi')
        self.dottore.setSpecialization('Cardiologia')
        self.dottore.setParcel(155.0)
        self.assertEqual(self.dottore.getName(), 'Mario')
        self.assertEqual(self.dottore.getLastName(), 'Bianchi')
        self.assertEqual(self.dottore.getAge(), 50)
        self.assertEqual(self.dottore.getSpecialization(), 'Cardiologia')
        self.assertEqual(self.dottore.getParcel(), 155.0)
    
    def test_valid_doctor(self):
        self.assertTrue(self.dottore.isAValidDoctor())
        self.dottore.setAge(28)
        self.assertFalse(self.dottore.isAValidDoctor())



# Test della Classe Paziente
# - Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Paziente.

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente('Luigi', 'Esposito', '1234')

    def test_attributi(self):
        self.assertEqual(self.paziente.getName(), 'Luigi')
        self.assertEqual(self.paziente.getLastName(), 'Esposito')
        self.assertEqual(self.paziente.getAge(), 0)
        self.assertEqual(self.paziente.getIdCode(), '1234')

# Test della Classe Fattura
# - Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta della classe Fattura.
#   - Il calcolo corretto del salario e del numero di fatture.
#   - L'aggiunta e la rimozione di pazienti dalla lista.

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore1 = Dottore('Francesco', 'Puccini', 'Cardiologia', 200.0)
        self.dottore1.setAge(55)
        self.paziente1 = Paziente('Anna', 'Russo', '2345')
        self.paziente2 = Paziente('Laura', 'Verdi', '6789')
        self.paziente3 = Paziente('Giulia', 'Bianchi', '0123')
        self.pazienti1 = [self.paziente1,
                           self.paziente2]
        for paziente in self.pazienti1:
            paziente.setAge(35)  # Imposta l'età di ogni paziente a 35
        self.fattura1 = Fattura(self.pazienti1, self.dottore1)

    def test_init(self):
        self.assertEqual(self.fattura1.patients, self.pazienti1)
        self.assertEqual(self.fattura1.doctor, self.dottore1)
        self.assertEqual(self.fattura1.invoices, 2)
        self.assertEqual(self.fattura1.salary, 0)
    
    def test_salario_fatture(self):
        self.assertEqual(self.fattura1.getFatture(), 2)
        self.assertEqual(self.fattura1.getSalary(), 400.0)

    def test_patients(self):
        self.assertIn(self.paziente1, self.fattura1.patients)
        self.fattura1.addPatient(self.paziente3)
        self.assertIn(self.paziente1, self.fattura1.patients)
        self.fattura1.removePatient('2345')
        self.assertNotIn(self.paziente1, self.fattura1.patients)

    

if __name__ == '__main__':
    unittest.main()