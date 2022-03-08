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

        result= soup.find('div',{'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1


        hasil=dict()
        hasil['tanggal'] = tanggal
        hasil ['jam'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls' : ls,  'bt' : bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
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
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"lokasi {result['lokasi']}")
    print(f"dirasakan {result['dirasakan']}")

#if __name__ == '__main__':
#    print('ini adalah package gempaterkini')