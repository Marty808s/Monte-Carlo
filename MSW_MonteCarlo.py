import random
import matplotlib.pyplot as plt
import numpy as np

#SPORTKA
class Sportka:
    def __init__(self):
        self.vylos_cisla = []
        self.bonus_cislo = []
        self.hrac_hl_losovani = []
        self.hrac_bonus_num = []

    def losovani(self, pocet_cisel):
        self.vylos_cisla.clear()
        for _ in range(pocet_cisel):
            pick = random.randint(1,48)
            self.vylos_cisla.append(pick)
        #print("Vylosovaná čísla:",self.vylos_cisla)
        return

    def bonus_num(self):
        self.bonus_cislo.clear()
        bonus_pick = random.randint(1,48)
        self.bonus_cislo.append(bonus_pick)
        print("-----------------------------BONUSY:-----------------------------")
        print("Bonusové číslo:",self.bonus_cislo)
        return

#-----------------------------------------------------------------------------------------
#HRÁČ

    def losovani_hrace(self,pocet_cisel):
        self.hrac_hl_losovani.clear()
        for _ in range(pocet_cisel):
            pick = random.randint(1, 48)
            self.hrac_hl_losovani.append(pick)
        #print("Vylosovaná čísla HRÁČE:",self.hrac_hl_losovani)
        return

    def bonus_hrac(self):
        self.hrac_bonus_num.clear()
        bonus_pick = random.randint(1,48)
        self.hrac_bonus_num.append(bonus_pick)
        print("Bonusové číslo HRÁČ:",self.hrac_bonus_num)
        return

#VÝSLEDKY

    def vyhodnotit_vysledky(self):
        global vyhra
        global status
        bank = 100000
        vyhra = 0

        #vyhodnoceni kola
        spravne_cisla = set(self.hrac_hl_losovani).intersection(self.vylos_cisla)
        pocet_spravnych_cisel = len(spravne_cisla)

        pocet_bonus = set(self.bonus_cislo).intersection(self.hrac_bonus_num)
        bonus_inter = len(pocet_bonus)

        print("-----------------------------Výsledky:-----------------------------")
        print(f"Hráčovy čísla: {self.hrac_hl_losovani}")
        print(f"Vylosovaná čísla: {self.vylos_cisla}")
        print(f"Počet správných čísel: {pocet_spravnych_cisel}")
        print(f"Počet správných BONUSŮ: {bonus_inter}")


        if pocet_spravnych_cisel == 6:
            vyhra = bank
            status = 1
            print("Jackpot! Všechna čísla uhodnuta!", vyhra ,"Kč!")

        elif pocet_spravnych_cisel == 5:
            vyhra = 50000
            status = 0
            print("Gratulujeme, máte výhru!", vyhra ,"Kč!")

        elif pocet_spravnych_cisel == 4:
            vyhra = 1200
            status = 0
            print("Gratulujeme, máte výhru!", vyhra ,"Kč!")

        elif pocet_spravnych_cisel == 3:
            vyhra = 100
            status = 0
            print("Gratulujeme, máte výhru!", vyhra ,"Kč!")

        elif pocet_spravnych_cisel == 2:
            vyhra = 40
            status = 0
            print("Gratulujeme, máte výhru!", vyhra ,"Kč!")

        else:
            print("Bohužel, nemáte výhru!", vyhra ,"Kč!")
            status = 0

        if bonus_inter > 0:
            bonus_vyhra = bonus_inter * 5000
            vyhra += bonus_vyhra
            status += 0
            print(f"Vyšel Vám bonus: {vyhra} Kč")
        return status
        #return vyhra -> pokud bych chtel pocitat penezni vyhru


    def monte_carlo(self, pocet_iteraci):
        okamzite_pravdepodobnost = []
        soucet_hodnot = 0

        for pokus in range(pocet_iteraci):
            self.losovani(6)
            self.bonus_num()
            self.losovani_hrace(6)
            self.bonus_hrac()


            vysledek_iterace = self.vyhodnotit_vysledky()

            soucet_hodnot += vysledek_iterace
            print("SOUČET HODNOT:", soucet_hodnot)

            okamzite_pravdepodobnost.append(soucet_hodnot / (pokus + 1)*100)

        #VÝPOČET PRŮMĚRU
        avg = np.average(okamzite_pravdepodobnost)
        print("AVARAGE JE:", avg)

        #FORMÁT GRAFU - VÝSTUP
        plt.title("PRAVDĚPODOBNOST: Sportka JACKPOT x 10 000 000 iterací")
        plt.axhline(y=avg, color="r", linestyle="-")
        plt.xlabel("Počet iterací")
        plt.ylabel("Pravděpodobnost [%]")
        plt.legend(['Průměr'], loc='upper right')

        # Přidání popisku s hodnotou avg

        plt.text(0.5, avg, f"{round(avg,3)}", ha='right', va='bottom', color='r')
        #plt.text(0.5, avg, f"{avg}", ha='right', va='bottom', color='r')

        plt.xticks(fontsize=10)  # Velikost čísel na ose x
        plt.yticks(fontsize=10)  # Velikost čísel na ose y
        plt.grid(True)  # Zobrazení mřížky

        plt.tight_layout()  # Optimalizace umístění os a popisků

        plt.plot(okamzite_pravdepodobnost)
        plt.show()

#PRINCIP SPORTKY: CLASS SPORTKA NÁM VYGENERUJE 6 ČÍSEL Z ROZSAHU <1,48> + BONUSOVÉ ČÍSLO
#výhry budou záležet na počtu uhádnutých čísel ze Sportky / uhodnutí BONUSU

#6 správných čísel: Jackpot
#5 správných čísel: 50 000 Kč
#4 správná čísla: 1 200 Kč
#3 správná čísla: 100 Kč
#2 správná čísla: 40 Kč
#uhodnuti BONUS num += 5 000 KČ

sportka = Sportka()
sportka.monte_carlo(10000000)
