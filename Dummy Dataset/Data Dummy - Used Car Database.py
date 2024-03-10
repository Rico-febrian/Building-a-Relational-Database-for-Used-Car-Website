# Create dummy data for used car database

# Import library yang akan digunakan
from faker import Faker
from tabulate import tabulate
import random
from datetime import datetime
import csv

# Generate lokalisasi faker
FAKER = Faker('id_ID')

# Fungsi untuk menampilkan data dalam bentuk tabular
def show_data(table):
    """
    Fungsi untuk menampilkan data

    Args:
        table (dict): Data dictionary yang ingin ditampilkan

    Returns:
        None
    """
    # Mengubah data dictionary menjadi tabel dengan format "psql"
    tab = tabulate(tabular_data= table,
                   headers= table.keys(),
                   tablefmt= "psql",
                   numalign= "center")
    print(tab)

# Fungsi untuk menyimpan file kedalam csv
def save_to_csv(data, nama_file):
    """
    Fungsi ini untuk membuat format menyimpan data dummy ke CSV

    Args:
        data (list): List of dictionary yang akan dijadikan CSV
        nama_file (str): Nama untuk file CSV

    Returns:
        None
    """
    # Membuka file CSV untuk ditulis beserta fitur yang akan digunakan.
    with open(file=f"{nama_file}.csv", mode='w', newline='', encoding='utf-8') as csv_file:

        # Membuat objek writer yang akan digunakan untuk menulis ke file CSV
        writer = csv.writer(csv_file)

        # Membuat header CSV dengan menggunakan key dari dictionary data.
        writer.writerow(list(data.keys()))

        # Mengetahui panjang data
        len_data = len(list(data.items())[0][1])

        # Menulis data ke file CSV
        for i in range(len_data):

            row = []

            for key in data.keys():
                row.append(data[key][i])
            writer.writerow(row)

# Fungsi untuk generate data dummy tabel cities
def cities_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel cities
    Args:
        n_data(int): Jumlah data dummy yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel
    table = {}

    # Membuat list berisi ID kota mulai dari 1 sampai n_data
    table["city_id"] = [i+1 for i in range(n_data)]

    # Membuat list berisi nama kota acak menggunakan library Faker sebanyak n_data.
    table["city_name"] = [FAKER.city() for i in range(n_data)]

    # Mengambil nilai baris pertama dari Faker.address().
    # Menggabungkanya dengan nilai dari kolom city_name
    table["address"] = [f"{FAKER.address().splitlines()[0]}, {' '.join(city.split()[0:])}"
                       for city in table["city_name"]]

    # Mengambil 2 elemen pertama dari FAKER.local_latlng(country_code="ID")
    # Kemudian, mengubah bentuk dan tipe datanya menjadi tuple dan float
    table["location"] = [tuple(map(float, FAKER.local_latlng(country_code="ID")[0:2])) for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

cities_table = cities_dummy(n_data=10, is_print=True)
#save_to_csv(data=cities_table, nama_file='cities')


# Fungsi untuk generate username unik
def generate_username():
    unique_username = set()
    username = FAKER.user_name()

    while username in unique_username:
        username = FAKER.user_name()

    unique_username.add(username)
    return username

# Fungsi untuk generate nama lengkap
def generate_name():
    first_name = FAKER.first_name()
    last_name = FAKER.last_name()
    full_name = f"{first_name} {last_name}"

    return full_name

# Fungsi untuk generate tanggal
def date_generator():
    # Set tanggal awal dan akhir
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)

    # Atur tanggal
    date = FAKER.date_time_between(start_date=start_date, end_date=end_date)

    return date.strftime('%Y-%m-%d')

