# 🖼️ Shopping Art 🛒 🎨


```
Tempat Memamerkan karya-karya inspiratif 👨🏻‍🎨
```
# Tugas 2

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


# Tugas 3

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


# Tugas 4

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

- [x] Menghubungkan model Item dengan User.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

- [x]  Melakukan add-commit-push ke GitHub.

