# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

## Nama         : Nadhif Rahman Alfan

## NPM          : 2106751783

## Link Heroku  : `https://nadhif-tugas-2-pbp.herokuapp.com/mywatchlist/html/` , `https://nadhif-tugas-2-pbp.herokuapp.com/mywatchlist/json/`, `https://nadhif-tugas-2-pbp.herokuapp.com/mywatchlist/xml/`

## Jelaskan perbedaan antara JSON, XML, dan HTML!
**JSON**
JSON atau singkatan dari JavaScript Object Notation merupakan sebuah format format yang digunakan untuk menyimpan dan mentransfer data.
**XML**
XML atau singkatan dari eXtensible Markup Language adalah bahasa markup yang diciptakan oleh konsorsium World Wide Web (W3C) yang berfungsi untuk menyederhanakan proses penyimpanan dan pengiriman data antarserver.
**HTML**
HTML atau singkatan dari Hypertext Markup Language adalah bahasa markup yang digunakan untuk membuat halaman website dan isinya terdiri dari berbagai kode yang dapat menyusun struktur suatu website.
**Perbedaan**
| | JSON | XML | HTML |
|---|---|---|---|
|Memerlukan End Tag| Tidak | Ya | Ya (dengan Pengecualian Empty Element) |
|Menampilkan Data(Secara Estetika)| Kurang Bagus | Kurang Bagus | Bagus |
|Membawa Data| Baik | Baik | Kurang Baik |
|Mendukung Penggunaan Comment| Tidak | Ya | Ya |
|Encoding| UTF-8 | Apa Saja | UTF-8, UTF-16, UTS-32 |
|Mendukung Penggunaan Array | Ya | Tidak | Tidak |

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Pada era digital saat ini, jumlah penggunaan data telah meningkat berkali-kali lipat. Hal tersebut juga membuat kesulitan dalam penanganan dan pengelolaan data juga naik. Situasi tersebut membutuhkan solusi berupa pengelolaan dan pengiriman data yang lebih sederhana dan mudah dengan menggunakan standarisasi format data delivery. Data delivery dapat membuat pengelolaan dan penanganan data menjadi lebih kompatibel, fleksibel, dan efisien. Selain itu, data delivery membuat pengiriman data tidak memerlukan daya komputasi yang tinggi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi mywatchlist menggunakan command `python manage.py startapp mywatchlist`.
2. Mendaftarkan aplikasi mywatchlist kedalam `INSTALLED_APPS` pada `settings.py` di folder project_django.
3. Membuat model MyWatchList pada `models.py` pada folder mywatchlist dengan atribut berdasarkan deskripsi soal dan menggunakan field yang sesuai dengan data type yang dibutuhkan.
4. Menambahkan path `path('mywatchlist/', include('mywatchlist.urls'))` ke dalam `urlpatterns` pada `urls.py` di folder project_django.
5. Membuat folder fixtures kemudian membuat initial data pada file `initial_mywatchlist_data.json` di dalam folder fixtures.
6. Melakukan load data pada `initial_mywatchlist_data.json` dengan menggunakan command `python manage.py loaddata initial_mywishlist_data.json`.
7. Membuat folder templates kemudian membuat `mywatchlist.html` di dalamnya untuk menampilkan mywatchlist dalam format HTML.
8. Membuat function pada `views.py` di folder mywatchlist untuk menyajikan data. Function yang dibuat yakni:
- show_mywatchlist_html &rarr; Menampilkan data dalam format HTML
- show_mywatchlist_json &rarr; Menampilkan data dalam format JSON
- show_mywatchlist_xml &rarr; Menampilkan data dalam format XML
- show_mywatchlist_json_by_id &rarr; Menampilkan data dalam format JSON dengan filter id
- show_mywatchlist_xml_by_id &rarr; Menampilkan data dalam format XML dengan filter id
9. Melakukan routing setiap function pada `view.py` supaya memiliki path masing-masing dan dapat diakses di web. Menambahkan semua path ke dalam `urlpatterns` pada `urls.py` di folder mywatchlist. Path yang ditambahkan yakni:
```
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_mywatchlist_xml, name='show_xml'),
    path('json/', show_mywatchlist_json, name='show_json'),
    path('json/<int:id>', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),
    path('xml/<int:id>', show_mywatchlist_xml_by_id, name='show_mywatchlist_xml_by_id'),
```
10. Menambahkan command `python manage.py loaddata initial_mywishlist_data.json` pada `Procfile`.
11. Melakukan git `add`, `commit`, dan `push` yang nantinya akan otomatis github Actions yang melakukan deploy menuju Heroku.

## Mengakses URL dengan Postman
