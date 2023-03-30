from modules import PajamuIrasas, IslaiduIrasas
import pickle

def nuskaityti_is_failo():
    try:
        with open("zurnalas.pkl", "rb") as file:
            zurnalas = pickle.load(file)
    except:
        zurnalas = []
    return zurnalas
zurnalas = nuskaityti_is_failo()

def irasyti_i_faila():
    with open("zurnalas.pkl", "wb") as file:
        pickle.dump(zurnalas, file)


while True:
    pasirinkimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - atvaizduoti žurnalą\n4 - balansas\n5 - išeiti\n"))
    match pasirinkimas:
        case 1:
            suma = int(input("Įveskite sumą: "))
            siuntejas = input("Įveskite siuntėją: ")
            info = input("Įveskite papildomą informaciją: ")
            irasas = PajamuIrasas(suma, siuntejas, info)
            zurnalas.append(irasas)
            irasyti_i_faila()
        case 2:
            suma = int(input("Įveskite sumą: "))
            budas = input("Įveskite atsiskaitymo būdą: ")
            isigyta = input("Įveskite įsigytą prekę/paslaugą: ")
            info = input("Įveskite papildomą informaciją: ")
            irasas = IslaiduIrasas(suma, budas, isigyta, info)
            zurnalas.append(irasas)
            irasyti_i_faila()
        case 3:
            for irasas in zurnalas:
                print(irasas)
        case 4:
            balansas = 0
            for irasas in zurnalas:
                if type(irasas) is PajamuIrasas:
                    balansas += irasas.suma
                if type(irasas) is IslaiduIrasas:
                    balansas -= irasas.suma
            print("Balansas:", balansas)
        case 5:
            print("Viso gero")
            break

