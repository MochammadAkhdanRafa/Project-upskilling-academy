# Impor modul 
import requests
import pandas as pd

# mengubah deskripsi cuaca mennjadi bahasa indonesia
deskripsi_cuaca_id = {
    'clear sky': 'cerah',
    'few clouds': 'berawan sebagian',
    'broken clouds': 'berawan',
    'overcast clouds': 'mendung',
    'moderate rain': 'hujan sedang',
    'light rain': 'hujan ringan',
    'shower rain': 'hujan gerimis',
    'rain': 'hujan',
    'thunderstorm': 'badai petir',
    'snow':'salju',
    'mist': 'kabut'
}
    
# Fungsi untuk mengambil data cuaca
def ambil_data_cuaca(kota, api_key):
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}'
  response = request.get(url)
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print(f'Error {response.status_code}: {response.text}')
    return None

# fungsi untuk mendapatkan cuaca
def analisis_cuaca(data):
    if data is None:
      return None
    
forecast_list = data.get('list', [])
dates = []
temperature = []
humidities = []
weather_descriptions = []

for item in forecast_list:
    date = item['dt_txt'].split(' ')[0]
    dates.append(date)
    temperature.append(item['main']['temp'])
    humidities.append(item['main']['humidity'])
    desc = item['weather'][0]['description']
    weather_descriptions.append(deskripsi_cuaca_id.get(desc, desc))
    
    df = pd.DataFrame({
        'Tanggal': dates,
        'Suhu (k)': temperature,
        'Kelembapan (%)':  humidities,
        'Deskripsi Cuaca': weather_description
    })
    
    df['suhu (C)'] = df['suhu (K)'] - 273.15
    df = df.drop(columns=['suhu (K)'])
    
    df_daily = df.groupby('tanggal').agg({
        'suhu (C)' : 'mean',
        'kelembapan (%)' : 'mean',
        'Deskripsi Cuaca' : lambda x: x.mode()[0]
    }).reset_index()
    
    df_daily.index = df_daily.index + 1
    return df_daily

def start():
    while True:
        kota = input('Masukan Nama Kota: ')
        api_key = 'c40b679d5307e4b29a19e44392b1e5f3'
        
        data = ambil_data_cuaca(kota, api_key)
        df = analisis_cuaca(data)
        
        if df is not None:
            print(df.head())
        
        pilihan = input("\nApakah kamu ingin menjalankan program lagi? [y/n] ")
        if pilihan.lower() == "n":
            main.menu()
        
if __name__ == '__main__':
    start()