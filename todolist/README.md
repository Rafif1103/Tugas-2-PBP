**Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode     tersebut pada elemen <form>?**

CSRF token berguna untuk menyediakan proteksi bagi user terhadap data pribadi seperti username dan password account. Biasanya ada beberapa website tidak bertanggung jawab yang meminta user untuk mengisi data dari website lain atas nama user tersebut. Django menggunakan proteksi CSRF ini dengan cara membuat suatu token pada server saat website dirender dan melakukan cek pada setiap request yang masuk. Jika request tidak mengandung token yang sesuai dengan yang ada di server, maka request ini akan dibatalkan oleh Django.

**Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.**

Kita dapat membuat elemen <form> secara manual tanpa menggunakan generator, caranya adalah tinggal menambah <input> dengan type="text" untuk mengisi form berupa text, type="password" untuk mengisi form dalam bentuk password (text di hidden), dan masih banyak lagi type lainnya. Berikan nama pada masing-masing input yang sudah dibuat agar nantinya tidak tertukar antara 1 data dengan data lainnya. Lalu, setelah masing-masing input tadi diikuti <input> dengan type="submit" agar data yang sudah diinput dapat tersimpan di database. Untuk mengambil datanya, kita tinggal membuat variabel dan memasukkan data dari database dengan menggunakan request.POST('nama_variabel_di_input_html'). Kemudian, kita dapat mengupdate isi variabel models dengan assign sesuai dengan data tadi. Misal: update = Task(variabel_1 = variabel_simpan_data) lalu diikuti perintah update.save()

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

Saat pengguna menekan tombol submit, sistem akan membuat sebuah HTTP request kepada fungsi di views.py yang dituju. Lalu, request tadi akan dicek validasinya. Jika, form request valid, maka form dapat disimpan beserta dengan datanya ke database (melalui models.py). Setelah itu, fungsi yang menjalankan request tadi akan redirect ke fungsi yang ditujukan untuk menampilkan data yang sudah diinput. Pada fungsi penampilan ini (katakanlah show_todolist), atribut dari models.py akan diimport dan diambil datanya dan dirender oleh Django untuk ditampilkan sebagai halaman html.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

Pertama, kita membuat sebuah registration form sebagai tempat untuk user membuat akun dan masuk ke halaman utamanya nanti menggunakan UserCreationForm() dan input type submit berbentuk button. Kedua, membuat sebuah fungsi untuk login dari data yang sudah disimpan pada pembuatan registration form dan tombol untuk memverifikasi data yang dimasukkan. Jika username dan password sesuai, maka user akan diarahkan ke halaman utama (/todolist/) dengan cara ```return redirect('todolist:show_todolist')```. Akan tetapi, bila user menginput username atau password tidak sesuai dengan yang ada di database, user akan diminta untuk menginput ulang sampai data yang dimasukkan sesuai. Pada halaman utama, kita membuat sebuah fungsi bernama show_todolist yang akan menampilkan data list task yang nanti akan ditambahkan oleh user. Data ini ditampilkan berbentuk tabel yang diambil dari variabel context pada show_todolist. Variabel ini berisikan data pada setiap atribut dari models.py yang dihubungkan dengan user yang sedang login ```data_todolist = Task.objects.filter(user=request.user)``` dan ```context={'data'=data_todolist}```. variabel data pada context ini nantinya akan diloop pada todolist.html dan ditampilkan sesuai dengan banyaknya elemen. Untuk halaman user menambahkan task baru (addTask) dapat dibuat dengan menggunakan custom form melalui forms.py. Kita dapat exclude atribut user karena sesuai dengan user yang login dan atribut date karena sudah terisi secara terotomatis. Jika user klik tombol tambah, maka fungsi addTask pada views.py akan dieksekusi dan form tadi akan di-save sehingga bisa ditampilkan oleh fungsi show_todolist.


***Link Heroku:***
HALAMAN LOGIN: https://tugas-2-pbp-rafif.herokuapp.com/todolist/login/
HALAMAN REGISTER: https://tugas-2-pbp-rafif.herokuapp.com/todolist/register/
HALAMAN UTAMA: https://tugas-2-pbp-rafif.herokuapp.com/todolist/
HALAMAN TAMBAH TODOLIST: https://tugas-2-pbp-rafif.herokuapp.com/todolist/create-task/

