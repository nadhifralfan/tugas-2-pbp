# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

## Nama         : Nadhif Rahman Alfan

## NPM          : 2106751783

## Link Heroku  : 
`https://nadhif-tugas-2-pbp.herokuapp.com/mywatchlist/html/`

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
`{% csrf_token %}` memiliki fungsi untuk mencegah serangan CSRF. CSRF atau Cross-Site Request Forgery adalah jenis serangan eksploitasi web yang membuat user tanpa sadar mengirim sebuah request ke website melalui website yang sedang digunakan pada saat itu. Serangan CSRF memungkinkan exploiter melakukan permintaan HTTP sembarang berupa POST atau GET dengan mengatasnamakan user yang saat ini diautentikasi pada situs web.

Token CSRF akan menghasilkan token saat melakukan render pada halaman di website server. Kemudian, server akan melakukan cek pada token tersebut setiap kali halaman mengirim request. Pada Django, token CSRF akan membuat token dalam bentuk input tersembunyi. Apabila `{% csrf_token %}` dihapus pada elemen `form`, aplikasi tidak dapat melakukan verifikasi HTTP request dan akan membuat HTTP request user dibatalkan.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual. 
Ya, kita dapat membuat elemen `<form>` secara manual. Hal tersebut karena pada dasarnya HTML form merupakan kumpulan dari berbagai jenis field `<input>` yang dibungkus dengan `<form>`. Secara umum, untuk membuat suatu HTML form kita perlu menyediakan elemen `<form>` sebagai wrapper. Kemudian, kita perlu mengatur `method` dan `action` attributes dengan value yang diperlukan. `method` attributes digunakan untuk menentukan HTTP method yang akan digunakan untuk mengirim request ke server, sedangkan `action` attributes digunakan untuk menentukan endpoint dari request yang akan dikirim. Pada Django, apabila endpoint memiliki endpoint yang sama dengan URL saat ini, maka hanya dapat menetapkan `method` dan mengabaikan `action` attributes.

Setelah membuat elemen `<form>`, kita dapat memberikan variasi elemen `<input>` sebagai elemen child dari `<form>`. Kita dapat mengubah `type` attribute untuk menentukan jenis input apa yang ingin user masukkan dan kita harus memberikan value pada `name` attribute untuk menentukan key dari data yang akan dikirim. Terakhir, kita dapat menambahkan elemen `<input>` ataupun `<button>` dengan type `submit` untuk memicu HTTP request ke server. Selain itu, kita juga perlu menambahkan `{% csrf_token %}` untuk melindungi request tersebut.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user menekan tombol submit pada elemen `<form>`, hal tersebut akan memicu HTTP request ke server dengan `method` dan `action` yang ditentukan. Kemudian, `action` tersebut akan memetekan request ke URL terkait yang terdapat pada `urls.py` untuk meneruskan permintaan ke handler yang ditentukan pada `views.py`. Jika `action` tersebut sama dengan URL saat ini namun dengan method HTTP yang bebeda, kita dapat mengontrol flow berdasarkan request tersebut.

Pada handler yang terdapat di `views.py`, request data akan divalidasi menggunakan Django form. Apabila data tidak valid, server akan mengirim respon yang berisi error message. Jika tidak, request data akan disimpan dalam database. Setelah itu, server akan merespon dengan HTTP redirect menuju URL yang ditentukan untuk menampilkan data yang disimpan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama, saya membuat aplikasi baru bernama todolist dan kemudian mendaftarkan aplikasi tersebut pada `settings.py` dan `urls.py` pada folder `project_django`. Setelah itu, saya membuat model Task pada `models.py` dan melakukan `migrate` serta `makemigrations`. Kemudian, saya membuat handler atau method yang diperlukan pada `view.py` seperti register, login, logout, dan menampilkan todolist. Berikutnya saya membuat `forms.py` yang berisi class untuk membuat form task baru. Lalu saya membuat template yang diperlukan seperti create-task, login, register, dan todolist. Terakhir saya membuat routing `urls.py` pada folder `todolist`. Dalam memunculkan data pada `todolist.html`, saya mengambil data dengan cara melakukan filter menggunakan user yang sedang terlogin sehingga data yang muncul hanya data user tersebut. Saya mengimplementasikan update task dengan menambahkan atribut pada model Task dan membuat method baru pada `view.py`. Terakhir, saya juga mengimplementasikan delete task dengan membuat method baru pada `view.py` dan menghapus data task dengan cara melakukan filter menggunakan id data task yang ingin dihapus.