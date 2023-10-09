# 🖼️ Shopping Art 🛒 🎨


`Dalam era digital ini 🏙️, seni sering diabaikan dan kurang dihargai 😢. Website shopping art muncul sebagai solusi, memberikan seniman platform untuk memamerkan dan menjual karya mereka kepada audiens yang lebih luas 🖼️, mengubah cara kita melihat dan menghargai seni dalam konteks digital 👨🏻‍🎨`


#  Tugas 2
<details>

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 

- [x] Membuat sebuah proyek Django baru.

    Pada membuat project Django baru kita pertama tama perlu membuat file bernama `shopping art` dan repository baru pada github baru untuk diisi. Setelah membuat file baru, dan github maka membuat perintah pada terminal mendambahkan readme dengan `echo "#readme" >> README.md` + `git init`+ `git add README.md` yang berguna untuk mendambahkan readme. Selanjutnya melakukan `git commit -m "first commit"`  untuk commit, selanjutnya mengetik `git branch -M main` untuk membuat branch utama pada repo, Menyambungkan dan membuat remote `git remote add origin <URL_REPO> `, dan tahapan terakhir mempush ke repo dengan `git push -u origin main`.

    Selanjutnya membuat virtual environtment dengan mengetik perintah `python -m venv env` dan mengkaktifkannya. Untuk mengaktifkannya pada macbook menggunakan `source env/bin/activate`. ketika virtual envieonrment telah aktif dengan ditandai dengan (env) pada terminal, diharuskan menambahkan `requirments.txt` sebagai dependensi yang akan digunakan dan menjalankan perintah `pip install -r requirements.txt` untuk menginstallnya. Setelah itu membuat projek djanggo dengan menjalankan `django-admin startproject shopping_list .`. 

    Setelah berhasil mengsintall djanggo, kita harus mengkonfigurasikan proyek dan menjalankan server. Untuk mengkonfigurasikan proyek dengan menambahkan `*` pada `ALLOWED_HOSTS` sehingga menjadi `ALLOWED_HOSTS = ["*"]`. Tanda `*` berguna untuk mengizinkan akses dari semua host, yang akan memungkinkan aplikasi diakses secara luas. Setelah mengkonfigurasikan proyek selanjutnya saya menginisiasi `.gitignore` yang berguna untuk mengabaikan beberapa berkas-berkas atau direktori-direktori pada Git.
    

- [x] Membuat aplikasi dengan nama main pada proyek tersebut.
    Pada langkah ini, saya menambahkan folfer `templates` dan menambahkan file `main` sebagai html utama. Untuk membuatnya sebagai bagian int, harus menjalankan perintah `python3 manage.py startapp main`. setelah itu, mendaftarkan folder ke dalam proyek dengan menambahkan main pada `INSTALLED_APPS` yang berada pada folder `settings.py`.


- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Pada tahap ini, melakukan routing agar aplikasi `main` dapat diakses melalui projek hingga aplikasi dan juga perambaan web. aplikasi main akan menambahkan path ke variabel `urlpatterns` pada `urls.py`.  Setlah itu, pada variabel `urlpatterns` terdapat path URL `main/` yang mendefinisikan rute ke file `urls.py` pada aplikasi `main`.


- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
  +  `name` sebagai nama item dengan tipe `CharField`.
  + `amount` sebagai jumlah item dengan tipe `IntegerField`.
  + `description` sebagai deskripsi item dengan tipe `TextField`.
    Pada folder `main` terdapat file `models.py`, dan kita disuruh untuk membuat model yang berisikan atribut diatas. Data data yang kita buat nantinya bisa diakses, di perbarui, dan dihapus dengan perintah SQL. setelah mendefine model atribut, saya melakukan penjalankan perintah `python3 manage.py makemigrations` yang berfungsi melakukan migrasi model ke dalam database. Setelah itu melakukan perintah `python3 manage.py migrate` untuk mengaplikasikan file migrasi ke dalam database.


- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Pada tahap ini, saya mengimport funsi render dari django.shortcut untuk keperluan nantinya di HTML.  Dari sebelumnya itu data sama dengan langsung dimasukan ke dalam html, namun pada tahap ini membuat tempat untuk mengemnbalikan nilai pada html.  Cara mengembalikannya adalah dengan  menambahkan data `app_name`, `name`, dan `class` ke dalam `context` yang terdapat di dalam fungsi `show_app_name`. setelah itu pada tampilan html dari yang tadinya `Name : Arya Wijaya Kusuma` menjadi `Name : {name}` agar dapat meminta dara daro `views.py`.


- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Pada tahap ini, diharuskan untuk menimpor `path` dari `django.urls`. Selain itu kita juga mengimport fungsi `show_app_name` dari file `views.py`. Hal ini dilakukan dengan jara membuat file `urls.py` pada folder `main` dengan isi 
    ```
    from django.urls import path, include
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main')
    ]
    ```


