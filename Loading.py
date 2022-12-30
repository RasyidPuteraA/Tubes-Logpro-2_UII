import time

def page():
    # Tunggu selama 1 detik 10 kali
    print("\nMohon menunggu\n")
    for i in range(6):
        print("*", end="")
        time.sleep(0.5)

    print("\n\nTerimakasih Telah menunggu\n")