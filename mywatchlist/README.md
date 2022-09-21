Screenshot Postman HTML
![Screenshot (11)](https://user-images.githubusercontent.com/112463116/191392786-7bd2787c-d940-4ba7-be2d-f46acae309c9.png)
Screenshot Postman JSON
![Screenshot (12)](https://user-images.githubusercontent.com/112463116/191392805-3d754d93-bb56-47d6-b2b0-1bcc1786676b.png)
Screenshot Postman XML
![Screenshot (13)](https://user-images.githubusercontent.com/112463116/191392814-faa20ce6-675e-4f4f-9dad-40a50704f1c6.png)

**1. Jelaskan perbedaan antara JSON, XML, dan HTML!**

   JSON dapat menyimpan suatu objek informasi dengan efisien tetapi agak susah untuk dimengerti manusia, XML menyimpan informasi dengan cara yang kurang efisien
   tapi mudah dibaca manusia dan mesin, HTML juga tidak terlalu efisien dalam menyimpan data tapi tampilan HTML dapat menjadi paling enak dilihat dengan bantuan css.
   Perbedaan lainnya adalah JSON menguraikan data terlebih dahulu lalu mengirimkannya ke internet, sedangkan XML dan HTML dapat langsung mengirimkan datanya ke internet karena lebih
   terstruktur.
   
**2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

   Dalam pengimplementasian sebuah platform, tentunya ada data yang harus diolah atau diproses. Data-data yang sudah diproses akan dikirim kembali kepada user
   untuk digunakan. Oleh karena itu, diperlukan proses data delivery dengan bantuan JSON, HTML, ataupun XML sehingga data dapat dibaca dan dimengerti oleh user (dalam
   hal ini sebagai receiver).
   
**3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

   Langkah pertama yang dilakukan adalah membuat app berbasis django yang bernama mywatchlist. Kemudian membuat class MyWatchList pada mywatchlist.models beserta
   variabel yang diperlukan. Kemudian, buat file JSON yang berisi 10 data film yang akan ditampilkan dan juga HTML untuk mengatur letak data yang ditampilkan. 
   Setelah itu, pada mywatchlist.views akan mengambil data yang sudah disimpan di models (data JSON) dengan cara membuat function yang akan mengembalikan request, 
   context, dan mywatchlist.html. Pada mywatchlist.urls akan dilakukan routing sehingga function seperti show_watchlist, show_xml, show_json, show_json_by_id, 
   show_xml_by_id dapat terbaca oleh django dan dapat membuat url sesuai bentuk data deliverynya. Terakhir, tinggal menambahkan routing mywatchlist pada urls.py 
   di folder project_django.

Link Heroku:
HTML = https://tugas-2-pbp-rafif.herokuapp.com/mywatchlist/html/
XML = https://tugas-2-pbp-rafif.herokuapp.com/mywatchlist/xml/
JSON = https://tugas-2-pbp-rafif.herokuapp.com/mywatchlist/json/
