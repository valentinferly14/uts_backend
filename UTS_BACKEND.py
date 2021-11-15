print("======================")
print("===  Kedai Voucher ===")
print("======================")
belivoucher = []
while True:
    menu_provider = input('======================\n===  Kedai Voucher ===\n===   1. Tri       ===\n===   2. XL        ===\n===   3. Telkomsel ===\n======================\n Pilih Provider 1-3: \n')
    if menu_provider == "1":
        print("======================")
        print("Anda Memilih Provider : Tri")
        print("Pilih paket voucher Tri")
        voucher_tri = ["Tri 2 GB (1 Hari)", "Tri 10 GB (7 Hari)", "Tri 20 GB (30 Hari)"]
        while True:
            for a in range(0, len(voucher_tri)):
                print(f'{a + 1}.{voucher_tri[a]}')
            list_voucher_tri = int(input('Pilih paket voucher 1-3:\n'))
            if list_voucher_tri == 1:
                belivoucher.append(voucher_tri[0])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            elif list_voucher_tri == 2:
                belivoucher.append(voucher_tri[1])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            elif list_voucher_tri == 3:
                belivoucher.append(voucher_tri[2])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            else:
                print("======================")
                print("voucher tidak tersedia\n")
                continue
    elif menu_provider == "2":
        print("======================")
        print("Anda Memilih Provider : XL")
        print("Pilih paket voucher XL")
        voucher_xl = ["XL 2 GB (7 Hari) ", "XL 8 GB (30 Hari)", "XL 16 GB (30 Hari)"]
        while True:
            for a in range(0, len(voucher_xl)):
                print(f'{a + 1}.{voucher_xl[a]}')
            list_voucher_xl = int(input('Pilih paket voucher 1-3:\n'))
            if list_voucher_xl == 1:
                belivoucher.append(voucher_xl[0])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            elif list_voucher_xl == 2:
                belivoucher.append(voucher_xl[1])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            elif list_voucher_xl == 3:
                belivoucher.append(voucher_xl[2])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            else:
                print("======================")
                print("voucher tidak tersedia\n")
                continue
    elif menu_provider == "3":
        print("======================")
        print("Anda Memilih Provider : Telkomsel")
        print("Pilih paket voucher Telkomsel")
        voucher_tsel = ["Tsel 10 GB (7 Hari)", "Tsel 25 GB (30 Hari)", "Tsel 50GB (60 Hari)"]
        while True:
            for a in range(0, len(voucher_tsel)):
                print(f'{a + 1}.{voucher_tsel[a]}')
            list_voucher_tsel = int(input('Pilih paket voucher 1-3:\n'))
            if list_voucher_tsel == 1:
                belivoucher.append(voucher_tsel[0])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            elif list_voucher_tsel == 2:
                belivoucher.append(voucher_tsel[1])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            elif list_voucher_tsel == 3:
                belivoucher.append(voucher_tsel[2])
                print('=== voucher yang dibeli ===')
                for b in range(0, len(belivoucher)):
                    print(f'{b + 1}.{belivoucher[b]}  1x')
                break
            else:
                print("======================")
                print("voucher tidak tersedia\n")
                continue
    else:
        print("voucher tidak tersedia")
        continue
    validasi_voucher = input('isi lagi? Y/n\n')
    if validasi_voucher == "Y" or validasi_voucher == "y":
        print("======================")
        continue
    else:
        print("Terimakasih telah beli voucher di kedai kami...")
        break
