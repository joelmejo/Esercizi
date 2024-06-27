

# Hai il compito di indagare su un caso di numeri mancanti!
#  Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, dove n è la lunghezza dell'elenco.
#  Sembra però che ci sia un problema: mancano alcuni numeri!

# La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti.
#  Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.

# La funzione restituisce una nuova lista contenente tutti i numeri mancanti
#  da 1 a n che non sono presenti nella lista originale. 
def swap(x: int, y: int):
    return y, x
def flag_bubble_sort(a: list):
    for i in range(len(a)):
        swap_flag = False
        for j in range(len(a) - i - 1):
            if(a[j] > a[j + 1]):
                swap_flag = True
                a[j], a[j + 1] = swap(a[j], a[j +1])
        if swap_flag is False:
            return None
    return None

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    # elimina il pass e inserisci il codice
    flag_bubble_sort(nums)
    missing_numbers: list= []
    for i in range(len(nums) -1):
        if(nums[i] < len(nums)):
            if(nums[i] +1 != (nums[i +1])):
                temp = 0
                for j in range((nums[i +1] - nums[i]) -1):
                    temp = nums[i] + (j + 1)
                    if(temp <= len(nums)):
                        missing_numbers.append(temp)
    return missing_numbers
    
print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) #[5, 6]
print()
print(find_disappeared_numbers([1,8,9,150])) #[2, 3, 4]
print()
print(find_disappeared_numbers([1,8,9,150,9,2189,2,82,3,3,3])) #[4, 5, 6, 7, 10, 11]