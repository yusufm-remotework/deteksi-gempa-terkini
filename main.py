"""
Aplikasi deteksi gempa terkini
"""


def ekstraksi_data():
    """
   Tanggal : 06 Maret 2022
   Jam : 05:40:28 WIB
   Skala : 5.0
   Kedalaman : 43 km
   Lokasi : LU = 3.55 BT = - 126.10
   Pusat gempa : 67 km Tenggara TAHUNA-KEP.SANGIHE-SULUT
   Keterangan : tidak berpotensi TSUNAMI
    :return:
    """
    hasil=dict()
    hasil['tanggal'] = '06 Maret 2022'
    hasil ['jam'] = '05:40:28 WIB'
    hasil['skala'] = 5.0
    hasil['kedalaman'] = '43 km'
    hasil['lokasi'] = {'lu' : 3.55,  'bt' : - 126.10}
    hasil['pusat gempa'] = '67 km Tenggara TAHUNA-KEP.SANGIHE-SULUT'
    hasil['keterangan'] = 'tidak berpotensi TSUNAMI'


    print(hasil)
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"jam {result['jam']}")
    print(f"skala {result['skala']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi {result['lokasi']}")
    print(f"pusat gempa {result['pusat gempa']}")
    print(f"keterangan {result['keterangan']}")


    pass


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)