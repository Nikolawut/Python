pocetni_iznosi = [1000, 1500, 2000, 2500]
kamatna_stopa = 0.03
gubitak = sum(iznos * kamatna_stopa for iznos in pocetni_iznosi)
print("Ukupni gubitak banke od kamate na štednju:", gubitak)