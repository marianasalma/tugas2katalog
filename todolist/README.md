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


