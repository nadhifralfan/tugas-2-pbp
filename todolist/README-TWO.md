# Tugas 6: Javascript dan AJAX
## Nama         : Nadhif Rahman Alfan

## NPM          : 2106751783

## Link Heroku  : 
`https://nadhif-tugas-2-pbp.herokuapp.com/todolist/ajax/`

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

Secara umum, asynchronous programming merupakan suatu pemrograman yang memungkinkan untuk menjalankan beberapa proses sekaligus, sementara synchronous program merupakan suatu pemrograman yang berjalan secara berurut dan bertahap. Contohnya apabila terdapat 2 thread yakni thread A dan thread B. Pada asynchronous programming kedua thread dapat berjalan pada waktu yang bersamaan dan selesai kapan saja tanpa menunggu thread yang lainnya selesai tereksekusi. Sementara pada synchronous programming, apabila salah satu thread sedang berjalan, maka thread yang lain harus menunggu thread tersebut selesai untuk bisa berjalan.

Asynchronous programming memiliki beberapa keunggulan dengan tidak diperlukannya menunggu. Salah satu contohnya yaitu user interface yang lebih responsive dengan adanya program lain yang sudah dipersiapkan terlebih dahulu. Synchronous programming juga memiliki keunggulan sendiri yakni lebih metodikal dan presisi.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming adalah sebuah paradigma dimana control flow ditentukan oleh terjadinya event. Salah satu contohnya adalah kejadian DOM dalam manipulasi DOM Javascript. DOM events memungkinkan JavaScript untuk menyetel pengendali untuk event tertentu yang dipicu oleh interaksi DOM seperti click, submit, dll. Kita dapat menyetel pengendali sebaris dalam tag HTML atau menggunakan `addEventListener`.

## Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronous programming pada AJAX membuat penundaan pengambilan data dapat dihindari. Hal tersebut membuat pengguna dapat terus berinteraksi dengan halaman saat AJAX memproses permintaan di latar belakang. Kemudian, ketika server mengirimkan respons kembali, AJAX akan memperbarui data di halaman dengan mulus.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama-tama saya membuat views.py menggunakan AJAX dengan membuat show_json,dan show_todolist_ajax. Berikutnya saya membuat path routing baru menuju `/todolist/json` pada urls.py. Setelah itu, saya membuat todolist_ajax.html yang merupakan modifikasi dari todolist.html yang menggunakan AJAX. Dalam menggunakan AJAX GET, saya membuat function getData pada json dan kemudian membuat cards sesuai elemen dan letaknya.

Untuk mengimplementasikan AJAX POST, pertama-tama saya menggunakan show_json pada vies.py dan routing pada urls.py yang sudah ada. Setelah itu saya membuat modal menggunakan bootstrap. Kemudian saya membuat function event handler ketika tombol create di klik. Pada function event handler tersebut, saya memanggil add_todolist pada views.py dan membuat task baru. Program tersebut akan berjalan secara asynchronous dengan menampilkan kembali function getData yang menggunakan AJAX GET.