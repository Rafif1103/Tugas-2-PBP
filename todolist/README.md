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


TUGAS 6

**Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming*.**
1. *Asynchronous programming* merupakan suatu model pemrograman yang bersifat *multi thread* sehingga program dapat berjalan secara paralel, sedangkan *synchronous programming* bersifat *single thread* sehingga hanya satu program yang dapat berjalan pada satu waktu.
2. *Asynchronous programming* dapat mengirimkan banyak *request* ke server, sedangkan *synchronous programming* hanya dapat mengirimkan *request* satu per satu dan akan menunggu sampai *request* yang dikirim untuk dieksekusi oleh server untuk dapat mengirimkan request kembali.
3. *Asynchrounous programming* dapat meningkatkan jumlah *output* yang dihasilkan karena banyak proses dapat berjalan secara bersamaan, sedangkan *synchronous programming* akan cenderung lebih lama.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *Event-Driven Programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
*Event-Driven Programming* merupakan suatu paradigma dimana alur eksekusi program dikontrol oleh suatu kejadian (*event occurence*). Kemunculan *event* akan dipantau oleh bagian kode yang dikenal sebagai *event listener*. Jika *event listener* mendeteksi suatu kejadian yang muncul, maka dia akan melakukan pemanggilan terhadap *handler* untuk mengeksekusi program sesuai *event* yang terjadi (*handler* biasanya merupakan sebuah *callback function* atau *method*). Dalam tugas kali ini, terdapat *Event-Driven Programming* yaitu saat *user* menekan tombol *add* pada modal "add task". Saat tombol ini ditekan, AJAX akan melakukan pemanggilan *method* "async function addTask()" agar data yang sudah di-*input* oleh *user* dapat disimpan kedalam *database*.

**Jelaskan penerapan asynchronous programming pada AJAX.**
AJAX membuat *user* tidak harus melakukan *refresh* webpage pada browser untuk meng-*update* data pada *webpage* tersebut. Hal ini disebabkan karena AJAX melakukan pertukaran data antara *web browser* dan *web server* serta melakukan *render* untuk menampilkan data yang sudah didapatkan dari server. Proses *update* data ini dapat dilakukan berdasarkan *user-action* seperti menekan tombol ataupun gerakan *mouse*. Hal yang membedakan AJAX dengan HTTP *request* adalah saat HTTP *request*, *user* harus menunggu agar seluruh *webpage* selesai *loading*. Akan tetapi, AJAX dapat mengakses data dari sumber eksternal meskipun *webpage* sudah selesai *loading*.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Membuat fungsi pada views.py yang mengembalikan sebuah JSON response `return HttpResponse(serializers.serialize("json", data_todolist))`
2. Membuat sebuah file html baru yang akan menampilkan *webpage* secara *asynchronous*. Isi dari html ini kurang lebih sama seperti html yang membuat tampilan todolist menjadi *cards*.
3. Membuat suatu fungsi di views.py untuk mengembalikan data dari model berdasarkan *user* yang login 
```py
def views_ajax(request):
      return render(request, "todolist_ajax.html")
```
4. Melakukan import function views_ajax dan routing di urls.py sehingga *webpage* AJAX dapat diakses melalui link /todolist/json
```py
 path('json/', views_ajax, name='views_ajax'),
```
6. Membuat suatu tag <div> sebagai tempat untuk menampung data yang diambil dari database dengan menggunakan AJAX
```html
<div id="ajax-cards"></div>
```
5. Membuat sebuah tag script pada html AJAX yang berisi sebuah async function untuk fetch() data dari fungsi views_ajax dan melakukan *append* ke tag <div id="ajax-cards"></div> beserta dengan mekanisme untuk refresh page secara *asynchronous*
```js
 async function getTodolist(){
    return fetch("{% url 'todolist:show_json' %}").then((res) => res.json())
  }

  async function refreshTodolist(){
    document.getElementById("ajax-cards").innerHTML = ""
    const todolist = await getTodolist()
    let htmlString = ``
    todolist.forEach(item=> {
      htmlString+=`\n
      <div class="card">
        <div class="container">
          <h4><b>Tanggal Pembuatan Tugas</b></h4>
          <p>${item.fields.date}</p>
          <h4>Judul Tugas</h4>
          <p>${item.fields.title}</p>
          <h4>Deskripsi Tugas</h4>
          <p>${item.fields.description}</p>
          <h4>Status</h4>
          ${item.fields.is_finished ? "<p>Selesai</p>" : "<p>Belum Selesai</p>"}
              <form method="POST" action="{% url 'todolist:change_status_cards' %}">  
          {% csrf_token %}
              <input type="hidden" value=${item.pk} name="task_id">
              <p><input id = "tombol_ubah" type="submit" value="Ubah" /></p>
          </form>
          <form method="POST" action="{% url 'todolist:delete_status_cards' %}">
              {% csrf_token %}  
              <input type="hidden" value=${item.pk} name="task_id">
              <input id = "tombol-delete" type="submit" value="Delete"></button>
            </form>
        </div>
      </div>
      `
    });
    document.getElementById("ajax-cards").innerHTML = htmlString
  }
  refreshTodolist()
```
6. Membuat sebuah modal dengan framework Bootstrap yang berisi sebuah form sebagai sarana *user* untuk menambahkan todolist pada akun tersebut.
```html
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Add task</button>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">New Task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="formtask">
          {% csrf_token %}
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Title:</label>
            <input type="text" class="form-control" id="field_title" name="judul">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Description:</label>
            <textarea class="form-control" id="field_desc" name="deskripsi"></textarea>
          </div>
        </form>
      </div>
        <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" id="addtaskbutton" data-bs-dismiss="modal">Add</button>
      </div>
    </div>
  </div>
</div>
```
7. Membuat sebuah async function sebagai *handler* saat tombol add pada modal ditekan
```js
  async function addTask() {
    fetch("{% url 'todolist:addTask_ajax' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#formtask'))
      }).then(refreshTodolist)
    return false
  }
  
  document.getElementById("addtaskbutton").onclick = addTask
```
8. Membuat sebuah fungsi di views.py dengan nama addTask_ajax agar data yang di-*input* *user* dapat disimpan pada database
```py
def addTask_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")

        new_todolist = Task(title=title, description=deskripsi, user=request.user)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
9. Melakukan routing terhadap fungsi addTask_ajax
```py
path('add/', addTask_ajax, name='addTask_ajax'),
```