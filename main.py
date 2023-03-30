from modules import Irasas
zurnalas = []


while True:
    pasirinkimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - atvaizduoti žurnalą\n4 - balansas\n5 - išeiti\n"))
    match pasirinkimas:
        case 1:
            suma = int(input("Įveskite sumą: "))
            irasas = Irasas(suma, "Pajamos")
            zurnalas.append(irasas)
        case 2:
            suma = int(input("Įveskite sumą: "))
            irasas = Irasas(suma, "Išlaidos")
            zurnalas.append(irasas)
        case 3:
            print(zurnalas)
        case 4:
            balansas = 0
            for irasas in zurnalas:
                if irasas.tipas == "Pajamos":
                    balansas += irasas.suma
                if irasas.tipas == "Išlaidos":
                    balansas -= irasas.suma
            print("Balansas:", balansas)
        case 5:
            print("Viso gero")
            break