- [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Setelah menyelesaikan semua proses diatas, saya akan mengupdate isi dari repositori github saya dengan mempush file saat ini yang ada di komputer saya ke repo. Untuk mempush dapat dilakukan dengan pertama tama menjalankan `git add .` untuk menambahkan semua yang ada di stage. Setelah menambahkan semuanya saya melakukan commit dengan `git commit -m "<komentar>"` dan terakhir mempush ke git push -u origin main`.



### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan Tugas 2 ](https://github.com/aryawijayak/shopping-art/assets/119391657/081fc00c-04ba-4c88-8e09-029213b76be2)




### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah alat yang sangat penting dalam pengembangan perangkat lunak, termasuk dalam pengembangan aplikasi web berbasis Django. Fungsi utamanya adalah memisahkan dan mengisolasi lingkungan kerja proyek Anda dari lingkungan sistem operasi yang lebih luas. Ini memungkinkan Anda untuk menginstal paket dan dependensi proyek secara lokal tanpa mengganggu atau berinterferensi dengan paket global sistem operasi atau proyek lain yang mungkin Anda kerjakan. Selain itu, virtual environment memungkinkan Anda untuk mengelola versi paket yang digunakan dalam proyek tertentu, sehingga Anda dapat memastikan konsistensi dan stabilitas aplikasi Anda. Hal ini juga memudahkan untuk berbagi proyek dengan tim pengembang atau menggantinya ke lingkungan produksi tanpa masalah kompatibilitas.

> Virtual environment dibuat dengan perintah `python -m venv env`, dan diaktifkan dengan perintah `source env/bin/activate`.

Meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, sangat disarankan untuk selalu menggunakannya. Tanpa virtual environment, Anda mungkin akan menghadapi berbagai masalah, seperti konflik dependensi antara proyek, kesulitan dalam mengelola versi paket, dan risiko merusak paket sistem operasi. Dengan menggunakan virtual environment, Anda dapat menjaga lingkungan proyek Anda bersih, teratur, dan terisolasi, yang pada akhirnya akan membuat pengembangan dan pemeliharaan aplikasi Anda menjadi lebih mudah dan lebih dapat diandalkan. Implementasi virtual environment adalah sebuah praktik terbaik yang akan membantu Anda mengelola konsistensi dari dependencies masing-masing proyek secara efisien, menjauhkan risiko konflik dependencies, dan memastikan kestabilan serta portabilitas aplikasi Anda.


### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
| MVC         | MVT         | MVVM          |
| ---        |    ----   |          --- |
| Model-View-Controller      | Model-View-Template     | Model-View-View-Model   
| View: Menggambarkan data dari model dalam antarmuka pengguna (UI) dan menampilkan informasi kepada pengguna.| View: Bertanggung jawab untuk menampilkan data kepada pengguna dan menggambarkan tampilan.| View: Menginformasi ke ViewModel terkait interaksi pengguna, dan hanya menampilkan data yang disediakan oleh ViewModel |
| Controller: Menjembatani hubungan antara View dan Model dan sebagai inti logika dan alur aplikasi dengan menginformasi interaksi user ke Model | Template: Mengambil data dari model dan menampilkannya, berupa HTML  | ViewModel: Perantara antara Model dan View, mengubah data dari Model menjadi format sesuai dengan tampilan |
|![mvc](https://user-images.githubusercontent.com/119391657/268604124-47902dbc-cc01-46af-b077-9ba64c31e042.png) |![mvp](https://user-images.githubusercontent.com/119391657/268604321-e031b08c-f41e-4e57-81e7-184fd9a8959b.png) |![mvvm](https://user-images.githubusercontent.com/119391657/268604466-b3808d32-e983-4b1e-a385-1c6ea8e8c89b.png) |
| MVC merupakan konsep yang sering diterapkan dalam pengembangan perangkat lunak, terutama pada aplikasi desktop dan web konvensional. Prinsip ini memisahkan tiga komponen utama dari aplikasi dengan tujuan untuk meningkatkan kemudahan dalam merawat dan mengembangkan kode.| MVT merupakan pola desain yang khusus digunakan dalam kerangka kerja Django, yang diciptakan khusus untuk pengembangan aplikasi web menggunakan bahasa pemrograman Python. Pola ini menggantikan komponen View dalam MVC dengan yang disebut sebagai Template, yang bertujuan untuk memisahkan dengan lebih tegas antara aspek tampilan dan pemrosesan HTTP. | MVVM merupakan pola desain yang umum diterapkan dalam pengembangan aplikasi yang menekankan antarmuka pengguna (UI), terutama pada platform seperti WPF (Windows Presentation Foundation). Pola ini difokuskan pada konsep pemisahan antara komponen tampilan dan logika bisnis, dengan memanfaatkan ViewModel sebagai perantara di antara keduanya.|
</details>

<br>

# Tugas 3

<details>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?
| Form POST         | Form GET         |
| ---        |    ----   |
| Method POST akan mengirimkan data atau nilai langsung ke action untuk ditampung, tanpa menampilkan pada URL. | Method GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action.
|![POST](https://user-images.githubusercontent.com/119391657/268960230-4ca02611-ab78-4685-913b-79ca724cdd0e.png) | ![GET](https://user-images.githubusercontent.com/119391657/268960029-d7e2cba8-1164-40a6-96bc-97ac26ad07f4.png)| 
|Method POST menggunakan variable $_POST untuk menampung data/nilai. | Sedangkan method GET menggunakan variable $_GET untuk menampung data/nilai.
|Method POST data yang dikirim tidak terbatas| Method GET tidak boleh lebih dari 2047 karakter.

###  2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
| XML         | JSON         | HTML          |
| ---        |    ----   |          --- |
|**Struktur Data**: Bahasa markup yang memiliki fleksibilitas tinggi dan dapat digunakan untuk menggambarkan berbagai jenis informasi. Ini memiliki kerangka yang kuat dan menetapkan pedoman untuk mengatur informasi.| **Struktur Data**: Format data yang sederhana yang berisi objek dan larik. Sangat berguna untuk menggambarkan data yang teratur | **Struktur Data**: Sebuah bahasa markup yang digunakan untuk menghasilkan dokumen di lingkungan web.|
|**Penggunaan**: Transfer data antara aplikasi, mengatur konfigurasi, dan menyimpan data yang memiliki struktur data yang tidak sepenuhnya terstruktur. | **Penggunaan**: Proses pertukaran data antara aplikasi, terutama dalam konteks pengembangan web. Format JSON banyak digunakan dalam aplikasi dan layanan web modern sebagai format standar untuk menerima dan mengirim data. |**Penggunaan**: Membuat halaman web yang dirancang khusus untuk tujuan penyajian dan interaksi dengan pengguna. |

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering menjadi pilihan utama para pengembang dalam pertukaran data antar aplikasi karena beberapa alasan yang signifikan:
1. **Format yang Mudah di-parse**: JSON memiliki format yang sangat mudah untuk di-parse, memudahkan pengolahan dan penguraian data. Ini sangat penting dalam pertukaran data antar aplikasi di lingkungan yang serba cepat.

2. **Ringan dan Berbasis Teks**: Sebagai format berbasis teks, JSON memiliki ukuran yang ringan. Hal ini sangat menguntungkan ketika data perlu dikirimkan melalui jaringan, karena tidak membebani bandwidth.

3. **Dukungan Native Banyak Bahasa**: Banyak bahasa pemrograman memiliki dukungan native untuk parsing JSON. Ini memungkinkan pengembang untuk dengan mudah mengintegrasikan JSON dalam aplikasi mereka tanpa perlu mengandalkan pustaka pihak ketiga atau implementasi khusus.

4. **Efisien dibandingkan XML**: JSON lebih efisien dalam hal penggunaan karakter dibandingkan dengan format lain seperti XML yang menggunakan sistem tag. JSON menggunakan format key-value pair yang lebih sederhana.

5. **Mudah Dibaca Manusia**: JSON lebih mudah dibaca oleh manusia, sehingga mempermudah dalam debugging dan analisis data. Karakter yang lebih sedikit membuatnya lebih bersahabat bagi pengembang.

Dengan kelebihan-kelebihan ini, tidak mengherankan jika JSON menjadi format yang lebih sering digunakan dalam pertukaran data antar aplikasi. Kelebihan ini juga membantu dalam mempercepat proses pemrosesan data, yang sangat penting dalam aplikasi modern yang serba cepat.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
    Pertama Buatlah file `template/base.html` pada direktori root yang berguna untuk memberikan inisiasi html default tanpa perlu membuat inisiasi html ddi setiap page .html yang kita buat. Isi dari base.html adalah sebagai berikut:
    ``````
        {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
   ``````
    Setelah membuat `base.html` saya mengedit file `setting.py` lalu libatkan `base.html` dengan menambahkan baris template agar `base.html` bisa sdideteksi sebagai berkas html. Lebih jelaskan dapat melihat kode berikut:
    ```
    ...
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

    setelah melibtatkan `base.html`, saya membuat struktur form agar dapat menerima data beruma art baru yang diinput dengan membuat file `forms.py`. File tersebut berisi kode dibawah ini : 
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description"]
    ```
    Fungsi `fields` diatas merupakan tipe apa saja yang akan menjadi header dari tabel kita nantinya yang berisi name, price dan description. 

    Setelah membuat `forms.py`, saya mengubah function `show_main` pada `views.py`  memasukan context baru yang dapat dilihat lebih jelas pada kode berikut ini:
    ```
    context = {
        'products': products,

        'karya1': 'Online Course App', 
        'artist1': 'Arya Wijaya Kusuma', 

        'karya2': 'Private Tutor App', 
        'artist2': 'Arya keren',

        'karya3': 'Task Management App', 
        'artist3': 'Aweka Design'
    }
    ```
    Sebelumnya pada Tutorial Berisi dengan Nama dan kelas, namun saya memodifikasinya dengan mengganti menjadi karya dan artist, dan context ini akan dipanggil nanti pada html pada section `card` yang mendisplay product dari shopping art.

    Selanjutnya saya membuat `create_product.html` pada files `main/templates` sebagai html untuk menambahkan produk yang berisi kode seperti dibawah ini:

    ```
        {% extends 'base.html' %} 

    {% block content %}


    <style>

        body {
            background-color: #f4f7ff;
        }

        h1, h2, h3, h4, h5, p, th, td, a, button {
            font-family: 'Poppins', sans-serif;
        }
        
        .navbar {
            position: sticky;
            top: 0;
            background-color: #ffffff;
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100; 
            margin-bottom: 20px;
        }

        .navbar img {
            max-height: 28px;
            
        }

        .content-container {
            display: flex;
            flex-direction: column; 
            align-items: center;
            min-height: 0;
            text-align: center;
            margin-bottom: 5px;
        }
        
        .banner {
        max-width: 100%;
        height: auto;
        margin-bottom: 50px; 
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            background-color: #4162FF; 

            margin-bottom: 20px
        }

        th {
            border: 1px solid #ffffff;
            padding: 16px; 
            text-align: left;
            color: #fff; 
            font-size: 18px; 
        }

        td {
            border: 1px solid #ffffff;
            padding: 12px;
            text-align: left;
            background-color: #EEF4FB; 
            color: #060a21; 
            line-height: 150%;
        }

        td.description {
            max-width: 400px; 
            overflow-y: auto;
        }

    .add-product-button {
        display: inline-flex;
        height: 48px;
        padding: 4px 16px;
        justify-content: center;
        align-items: center;
        gap: 8px;
        border-radius: 12px;
        background: var(--primary-blue, #4162FF);
        color: #fff;
        text-decoration: none;
        border: none;
        cursor: pointer; 
    }

    </style>

    <div class="navbar">
        <img src="https://github.com/aryawijayak/shopping-art/assets/119391657/7ea7f648-a457-4e65-a45f-f90796663489" alt="Logo">
    </div>


    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input  type="submit" value="Add Product" class="add-product-button"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    Pada kode diats saya menambahkan sedikit inline css agar tampilan website saya lebih enak dilihat dan unik dari teman teman lainnya. 

    Dan apda tahap terakhir pembuatan form saya menambahkan fungsi `create_product` pada `view.py` dan membuat path agar file html create product dapat diakses. Isi dari fungsi `create_product` antara lain:

    ```
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

    ```
    Fungsi create product berguna untuk memasukan akses ke `create_product.html`

- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

    Pertama tama buatlah fungsi `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id`. Untuk show xml dan json tanpa id dapat memberikan akses ke semua data, namun untuk by id akan menampilkan data pada id yang dipanggil. Isi dari fungsi`show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` antara lain:

    ```
    def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    ```
    def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    ```
    def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    ```
    def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Keempat fungsi diatas berguna untuk melihat input dari  html pada file `create_product.html`. 

- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    Setelah membuat keempat fungsi diatas, saya selanjutnya memanggil keempat fungsi tersebut pada urls.py dengan mengimport 
    ```
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
    ```
    Selanjutnya mengubah `urlpatterns` menjadi sebagai berikut:
    ```
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'), 
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```
- [x]  Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data. Kalimat pesan boleh dikustomisasi sesuai dengan tema aplikasi, namun harus memiliki makna yang sama.
    Untuk membuat total item yang tersimpan itu dapat menggunakan key `total` pada dictionary context pada `views.py`. Caranya adalah dengan menambakan direktori total panjang seperti dibawah ini:
    ```
    'total' : products.__len__(),
    ```

    Setelah tahap tersebut, panggil total di `main.html` dengan menggunakan kode dibawah ini:

    ```
    <h4 class="total">Anda telah membuat karya sebanyak: {{total}} karya 🎨🖼️</h4>
    ```

Pada akhirnya kita berhasil menambahkan fungsi tabel 🤩 pada website shopping art kita 😉

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. HTML
![HTML ](https://user-images.githubusercontent.com/119391657/268957657-ef90f573-6e43-465a-bf71-1ad414ca9841.png)

2. XML (ALL DATA)
![XML ALL](https://user-images.githubusercontent.com/119391657/268959612-901e45a8-ddb1-47d3-b97a-75bc75b34192.png)

3. XML (BY ID)
![XML ID](https://user-images.githubusercontent.com/119391657/268959801-9db045a6-847a-4923-b94c-bec4d6011efe.png)

4. JSON (ALL DATA)
![JSON ALL](https://user-images.githubusercontent.com/119391657/268958115-e29deec4-9a0a-41cb-b881-ebf9c3166d4f.png)

5. JSON (BY ID)
![JSON ID](https://user-images.githubusercontent.com/119391657/268959285-0bb6efa8-7f78-4c0e-a7e1-32eae7321d73.png)
</details>

<br>

# Tugas 4
<details>

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

| UserCreationForm        |
| ---        |
|`UserCreationForm` di Django adalah jenis formulir yang sudah ada sebelumnya untuk memudahkan pembuatan akun pengguna baru di aplikasi web Anda. Formulir ini mencakup kolom-kolom umum seperti username, password, dan konfirmasi password.|

Keuntungan menggunakan UserCreationForm adalah:

1. `Kemudahan Penggunaan:` Anda tidak perlu mengembangkan formulir pendaftaran dari awal karena Django sudah menyediakannya.

2. `Validasi Otomatis:` Formulir ini secara otomatis memastikan bahwa pengguna mengisi informasi yang benar dan sesuai.

3. `Kemampuan Kustomisasi:` Anda masih dapat menyesuaikan formulir ini sesuai dengan kebutuhan Anda. Anda bisa menambahkan kolom tambahan, seperti alamat email.

4. `Terhubung dengan Model Pengguna:` Data yang dimasukkan ke dalam formulir akan langsung disimpan di database aplikasi Anda.

Namun, ada beberapa kekurangan:

1. `Tampilan Bawaan:` Tampilan formulir mungkin tidak sesuai dengan desain visual aplikasi Anda, sehingga Anda perlu melakukan penyesuaian tampilan.

2. `Ketergantungan pada Django:` Anda hanya bisa menggunakan UserCreationForm jika aplikasi Anda menggunakan Django.

3. `Kustomisasi yang Memerlukan Pemahaman:`Untuk kustomisasi yang lebih kompleks, Anda mungkin perlu bekerja lebih keras.

4. `Memerlukan Pemahaman tentang Django:` Penggunaan UserCreationForm memerlukan pemahaman tentang cara Django mengelola pengguna dan otentikasi.

Jadi, UserCreationForm adalah alat yang sangat berguna untuk membuat formulir pendaftaran pengguna dalam aplikasi web Django, meskipun Anda perlu mempertimbangkan apakah sesuai dengan kebutuhan dan desain aplikasi Anda sebelum menggunakannya.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- [x]
| Definisi  | Autentikasi adalah proses verifikasi identitas pengguna, yaitu memastikan bahwa seseorang yang mencoba mengakses aplikasi adalah pengguna yang mereka klaim | Otorisasi adalah proses yang menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna yang telah diautentikasi.
|Tujuan | Autentikasi digunakan untuk memeriksa identitas pengguna, misalnya, apakah mereka adalah pengguna terdaftar atau tamu | Otorisasi mengendalikan akses pengguna ke berbagai bagian atau fungsi dalam aplikasi, memastikan hanya pengguna yang berwenang yang dapat mengakses sumber daya tertentu
|Waktu Pelaksanaan |Autentikasi umumnya terjadi di awal sesi pengguna, ketika mereka mencoba masuk atau mengakses aplikasi Anda untuk pertama kalinya |

`Mengapa Keduanya Penting:`

1. `Keamanan:` Autentikasi membantu mencegah akses tidak sah ke aplikasi Anda dengan memverifikasi identitas pengguna. Otorisasi memastikan bahwa pengguna hanya memiliki akses ke bagian aplikasi yang sesuai dengan peran dan izin mereka, mengurangi risiko pelanggaran keamanan.

2. `Kontrol Akses: ` Otorisasi memungkinkan Anda untuk mengelola akses pengguna ke berbagai fitur dan data dalam aplikasi Anda. Ini membantu mencegah pengguna yang tidak berwenang mengakses atau memodifikasi informasi penting.

3. `Pengelolaan Peran:` Autentikasi dan otorisasi memungkinkan Anda untuk mengorganisasi pengguna dalam peran yang berbeda, seperti administrator, pengguna biasa, atau pengguna tamu. Hal ini memudahkan pengaturan izin berdasarkan peran, sehingga Anda dapat mengendalikan apa yang dapat dilakukan setiap peran.

4. `Pelacakan Aktivitas:` Kombinasi autentikasi dan otorisasi memungkinkan Anda untuk melacak aktivitas pengguna dan melakukan audit terhadap tindakan mereka. Ini berguna untuk melacak siapa yang melakukan apa dalam aplikasi Anda.

Secara keseluruhan, autentikasi dan otorisasi adalah komponen kunci dalam mengamankan aplikasi web Django Anda dan memastikan bahwa pengguna hanya memiliki akses ke sumber daya yang sesuai dengan peran dan izin mereka.


### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah mekanisme penyimpanan data kecil yang digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien (browser) pengguna. Cookies adalah file teks kecil yang dikirimkan oleh server web ke browser pengguna saat pengguna mengunjungi sebuah situs web. Cookies kemudian disimpan di komputer pengguna dan dikirimkan kembali ke server web setiap kali pengguna melakukan permintaan ke situs tersebut. Dengan cookies, situs web dapat "mengingat" informasi tertentu tentang pengguna, seperti preferensi, sesi, atau informasi pengidentifikasi.

Dalam konteks Django, sebuah kerangka kerja pengembangan web yang kuat, cookies digunakan untuk mengelola data sesi pengguna dengan mudah. Django memiliki dukungan bawaan yang kuat untuk mengelola cookies dan data sesi pengguna. Berikut adalah cara Django menggunakan cookies untuk mengelola data sesi pengguna:

- Penyimpanan Data Sesi: Django memungkinkan pengembang untuk menyimpan data sesi pengguna dalam cookies. Ini berarti Anda dapat menyimpan informasi seperti ID pengguna, preferensi, atau keadaan sesi pengguna dalam cookies.
- Middleware Sesi: Django menggunakan middleware sesi untuk mengelola data sesi pengguna. Middleware ini memproses cookies sesi dan memungkinkan Anda untuk mengakses data sesi dalam tampilan (view) aplikasi Anda. Middleware ini otomatis termasuk dalam daftar MIDDLEWARE di file settings.py.
- Pengaturan Cookies: Anda dapat mengonfigurasi penggunaan cookies dalam Django melalui berbagai pengaturan di file settings.py. Anda dapat mengatur parameter seperti SESSION_COOKIE_SECURE untuk memastikan cookies hanya dapat digunakan melalui koneksi HTTPS, SESSION_COOKIE_HTTPONLY untuk membatasi akses JavaScript ke cookies sesi, dan lainnya.
- Cookie Pengenal Sesi: Django secara otomatis menghasilkan cookie pengenal sesi unik untuk mengidentifikasi pengguna. Cookie ini mengandung ID sesi yang digunakan untuk mengambil data sesi dari penyimpanan sesi.
- Akses Data Sesi: Anda dapat dengan mudah mengakses data sesi pengguna dalam Django melalui objek request dalam tampilan (view). Anda dapat menambahkan, mengubah, atau menghapus data sesi sesuai kebutuhan aplikasi Anda.
- Keamanan Cookies: Django telah menerapkan langkah-langkah keamanan untuk melindungi cookies sesi dari serangan potensial seperti Cross-Site Request Forgery (CSRF) dan Cross-Site Scripting (XSS). Ini memastikan bahwa cookies sesi hanya dapat diakses dan digunakan dengan aman oleh pengguna yang berwenang.

Dengan menggunakan cookies dalam Django, pengembang dapat dengan mudah mengelola informasi sesi pengguna, menjaga keadaan sesi, menyimpan preferensi, dan mengidentifikasi pengguna yang telah diautentikasi. Hal ini membantu membangun pengalaman pengguna yang lebih interaktif dan konsisten dalam aplikasi web Anda.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web tidak selalu aman secara default, dan ada beberapa risiko potensial yang harus diwaspadai. Berikut adalah beberapa risiko yang terkait dengan penggunaan cookies:

1. `Penyadapan Data:` Cookies dapat menjadi sasaran potensial untuk penyadapan data oleh pihak ketiga yang tidak berwenang. Jika cookies mengandung informasi sensitif, seperti token otentikasi atau informasi pribadi, penyadapan data tersebut dapat membahayakan keamanan pengguna.

2. `Cross-Site Scripting (XSS):` Dalam serangan XSS, penyerang mencoba menyisipkan kode berbahaya ke dalam cookies yang diterima oleh pengguna. Kode berbahaya ini dapat dieksekusi oleh browser pengguna dan membahayakan keamanan pengguna.

3. `Cross-Site Request Forgery (CSRF):` Serangan CSRF melibatkan pengiriman permintaan yang tidak sah dari situs web yang dikompromikan ke situs web yang diakses oleh pengguna. Jika situs web yang diakses menggunakan cookies untuk otentikasi, serangan CSRF dapat memengaruhi pengguna yang sudah diautentikasi.

4. `Cookies Tidak Aman (Non-Secure): `Cookies yang dikirimkan melalui koneksi HTTP (non-HTTPS) dapat disadap lebih mudah oleh penyerang. Oleh karena itu, menggunakan koneksi HTTPS untuk mengirim cookies adalah praktik yang lebih aman.

5. `Penyimpanan Data Terlalu Lama:` Jika data dalam cookies disimpan terlalu lama, informasi sensitif yang ada dalam cookies dapat menjadi risiko yang berkelanjutan. Dalam situasi tertentu, cookies yang tumpang tindih dapat mengekspos data sensitif.

Penggunaan cookies aman atau tidak tergantung pada cara Anda mengimplementasikannya dalam aplikasi web Anda. Dengan tindakan pencegahan yang tepat, Anda dapat meminimalkan risiko keamanan terkait cookies dan memastikan bahwa data pengguna tetap aman.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1. **Registrasi**
   
   Registrasi berguna untuk membuat akun pada database, dalam pembuatannya pertama-tama, Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `register` dan memiliki parameter `request`. Lalu impor `redirect`, `UserCreationForm`, dan `messages`. Isi dari fungsi `register` adalah:
   ```
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
   ```
   Fungsi `register` adalah bagian dari aplikasi web yang memungkinkan pengguna untuk mendaftar. Pada akses pertama, formulir pendaftaran kosong disiapkan. Jika data valid dikirimkan melalui POST, akun pengguna akan dibuat, pesan sukses ditampilkan, dan pengguna diarahkan ke halaman login. Jika formulir tidak valid atau akses bukan POST, halaman registrasi akan dirender kembali dengan pesan kesalahan yang sesuai. Setelah menambahkan `pada views.py`, buat html baru dengan bernama `register.html` yang berisi sebagai berikut
   ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "register-card">

        <img src="https://user-images.githubusercontent.com/119391657/270732366-2e835f39-83cc-43de-b22b-df914ade0c93.png" alt="Logo" class="logo-image">

        <h1 class="center-align" >Register</h1>  

        <form method="POST">
            {% csrf_token %}
            <div class="form-group">
                <label for="{{ form.username.id_for_label }}">Username</label>
                {{ form.username }}
                <p class="left-align">{{ form.username.help_text }}</p>
            </div>

            <div class="form-group">
                <label for="{{ form.password1.id_for_label }}">Password</label>
                {{ form.password1 }}
                <p class="left-align">{{ form.password1.help_text }}</p>
            </div>

            <div class="form-group">
                <label for="{{ form.password2.id_for_label }}">Confirm Password</label>
                {{ form.password2 }}
                <p class="left-align">{{ form.password2.help_text }}</p>
            </div>

            <div class="center-align">
                <input type="submit" name="submit" value="Daftar" class="add-product-button">
            </div>

            <div class="center-align padding-top">
                Back to Login? <a href="{% url 'main:login' %}">Login</a>
            </div>
            
        </form>
        
    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

    </div>  

    {% endblock content %}
   ```
   Dikarenakan saya ingin memodifikasi style dari css dari registrasi, maka saya membuat sedikit berbeda dari template. Tambahkan path url milik halaman register ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `register` dari `views.py` dan tambahkan `path('register/', register, name='register')` pada variabel `urlpatterns`. Hal ini berfungsi agar registrasi bisa dipanggil menggunakan MVT dan dipanggil dengan cara `href="{% url 'main:register' %}"`
   

2. **Login**
   
   Login berguna untuk masuk ke akun yang sudah di daftarkan pada datapase pada fungsi registration sebelumnya. Pembuatan login dilakukan dengan cara buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `login_user` yang menerima parameter `request`. Lalu impor `authenticate` dan `login`. Isi dari fungsi `login` adalah:
   ```
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
   ```
    Fungsi `login_user` digunakan untuk memproses login pengguna dalam aplikasi web. Jika pengguna mengirimkan formulir dengan username dan password melalui metode POST, fungsi akan mencoba mengotentikasi pengguna. Jika autentikasi berhasil, pengguna akan diarahkan ke halaman utama dengan cookie 'last_login' yang disetel untuk melacak waktu login terakhir. Setelah menambahkan `pada views.py`, buat html baru dengan bernama `login.html` yang berisi sebagai berikut
   ```
   {% extends 'base.html' %}
   
   {% block meta %}
       <title>Login</title>
   {% endblock meta %}
    
    {% endblock meta %}

    {% block content %}

    <div class="login-card">
        
        <img src="https://user-images.githubusercontent.com/119391657/270732366-2e835f39-83cc-43de-b22b-df914ade0c93.png" alt="Logo" class="logo-image">

        <h1>Login Shopping Art</h1>
        
        <form method="POST" action="">
            {% csrf_token %}
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" name="username" id="username" placeholder="Username" class="form-control">
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" placeholder="Password" class="form-control">
            </div>
            <div class="form-group">
                <input class="add-product-button" type="submit" value="Login">
            </div>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
        <div class="login-black">
            Don't have an account yet? 
            <div class="login-blue" >
                <a href="{% url 'main:register' %}" >Register Now</a>
            </div>
            
        </div>
        
    </div>

    {% endblock content %}
   ```
   Tambahkan path url milik halaman login ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `login` dari `views.py` dan tambahkan `path('login/', login_user, name='login')` pada variabel `urlpatterns`.  Hal ini berfungsi agar registrasi bisa dipanggil menggunakan MVT dan dipanggil dengan cara `href="{% url 'main:login' %}"`

3. **Logout**
   
   Logout berguna untuk keluar dari akun, fungsi logout dilakukan dengan cara buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `logout_user` yang menerima parameter `request`. Lalu impor `logout`. Isi dari fungsi `logout_user` adalah:

   ```
   def logout_user(request):
       logout(request)
       return redirect('main:login')
   ```
   Fungsi logout_user bertujuan untuk mengelola proses logout pengguna dalam aplikasi web. Ketika fungsi ini dipanggil, pengguna yang saat ini terotentikasi akan dikeluarkan dari sesi mereka dengan menggunakan Django's authentication system, yang menghapus status login mereka. Setelah itu, pengguna akan diarahkan kembali ke halaman login, memastikan bahwa mereka harus melakukan login ulang untuk mengakses konten yang memerlukan autentikasi, menjaga keamanan akun pengguna dan mengakhiri sesi mereka dengan aman. Setelah itu tambahkan kode berikut pada `main.html`
   ```
   ...
   <a href="{% url 'main:logout' %}">
       <button>
           Logout
       </button>
   </a>
   ...
   ```
   Setelah hyperlink tag untuk Add New Product yang ada di file `main.html`.
   Tambahkan path url milik halaman logout ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `logout_user` dari `views.py` dan tambahkan `path('logout/', logout_user, name='logout')` pada variabel `urlpatterns`.

    Setelah Melakukan ketiga step diatas, Sudah berhasil membuat, mendaftar dan keluar dari akun mu di shopping art


- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal 

    `Akun Pertama:`

    ![LoginPertama](https://user-images.githubusercontent.com/119391657/270840411-5af0731d-2fbc-481d-96fb-1140b3dc5a4e.png)

    ![DataPertama](https://user-images.githubusercontent.com/119391657/270840439-52ba680e-267a-464b-a2de-82e4772dbee1.png)

    Akun Kedua:

    ![LoginKedua](https://user-images.githubusercontent.com/119391657/270840442-1889fa75-9bb8-45a2-a181-c6a2b2b0478f.png)

    ![DataKedua](https://user-images.githubusercontent.com/119391657/270840446-828bc67b-0bae-4ae0-bd77-00c42b0a4dcb.png)


- [x] Menghubungkan model Item dengan User.

    Untuk menghubungkan model item dengan user pertama tama lakukna, membukauka `models.py` yang ada di direktori `main` lalu impor `User` dari `django.contrib.auth.models`. Pada model `Product` yang ada tambahkan kode:
   ```
   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
   ```
   Hal ini dilakukan supaya kita menghubungkan satu produk dengan satu user menggunakan relationship, jadi sebuah produk pasti terasosiasi dengan user.
   Buka `viwes.py` yang ada di direktori `main` dan modifikasi fungsi `create_product` menjadi:
   ```
   def create_product(request):
   form = ProductForm(request.POST or None)
   
   if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
   ...
   ```

   Setleah itu Ubah fungsi `show_main` menjadi:
   ```
   def show_main(request):
       products = Product.objects.filter(user=request.user)
   
       context = {
           'name': request.user.username,
       ...
   ...
   ```
   Langkah ini dilakukan untuk memungkinkan tampilan objek Product yang terkait dengan pengguna yang sedang masuk. Ini dicapai dengan melakukan penyaringan terhadap semua objek dan hanya mengambil Product yang memiliki nilai pada kolom user yang sesuai dengan pengguna yang saat ini masuk. Untuk menampilkan nama pengguna yang sedang masuk di halaman utama, kita menggunakan request.user.username. Selanjutnya, kita perlu menjalankan migrasi model dengan perintah python manage.py makemigrations, namun jika muncul kesalahan, kita dapat memilih opsi 1 untuk menetapkan nilai default pada kolom user untuk semua baris yang akan dibuat di dalam basis data. Nilai ini akan mengacu pada pengguna dengan ID 1, yang merupakan pengguna yang baru saja kita buat. Setelah itu, kita menjalankan perintah python manage.py migrate untuk menerapkan perubahan ke dalam basis data.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    Untuk menampilkan informasi dengan menerapkan cookies, pertama tama buuka file `views.py` yang ada di direktori `main` dan impor `HttpResponseRedirect`, `reverse`, dan `datetime`. Kita tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` pada fungsi `login_user`, fungsi `last_login` digunakan untuk mengetahui kapan terakhir kali user login. Cara ini dilakukan dengan mengganti kode yang ada pada conditional `if user is not None` menjadi:
   ```
   ...
   if user is not None:
       login(request, user)
       response = HttpResponseRedirect(reverse("main:show_main")) 
       response.set_cookie('last_login', str(datetime.datetime.now()))
       return response
   ...
   ```
   `login(request, user)` berguna supaya logint terlebih dahulu. Untuk membuat response, kita menggunakan variabel `response` dan mengisinya dengan `HttpResponseRedirect(reverse("main:show_main"))`. `response.setcookie('last_login', str(datetime.datetime.now()))` berfungsi untuk membuat cookie `last_login` dan menambahkannya ke response tadi.
   Pada fungsi `show_main` tambahkan `'last_login': request.COOKIES['last_login']` pada variabel `context` supaya kita bisa menambahkan informasi cookie last_login pada response yang akan ditampilkan di web `main.html`.
   Di dalam fungsi logout_user, kita menghapus cookie last_login dengan menggunakan response.`delete_cookie('last_login').` Ini memastikan bahwa cookie last_login dihapus saat pengguna berhasil logout, sehingga informasi tersebut tidak tersedia lagi setelah logout.
   
   ```
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```
   Lalu pada `main.html` tambahkan:
   ```
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```
   Untuk menampilkan data last login.

   Akhirnya login dapat dilihat pada halaman bawah apabila kita melkaukan run server dan dapat melihatnya pada localhost:8000

- [x]  Melakukan add-commit-push ke GitHub.

    Setelah menyelesaikan semua step step diatas, saatnya untuk add-commit push ke repositoi github kita. Caranya dengan pertama tama melakukan  add dengan command `git add .` setelah itu commit dengan `git commit -m " Selesai mengerjakan tugas 4"` dan terakhir mempushnya pada branch main dengan `git push -u origin main`

</details>

<br>

# Tugas 5

<details>

### 1.  Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
| Elemen Selector         | 
| ---        |
| `Elemen Selector `merupakan salah satu jenis selektor CSS yang digunakan untuk memilih elemen HTML berdasarkan jenis tagnya. Setiap jenis selektor CSS memiliki manfaat dan penggunaannya yang berbeda tergantung pada kebutuhan desain dan struktur HTML.|

Berikut ini merupakan lebih jelas mengenai jenis element selector, manfaat, dan kapan waktu yang tepat untuk menggunakannya

| Nama  |Manfaat | Waktu Penggunaan| 
| ---   | ---  | ---   |
|elektor Elemen (Tag)| Selektor ini digunakan untuk memilih semua elemen HTML yang sesuai dengan jenis tag tertentu. Ini adalah selektor yang paling umum dan memengaruhi semua elemen yang sesuai.|  Selektor elemen cocok digunakan ketika Anda ingin menerapkan gaya yang sama pada semua elemen dengan jenis tag yang sama. Misalnya, untuk mengatur gaya default untuk semua paragraf <p> atau judul level 1 `<h1>` di halaman web|
|Selektor Universal (*) | Selektor ini memilih semua elemen dalam dokumen HTML. Ini sangat kuat dan dapat digunakan untuk mengatur gaya default atau menghapus margin/padding di seluruh halaman. | Harus digunakan dengan hati-hati karena dapat memengaruhi semua elemen dalam halaman. Sebaiknya digunakan untuk mengatur reset CSS atau gaya default di tingkat tinggi.
|Selektor ID (#id)| Selektor ini digunakan untuk memilih elemen berdasarkan atribut `id` yang unik. Ini memungkinkan Anda menargetkan elemen tertentu secara spesifik. |Digunakan ketika Anda ingin mengatur gaya untuk elemen tunggal yang memiliki atribut `id` unik. Ini juga sangat berguna dalam konteks JavaScript ketika Anda perlu merujuk ke elemen tertentu.|
|Selektor Kelas (.class)|Selektor ini digunakan untuk memilih elemen berdasarkan atribut `class`. Cocok digunakan untuk menerapkan gaya yang sama pada beberapa elemen.| Ketika Anda ingin menerapkan gaya yang sama pada beberapa elemen dengan atribut `class` yang sama atau saat Anda ingin menambahkan perilaku JavaScript ke elemen-elemen serupa.|
|Selektor Atribut ([attribute])|Selektor ini memungkinkan Anda memilih elemen berdasarkan atribut HTML mereka, seperti `href`, `src`, atau atribut kustom.| Saat Anda ingin memilih elemen berdasarkan atribut tertentu. Contohnya, ketika Anda ingin mengatur gaya untuk semua tautan eksternal (`<a>` dengan `href` eksternal)

### 2.  Jelaskan HTML5 Tag yang kamu ketahui.

|No  |Tag    |Penjelasan |
|---    |---    |---|
|1  | `<html>`  |  Ini adalah elemen root yang digunakan untuk mengawali dan mengakhiri seluruh dokumen HTML.|
|2|`<head>`|  Elemen ini digunakan untuk menyertakan informasi-informasi meta dan judul halaman web, serta menghubungkan dokumen dengan berkas-berkas eksternal seperti stylesheet dan skrip JavaScript.|
|3| `<title>`| Tag ini digunakan untuk menentukan judul halaman web yang akan ditampilkan di bilah judul browser.|
|4 | `<meta>` | Elemen ini digunakan untuk menyediakan informasi meta, seperti karakter encoding, deskripsi halaman, dan instruksi-instruksi lainnya kepada browser.|
|5 |  `<link>` |Tag ini digunakan untuk menghubungkan dokumen HTML dengan berkas-berkas eksternal, seperti stylesheet CSS.|
|6| `<style>:` | Elemen ini digunakan untuk menentukan gaya dan tampilan halaman web dengan menggunakan CSS (Cascading Style Sheets) secara internal.|
|7| `<script>` | Ini digunakan untuk menyisipkan skrip JavaScript ke dalam halaman web. |
|8 | `<body>` | Elemen ini berisi seluruh konten yang akan ditampilkan di halaman web, seperti teks, gambar, video, dan elemen-elemen lainnya. |
|9 | `<div>` | Elemen ini digunakan untuk mengelompokkan dan mengatur konten dalam sebuah blok yang dapat diubah tampilannya menggunakan CSS.|
| 10 | `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`|  Tag ini digunakan untuk menentukan tingkat kepentingan berbagai judul atau heading dalam halaman web, dengan `<h1>` sebagai yang paling besar dan utama dan `<h6>` sebagai yang paling kecil.|
|11 | `<p>`| Digunakan untuk menampilkan paragraf teks.|
|12| `<a>`| Tag ini digunakan untuk membuat tautan atau hyperlink ke halaman web atau berkas lain.|
|13| `<img>`| Ini digunakan untuk menampilkan gambar di halaman web.|
|14 | `<ul>`, `<ol>`, `<li>` | Digunakan untuk membuat daftar tak terurut (unordered list) dan daftar terurut (ordered list), serta elemen-elemen dalam daftar tersebut |
|15|  `<table>`, `<tr>`, `<th>`, `<td>`| Tag ini digunakan untuk membuat tabel dan elemen-elemen di dalamnya.|
|16| `<form>`, `<input>`, `<textarea>`, `<button>` |Digunakan untuk membuat formulir dan elemen-elemen dalam formulir tersebut seperti kotak input, area teks, dan tombol submit.|
|17| `<video>` dan `<audio>` | Digunakan untuk menyematkan video dan audio ke dalam halaman web.|
|18 | `<canvas>` |Ini digunakan untuk menggambar grafis atau animasi menggunakan JavaScript.|
|19| `<svg>` | Digunakan untuk menyisipkan grafik vektor dalam format SVG (Scalable Vector Graphics) ke dalam halaman web.|
|20.| `<footer>`, `<header>`, `<nav>`, `<section>`, `<article>` |Tag ini digunakan untuk mengorganisir konten halaman web menjadi bagian-bagian yang lebih terstruktur, seperti header, footer, dan artikel.|

### 3.  Jelaskan perbedaan antara margin dan padding.
|Aspek   | Margin         | Padding         |
|---    | ---        |    ----   |
| Pengertian   | Margin mengacu pada kesenjangan antara batas dua elemen. | Padding mengacu pada ruang antara konten suatu elemen dan batasnya.	
|Lokasi Ruang   | Ini berkaitan dengan celah ruang di luar elemen. |Ini berkaitan dengan kesenjangan ruang yang ada dalam suatu elemen.	
|Elemen Penataan| Elemen gaya internal seperti warna latar belakang tidak memengaruhi margin | Elemen gaya internal apa pun memengaruhi padding seperti warna latar belakang|
|Pengaturan Optimasi | Margin dapat diotomatisasi. | Otomatisasi tidak tersedia untuk padding.|
|Nilai Numerik | Namun bilangan bulat adalah nilai numerik margin. | Bilangan real positif hanya memenuhi syarat untuk nilai padding|
|Nilai Ukuran | Nilai margin menggunakan properti invers dimana penurunan nilai akan meningkatkan garis margin dan sebaliknya.| Nilai padding digunakan untuk mengontrol ukuran elemen.	|


### 4.  Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Aspek   | CSS Tailwind         | Bootstrap         |
|---    | ---        |    ----   |
| Design    | Tailwind menganut pendekatan yang lebih "utility-first", di mana kita membangun antarmuka dengan menggabungkan class utilitas yang lebih kecil. Ini memberikan kebebasan kreatif yang lebih besar dan memungkinkan penggunaan class yang sangat spesifik.| Bootstrap menawarkan set class CSS dan komponen yang telah dirancang sebelumnya dengan tampilan yang cukup terstruktur dan konsisten. Ini cocok untuk proyek dengan desain tradisional yang membutuhkan kerangka kerja yang stabil dan mudah digunakan.|
| Fleksibilitas | Tailwind memberikan fleksibilitas yang lebih besar dengan pendekatan "utility-first" yang memungkinkan kita membangun desain yang sangat kustom sesuai kebutuhan. kita memiliki kendali penuh atas gaya dan tata letak dengan kombinasi class utilitas yang spesifik. | Bootstrap menawarkan kerangka kerja yang relatif terstruktur dengan banyak komponen yang telah dirancang sebelumnya. Ini memberikan stabilitas dan kemudahan penggunaan, tetapi mungkin memiliki batasan dalam hal fleksibilitas desain yang unik. |
| Ukuran File | Tailwind dirancang untuk lebih ringan dalam hal ukuran file. Namun, ketika kita menggunakan banyak class utilitas dalam kode, ukuran file CSS dapat meningkat. | Bootstrap adalah kerangka kerja yang lebih besar dalam hal ukuran file karena menyediakan banyak fitur dan komponen yang siap pakai. Ini mungkin berdampak pada kecepatan pengunduhan dan performa halaman web.|
|Ekosistem Pengembangan| Tailwind juga memiliki ekosistem yang berkembang pesat dengan dokumentasi yang baik dan komunitas yang aktif, kita dapat menemukan banyak sumber daya, plugin, dan integrasi dengan kerangka kerja JavaScript seperti React atau Vue. | Bootstrap memiliki ekosistem yang sangat kuat dengan dokumentasi yang kaya, banyak tema dan template yang tersedia, serta dukungan komunitas yang luas. Ini membuatnya mudah untuk memulai dan mendapatkan sumber daya yang diperlukan.


### 5.  Checklist Tugas

- [x]Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut

    Pertama tama untuk mengkostumisasi desain pada HTML, perlu menambahkan link CSS framework dalam case ini adalah Bootstrap dan Java Scriptke dalam `templates/base.html` dan menambahkan tag `<meta name="viewport">` . Untuk menambahkannya bisa dengan menambahkan:
    ```
    <head>
        {% block meta %}
            ...
        {% endblock meta %}

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>

    </head>
    
    ```
    Kita menambahkannya pada `base.html` dikarenakan pada file tersebut akan digunakan sebagai tempalte dasar html yang berguna untuk template lainnya.

- [x] Menambahkan Fitur Edit dan Delete Pada Aplikasi
    Untuk mengedit dan menghapus list pada tabel.

    Untuk membuat Edit, pertama tama kita membuka file `views.py` yang ada pada subdirektori main. Menambahkan views.py berguna untuk menambahkan fungsi yang nantinya akan berguna untuk mengedit produk kita pada shopping art. dan buatlah fungsi baru bernama `edit_product` yang menerima parameter request dan id. Tambahkan `views.py` dengan kode berikut

    ```
    def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
    
    ```

    Setelah membuat fungsi, selanjutnya kita harus membuat HTML untuk mengedit productnya. Untuk membuat HTML untuk edit pertama tama buat file baru pada folder `main/templates` dengan nama `edit_product.html ` yang berisi :
    ```
    {% extends 'base.html' %}

    {% load static %}

    {% block content %}

    <h1>Edit Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```


    Setelah membuat Fungsi, buat masukan juga fungsi tersebut pada `urls.py` agar dapat dipanggil pada `main.html`. tambahkan dengan cara berikut: 
    ```
    from main.views import edit_product
    ```
    Lalu setelah mengimport tambahkan url ke `urlpatterns` dengan cara berikut:

    ```
    ...
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    ...
    ```

    Panggil edit product yang sudah dibuat diatas dan delete product (Pada tugas sebelumnya sudah dibuat) pada `main.html` dengan menggunakan berikut ini:

    ```
    <td class="action-row"> 
        <div class="action-buttons ">
            <a href="{% url 'main:edit_product' product.pk %}" class="add-product-button">
                    Edit

            <a href="{% url 'main:remove_product' product.id %}" class="add-product-button svg-button">
                <img src="https://svgur.com/i/xtJ.svg" alt="SVG Image">
            </a>

        </div>
    </td>
    ```

- [x]Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

    Untuk mengkostumisasi halaman login, register dan tambah product saya menggunakan inline css dengan memanggil `<style>` pada bagian atas html serta dipadukan dengan framework bootstrap. Saya menggunakan inline CSS karena menurut saya ini yang mudah disetup dan digunakan untuk pemula.
    <br>

    ### Pada halaman login, berikut inline CSS yang saya tambahkan
    <details>
    <summary>
    Style Login
    </summary>

    ```
    <style>
        body {
            background-image: url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/089d21ad-7782-4104-89c2-a65435feaa61/d9dbds5-953028f0-861a-4db8-9b6f-91162fe1959d.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA4OWQyMWFkLTc3ODItNDEwNC04OWMyLWE2NTQzNWZlYWE2MVwvZDlkYmRzNS05NTMwMjhmMC04NjFhLTRkYjgtOWI2Zi05MTE2MmZlMTk1OWQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.V4cjYqRZbpYo5gZ_cXGMswU-GI-vp3KNKuVhEjE6Clw'); /* Gantilah 'path-to-your-image' dengan path ke gambar GIF Anda */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            margin: 12px;
            padding: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            position: relative; 
        }

        .login-card h1,
        .login-card label,
        .login-card a {
            font-family: 'Poppins', sans-serif;
            color: rgb(19, 10, 54);
        }

        .login-card a {
            font-family: 'Poppins', sans-serif;
            color: #4162FF;
            text-decoration: underline; 
        }

        .login-black{
            font-family: 'Poppins', sans-serif;
            color:rgb(19, 10, 54);
        }

        .login-card {
            text-align: center;
            background-color: #ffffffa9;
            border-radius: 32px;
            padding: 30px;
            width: 400px;
            text-align: center;
            padding-top: 50px;
            backdrop-filter: blur(6px);
            border: 2px solid rgba(255, 255, 255, 0.439); 
        }

        .login-card h1 {
            font-family: 'Poppins', sans-serif;
        }

        .login-card form {
            font-family: 'Poppins', sans-serif;
        }

        .login-card input[type="text"],
        .login-card input[type="password"] {
            font-family: 'Poppins', sans-serif;
            color: black; 
            background-color: white;
        }

        .login-card .form-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 24px;
        }

        .login-card .form-group label {
            font-family: 'Poppins', sans-serif;
            margin-bottom: 8px;
            text-align: left; 
        }

        .login-card .form-control {
        font-family: 'Poppins', sans-serif;
        width: 100%;
        padding: 12px; 
        border: 1px solid #ccc;
        border-radius: 6px;
        box-sizing: border-box;
        margin-bottom: 12px;
        font-size: 16px; 
        background-color: white;
        }


        .login-card .add-product-button {
            font-size: 16px;
            display: inline-flex;
            height: 56px;
            padding: 8px 48px;
            justify-content: center;
            align-items: center;
            gap: 16px;
            border-radius: 16px;
            background: var(--primary-blue, #4162FF);
            color: #ffffff;
            text-decoration: none;
            border: none;
            cursor: pointer;
        }

        .logo-image {
        max-width: 100px; 
        height: auto; 
        display: block; 
        margin: 0 auto; 
        }

        .text-title{
            font-size:28px;
            font-weight: 600;
            padding-bottom: 8px;
            padding-top: 12px;
            
        }

    </style>
    ```
    </details>

    <br>

    ### Pada halaman Register, berikut inline CSS yang saya tambahkan

    <details>
    <summary>
    Style Register
    </summary>

    ```
    <style>
        body {
            background-image: url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/089d21ad-7782-4104-89c2-a65435feaa61/d9dbds5-953028f0-861a-4db8-9b6f-91162fe1959d.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA4OWQyMWFkLTc3ODItNDEwNC04OWMyLWE2NTQzNWZlYWE2MVwvZDlkYmRzNS05NTMwMjhmMC04NjFhLTRkYjgtOWI2Zi05MTE2MmZlMTk1OWQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.V4cjYqRZbpYo5gZ_cXGMswU-GI-vp3KNKuVhEjE6Clw'); /* Gantilah 'path-to-your-image' dengan path ke gambar GIF Anda */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            position: relative; 
        }

        .login-card h1,
        .login-card label,
        .login-card a {
            font-family: 'Poppins', sans-serif;
            color: rgb(19, 10, 54);
        }

        .login-card a {
            font-family: 'Poppins', sans-serif;
            color: #4162FF;
            text-decoration: underline; 
        }

        .text-titile{
            font-size: 32px;
        }

        .register-card {
            text-align: center;
            background-color: #ffffffbb;
            border-radius: 32px;
            padding: 30px;
            width: 400px;
            text-align: left;
            padding-top: 50px;
            backdrop-filter: blur(6px);
            border: 2px solid rgba(255, 255, 255, 0.439); 
        }

        .register-card h1 {
            font-family: 'Poppins', sans-serif;
        }

        .register-card form {
            font-family: 'Poppins', sans-serif;
            margin-top: 20px; 
        }

        .register-card input[type="text"],
        .register-card input[type="password"] {
            font-family: 'Poppins', sans-serif;
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
        }

        .register-card .form-group {
            margin-bottom: 24px;
        }

        .register-card .form-group label {
            font-family: 'Poppins', sans-serif;
            margin-bottom: 8px;
            text-align: left;
            display: block; 
        }

        .register-card .add-product-button {
            font-size: 18px;
            display: inline-flex;
            height: 56px;
            padding: 8px 48px;
            justify-content: center;
            align-items: center;
            gap: 16px;
            border-radius: 16px;
            background: var(--primary-blue, #4162FF);
            color: #fff;
            text-decoration: none;
            border: none;
            cursor: pointer;
        }

        .logo-image {
            max-width: 100px;
            height: auto;
            display: block;
            margin: 0 auto;
        }

        .left-align {
        text-align: left;
        }

        .center-align {
        text-align: center;
        }

    .password{
            text-align: center;
        }
        .padding-top{
            padding-top: 20px;
        }
        
    </style>
    ```
    </details>

    <br>

    ### Pada halaman Tambah Inventori, berikut inline CSS yang saya tambahkan

    <details>
    <summary>
    Style Tambah Inventori
    </summary>

    ```
    <style>
        body {
            background-image: url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/089d21ad-7782-4104-89c2-a65435feaa61/d9dbds5-953028f0-861a-4db8-9b6f-91162fe1959d.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA4OWQyMWFkLTc3ODItNDEwNC04OWMyLWE2NTQzNWZlYWE2MVwvZDlkYmRzNS05NTMwMjhmMC04NjFhLTRkYjgtOWI2Zi05MTE2MmZlMTk1OWQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.V4cjYqRZbpYo5gZ_cXGMswU-GI-vp3KNKuVhEjE6Clw'); /* Gantilah 'path-to-your-image' dengan path ke gambar GIF Anda */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            position: relative; 
        }

        .login-card h1,
        .login-card label,
        .login-card a {
            font-family: 'Poppins', sans-serif;
            color: rgb(19, 10, 54);
        }

        .login-card a {
            font-family: 'Poppins', sans-serif;
            color: #4162FF;
            text-decoration: underline; 
        }

        .text-titile{
            font-size: 32px;
        }

        .register-card {
            text-align: center;
            background-color: #ffffffbb;
            border-radius: 32px;
            padding: 30px;
            width: 400px;
            text-align: left;
            padding-top: 50px;
            backdrop-filter: blur(6px);
            border: 2px solid rgba(255, 255, 255, 0.439); 
        }

        .register-card h1 {
            font-family: 'Poppins', sans-serif;
        }

        .register-card form {
            font-family: 'Poppins', sans-serif;
            margin-top: 20px; 
        }

        .register-card input[type="text"],
        .register-card input[type="password"] {
            font-family: 'Poppins', sans-serif;
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
        }

        .register-card .form-group {
            margin-bottom: 24px;
        }

        .register-card .form-group label {
            font-family: 'Poppins', sans-serif;
            margin-bottom: 8px;
            text-align: left;
            display: block; 
        }

        .register-card .add-product-button {
            font-size: 18px;
            display: inline-flex;
            height: 56px;
            padding: 8px 48px;
            justify-content: center;
            align-items: center;
            gap: 16px;
            border-radius: 16px;
            background: var(--primary-blue, #4162FF);
            color: #fff;
            text-decoration: none;
            border: none;
            cursor: pointer;
        }

        .logo-image {
            max-width: 100px;
            height: auto;
            display: block;
            margin: 0 auto;
        }

        .left-align {
        text-align: left;
        }

        .center-align {
        text-align: center;
        }

    .password{
            text-align: center;
        }
        .padding-top{
            padding-top: 20px;
        }
        
    </style>
    ```
    </details>

    <br>
    <br>

- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

    Untuk mengkostumisasi halaman daftar inventori menjadi berwarna saya sama seperti halaman sebelumnya menggunakan inline CSS dengan menambahkan `<style>` Untuk mengkostumisasi daftar inventori maka menambahkan code style berikut

        ```
        <style>
    
            body {
                background-color: #f4f7ff;
                margin: 12px;
            }
    
            h1, h2, h3, h4, h5, p, th, td, a, button {
                font-family: 'Poppins', sans-serif;
            }
            
            .navbar{
            position: sticky;
            top: 0;
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            margin-bottom: 20px;
            background-color: rgba(255, 255, 255, 0.5);
            }
    
            .navbar img {
                max-height: 28px;
                padding-right: 20px;
                
            }
    
            .navbar-brand {
                color: #76797b;
                font-weight: 500;
                font-size: 16x;
            }
    
    
            .navbar .navbar-nav .nav-item {
                margin-right: 10px; /* Mengatur jarak antar item */
                padding-top: 3px;
                padding-bottom: 3px;
            }
    
            .navbar .navbar-nav .nav-item-active{
                background: #4161ff20; ;
                border-radius: 99px; 
                padding-left: 20px;
                padding-right: 20px;
                margin-left: 20px;
                margin-right: 20px;
                padding-top: 3px;
                padding-bottom: 3px;
                color: #4162FF;
                font-weight: 600;
            }
            
            .content-container {
                display: flex;
                flex-direction: column; 
                align-items: center;
                min-height: 0;
                text-align: center;
                margin-bottom: 5px;
            }
    
            .text-center {
                text-align: center;
                margin-bottom: 2px
            }
            
            .banner {
            max-width: 100%;
            height: auto;
            margin-bottom: 50px; 
            }
    
            table {
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
                background-color: #4162FF; 
                border-radius: 20px 20px 20px 20px; 
                margin-bottom: 20px
            }
    
            table tr:last-child td {
                background-color: #d7e3ef; 
                color: #160323; 
                font-weight: 500; 
            }
    
            th {
                border: 1px solid #ffffff;
                padding: 16px; 
                text-align: left;
                color: #fff; 
                font-size: 18px; 
            }
    
            td {
                border: 1px solid #ffffff;
                padding: 12px;
                text-align: left;
                background-color: #EEF4FB; 
                color: #060a21; 
                line-height: 150%;
            }
    
            td.description {
                max-width: 400px; 
                overflow-y: auto;
            }
    
            .center-text {
                text-align: center;
            }
    
            .card-container {
                margin-top: 8px;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                flex-wrap: nowrap; 
                justify-content: flex-start; 
                gap: 5px;
                overflow-x: auto; 
                justify-items: center; 
                align-items: center;
                justify-content: center;
                margin: 28px;
            }
            .card {
                background-color: #ffffff;
                margin: 12px;
                border-radius: 24px;
                box-shadow: 0px 5px 10px rgba(0, 0, 0, 0);
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                margin-bottom: 16px;
                width:100%;
                min-width: 420px;
            }
    
                @media (min-width: 768px) {
                .card-container {
                    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
                    justify-content: center;
                }
            }
    
                @media (min-width: 1200px) {
                .card-container {
                    grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); 
                    justify-content: center;
                }
            } 
    
                @media (min-width: 2400px) {
                    .card-container {
                        grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); 
                        justify-content: center;
                    }
                } 
    
            .card img {
                max-width: 100%;
                border-radius: 24px;
                height: auto;
            }
    
            .card-content {
                padding: 10px; 
                display: flex;
                flex-direction: column;
                align-items: center;
            }
    
            .card-content h4 {
                font-size: 18px;
                margin: 5px 0; 
            }
    
            .card-content p {
                font-size: 14px;
                margin: 5px 0; 
            }
    
            
            .card-grid {
                display: flex;
                flex-direction: row; 
                flex-wrap: nowrap; 
                justify-content: flex-start; 
                gap: 20px; 
                overflow-x: auto; 
                white-space: nowrap; 
            }
    
            .add-product-button {
                display: inline-flex;
                height: 48px;
                padding: 4px 16px;
                justify-content: center;
                align-items: center;
                gap: 8px;
                border-radius: 12px;
                background: var(--primary-blue, #4162FF);
                color: #fff;
                text-decoration: none;
                border: none;
                cursor: pointer; 
            }
    
            .add-amount-button{
                background: var(--primary-blue, #4161ff1f);
                color:#4162FF;
                padding: 20px 0px;
                margin:4px;
                border-radius: 1000px;
            }
    
            .logout-button {
                background-color: #ff1d1d; 
                width:96px
            }
    
            .action-buttons {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 8px;
                width: 100%; 
                
            }
    
            .action-buttons a {
                width: 100%;
            }
    
            .svg-button {
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 12px;
                background-color: var(--primary-red, #ff1d1d);
                color: #fff;
                text-decoration: none;
                border: none;
                cursor: pointer;
                height: 48px;
                padding: 4px 16px;
                min-width: 56px;
            }
    
            .color-gray{
                color:#76797b;
            }
            
            .action-gap{
                padding: 12px;
            }
    
            @media (max-width: 768px) {
                .card {
                    width: calc(50% - 20px); 
                }
            }
    
            @media (min-width: 769px) {
                .card {
                    width: calc(33.33% - 20px); 
                }
            }
    
            .text-title{
                font-weight: 700;
                font-size: 28px;
            }
    
            .text-title-semi{
                font-weight: 600;
                font-size:28px;
            }
    
            .amount-img {
                max-height: 28px;
                max-width: 28px;
                
            }

        </style>

        ```
 

    Selain itu saya juga menambahkan inventori menjadi card diatas tabel dengan menggunakan kode berikut:

        <div class="card-container">
            {% for product in products %}
            <div class="card border-0" style="padding: 10px;  padding-bottom: 30px;" >
                <img class="card-img" src={{product.image_url}} alt="Product Image">
                <h3 style="margin: 20px 0px; font-size: 24px; font-weight: 700;" >{{product.name}}</h4>
                <p style="margin: 0px 8px; font-size:16px; font-weight: 500" >By: {{product.artist}}</p>
            </div>
            {% endfor %}
        </div>

    Untuk membuat card pertama tama panggil kelas `card-container` yang sudah dibuat di style CSS yang berguna agar grid dari card menjadi rapi, selanjutnya memanggil `{% for product in products %}` yang dimana konten dari card akan menjadi dinamis sesuai dengan input dari `create_product`. Setelah itu untuk mendapatkan gambarnya dapat diambil dari source : `src={{product.image_url}}`, untuk namanya bisa dengan `{{product.name}}` dan terakhit untuk menambahkan artist atau pembuat dari gambar tersebut tambahkan `{{product.artist}}`. Setelah itu semua card akan menjadi dinamis menyesuaikan konten dari isi tabel.

    Untuk menambahkan gambar pada card saya memodifikasi file `forms.py` dengan menambahkan input `image_url` seperti berikut ini:

    ```
    class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "artist", "price","description", "image_url"]
    ```
    
- [x] Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.

    Untuk menambahkan penanda berbeda di akhir tabel, saya menambahkan CSS untuk last child pada `tr` dengan kode berikut:
    ```
    table tr:last-child td {
        background-color: #d7e3ef; 
        color: #160323; 
        font-weight: 500; 
    }
    ```

</details>

# Tugas 6
### 1.  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

### 2. 

### 3. 