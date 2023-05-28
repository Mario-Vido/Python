import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

i = 1
pocitadlo = 0
while True:
    i = 1
    pocitadlo += 1
    print(pocitadlo)
    driver = webdriver.Chrome()

    driver.get("https://docs.google.com/forms/d/1mfPYHgcqv8aNSZZot9DkOMtewkIodUo4pBBFcn9A4kM/viewform?edit_requested=true")
    # https://docs.google.com/forms/d/1mfPYHgcqv8aNSZZot9DkOMtewkIodUo4pBBFcn9A4kM/viewform?edit_requested=true
    # "https://docs.google.com/forms/d/e/1FAIpQLScvBclavzzhzQPKhq-2fg3EWiabPdrGyDsFOSn0JaJ0SzaM-A/viewform?vc=0&c=0"
    wait = WebDriverWait(driver, 10)
    questions_container = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']")))

    # Find all the question containers on the page
    # questions = driver.find_elements(By.XPATH, "//div[@role='listitem']")
    questions = driver.find_elements(By.XPATH, "//div[@class='Qr7Oae']")

    # Loop through each question and randomly select an answer
    for question in questions:
        if 'Demografické údaje\n\n1. Pohlavie:\n*\nŽena\nMuž' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            radio_buttons[1].click()
            # random_radio_button = random.choice(radio_buttons[0:2])
            # random_radio_button.click()
        elif '2. Do ktorej vekovej skupiny spadáte?\n*\n18 až 25 rokov\n26 až 39 rokov\n40 až 59 rokov\n60 a viac rokov' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[2:6])
            random_radio_button.click()
        elif '3. Aké je Vaše najvyššie dosiahnuté vzdelanie?\n*\nZákladné vzdelanie\nUčňovské alebo stredné odborné vzdelanie bez maturity\nÚplné stredné vzdelanie s maturitou\nVysokoškolské vzdelanie' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[6:10])
            random_radio_button.click()
        elif '4. V ktorom kraji bývate, resp. sa najviac zdržiavate?\n*\nBratislavský kraj\nTrnavský kraj\nTrenčiansky kraj\nNitriansky kraj\nBanskobystrický kraj\nŽilinský kraj\nPrešovský kraj\nKošický kraj' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[10:18])
            random_radio_button.click()
        elif '5. Bývate:\n*\nV meste\nNa dedine' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            # random_radio_button = random.choice(radio_buttons[18:19])
            # random_radio_button.click()
            radio_buttons[19].click()
        elif '6. Pracovný status:\n*\nZamestnaný/á\nNezamestnaný/á\nŠtudent/ka\nSamostatne zárobková činná osoba\nSom na materskej\nSom na dôchodku' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[20:26])
            random_radio_button.click()
        elif 'Spoločensky zodpovedné podnikanie očami spotrebiteľa\n7. Zaregistrovali ste už pojem Spoločenská zodpovednosť podnikov?\n„V Spoločenskej zodpovednosti podnikov ide o trvalý záväzok samotného podniku správať sa eticky, prispievať k trvalo udržateľnému ekonomickému rozvoju a súčasne prispievať k zlepšeniu kvality života svojich zamestnancov, ich rodín a miestnej komunity a spoločnosti ako celku.“\n*\nÁno počul/a som už o tom a viem čo to znamená\nÁno počul/a som už o tom, ale nevedel/a som čo to znamená\nNie nepočul/a som ešte o tom a nevedel/a som čo to znamená' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[26:29])
            random_radio_button.click()
        elif '8. Vyhľadávate si, alebo sa zaujímate o to či je podnik spoločensky zodpovedný?\n*\nUrčite áno\nSkôr áno\nNeutrálny postoj\nSkôr nie\nNie' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")
            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue
            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[29:34])
            random_radio_button.click()
        elif '9. Myslíte si, že by mal každý podnik dodržiavať spoločensky zodpovedné správanie?\n*\nUrčite áno\nSkôr áno\nNeutrálny postoj\nSkôr nie\nNie' in question.text:
            print("The text is present in the web element")
            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[34:39])
            random_radio_button.click()
        elif '10. Kúpili by ste si produkt, ak by bol spoločensky zodpovedný, no stál by viac ako produkt od firmy, ktorá vo svojom podnikaní nedodržiava SZP?\n*\nUrčite áno\nSkôr áno\nNeutrálny postoj\nSkôr nie\nNie' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[39:44])
            random_radio_button.click()
        elif '11. Vraciate sa ako spotrebitelia k opätovnému nákupu produktu, ktorý je vyrobený firmou, ktorá je spoločensky zodpovedná?\n*\nUrčite áno\nSkôr áno\nNeutrálny postoj\nSkôr nie\nNie' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[44:49])
            random_radio_button.click()
        elif '12. Myslíte si, že je pre podnik výhodou, že sa správa spoločensky zodpovedne?\n*\nUrčite áno\nSkôr áno\nNeutrálny postoj\nSkôr nie\nNie' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[49:54])
            random_radio_button.click()
        elif '13. Ak ste na vyššie položenú otázku odpovedali áno, tak v čom konkrétne je to pre ňu výhodou? (Vyberte akýkoľvek počet odpovedí. Ak ste označili možnosť nie označte odpoveď: Nevidím v tom výhodu pre podnik)\n*\nSZP zvyšuje dlhodobý potenciál podniku\nSZP pomáha pri budovaní dôvery, značky a dobrého mena podniku\nNapomáha manažovať riziká\nPodporuje inováciu\nNapomáha zvyšovať zisky podniku\nZvýšenie lojality zákazníkov, zamestnancov, dodávateľov a akcionárov\nNevidím v tom výhodu pre podnik\nIné:' in question.text:

            # Find all the checkboxes for this question
            checkboxes = question.find_elements(By.XPATH, "//div[@role='checkbox']")
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
            # Randomly select one checkbox to click
            print(radio_buttons[49].get_attribute("aria-checked"),radio_buttons[50].get_attribute("aria-checked"))
            if radio_buttons[49].get_attribute("aria-checked") == "true" or radio_buttons[50].get_attribute("aria-checked") == "true":
                random_checkbox = random.choice(checkboxes[0:6 - 1])
                random_checkbox.click()
            else:
                checkboxes[7-1].click()
        if '14. Zmenila nejako Váš postoj k SZP momentálna energetická kríza?\n*\nUrčite áno\nSkôr áno\nNeutrálny postoj\nSkôr nie\nNie' in question.text:

            radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")

            # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
            if len(radio_buttons) == 0:
                continue

            # Náhodne vyberte jedno začiarkavacie políčko v riadku
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
            # Randomly select one radio button to click
            random_radio_button = random.choice(radio_buttons[54:59])
            random_radio_button.click()
        if '15. Ak ste na vyššie položenú otázku odpovedali áno tak v čom konkrétne to zmenilo Váš postoj? (Vyberte akýkoľvek počet odpovedí. Ak ste označili možnosť nie označte odpoveď: Nie neovplyvnilo to môj postoj)\n*\nViac sa zaujímam o to, či podnik praktizuje SZP\nViac sa zaujímam o to, či firma dáva možnosť znevýhodneným skupinám obyvateľstva zamestnať sa\nViac sledujem a zaujímam sa o to, či má firma ekologickú podnikovú kultúru\nSnažím sa viac podporiť firmy, ktoré uplatňujú SZP\nViac sledujem pomoc štátu podnikom, ktoré sa snažia udržať si SZP aj napriek momentálnej situácií\nNie neovplyvnilo to môj postoj\nIné:' in question.text:

            # Find all the checkboxes for this question
            checkboxes = question.find_elements(By.XPATH, "//div[@role='checkbox']")
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
            # Randomly select one checkbox to click
            if radio_buttons[54].get_attribute("aria-checked") == "true" or radio_buttons[55].get_attribute("aria-checked") == "true":
                random_checkbox = random.choice(checkboxes[8:13 - 1])
                random_checkbox.click()
            else:
                checkboxes[14-1].click()
        elif 'Sociálna oblasť\n16. Zhodnoťte na škále od 1-5, pričom 1 je úplne súhlasím a  5 je úplne nesúhlasím vaše vnímanie jednotlivých aktivít v rámci sociálnej oblasti: \n*\n1 2 3 4 5\nZamestnávanie ľudí s horšou pozíciou na trhu práce - ZŤP, staršie osoby, študentov, dlhodobo nezamestnané osoby...\nStarostlivosť a rekvalifikácia pre zamestnancov -financovanie kurzov a školení, ktoré by zlepšili výkon zamestnancov v práci\nPodpora zdravia a bezpečnosti zamestnancov\nVyrovnanosť medzi osobným a pracovným životom zamestnancov\nZákaz a odmietanie detskej práce\nStarostlivosť  a podpora pre prepustených zamestnancov - pomoc pri hľadaní novej práce, poskytnutie finančnej podpory...\nZamestnávanie ľudí s horšou pozíciou na trhu práce - ZŤP, staršie osoby, študentov, dlhodobo nezamestnané osoby...\nStarostlivosť a rekvalifikácia pre zamestnancov -financovanie kurzov a školení, ktoré by zlepšili výkon zamestnancov v práci\nPodpora zdravia a bezpečnosti zamestnancov\nVyrovnanosť medzi osobným a pracovným životom zamestnancov\nZákaz a odmietanie detskej práce\nStarostlivosť  a podpora pre prepustených zamestnancov - pomoc pri hľadaní novej práce, poskytnutie finančnej podpory...' in question.text:

            rows = question.find_elements(By.XPATH, ".//div[@role='group']")
            for row in rows:
                # Nájdite všetky začiarkavacie políčka v riadku
                checkboxes = row.find_elements(By.XPATH, ".//div[@role='checkbox']")
                # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
                if len(checkboxes) == 0:
                    continue
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
                # Náhodne vyberte jedno začiarkavacie políčko v riadku
                random_checkbox = random.choice(checkboxes)
                # Kliknite na náhodne vybrané začiarkavacie políčko
                random_checkbox.click()
        elif 'Ekonomická oblasť\n17. Zhodnoťte na škále od 1-5, pričom 1 je úplne súhlasím a  5 je úplne nesúhlasím vaše vnímanie jednotlivých aktivít v rámci ekonomickej oblasti: \n*\n1 2 3 4 5\nMarketingová a reklamná etika - poskytovanie presných a jasných informácií o produktoch a službách\nOdmietanie korupcie\nZameranie sa na spokojnosť zákazníkov, znižovanie počtu sťažností a reklamácií - po predajný servis, osobnejší prístup k zákazníkom...\nFérové vzťahy pri dodávateľoch - platenie faktúr v dobe splatnosti, ochrana dát, diskrétnosť, spoľahlivosť...\nBezpečnosť a kvalita produktov a služieb\nDobré vzťahy s akcionármi, investormi a spoločníkmi\nMarketingová a reklamná etika - poskytovanie presných a jasných informácií o produktoch a službách\nOdmietanie korupcie\nZameranie sa na spokojnosť zákazníkov, znižovanie počtu sťažností a reklamácií - po predajný servis, osobnejší prístup k zákazníkom...\nFérové vzťahy pri dodávateľoch - platenie faktúr v dobe splatnosti, ochrana dát, diskrétnosť, spoľahlivosť...\nBezpečnosť a kvalita produktov a služieb\nDobré vzťahy s akcionármi, investormi a spoločníkmi' in question.text:

            rows = question.find_elements(By.XPATH, ".//div[@role='group']")
            for row in rows:
                # Nájdite všetky začiarkavacie políčka v riadku
                checkboxes = row.find_elements(By.XPATH, ".//div[@role='checkbox']")
                # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
                if len(checkboxes) == 0:
                    continue
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
                # Náhodne vyberte jedno začiarkavacie políčko v riadku
                random_checkbox = random.choice(checkboxes)
                # Kliknite na náhodne vybrané začiarkavacie políčko
                random_checkbox.click()
        elif 'Environmentálna oblasť \n18. Zhodnoťte na škále od 1-5, pričom 1 je úplne súhlasím a  5 je úplne nesúhlasím vaše vnímanie jednotlivých aktivít v rámci environmentálnej oblasti: \n*\n1 2 3 4 5\nVplyv výroby na životné prostredie v mieste pôsobiska\nInvestovanie do ekologickejších technológií\nEkologická podniková kultúra – šetrenie energií, vody a tepla pri prevádzke alebo výrobe...\nEkonomické zaobchádzanie a ochrana  prírodných zdrojov – opätovné využitie úžitkovej vody z výrobných procesov, slnečná energia ako zdroj energie, snaha o trvale udržateľný rozvoj...\nMinimalizácia tvorby odpadu jeho následná recyklácia a snaha o opätovné využitie vyprodukovaného odpadu\nSnaha o komplexné a bezodpadové spracovanie\nVplyv výroby na životné prostredie v mieste pôsobiska\nInvestovanie do ekologickejších technológií\nEkologická podniková kultúra – šetrenie energií, vody a tepla pri prevádzke alebo výrobe...\nEkonomické zaobchádzanie a ochrana  prírodných zdrojov – opätovné využitie úžitkovej vody z výrobných procesov, slnečná energia ako zdroj energie, snaha o trvale udržateľný rozvoj...\nMinimalizácia tvorby odpadu jeho následná recyklácia a snaha o opätovné využitie vyprodukovaného odpadu\nSnaha o komplexné a bezodpadové spracovanie' in question.text:

            rows = question.find_elements(By.XPATH, ".//div[@role='group']")
            for row in rows:
                # Nájdite všetky začiarkavacie políčka v riadku
                checkboxes = row.find_elements(By.XPATH, ".//div[@role='checkbox']")
                # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
                if len(checkboxes) == 0:
                    continue
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
                # Náhodne vyberte jedno začiarkavacie políčko v riadku
                random_checkbox = random.choice(checkboxes)
                # Kliknite na náhodne vybrané začiarkavacie políčko
                random_checkbox.click()
        elif '19. Posúďte dôležitosť jednotlivých oblastí na škále 1-5, pričom 1 veľmi dôležité a 5 vôbec nie je dôležité:\n*\n1 2 3 4 5\nSociálna oblasť\nEkonomická oblasť\nEnvironmentálna oblasť\nSociálna oblasť\nEkonomická oblasť\nEnvironmentálna oblasť' in question.text:

            rows = question.find_elements(By.XPATH, ".//div[@role='group']")
            for row in rows:
                # Nájdite všetky začiarkavacie políčka v riadku
                checkboxes = row.find_elements(By.XPATH, ".//div[@role='checkbox']")
                # Ak nie sú žiadne začiarkavacie políčka v riadku, pokračujte na ďalší riadok
                if len(checkboxes) == 0:
                    continue
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
                # Náhodne vyberte jedno začiarkavacie políčko v riadku
                random_checkbox = random.choice(checkboxes)
                # Kliknite na náhodne vybrané začiarkavacie políčko
                random_checkbox.click()
        elif '20. Čo by ste ocenili od podnikov v spojitosti so spoločensky zodpovedným podnikaním? (Vyberte akýkoľvek počet odpovedí)\n*\nVyužívanie lokálnych obnoviteľných zdrojov\nRiešenie sťažností verejnosti na porušovanie pravidiel SZP\nPodiel lokálnych dodávateľov\nVyhodnocovanie environmentálnej výkonnosti firmy\nSpolupráca pri riešení environmentálnych problémov\nVzdelávanie verejnosti v oblasti SZP\nIné:' in question.text:

            # Find all the checkboxes for this question
            checkboxes = question.find_elements(By.XPATH, "//div[@role='checkbox']")
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
            # Randomly select one checkbox to click
            random_checkbox = random.choice(checkboxes[225:231 - 1])
            random_checkbox.click()
        elif '21. Uplatňujete ako spotrebiteľ nejaké spoločensky zodpovedné aktivity vo vašej domácnosti? (Vyberte akýkoľvek počet odpovedí)\n*\nRecyklovanie odpadu\nObmedzenie nákupu výrobkov v plastových obaloch\nNákup v bezobalových obchodoch\nPri nákupe si vyberáte produkty s minimálnym alebo žiadnym obalom\nNákupy si balíte do vlastných opakovane použiteľných tašiek z bio bavlny alebo recyklovaných materiálov\nVyberáte si iba dôveryhodných lokálnych pestovateľov a farmárov v okolí\nNie neuplatňujem žiadne spoločensky zodpovedné aktivity\nIné:' in question.text:

            # Find all the checkboxes for this question
            checkboxes = question.find_elements(By.XPATH, "//div[@role='checkbox']")
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox']")))
            # Randomly select one checkbox to click
            random_checkbox = random.choice(checkboxes[232:239 - 1])
            random_checkbox.click()
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Odoslať']")))

    # click on the button
    button.click()

    # Close the webdriver
    time.sleep(2)
    driver.quit()

    # check if the condition is met and break out of the loop if it is
    if pocitadlo == 20:
        break
