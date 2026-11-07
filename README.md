# 🌸 Deskripsi Project — My Portofolio by Gwen 🌸

Nama      : Stefani Gwen Rolanda Tumbelaka

NPM       : 2506594263

Kelas	    : PBP C

Project **My Portofolio** merupakan project website portofolio pribadi menggunakan framework Django sebagai bagian dari penilaian Tutorial dan Tugas Individu untuk mata kuliah Pemrograman Berbasis Platform (CSGE602022) Gasal 2026/2027, Fakultas Ilmu Komputer, Universitas Indonesia. Project ini pun bertujuan sebagai wadah untuk mempresentasikan diri saya melalui konten terkait riwayat serta apa yang bisa saya tawarkan pada audiens dengan elemen visual yang menyesuaikan kesukaan dan karakteristik diri saya.

[🌐 Klik di sini untuk membuka versi deployment](https://stefani-gwen-myportofolio.pws.cs.ui.ac.id/)

# 📝 Daftar Isi
- 💻 [Penjelasan Fitur](https://github.com/stefanigwen14/myportofolio#-penjelasan-fitur)
- ⚙️ [Panduan Setup Instalasi Project secara Local](https://github.com/stefanigwen14/myportofolio#%EF%B8%8F-panduan-setup-instalasi-project-secara-local)
- ❓ [Pertanyaan Refleksi & AI Disclosure](https://github.com/stefanigwen14/myportofolio#-pertanyaan-refleksi--ai-disclosure)
  * [Tugas 1](https://github.com/stefanigwen14/myportofolio#tugas-1)
  * [Tugas 2](https://github.com/stefanigwen14/myportofolio#tugas-2)
  * [Tugas 3](https://github.com/stefanigwen14/myportofolio#tugas-3)
  * [Tugas 4](https://github.com/stefanigwen14/myportofolio#tugas-4)
  * [Tugas 5](https://github.com/stefanigwen14/myportofolio#tugas-5)
  * Tugas 6

# 💻 Penjelasan Fitur
Semua fitur pada website ini dijalankan pada satu Django app, yaitu `main`. Terdapat beberapa fitur, yaitu:
1. **Profile** - profil perkenalan singkat yang mencakup identitas mahasiswi, perkenalan singkat, social links (GitHub, LinkedIn, Email), informasi last login session, serta garis besar bidang yang saya tekuni.
2. **Experience** - berisi riwayat pengalaman kepanitiaan, organisasi, dsb. Pada saat ini, operasi CRUD perlu dilakukan secara manual melalui terminal.
3. **Education** - berisi riwayat pendidikan. Pada saat ini, operasi CRUD perlu dilakukan secara manual melalui terminal.
4. **Projects** - berisi project yang sudah pernah saya lakukan. Modul inilah yang saya gunakan untuk keperluan mengerjakan **Tutorial**. Operasi penambahan dan penghapusan project sudah terimplementasi bagi User dengan roles tertentu, tetapi untuk pembaharuan data masih belum. User yang terautentikasi bisa memberikan Star pada project yang ada.
5. **Testimonials** - berisi testimonial dari orang-orang terdekat dan yang pernah bekerja sama dengan saya. Modul inilah yang saya gunakan untuk keperluan mengerjakan **Tugas Individu**. User yang terautentikasi dan diberikan roles tertentu mampu meninggalkan pesan langsung tentang saya dengan kategori yang relevan (baik itu dari Experience, Project, ataupun Education) dengan operasi CRUD yang sudah terimplementasi secara matang. User yang terautentikasi bisa memberikan Heart pada testimonial yang ada.

# ⚙️ Panduan Setup Instalasi Project secara Local
1. Lakukan cloning terhadap repository ini dengan command berikut pada terminal dan ganti current directory ke clone local tersebut
   ```
   git clone https://github.com/stefanigwen14/myportofolio.git
   cd myportofolio
   ```
2. Buat dan aktifkan virtual environment pada directory tersebut
   Windows:
   ```
   python -m venv env
   env\Scripts\activate
   ```
   Unix (macOS/Linux):
   ```
   python3 -m venv env
   source env\bin\activate
   ```
3. Lakukan instalasi terhadap dependencies
   ```
   pip install -r requirements.txt
   ```
4. Lakukan konfigurasi environment variables dengan membuat berkas `.env` pada root project supaya bisa dijalankan secara lokal 
   `.env:`
   ```
   PRODUCTION=False
   ```
5. Lakukan migrasi terhadap database dengan command berikut pada terminal
   ```
   python manage.py migrate
   ```
6. Jalankan server pada `http://localhost:8000/` di browser dengan menjalankan command berikut pada terminal, sekarang project sudah bisa berjalan secara lokal!
   ```
   python manage.py runserver
   ```
  📜 Referensi (mohon merujuk ke sini lebih lanjut, terutama jika ingin melakukan production): [Tutorial 0 PBP Gasal 2026/2027](https://pbp.cs.ui.ac.id/tutorial/tutorial-0.html#instalasi-django-dan-inisiasi-proyek-django)

# ❓ Pertanyaan Refleksi & AI Disclosure
## Tugas 1
1. Iya, saya sudah menggunakan elemen semantik HTML5, yaitu section. Saya menggunakan elemen tersebut untuk menciptakan section baru untuk bagian "Experiences" (mencontoh bagian hero website pada template tutorial 1 yang sudah menggunakan section) supaya terpisahkan dari section lain seperti hero. section membantu saya dalam membuat static web karena bisa memudahkan proses navigasi (UX) ke bagian tertentu tanpa perlu scripting yang jika dilihat dari sisi user seandainya mereka melihat website portofolio saya mereka ingin langsung melihat Experiences saya saja.
2. Saya menemukan tantangan tata letak ini ketika menyusun elemen p untuk deskripsi di bawah header section saya (dalam cards container). Ketika saya melakukan test seberapa responsive di localhost dan mengecilkan window browser saya (supaya bisa memperkirakan bagaimana tampilannya pada layar yang lebih kecil seperti mobile), saya melihat bahwa teks deskripsinya terlalu mepet dengan ujung kiri-kanan browser. Lalu saya mencoba styling css untuk elemen p pada cards container dengan mengatur marginnya dan sekarang sudah terlihat lebih rapih (ada jarak dengan kiri-kanan browser).
3. Saya merasa static web murni membatasi saya dalam membuat interaktivitas menyajikan informasi pada portofolio saya secara optimal, seperti dalam menampilkan cards Experience saya. Dalam iterasi selanjutnya, saya ingin membuat foto dalam cards bisa bergerak berupa animasi/slideshow serta container untuk cardsnya bisa digeser (slider) supaya ketika saya menambahkan card baru semuanya tidak memanjang ke samping/bawah.
- AI Disclosure: untuk tugas 1 ini, saya menggunakan AI Gemini, tetapi hanya dalam bentuk AI overview yang muncul saat melakukan pencarian Google menggunakan keywords seperti properti html/css yang ingin saya buat, dsb. Saya berusaha untuk mengerjakan tugas 1 ini dengan membaca AI overview lalu membuka website sumber AI overview tersebut (seperti W3Schools, dll) dan mencoba trial and error langsung pada kode yang saya tulis dari apa yang sudah saya baca. 

## Tugas 2
1. Ketika pengguna membuka halaman portofolio baru, Django memetakan URL tersebut ke View melalui urls.py proyek (/portofolio/urls.py) yang menghubungkan aplikasi, dalam hal ini karena sudah ada path("", include("main.urls")) pada urlpatterns di urls.py proyek maka sekarang routing bisa ditangani oleh urls.py milik aplikasi (/main/urls.py). Karena sudah ditangani oleh urls.py aplikasi yang memiliki urlpatterns untuk masing-masing View pada aplikasi, sekarang View tersebut mengambil dan memproses data dari model yang bersesuaian dengan halaman portofolio tsb. View mengirim context yang ada pada model ke template lalu Django mengembalikan HTML yang telah dirender sebagai response sehingga halaman tersebut bisa menampilkan halaman yang sesuai.
2. Data untuk bagian portofolio baru sebaiknya disimpan pada model supaya ketika diperlukan adanya entry data baru bisa langsung saja dengan mudah ditambahkan melalui perintah pada py manage-py shell. Jika ditulis langsung dalam template, hal ini akan membuat kode pada template HTML semakin panjang (harus diatur satu-satu untuk masing-masing entry data baru), tetapi kalau menggunakan model kode pada template untuk objek model yang ingin ditampilkan hanya perlu ditulis sekali karena sudah dibungkus oleh for loop untuk menampilkan data pada database models dengan susunan template yang sama. Hal ini cukup praktis untuk pemeliharaan dan pengembangan aplikasi untuk ke depannya. 
3. Fungsi makemigrations hanya membuat berkas (file baru pada /main/migrations/) yang berisi apa saja yang sudah diubah pada file models.py. Supaya perubahan yang tercantum dalam berkas ini bisa dimasukkan ke dalam database lokal, perlu dilakukan fungsi migrate. Contoh perubahan model yang mengharuskan menjalankan kedua perintah tersebut adalah ketika baru saja membuat model baru dan mengubah struktur (seperti field) pada model yang sudah ada. Penambahan object model baru tidak mengharuskan adanya pemanggilan 2 fungsi ini.
- AI Disclosure: untuk tugas 2 ini, saya menggunakan AI Gemini, tetapi hanya dalam bentuk AI overview yang muncul saat melakukan pencarian Google menggunakan keywords seperti properti html/css yang ingin saya buat, cara menmbuat objek dengan field tertentu untuk models, dsb. Saya berusaha untuk mengerjakan tugas 2 ini dengan membaca AI overview dan jika belum terjawab saya membuka website sumber AI overview tersebut (seperti W3Schools, dll) dan mencoba trial and error langsung pada kode yang saya tulis dari apa yang sudah saya baca.

## Tugas 3
1. Form HTML manual hanyalah apa yang dirender di browser (client-side construct), sementara ModelForm Django merupakan server-side construct yang sudah terhubung langsung dengan model yang ingin dibuat menggunakan form. Jika kita menggunakan form HTML biasa, maka perlu kode tambahan seperti pada JavaScript untuk melakukan validasi, dsb sehingga menggunakan ModelForm Django akan sangat menghemat waktu. CSRF token diperlukan supaya penyerang aplikasi tidak bisa mengubah request yang awalnya ke server Django menjadi suatu API berbahaya dan mengirimkan data request ke mereka, sehingga CSRF trusted origins perlu mendaftarkan URL website sendiri supaya hanya URL tsb yang dipercaya untuk melakukan request ke server.
2. JSON lebih digunakan daripada XML karena ukurannya lebih ringkas, parser yang sangat cepat, dan integrasi ke JavaScript di sisi frontend. Hal ini dikarenakan notasi JSON berasal dari sintaks JavaScript. Akan tetapi, semua bahasa pemrograman memiliki built-in untuk membaca dan membuat struktur JSON. Format XML yang masih menggunakan tags/closing tags terlihat lebih "rumit" dibandingkan JSON yang direpresentasikan sebagai dictionary dengan key dan value
3. Untuk menampilkan data (seperti pada models Project & Testimonial), fungsi show_data (seperti show_projects dan show_testimonials) yang berfungsi untuk menampilkan data pada suatu halaman memanggil fungsi get_data_json(request). get_data_json pada kode saya digunakan untuk melakukan filtering, sehingga membuat suatu queryset dari semua objek data yang ada terlebih dahulu (Model.objects.all()) lalu jika terdapat query yang didapatkan dari request.get.GET (dalam artian sedang terjadi proses search/filter) maka queryset tersebut akan difilter terlebih dahulu. Karena data untuk server perlu dalam format JSON supaya lebih mudah di-parsing, maka queryset tersebut harus di-serialize dalam bentuk JSON sebagai salah satu parameter HttpResponse utk return type get_data_json. Kemudian, HttpResponse tsb di-deserialize supaya bisa di-return untuk rendering pada template.
- AI Disclosure: untuk tugas 3 ini, saya menggunakan AI Gemini & Claude secara langsung. Saya menggunakan kedua AI tersebut untuk debugging/menemukan apa yang salah dalam CSS saya yang membuatnya tampil tidak seperti saya inginkan, cara kerja pembuatan input type seperti dropdown dan checkbox, serta konsep create/edit/delete data menggunakan JSON supaya bisa lebih sesuai dengan apa yang saya inginkan. Saya tidak langsung menyuruh AI untuk membuat kode yang tinggal saya copy-paste ke dalam kode saya, tetapi saya prompting supaya AI bisa memberikan contoh kode atau sebatas hint saja yang relevan dengan kebutuhan saya karena saya tipe yang belajar dengan mencontoh langsung. Ketika memasukkan kode yang sudah saya tulis sendiri sebelumnya, saya memastikan saya mengubah nama variabel supaya AI tidak tahu pasti konteks website apa yang sedang saya bangun.
  
Log chat: [Gemini](https://share.gemini.google/7ZQ3TCVWDWgs)
[Claude](https://claude.ai/share/c51d715d-aaf5-40f9-9e40-7f8ff618272c)

## Tugas 4
Pada tugas kali ini, saya mengimplementasikan fitur Hearts untuk data Testimonials saya (sebagai pengganti star). Saya menerapkan peran editor hanya bisa melakukan edit pada projects dan testimonial.
- AI Disclosure: untuk tugas 4 ini, saya menggunakan AI Claude secara langsung pada bagian membuat navbar yang responsif untuk layar yang lebih kecil karena penambahan autentikasi sangat memakan tempat dalam navbar sehingga terlihat tidak rapih dalam layar yang lebih kecil. Saya juga bertanya kepada Claude bagaimana melakukan if-else untuk menyembunyikan komponen pada template HTML karena is_editor tidak berfungsi bagi saya. Untuk prompting, saya meminta Claude untuk menunjukkan contoh kode implementasi yang ingin saya implementasikan. Ada beberapa bagian yang saya copy langsung seperti penerapan hamburger menu, akan tetapi saya sesuaikan dengan kode yang sudah ada sebelumnya dan saya lakukan styling sendiri CSS-nya supaya lebih sesuai dengan tampilan web saya.
  
Log chat: [Claude](https://claude.ai/share/c557217e-13c5-4403-93f6-a3770118ec09)

## Tugas 5
1. Debouncing merupakah Teknik dalam JavaScript yang digunakan untuk menunda sebuah fungsi hingga suatu jeda Waktu berlalu tanpa event baru. Teknik ini penting diterapkan dalam fitur pencarian menggunakan AJAX supaya Ketika user masih mengetik, timer sebelumnya dibatalkan dan dimulai lagi, browser hanya mengirim permintaan setelah user berhenti mengetik sejenak (tidak terlalu banyak permintaan yang dikirim) dan menciptakan pengalaman pengguna yang lebih baik.
2. Penggunaan await dalam suatu async function untuk melakukan fetch berungsi untuk menunggu Promise selesai diproses sebelum melanjutkan ke baris kode berikutnya sehingga kode asinkron fetch() lebih mudah dibaca tanpa callback yang bersarang. Jika kita tidak menggunakan wait, Promise akan tetap berjalan di belakang layar dan kode berikutnya akan langsung dieksekusi tanpa menunggu hasilnya, sehingga kemungkinan terjadi callback bersarang di console.
3. XSS (Cross-Site Scripting) adalah jenis serangan yang dilakukan oleh penyerang dengan menyisipkan kode JavaScript pada jenis input mereka sehingga kode tersebut dijalankan sebagai kode yang berfungsi pada browser lain sehingga perlu dilindungi dengan menggunakan escape HTML untuk kode AJAX/JavaScript yang tidak memiliki auto-escaping. Django sudah memiliki auto-escaping sehingga jika terjadi XSS pada template Django sudah langsung terlindungi.
- AI Disclosure: Untuk tugas 5 ini, saya sangat dibantu dengan penggunaan AI Claude dalam proses debugging terkait mengapa kode saya tidak bekerja ketika saya mengimplementasikan penyesuaian pada kode testimonial dari kode projects yang berasal dari tutorial. Saya memberikan Claude kode yang sudah saya tulis untuk point out kira-kira kesalahan apa yang menyebabkan hasilnya tidak seperti semestinya (dengan melindungi data pribadi saya seperti menghapus kode yang mengandung nama saya) dan ada bagian kode terkait penerapan event listener dsb pada fitur edit yang dibantu generate oleh Claude.
  
Log Chat: [Claude](https://claude.ai/share/099c2f4b-117a-4aea-9a47-b52c1f18e5ff)
