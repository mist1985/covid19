import requests
import csv

api_odgovor_svet = requests.get('https://covid19api.herokuapp.com/latest')
assert api_odgovor_svet.status_code < 400 #proverka dali sajtot e online assert
api_odgovor_mk = requests.get('https://thevirustracker.com/free-api?countryTotal=MK', headers={"User-Agent": "Chrome"})
assert api_odgovor_mk.status_code < 400 #proverka dali sajtot e online so assert

covid_statistika = api_odgovor_mk.json()['countrydata']
covid_statistika_status = api_odgovor_mk.json()['stat']  #Ova e status dali podatocite se azurirani vo JSON fajlot

if covid_statistika_status == "ok":

    vkupno_svet = print("Вкупно случаи во светот: "+ str(api_odgovor_svet.json()['confirmed']))
    vkupno_svet = print("Вкупно смртни случаи во светот: " + str(api_odgovor_svet.json()['deaths']))
    mk_novi = print("Македонија - нови денес:", covid_statistika[0]["total_new_cases_today"])
    mk_smrt = print("Македонија - смртни случаи:", covid_statistika[0]["total_deaths"])
    mk_izl = print("Македонија - излекувани: ", covid_statistika[0]["total_recovered"])
    mk_teski= print("Македонија - тешки случаи: ", covid_statistika[0]["total_serious_cases"])


else:
    print("Нешто не е во ред со статистиката, обидете се повторно подоцна")


# Zapisuvanje na vrednostite za svetot i Makedonija vo CSV fajlot


with open('covid19.csv', 'a', newline='') as csvfile: # moze w, no vo slucajot e staven a za append (t.e sekoe pustanje na skriptata ke se dodavaat rezultati)

    fieldnames = ['vkupno_svet', 'mk_novi']

    #Vo forma na Dictionary
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'vkupno_svet': str(api_odgovor_svet.json()['confirmed']),'mk_novi': covid_statistika[0]["total_new_cases_today"]})

