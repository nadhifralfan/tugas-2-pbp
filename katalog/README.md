# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

## Nama: Nadhif Rahman Alfan

## NPM : 2106751783

1. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**

![bagan]("https://raw.githubusercontent.com/nadhifralfan/tugas-2-pbp/main/bagain-tugas-2.png")

Pertama, user akan mengirimkan GET HTTP request menuju server. Kemudian akan menggunakan 'urls.py' untuk memetakan permintaan ke controller (views) sesuai dengan URL yang ditentukan. Controller yang sudah ditentukan oleh 'views.py' akan merender file HTML di server bersama dengan data yang dibutuhkan. Data yang dirender menjadi HTML diambil dari database melalui 'models.py'. Terakhir, server akan mengirimkan respon berupa HTML yang akan ditampilkan menjadi tampilan website.

2. **Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment membantu mencegah pengembang melakukan instalasi dependensi yang tidak perlu di server. Selain itu, virtual environment juga dapat menyelesaikan masalah apabila terdapat dua proyek berbeda yang memerlukan dependensi yang sama namun dengan versi berbeda. Dalam membuat aplikasi web berbasis Django sebenarnya tidak harus menggunakan virtual environment. Pengembang masih dapat mengembangkan aplikasi Django tanpa menggunakan virtual environment hanya saja dependensi yang diinstalasi akan tercampur dengan proyek-proyek lainnya.

3. **Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

Hal pertama yang saya lakukan adalah melakukan clone template dari GitHub repositori PBP ke repositori saya dan melakukan git clone di local file. Setelah itu, saya membuat virtual environment, menginstalasi dependensi, dan melakukan load data fixtures. Berikutnya, saya melanjutkan mengerjakan 'view.py' dengan membuat function yang akan mengkueri model yang sudah dibuat atau didefinisikan pada 'models.py' menggunakan metode 'all()'. Kemudian, saya membuat dictionary yang berisi nama dan NPM saya, serta data yang diterima dari model. Lalu saya memetakan dictionary yang sudah dibuat dengan benar ke setiap tempat pada file HTML ('katalog.html'). Selanjutnya saya membuat view yang mengembalikan file HTML yang dirender menggunakan kamus. Setelah itu, saya melakukan routing pada 'katalog.urls' dan mendaftarkannya di 'project_django.urls'. Apabila sudah, saya dapat melakukan git add, commit, dan push lalu melanjutkan untuk tahapan deployment menuju aplikasi Heroku. Saya melanjutkan dengan membuat aplikasi baru pada Heroku, kemudian saya mengambil nama aplikasi dan API key yang akan saya daftarkan sebagai secrets pada repositori GitHub saya. Terakhir saya melakukan deploy ulang proyek di GitHub dan membiarkan GitHub Actions yang menjalankannya seperti build dan deploy pada Heroku.