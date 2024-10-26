def verifyIfTheresA(text):
    occurencies = text.lower().count('a')
    
    if occurencies > 0:
        print(f"A letra 'a' aparece {occurencies} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

text = input("Informe uma string: ")
verifyIfTheresA(text)
