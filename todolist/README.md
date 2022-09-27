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
