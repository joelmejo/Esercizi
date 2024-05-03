# Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari
# appaiano prima di tutti i numeri dispari. Restituisce l'elenco riorganizzato.

def even_odd_pattern(nums: list[int]) -> list[int]:
    # cancella il pass e inserisci il tuo codice
    for i in range(len(nums)):
        counter = 0
        for j in range(len(nums) - i):
            num = nums[j]/2
            if num%1 == 0:
                temp = nums[j]
                nums.remove(nums[j])
                nums.insert(counter, temp)
                counter += 1
    return nums

print(even_odd_pattern([3, 6, 1, 8, 4, 7])) #[6, 8, 4, 3, 1, 7]
print(even_odd_pattern([3, 6, 1, 8, 4, 7, -1])) #[6, 8, 4, 3, 1, 7, -1]
print(even_odd_pattern([3, 6, 1, 8, 4, 7, 0, -1])) #[6, 8, 4, 0, 3, 1, 7, -1]
print(even_odd_pattern([3, 6, 18, 1, 8, 4, 7, 0, -1])) #[6, 18, 8, 4, 0, 3, 1, 7, -1]
print(even_odd_pattern([1])) #[1]