# Fungsi untuk generate data dummy tabel users
def users_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel users
    Args:
        n_data(int): Jumlah data dummy yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel
    table = {}

    # Membuat list berisi ID user mulai dari 1 sampai n_data
    table["user_id"] = [i+1 for i in range(n_data)]

    # Membuat list berisi username yang dihasilkan dari fungsi generate_username
    table["username"] = [generate_username() for i in range(n_data)]

    # Memanggil elemen pertama dan kedua dari output fungsi generate_name
    # Masing-masing ditambahkan kedalam kolom first dan last name
    full_name = [generate_name() for i in range(n_data)]
    table["first_name"] = [first_name.split()[0] for first_name in full_name]
    table["last_name"] = [last_name.split()[1] for last_name in full_name]

    # Mengubah semua huruf menjadi kecil dan menghilangkan spasi data dalam variabel full_name
    # Membuat domain acak dengan library fake, gabungkan dan simpan ke list email
    table["email"] = [f"{name.lower().replace(' ', '')}@{FAKER.free_email_domain()}"
                      for name in full_name]

    # Membuat list berisi password acak menggunakan library faker
    table["password"] = [FAKER.password(length=15) for i in range(n_data)]

    # Membuat list berisi nomor telepon acak menggunakan library faker
    table["contact"] = [FAKER.phone_number() for i in range(n_data)]

    # Memanggil dan menyimpan nilai fungsi date generator ke dalam list
    date = [date_generator() for i in range(n_data)]
    table["registration_date"] = [date[i] for i in range(n_data)]

    # Membuat list berisi id kota secara acak dari variabel cities_tabel pada fungsi cities_dummy
    table["city_id"] = [random.choice(cities_table["city_id"]) for i in range(n_data)]

    # Membuat list berisi tipe status dan menyimpan datanya secara acak
    status = ['Active', 'Inactive']
    table["user_status"] = [random.choice(status) for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

users_table = users_dummy(n_data=50, is_print=True)
#save_to_csv(data=users_table, nama_file='users')

# Fungsi untuk generate nama brand dan model mobil
def cars_generator():
    cars_data = [
        ('Toyota', [
            ('Corolla Altis', 'Sedan'),
            ('Avanza', 'MPV'),
            ('Fortuner', 'SUV')
        ]),
        ('Honda', [
            ('Brio Satya', 'Hatchback'),
            ('Civic', 'Sedan'),
            ('CR-V', 'SUV')
        ]),
        ('Daihatsu', [
            ('Ayla', 'Hatchback'),
            ('Gran Max', 'Pickup'),
            ('Terios', 'SUV')
        ]),
        ('Suzuki', [
            ('Ertiga', 'MPV'),
            ('Ignis', 'Hatchback'),
            ('XL7', 'SUV')
        ]),
        ('Nissan', [
            ('March', 'Hatchback'),
            ('X-Trail', 'SUV'),
            ('Serena', 'MPV')
        ]),
        ('Mitsubishi', [
            ('Mirage', 'Hatchback'),
            ('Pajero Sport', 'SUV'),
            ('Xpander', 'MPV')
        ]),
        ('Mercedes-Benz', [
            ('C200', 'Sedan'),
            ('E250', 'Sedan'),
            ('GLA200', 'SUV')
        ]),
        ('Mazda', [
            ('2', 'Hatchback'),
            ('CX-3', 'SUV'),
            ('CX-5', 'SUV')
        ]),
        ('BMW', [
            ('318i', 'Sedan'),
            ('320i', 'Sedan'),
            ('520i', 'Sedan')
        ]),
        ('Chevrolet', [
            ('Captiva', 'SUV'),
            ('TraX', 'SUV'),
            ('Spark', 'Hatchback')
        ]),
        ('Hyundai', [
            ('Creta', 'SUV'),
            ('Santa Fe', 'SUV'),
            ('Stargazer', 'MPV')
        ]),
        ('Ford', [
            ('Fiesta', 'Hatchback'),
            ('Focus', 'Sedan'),
            ('Everest', 'SUV')
        ]),
        ('Wuling', [
            ('Almaz RS', 'SUV'),
            ('Confero S', 'MPV'),
            ('Cortez', 'MPV')
        ]),
        ('Isuzu', [
            ('Panther', 'MPV'),
            ('MU-X', 'SUV'),
            ('D-Max', 'Pickup')
        ]),
        ('Tesla', [
            ('Model 3', 'Sedan'),
            ('Model S', 'Sedan'),
            ('Model X', 'SUV')
        ]),
    ]

    return cars_data

# Fungsi untuk generate data dummy tabel products
def products_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel products
    Args:
        n_data(int): Jumlah data dummy yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel.
    table = {}

    # Membuat list berisi ID produk mulai dari 1 hingga n_data
    table["product_id"] = [i+1 for i in range(n_data)]

    # Memanggil dan memilih data secara acak dari fungsi cars_generator
    cars_data = [random.choice(cars_generator()) for i in range(n_data)]

    # Membuat list kosong untuk menampung data merek, model dan tipe bodi
    brands = []
    models = []
    body_types = []

    for i in range(n_data):
        # Memilih dan menyimpan data acak dari list cars_data
        # Berdasarkan merek dan model nya masing-masing
        brand, models_per_brand = random.choice(cars_data)
        model, body_type = random.choice(models_per_brand)

        # Menambahkan merek mobil ke list brands
        brands.append(brand)

        # Menggabungkan dan menambahkan nama merek dan model ke list models
        models.append(f"{brand} {model}")

        # Menambahkan tipe bodi mobil ke list body_types
        body_types.append(body_type)

    table["brand"] = brands
    table["model"] = models
    table["body_type"] = body_types

    # Membuat list tipe transmisi dan menyimpan datanya secara acak
    transmission_type = ['Manual', 'Automatic', 'Automatic Triptonic']
    table["transmission"] = [random.choice(transmission_type) for i in range(n_data)]

    # Membuat list tipe bahan bakar dan menyimpan datanya secara acak
    fuel_type = ['Gasoline', 'Diesel', 'Electric', 'Hybrid']
    table["fuel_type"] = [random.choice(fuel_type) for i in range(n_data)]

    # Membuat list kapasitas mesin dan menyimpan datanya secara acak
    machine_capacity = ['<1000 cc',
                        '>1000 - 1500 cc',
                        '>1500 - 2000 cc',
                        '>2000 - 3000 cc',
                        '>3000cc']
    table["machine_capacity"] = [random.choice(machine_capacity) for i in range(n_data)]

    # Membuat list berisi tanggal acak dari abad ini dengan library faker
    table["production_year"] = [FAKER.date_this_century().year for i in range(n_data)]

    # Membuat list harga beserta kelipatannya dan memilih datanya secara acak
    table["price"] = [FAKER.random_int(50_000_000, 1_000_000_000, 10_000_000 ) for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

products_table = products_dummy(n_data=100, is_print=True)
#save_to_csv(data=products_table, nama_file='products')

# Fungsi untuk generate data dummy tabel advertisements
def advertisements_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel advertisements
    Args:
        n_data(int): Jumlah data yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel.
    table = {}

    # Membuat list berisi ID iklan mulai dari 1 sampai n_data.
    table["advertisement_id"] = [i+1 for i in range(n_data)]

    # Mengambil semua data product_id dari variabel products_table pada fungsi products_dummy
    product_id = products_table["product_id"]

    # Memilih product_id secara acak dari variabel products_table pada fungsi products_dummy
    chosen_product_id = [random.choice(product_id) for i in range(n_data)]
    table["product_id"] = chosen_product_id

    table["user_id"] = [random.choice(users_table["user_id"]) for i in range(n_data)]

    # Melakukan indeksing untuk mendapatkan model dan tahun produksi
    # yang sesuai dari output fungsi products_dummy
    table["title"] = [(f'{products_table["model"][product_id.index(id)]} '
                       f'{products_table["production_year"][product_id.index(id)]}') for id in chosen_product_id]

    # Membuat list berisi deskripsi iklan dan menyimpan datanya secara acak
    description_data = ["Mobil bekas, kondisi bagus, siap pakai. Info Detail Hub Tlp/Wa",
                        "Sudah dipakai, kondisi terawat, tidak ada masalah mesin. Info Detail Hub Tlp/Wa",
                        "AC dingin, audio mantap, siap jalan jauh. Info Detail Hub Tlp/Wa",
                        "Pajak panjang, kaki-kaki nyaman, siap pakai. Info Detail Hub Tlp/Wa",
                        "Harga nego, kondisi bagus, mesin sehat. Info Detail Hub Tlp/Wa",
                        "Banyak fitur, cocok untuk keluarga, nyaman dikendarai. Info Detail Hub Tlp/Wa",
                        "Mobil irit, cocok untuk perjalanan harian. Info Detail Hub Tlp/Wa",
                        "Dijual mobil bekas, harga nego, kondisi terawat. Info Detail Hub Tlp/Wa",
                        "Tidak pernah kecelakaan, dokumen lengkap, siap pakai. Info Detail Hub Tlp/Wa",
                        "Kondisi prima, siap luar kota, pajak masih panjang. Info Detail Hub Tlp/Wa",
                        "Tidak pernah mogok, perawatan rutin, siap pakai. Info Detail Hub Tlp/Wa"]

    table["description"] = [random.choice(description_data) for i in range(n_data)]

    # Memanggil dan menyimpan nilai fungsi date_generator kedalam list
    date = [date_generator() for i in range(n_data)]
    table["created_date"] = [date[i] for i in range(n_data)]

    # Membuat list berisi status iklan dan menyimpan datanya secara acak
    ads_status = ['Available', 'Sold']
    table["advertisement_status"] = [random.choice(ads_status) for i in range(n_data)]

    # Memilih secara acak angka 0 hingga 1000
    table["advertisement_view"] = [random.randint(0, 1000) for i in range(n_data)]

    # Membuat list berisi url gambar acak menggunakan library faker
    table["image"] = [FAKER.image_url() for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

ads_table = advertisements_dummy(n_data=200, is_print=True)
#save_to_csv(data=ads_table, nama_file='advertisements')


# Fungsi untuk generate data dummy tabel user_searches
def searches_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel user searches
    Args:
        n_data(int): Jumlah data yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel
    table = {}

    # Membuat list berisi ID pencarian mulai dari 1 sampai n_data
    table["search_id"] = [i+1 for i in range(n_data)]

    # Membuat list berisi id user secara acak dari variabel users_tabel pada fungsi users_dummy
    table["user_id"] = [random.choice(users_table["user_id"]) for i in range(n_data)]

    # Membuat list berisi kata kunci pencarian dan menyimpan datanya secara acak
    keyword_data = ['Lokasi', 'Harga', 'Tahun', 'Merek', 'Model', 'Tipe Bodi', 'Transmisi', 'Kondisi']
    table["keyword"] = [random.choice(keyword_data) for i  in range(n_data)]

    # Memanggil dan menyimpan nilai fungsi date_generator kedalam list
    date = [date_generator() for i in range(n_data)]
    table["search_date"] = [date[i] for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

user_searches_table = searches_dummy(n_data=50, is_print=True)
#save_to_csv(data=user_searches_table, nama_file='user_searches')


# Fungsi untuk generate data dummy tabel offers
def offers_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel offers
    Args:
        n_data(int): Jumlah data yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel
    table = {}

    # Membuat list berisi ID penawaran mulai dari 1 sampai n_data
    table["offer_id"] = [i+1 for i in range(n_data)]

    # Membuat list berisi id user secara acak dari variabel users_tabel pada fungsi users_dummy
    table["user_id"] = [random.choice(users_table["user_id"]) for i in range(n_data)]

    # Membuat list berisi id iklan secara acak dari variabel ads_tabel pada fungsi advertisements_dummy
    table["advertisement_id"] = [random.choice(ads_table["advertisement_id"]) for i in range(n_data)]

    # Membuat list kosong untuk menampung data harga penawaran dan status penawaran
    table["offer_price"] = []
    table["offer_status"] = []

    # Mengambil semua data product_id dari variabel products_table pada fungsi products_dummy
    product_id = products_table["product_id"]

    # Memilih product_id secara acak dari variabel products_table pada fungsi products_dummy
    chosen_product_id = [random.choice(product_id) for i in range(n_data)]

    # Melakukan indeksing pada kolom harga dalam dari variabel products_table pada fungsi products_dummy
    # dan menyimpannya kedalam variabel harga asli (original_price)
    for ori_price in chosen_product_id:
        original_price = products_table["price"][product_id.index(ori_price)]

        # Membuat range penawaran harga acak antara 80% dan 90% dari harga asli
        offer_price = random.uniform(0.8 * original_price, 0.9 * original_price)

        # Menentukan status penawaran berdasarkan range nilai penawaran dengan harga asli
        # Jika nilai penawarannya kurang dari 0.2, status penawaran = menunggu
        if random.random() < 0.2:
            offer_status = 'Waiting'
        # Jika nilai penawarannya antara 85 - 95% dari harga asli, status penawaran = diterima
        elif 0.85 * original_price <= offer_price <= 0.95 * original_price:
            offer_status = 'Accepted'
        # Selain itu, status penawaran = ditolak
        else:
            offer_status = 'Rejected'

        # Mengubah format output harga penawaran menjadi integer dan menyimpannya ke masing-masing list
        offer_price = format(offer_price, '.0f')
        table["offer_price"].append(offer_price)
        table["offer_status"].append((offer_status))

    # Memanggil dan menyimpan nilai fungsi date_generator kedalam list
    date = [date_generator() for i in range(n_data)]
    table["offer_date"] = [date[i] for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

offers_table = offers_dummy(n_data=100, is_print=True)
#save_to_csv(data=offers_table, nama_file='offers')


# Fungsi untuk generate data dummy tabel reviews
def reviews_dummy(n_data, is_print):
    """
    Fungsi ini untuk membuat data dummy tabel reviews
    Args:
        n_data(int): Jumlah data yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan meneghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel
    table = {}

    # Membuat list berisi ID penawaran mulai dari 1 sampai n_data
    table["review_id"] = [i+1 for i in range(n_data)]

    # Membuat list berisi id user secara acak dari variabel users_tabel pada fungsi users_dummy
    table["user_id"] = [random.choice(users_table["user_id"]) for i in range(n_data)]

    # Membuat list berisi id iklan secara acak dari variabel ads_table pada fungsi advertisements_dummy
    table["advertisement_id"] = [random.choice(ads_table["advertisement_id"]) for i in range(n_data)]

    # Membuat parameter bobot untuk rating dan memilihnya secara acak
    rating_weights = [0.1, 0.1, 0.27, 0.27, 0.26]
    table["rating"] = [random.choices([1,2,3,4,5], rating_weights)[0] for i in range(n_data)]

    # Membuat list berisi deskripsi ulasan dan menyimpan datanya secara acak
    review_description = ['Mobilnya masih kinclong banget! Mesinnya halus, mantap!',
                          'Harganya pas di kantong. Gak mahal-mahal amat untuk mobil sebagus ini',
                          'Oke banget, sangat nyaman dikendarai, mesinnya responsif dan bahan bakarnya cukup efisien',
                          'Bensin  awet dan jarang ada masalah, cocok untuk pemakaian jangka panjang.',
                          'Hemat bahan bakar, pas buat harian atau jalan jauh.',
                          'Harganya sebanding sama kualitasnya',
                          'Mobilnya oke, cocok buat harian.', ' ']

    table["review_description"] = [random.choice(review_description) for i in range(n_data)]

    # Memanggil dan menyimpan nilai fungsi date_generator kedalam list
    date = [date_generator() for i in range(n_data)]
    table["review_date"] = [date[i] for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

reviews_table = reviews_dummy(n_data=50, is_print=True)
#save_to_csv(data=reviews_table, nama_file='reviews')


# Fungsi untuk generate data dummy tabel reports
def reports_dummy(n_data, is_print):
    """
    Fungsi untuk membuat data dummy tabel reports
    Args:
        n_data(int): Jumlah data yang ingin dibuat
        is_print(bool): Jika TRUE, maka akan menghasilkan data tabular

    Returns:
        tabel(list)
    """
    # Membuat dictionary kosong untuk menampung data tabel
    table = {}

    # Membuat list berisi ID penawaran mulai dari 1 sampai n_data
    table["report_id"] = [i+1 for i in range(n_data)]

    # Membuat list berisi id user secara acak dari variabel users_tabel pada fungsi users_dummy
    table["user_id"] = [random.choice(users_table["user_id"]) for i in range(n_data)]

    # Membuat list berisi id iklan secara acak dari variabel ads_table pada fungsi advertisements_dummy
    table["advertisement_id"] = [random.choice(ads_table["advertisement_id"]) for i in range(n_data)]

    # Membuat list berisi tipe laporan dan menyimpan datanya secara acak
    report_type = ['Spam', 'Fraud', 'Inappropriate Content', 'Other']
    table["report_type"] = [random.choice(report_type) for i in range(n_data)]

    # Membuat list berisi deskripsi laporan dan menyimpan datanya secara acak
    report_description = ['Seller tidak ramah', 'Scam', 'Saya curiga ini penipuan', ' ']
    table["report_description"] = [random.choice(report_description) for i in range(n_data)]

    # Memanggil dan menyimpan nilai fungsi date_generator kedalam list
    date = [date_generator() for i in range(n_data)]
    table["report_date"] = [date[i] for i in range(n_data)]

    # Membuat list berisi tipe tindakan dan menyimpan datanya secara acak
    # berdasarkan parameter bobot untuk tipe tindakannya
    action_type = ['Investigation', 'Warning', 'Hide Ads', 'Remove Ads', 'Account Suspended']
    action_weights = [0.4, 0.3, 0.2, 0.1, 0.05]
    table["action_taken"] = [random.choices(action_type, weights=action_weights, k=1)[0] for i in range(n_data)]

    # Cetak tabel
    if is_print:
        show_data(table)

    return table

reports_table = reports_dummy(n_data=50, is_print=True)
#save_to_csv(data=reports_table, nama_file='reports')

print('Selesai ;)')

