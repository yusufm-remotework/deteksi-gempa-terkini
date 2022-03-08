import requests
from bs4 import BeautifulSoup


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
    try:
         content = requests.get('https://www.bmkg.go.id/')
    except Exception :
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class' : 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result= soup.find('span',{'class' : 'ic magnitude'})
        magnitude = result.text


        hasil=dict()
        hasil['tanggal'] = tanggal #'06 Maret 2022'
        hasil ['jam'] = waktu #'05:40:28 WIB'
        hasil['skala'] = 5.0
        hasil['kedalaman'] = '43 km'
        hasil['lokasi'] = {'lu' : 3.55,  'bt' : - 126.10}
        hasil['pusat gempa'] = '67 km Tenggara TAHUNA-KEP.SANGIHE-SULUT'
        hasil['keterangan'] = 'tidak berpotensi TSUNAMI'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("tidak bisa menemukan data gempa terkini")
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"jam {result['jam']}")
    print(f"skala {result['skala']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LU={result['lokasi']['lu']}, BT={result['lokasi']['bt']}")
    print(f"pusat gempa {result['pusat gempa']}")
    print(f"keterangan {result['keterangan']}")

#if __name__ == '__main__':
#    print('ini adalah package gempaterkini')