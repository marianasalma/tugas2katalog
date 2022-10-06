**Link menuju aplikasi Heroku:** https://katalogsalma.herokuapp.com/todolist/


**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**
CSRF token pada Django merupakan pelindung untuk mencegah CSRF atau Cross Site Request Forgery. 
Django akan mengeluarkan sebuah token pada server ketika me-render halaman. Request tidak dapat dieksekusi tanpa token.


**Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**
Ya. Forms dapat dibuat secara manual tanpa generator melalui elemen input dengan name yang bersesuaian untuk dilakukannya get.
 
**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
Pada form, user akan mengisi data pada input field. Saat submit, forms akan mengirimkan data yang diakses dengan GET. Program akan memuat object Task baru dengan data yang diinput bersesuaian dengan data models Task. Request akan di-render, dengan data yang ingin ditampilkan disimpan pada context dan di


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Melakukan django startapp untuk aplikasi todolist
2. Melakukan konfigurasi url pada urls.py pada folder project_django untuk path '/todolist' serta urlpatterns di urls.py aplikasi todolist
3. Membuat model data pada models.py dengan field user, date, title, description, dan is_finished
4. Membuat fungsi show_todolist, register, create, logout, dan login pada views 
5. Membuat template html untuk menampilkan data
6. Add, commit, push ke github

**README Tugas 5**

**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?** 
- External CSS disimpan pada satu file yang memiliki ekstensi .css. Style sheet tersebut menyimpan informasi styling yang dapat digunakan untuk seluruh website, sehingga memiliki kelebihan tidak harus mengubah masing-masing elemen HTML. Kelemahannya, proses upload eksternal css, terutama yang membutuhkan beberapa style sheet .css, bisa membuat waktu loading website lebih lama karena download untuk import file yang memiliki informasi styling.
- Internal CSS disimpan pada file HTML tersebut, yakni pada tag `<style>` di dalam tag `<html>` pada bagian awal file. Kelebihannya, tidak perlu melakukan membuat dan import lagi terhadap file eksternal .css dan mudah melakukan preview jika mengubah styling. Kelemahan dari internal css adalah perubahan yang dilakukan terkait informasi styling hanya diberlakukan pada file tersebut saja, sehingga repetitif.
- Inline CSS disimpan pada tag elemen HTML menggunakan atribut `style="..."`. Kelebihannya, informasi styling yang ada pada inline CSS hanya berlaku pada elemen yang memiliki atribut dengan informasi styling yang bersesuaian  sehingga cocok digunakan untuk styling elemen secara spesifik. Kelemahannya, membutuhkan waktu yang lama untuk implementasi seluruh styling serta membuat struktur HTML berantakan.

**Jelaskan tag HTML5 yang kamu ketahui.**
- `<body>` yang mendefinisikan konten body dari file HTML
- `<a>` yang merupakan hyperlink untuk redirect ke halaman atau section
- `<img>` untuk memuat gambar yang ingin ditampilkan
- `<li>` untuk elemen list dan berada di dalam tag `<ul>` untuk list tidak bernomor dan `<ol>` untuk list bernomor
- `<div>` yang mendefinisikan sebuah section atau block pada halaman

**Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
CSS selector digunakan untuk mendefinisikan sebuah elemen atau section yang akan diimplementasikan sebuah style CSS.
- HTML element selector: h1, h2, h3,..., p, button, div. Contoh implementasinya pada style CSS yakni dimulai dengan `h1 { ... }`
- id: menggunakan atribut pada sebuah elemen dengan `id="id-name"`. Contoh implementasinya pada style CSS yakni dimulai dengan `#id-name { ... }`
- class: menggunakan atribut pada sebuah elemen dengan `class="class-name"`. Contoh implementasinya pada style CSS yakni dimulai dengan `.class-name { ... }`
- attribute: melakukan styling untuk elemen dengan atribut tertentu. Contoh implementasinya pada style CSS yakni dimulai dengan `[href] { ... }` jika atributnya merupakan href.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Mengkonfigurasikan bootstrap sesuai dokumentasi
2. Menambahkan viewport meta tag untuk meninformasikan browser untuk adjust sesuai viewport device.
3. Melakukan styling dengan CSS dengan mengubah warna elemen-elemen, font, background, serta layout
4. Menambahkan cards pada page todolist, melakukan styling pada page tersebut, dan menyambungkannya ke forms
5. Melakukan adjustment terhadap alignment, padding, dan margin agar lebih rapih