**DUMMY ACCOUNT**:
1. username: ayambakar
   password: bukandigoreng123
2. username: ayamgoreng
   password: bukandibakar123

TUGAS 5

**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
1. Internal CSS adalah kode CSS yang ditulis pada halaman html yang ingin dikustomisasi dengan memberikan tag     <style></style>. Internal CSS biasanya dibuat pada bagian header dari kode HTML. Internal CSS ini berguna jika kita ingin mengubah tampilan halaman pada satu file html saja (tidak secara universal), kita juga tidak perlu melakukan upload file karena CSS dan HTML berada pada 1 file, dan Class & ID dapat digunakan oleh internal stylesheet. Internal CSS ini juga memiliki beberapa kekurangan seperti tidak efisien bila kita ingin membuat tampilan beberapa halaman web menjadi serupa dan membuat performa website menjadi menurun karena CSS yang berbeda-beda mengakibatkan adanya loading time setiap kali refresh halaman website

2. External CSS merupakan sebuah kode CSS yang ditulis di luar kode HTML nya pada file yang memiliki extension .css. Hal ini dapat dicapai dengan melakukan ref ke file CSS pada bagian <head> dari HTML. Keuntungan dari External CSS adalah style CSS dapat digunakan untuk banyak halaman website sekaligus sehingga performa website dapat meningkat karena berkurangnya waktu loading screen, serta struktur file HTML menjadi lebih rapih dan mudah dibaca. Kekurangan dari penggunaan CSS dengan metode ini adalah halaman default HTML akan menjadi berantakan bila file CSS gagal dipanggil oleh HTML.

3. Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Inline CSS berguna untuk melakukan pengujian dan melihat perubahan pada elemen yang diberikan inline CSS. Implementasi ini juga membuat proses permintaan HTTP (HTTP request) menjadi lebih keci dan load website menjadi lebih cepat. Kekurangan dari Inline CSS adalah kurang efisien hanya dapat diterapkan pada 1 elemen saja.

**Jelaskan tag HTML5 yang kamu ketahui.**
1. <h1></h1> - <h6></h6> tag heading yang berguna untuk membuat user lebih memperhatikan teks pada tag heading karena ukuran dan font style nya yang cukup berbeda dari text biasa pada tag html lain
2. <li></li> tag untuk membuat suatu list terurut pada HTML
3. <p></p> tag untuk membuat suatu teks paragraf, sehingga browser akan otomatis membuat suatu baris baru sebelum dan sesudah tag <p>
4. <br></br> tag untuk membuat suatu line baru tanpa harus mendefine suatu paragraf
5. <table></table> tag untuk membuat tabel (default tanpa border) pada HTML
6. <a></a> tag untuk melakukan redirect pada link atau function yang tertera di tag anchor

**Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
1. .class , untuk memilih semua elemen pada class yang dimaksud
2. #id, memilih semua elemen HTML dengan id="id"
3. element, memilih semua elemen HTML yang dimaksud (seperti p, h1, button, dll)
4. element1,element2 , memilih semua elemen pada element1 dan element2 secara bersamaan
5. * , memilih semua elemen yang ada pada file html
6. :hover, memilih suatu elemen saat mouse hover di atas elemen tersebut

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Membuat suatu file html baru yang bernama todolist_cards dengan routingnya sendiri yaitu show-cards pada urls.py
2. Membuat suatu function pada views.py yang dapat mengakses todolist_cards.html untuk melihat todolist dalam bentuk cards
3. Membuat suatu class cards menggunakan div class="cards" dan melakukan editing pada cards dengan menggunakan internal css
4. Melakukan modifikasi terhadap data yang ditampilkan agar muat dalam 1 card (1 todolist = 1 card)
5. Membuat fungsi dan routing baru untuk tombol ubah & delete pada todolist sehingga tidak perlu untuk kembali ke halaman utama todolist yang menampilkan tabel
6. Membuat suatu anchor button yang mengarah pada halaman todolist yang menampilkan tabel sehingga pengguna dapat memilih menampilkan todolist dalam tabel atau cards
7. Melakukan adjustment terhadap posisi button sehingga tidak bertabrakan dengan cards
8. Membuat animasi saat mouse di hover di atas cards (menambahkan shadow)
9. Menambahkan media querry sehingga halaman todolist dapat diakses dan dilihat dengan nyaman oleh pengguna pada device lain