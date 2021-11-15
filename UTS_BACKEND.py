print("======================")
print("===  Kedai  Pulsa  ===")
print("======================")
beliPulsa = []
while True:
    menu_provider = input('======================\n===   Kedai Pulsa  ===\n===   1. Tri       ===\n===   2. XL        ===\n===   3. Telkomsel ===\n======================\n Pilih Provider 1-3: \n')
    if menu_provider == "1":
        print("======================")
        print("Anda Memilih Provider : Tri")
        print("Pilih nominal pulsa Tri")
        pulsa_tri = ["Rp 5.000", "Rp 10.000", "Rp 20.000"]
        while True:
            for a in range(0, len(pulsa_tri)):
                print(f'{a + 1}.{pulsa_tri[a]}')
            list_pulsa_tri = int(input('Pilih Nominal 1-3:\n'))
            if list_pulsa_tri == 1:
                beliPulsa.append(pulsa_tri[0])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            elif list_pulsa_tri == 2:
                beliPulsa.append(pulsa_tri[1])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            elif list_pulsa_tri == 3:
                beliPulsa.append(pulsa_tri[2])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            else:
                print("======================")
                print("Pulsa tidak tersedia\n")
                continue
    elif menu_provider == "2":
        print("======================")
        print("Anda Memilih Provider : XL")
        print("Pilih nominal pulsa XL")
        pulsa_xl = ["Rp 10.000", "Rp 20.000", "Rp 45.000"]
        while True:
            for a in range(0, len(pulsa_xl)):
                print(f'{a + 1}.{pulsa_xl[a]}')
            list_pulsa_xl = int(input('Pilih Nominal 1-3:\n'))
            if list_pulsa_xl == 1:
                beliPulsa.append(pulsa_xl[0])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            elif list_pulsa_xl == 2:
                beliPulsa.append(pulsa_xl[1])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            elif list_pulsa_xl == 3:
                beliPulsa.append(pulsa_xl[2])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            else:
                print("======================")
                print("Pulsa tidak tersedia\n")
                continue
    elif menu_provider == "3":
        print("======================")
        print("Anda Memilih Provider : Telkomsel")
        print("Pilih nominal pulsa Telkomsel")
        pulsa_tsel = ["Rp 10.000", "Rp 20.000", "Rp 50.000"]
        while True:
            for a in range(0, len(pulsa_tsel)):
                print(f'{a + 1}.{pulsa_tsel[a]}')
            list_pulsa_tsel = int(input('Pilih Nominal 1-3:\n'))
            if list_pulsa_tsel == 1:
                beliPulsa.append(pulsa_tsel[0])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            elif list_pulsa_tsel == 2:
                beliPulsa.append(pulsa_tsel[1])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            elif list_pulsa_tsel == 3:
                beliPulsa.append(pulsa_tsel[2])
                print('=== Pulsa yang dibeli ===')
                for b in range(0, len(beliPulsa)):
                    print(f'{b + 1}.{beliPulsa[b]}  1x')
                break
            else:
                print("======================")
                print("Pulsa tidak tersedia\n")
                continue
    else:
        print("Pulsa tidak tersedia")
        continue
    validasi_pulsa = input('isi lagi? Y/n\n')
    if validasi_pulsa == "Y" or validasi_pulsa == "y":
        print("======================")
        continue
    else:
        print("Mohon Tunggu, Pulsa anda akan segera kami proses...")
        break
