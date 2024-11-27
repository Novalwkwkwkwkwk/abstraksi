from abc import ABC, abstractmethod

class Makanan(ABC):
    def __init__(self, variabel_privat, variabel_proteksi):
        self.__variabel_privat = variabel_privat  
        self._variabel_proteksi = variabel_proteksi  

    @abstractmethod
    def tampilkan(self):

        pass

    def tampilkan_privat(self):
      
        print(f"Variabel Privat: {self.__variabel_privat}")


class MakananTurunan(Makanan):
    def tampilkan(self):
       
        print(f"Variabel Proteksi: {self._variabel_proteksi}")

    def akses_proteksi(self):
       
        print(f"Mengakses Variabel Proteksi: {self._variabel_proteksi}")


makanan_turunan = MakananTurunan("Rahasia Baru", "Proteksi Baru")

makanan_turunan.tampilkan()           
makanan_turunan.akses_proteksi()      
makanan_turunan.tampilkan_privat()  
