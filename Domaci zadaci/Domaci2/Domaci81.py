cijene = [100, 110, 90, 120, 115]
najveci_pad = min(cijene[i] - cijene[i+1] for i in range(len(cijene)-1))
najveci_porast = max(cijene[i+1] - cijene[i] for i in range(len(cijene)-1))
print("Najveći pad cijena:", najveci_pad)
print("Najveći porast cijena:", najveci_porast)