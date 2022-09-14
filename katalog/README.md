![3](https://user-images.githubusercontent.com/112463116/190204963-dbab0a73-191b-4553-b3e6-7f1aa7149286.jpg)

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment memungkinkan kita untuk memiliki versi python/django yang berbeda pada perangkat kita tanpa menyebabkan adanya error akibat _clash_ antara 
1 versi dengan versi lainnya. Hal ini juga berarti masing-masing versi memiliki _libraries_ dan _modules_ yang terisolasi satu sama lain. Meskipun begitu, kita tetap
dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment karena pada dasarnya virtual environment ini bukanlah suatu hal yang wajib dilakukan.
Akan tetapi, ada baiknya kita mengimplementasikan penggunaan virtual environment untuk menghindari masalah perbedaan versi atau terjadinya tabrakan antara beberapa
versi sehingga kita tidak bisa membuat _source code_ dengan versi Django yang kita inginkan.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1) Melakukan migrate dengan menggunakan 'python manage.py makemigrations' dan 'python manage.py migrate' sehingga data pada katalog.models dapat terupdate pada database
   Django lokal serta load data yang ada pada file json dengan perintah 'python manage.py loaddata initial_catalog_data.json'
2) Pada katalog.views, melakukan import class yang ada pada file katalog.models
3) Membuat fungsi show_katalog yang menerima request dan mengembalikan render dari request, katalog.html, dan variabel context. Hal ini akan merubah data didalam
   variabel context kedalam bentuk html dan merubah beberapa variabel pada html menjadi {{variabel}} seperti {{nama}}
3) Mengimport class katalog.models dan import path, lalu melakukan routing file katalog.html via katalog.urls dengan menentukan path yang akan digunakan pada 
   saat load halaman web di browser
4) Menetapkan juga path yang ada pada project_django.urls sebagai berikut 'path('katalog/', include('katalog.urls')),'
5) Untuk menampilkan data tabel html katalog, dapat menggunakan loop dan menuliskan data berdasarkan variabel pada katalog.models
6) Setelah itu, kita dapat membuka heroku dan membuat aplikasi baru. Dalam kasus ini, app saya bernama "tugas-2-pbp-rafif"
7) Mengcopy app name dan juga API key kedalam secret pada github secara terpisah
8) Melakukan re-deploy action yang sebelumnya gagal di deploy

Link App Heroku: https://tugas-2-pbp-rafif.herokuapp.com/katalog/
