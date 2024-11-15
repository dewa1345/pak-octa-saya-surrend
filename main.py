from operatorku.tambah import jumlah
from operatorku.kurang import kurang
from operatorku.dot import dot_product
from operatorku.panjang import panjang
from operatorku.vector_unit import unit_vector

def main():
    while True:
        print("\nOperasi pada vektor 2D")
        print("1. Penjumlahan vektor")
        print("2. Pengurangan vektor")
        print("3. Dot Product")
        print("4. Panjang Vektor")
        print("5. Vektor Unit")
        print("6. Keluar")

        pilihan = input("Masukkan nomor 1-6: ")

        if pilihan == "6":
            print("Program selesai.")
            break

        #Input vektor dari pengguna
        try:
            vek_A = list(map(int, input("Masukkan vektor A (dalam format x,y): ").split(',')))
            vek_B = list(map(int, input("Masukkan vektor B (dalam format x,y): ").split(',')))
        except ValueError:
            print("Input tidak valid, silakan masukkan vektor dalam format x,y.")
            continue

        if pilihan == "1":
            print("Hasil Penjumlahan:", jumlah(vek_A, vek_B))
        elif pilihan == "2":
            print("Hasil Pengurangan:", kurang(vek_A, vek_B))
        elif pilihan == "3":
            print("Hasil Dot Product:", dot_product(vek_A, vek_B))
        elif pilihan == "4":
            print("Panjang Vektor A:", panjang(vek_A))
            print("Panjang Vektor B:", panjang(vek_B))
        elif pilihan == "5":
            print("Vektor Unit A:", unit_vector(vek_A))
            print("Vektor Unit B:", unit_vector(vek_B))
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#menu
main()
