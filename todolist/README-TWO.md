**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
Pada synchronous programming, sebuah request dieksekusi satu per satu. Sebuah perintah harus selesai dieksekusikan terlebih dahulu sebeulum mulai menjalankan perintah berikutnya.
Pada asynchronous programming, perintah dapat dijalankan secara bersamaan dan tidak harus menunggu perintah sebelumnya untuk selesai.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-driven programming merupakan paradigma programming di mana eksekusi serta alur program ditentukan oleh sebuah event, seperti melalui interaksi user dengan program. Trigger dari sebuah event salah satunya dapat terjadi ketika user memencet button atau memasukkan input. Contoh penerapan pada tugas ini adalah ketika memencet tombol button add task, terdapat modal serta program yang akan handle penambahan task baru.

**Jelaskan penerapan asynchronous programming pada AJAX.**
AJAX digunakan untuk load data tanpa harus terjadi reloading pada halaman tersebut. Penerapan asynchronous programming pada AJAX memungkinkan untuk menerima serta mengirim data, seperti menggunakan GET dan POST.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Melakukan routing pada urls.py untuk add dan json
2. Membuat views pada views.py untuk show_json dan add
3. Melakukan get terhadap json menggunakan jquery kemudian melakukan post
4. Membuat html card yang akan ditambahkan ke div cards-section
5. Membuat modal menggunakan bootstrap