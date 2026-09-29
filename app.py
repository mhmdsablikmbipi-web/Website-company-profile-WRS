"""
Website PT. Wahana Rezeki Sempurna (WRS) - 4 halaman
Home | Artikel Event | Lokasi Mal | Contact

CARA MENGEDIT
  1. Teks, artikel, daftar mal, kontak -> ubah di BAGIAN 1 (KONTEN).
  2. Foto -> taruh file di folder  images/  dengan nama persis seperti di
     konten (contoh "otomotif-1.jpg"). Foto yang belum ada tampil sebagai
     kotak putus-putus berisi nama file yang harus Anda siapkan.
  3. Warna, font, ukuran -> ubah di file style.css
  4. BAGIAN 2 ke bawah adalah mesin penyusun halaman, tidak perlu diubah.

Susunan file:
  app.py  style.css  logo.png  config.toml  requirements.txt  images/
"""

import base64
import mimetypes
from html import escape
from pathlib import Path
from urllib.parse import quote_plus

import streamlit as st
from streamlit.components.v1 import iframe

BASE = Path(__file__).resolve().parent
FOLDER_FOTO = BASE / "images"

# =============================================================================
# BAGIAN 1 - KONTEN  (edit di sini)
# =============================================================================

PERUSAHAAN = {"nama": "PT. Wahana Rezeki Sempurna", "logo": "logo.png"}

# Menu navbar: (teks menu, kode halaman)
MENU = [
    ("Home", "home"),
    ("Artikel Event", "event"),
    ("Lokasi Mal", "lokasi"),
    ("Contact", "kontak"),
]

# ------------------------------- HALAMAN HOME --------------------------------
HERO = {
    "judul": "Mau jualan di mal? Kami bantu usaha Anda naik kelas.",
    "deskripsi": (
        "PT. Wahana Rezeki Sempurna adalah Exhibition Organizer yang sejak 2003 "
        "menyelenggarakan pameran, bazaar, dan penyewaan space di berbagai mal "
        "dan pusat perbelanjaan."
    ),
    "tombol_utama": ("Lihat event kami", "?hal=event"),
    "tombol_kedua": ("Konsultasi gratis", "?hal=kontak"),
}

PROFIL = {
    "judul": "Profil perusahaan",
    "paragraf": [
        "PT. Wahana Rezeki Sempurna adalah perusahaan profesional di bidang Exhibition "
        "Organizer, penyelenggara event pameran dan promosi. Kami melayani berbagai "
        "industri: otomotif, properti, teknologi, furniture, perbankan, travel, fashion, "
        "F&B, hingga aksesori.",
    ],
    "foto": "profil.jpg",
}

PENDIRI = {
    "nama": "[Nama pendiri]",
    "jabatan": "[Jabatan, misalnya Pendiri & Direktur Utama]",
    "cerita": [
        "[Tulis profil singkat pendiri: latar belakang, alasan mendirikan WRS, dan pesan untuk klien.]",
    ],
    "foto": "pendiri.jpg",
}

VISI = "Menjadi Exhibition & Promotion Organizer profesional berskala nasional hingga internasional."
MISI = [
    "Melayani beragam kebutuhan klien dengan integritas.",
    "Menghadirkan ide dan konsep kreatif serta inovatif untuk setiap event.",
    "Menjalankan setiap proyek dengan analisa matang dan eksekusi yang rapi.",
    "Menjadikan setiap biaya yang klien keluarkan sebagai investasi yang menguntungkan.",
]

LATAR = {
    "judul": "Latar belakang perusahaan",
    "paragraf": [
        "WRS berdiri sejak 2003 dan sejak itu telah membantu puluhan ribu bisnis dan pameran "
        "tampil di mal dan pusat perbelanjaan, dari Jabodetabek hingga kota-kota besar lain "
        "di Indonesia.",
        "[Tambahkan cerita awal berdirinya WRS, perkembangan perusahaan, dan pencapaian penting.]",
    ],
}

GALERI_JUDUL = "Galeri kegiatan"
# (nama file di folder images/, keterangan). Tambah atau hapus baris sesuka Anda.
GALERI_HOME = [
    ("home-1.jpg", "Pameran di mal"),
    ("home-2.jpg", "Bazaar dan event promosi"),
    ("home-3.jpg", "Tim WRS di lokasi"),
    ("home-4.jpg", "Penataan area pameran"),
    ("home-5.jpg", "Kerja sama dengan mal mitra"),
    ("home-6.jpg", "Pengunjung event"),
]

# ---------------------------- HALAMAN ARTIKEL EVENT --------------------------
EVENT_JUDUL = "Artikel event WRS"
EVENT_DESKRIPSI = "Jenis event yang rutin kami selenggarakan di mal mitra, lengkap dengan dokumentasinya."
# "foto": 3 file. Foto pertama tampil besar, dua lainnya di sampingnya.
EVENT_TIPE = [
    {
        "judul": "Pameran otomotif",
        "lead": "Tempat merek, dealer, dan calon pembeli bertemu langsung di area publik mal.",
        "isi": [
            "Pameran otomotif adalah salah satu event andalan WRS. Berbagai merek dan dealer "
            "menampilkan unit terbaru di area mal, sehingga pengunjung bisa melihat, "
            "membandingkan, dan bertanya langsung kepada tenaga penjual.",
            "Bagi peserta, format ini efektif untuk menjaring calon pembeli dan memperkuat merek. "
            "Tim WRS membantu penataan area, alur pengunjung, dan promosi event.",
        ],
        "foto": ["otomotif-1.jpg", "otomotif-2.jpg", "otomotif-3.jpg"],
    },
    {
        "judul": "Pameran multi produk",
        "lead": "Satu event, banyak kategori usaha dalam satu area pameran.",
        "isi": [
            "Pameran multi produk menghadirkan beragam bisnis sekaligus, seperti perbankan, "
            "properti, teknologi, travel, dan kebutuhan rumah tangga. Pengunjung mal bisa "
            "menjelajahi banyak penawaran dalam satu kunjungan.",
            "Format ini cocok untuk bisnis yang ingin tampil di mal tanpa menyelenggarakan "
            "acara sendiri. Kami menyiapkan tempat, penataan, dan promosinya.",
        ],
        "foto": ["multiproduk-1.jpg", "multiproduk-2.jpg", "multiproduk-3.jpg"],
    },
    {
        "judul": "Pameran furniture",
        "lead": "Perlengkapan rumah dan interior, dipamerkan langsung kepada calon pembeli.",
        "isi": [
            "Pameran furniture mempertemukan produsen dan penjual perabot dengan pengunjung "
            "yang sedang mencari perlengkapan rumah. Produk bisa dilihat, disentuh, dan "
            "dibandingkan secara langsung.",
            "WRS mengatur tata letak area pameran agar setiap produk mudah dilihat dan "
            "pengunjung nyaman berkeliling.",
        ],
        "foto": ["furniture-1.jpg", "furniture-2.jpg", "furniture-3.jpg"],
    },
    {
        "judul": "Bazaar",
        "lead": "Ruang berjualan yang terjangkau untuk fashion, F&B, aksesori, dan usaha kecil.",
        "isi": [
            "Bazaar menyediakan counter dan kios di mal bagi pelaku usaha yang ingin "
            "bertemu pembeli secara langsung. Kategori yang biasa hadir antara lain fashion, "
            "F&B, dan aksesori.",
            "Baru pertama kali berjualan di mal? Tim kami siap membantu memilih lokasi, tanggal, "
            "dan ukuran space yang sesuai.",
        ],
        "foto": ["bazaar-1.jpg", "bazaar-2.jpg", "bazaar-3.jpg"],
    },
]

# ---------------------------- HALAMAN LOKASI MAL -----------------------------
# Susunan: (wilayah, [(label kelompok, kata tambahan untuk pencarian Google Maps, [daftar mal])])
# Mal boleh ditulis "Nama" saja, atau ("Nama tampilan", "kata pencarian Google Maps lengkap")
# kalau hasil pencarian Google Maps kurang tepat.
MAL = [
    ("Jabodetabek", [
        ("Jakarta Barat", "Jakarta Barat", [
            "Season City", "Mall Taman Palem", "Puri Indah Mall", "Lippo Puri Mall",
            "Neo Soho", "Central Park"]),
        ("Jakarta Timur", "Jakarta Timur", [
            ("Living World Kota Wisata Cibubur", "Living World Kota Wisata Cibubur"),
            "Aeon Mall JGC Cakung", "Pusat Grosir Cililitan (PGC)", "TSM Cibubur",
            "City Plaza Jatinegara", "Basura City Mall", "Lippo Kramat Jati",
            "Tamini Square", "Cibubur Junction", "Cijantung Mall"]),
        ("Jakarta Pusat", "Jakarta Pusat", [
            "Transmart Cempaka Putih", "ITC Cempaka Mas", "Pasar Baru Jakarta",
            "Senayan City", "Senayan Park", "Gajah Mada Plaza", "Kenari Plaza",
            "Thamrin City"]),
        ("Jakarta Utara", "Jakarta Utara", [
            "Koja Trade Mall", "Baywalk Mall", "Pluit Village", "Mall Artha Gading",
            "Central Market PIK"]),
        ("Jakarta Selatan", "Jakarta Selatan", [
            "Kemang Village", "Aeon Mall Tanjung Barat", "Mall Ambassador",
            "Blok M Square", "Pondok Indah Mall", "Kalibata City", "Kalibata Plaza",
            "Poins Square", "Kota Kasablanka", "Cilandak Town Square", "Kuningan City"]),
        ("Bekasi, Cikarang, Karawang", "", [
            "Revo Mall Bekasi", "Bekasi Trade Center", "CyberPark Bekasi",
            "Grand Metropolitan Mall Bekasi", "Sentra Grosir Cikarang (SGC)",
            "Aeon Delta Mas Cikarang", "Living Plaza Jababeka", "Karawang Central Plaza"]),
        ("Tangerang", "Tangerang", [
            "Aeon Mall BSD", "Bintaro Plaza", "ITC BSD", "Tang City", "Eastvara BSD",
            "Mall Ciputra Raya Tangerang", "The Barn BSD", "Supermall Karawaci",
            "Bintaro Xchange", "Greenlake Lavela Grand Lucky", "Living World Alam Sutera"]),
        ("Depok", "Depok", [
            "The Park Sawangan", "Margo City Depok", "Depok Town Square", "ITC Depok"]),
        ("Bogor", "Bogor", [
            "Aeon Mall Sentul City", "Botani Square Bogor", "Cibinong City Mall",
            "Pusat Grosir Bogor (PGB)"]),
        ("Banten", "Serang", ["Mall of Serang"]),
    ]),
    ("Luar Jabodetabek / luar kota", [
        ("Bandung / Jawa Barat", "Bandung", [
            "Botanica Bandung", "Summarecon Mall Bandung", "Paskal 23 Mall Bandung",
            "TSM Bandung", "Paris Van Java"]),
        ("Palembang", "", [
            "Palembang Square", "Palembang Icon", "Palembang Indah Mall",
            "Palembang Trade Center", "Citimall Lahat", "Lippo Plaza Lubuk Linggau",
            "Transmart Palembang"]),
        ("Sulawesi", "", ["TSM Makassar", "Transmart Kawanua Manado"]),
        ("Sumatera", "", [
            "Central Plaza Lampung", "Transmart Padang", "Transmart Pangkal Pinang",
            "Transmart Lampung", "Sunplaza Medan", "Pekanbaru Exchange",
            "Transmart Pekanbaru", "Living World Pekanbaru", "SKA Mall Pekanbaru",
            ("Sukaramai Trade Center", "Sukaramai Trade Center Pekanbaru"),
            "Delipark Mall Medan", "Centre Point Mall Medan"]),
        ("Surabaya / Jawa Timur", "", [
            "Kaza Mall Surabaya", "Pakuwon City Mall Surabaya", "Unimas District Sidoarjo",
            "Kediri Town Square", ("Delta Plaza", "Delta Plaza Surabaya"),
            "Trans Icon Surabaya", "Suncity Madiun", "Lippo Sidoarjo",
            ("Cito", "Cito City of Tomorrow Surabaya"), "Plaza Marina Surabaya",
            "Transmart Rungkut Surabaya", "Suncity Mall Sidoarjo", "Galaxy Mall Surabaya"]),
    ]),
]

# ------------------------------- HALAMAN CONTACT -----------------------------
KONTAK = {
    "judul": "Hubungi kami",
    "deskripsi": "Tanyakan slot pameran, sewa space, atau konsultasi strategi. Kami balas secepatnya.",
    "alamat": [
        "Graha WRS, Ruko Season City Blok A No. 33-35,",
        "Jl. Jembatan Besi, Latumenten, Jakarta Barat 11320",
    ],
    "telepon": ["(021) 2907 1225", "Call center: 0816 1415 671"],
    "email": "Wrsempurna.eo@gmail.com",
}

# Sosial media: (nama, teks yang tampil, link)
SOSMED = [
    ("Website", "www.wrs-eo.com", "https://www.wrs-eo.com"),
    ("Instagram", "@eo.wrs.id", "https://www.instagram.com/eo.wrs.id"),
    ("TikTok", "@wrs.eo", "https://www.tiktok.com/@wrs.eo"),
]

# WhatsApp: isi tanpa tanda + dan tanpa 0 di depan. Contoh: 6281614156710
WA_NOMOR = "628XXXXXXXXXX"
WA_PESAN = "Halo WRS, saya ingin bertanya tentang pameran atau sewa space di mal."

# Google Maps kantor pusat. KANTOR_QUERY dipakai untuk peta dan tombol.
# Kalau pin kurang pas, buka lokasi di Google Maps > Bagikan > salin link, lalu tempel di KANTOR_LINK.
KANTOR_QUERY = "Graha WRS, Ruko Season City Blok A No. 33-35, Jl. Jembatan Besi, Latumenten, Jakarta Barat 11320"
KANTOR_LINK = ""

FOOTER = "© 2026 PT. Wahana Rezeki Sempurna. Semua hak dilindungi."


# =============================================================================
# BAGIAN 2 - PENGATURAN HALAMAN & FOTO  (tidak perlu diubah)
# =============================================================================

LOGO = BASE / PERUSAHAAN["logo"]

st.set_page_config(
    page_title=PERUSAHAAN["nama"],
    page_icon=str(LOGO),
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_data(show_spinner=False)
def _baca(path_str: str, mtime: float) -> str:
    path = Path(path_str)
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def _data_uri(path_str: str) -> str:
    # mtime ikut jadi kunci cache: foto baru langsung tampil tanpa restart aplikasi.
    path = Path(path_str)
    return _baca(path_str, path.stat().st_mtime) if path.exists() else ""


def foto_uri(nama: str) -> str:
    if not nama:
        return ""
    if nama.startswith(("http://", "https://", "data:")):
        return nama
    return _data_uri(str(FOLDER_FOTO / nama))


def foto(nama: str, kelas: str, alt: str = "") -> str:
    """<img> kalau file ada; kalau belum ada, kotak penanda berisi nama file yang dibutuhkan."""
    if not nama:
        return ""
    uri = foto_uri(nama)
    if uri:
        return f'<img class="{kelas}" src="{uri}" alt="{escape(alt)}" loading="lazy">'
    return f'<div class="{kelas} slot"><span>Taruh foto di<br>images/{escape(nama)}</span></div>'


def tombol(teks: str, tujuan: str, gaya: str) -> str:
    buka = ' target="_self"' if tujuan.startswith("?") else ' target="_blank" rel="noopener"'
    return f'<a class="btn {gaya}" href="{escape(tujuan)}"{buka}>{escape(teks)}</a>'


def paragraf(daftar: list) -> str:
    return "".join(f"<p>{escape(p)}</p>" for p in daftar)


def rapatkan(html: str) -> str:
    """Hapus baris kosong dan spasi depan agar Markdown tidak merusak HTML."""
    return "\n".join(b.strip() for b in html.splitlines() if b.strip())


def tampilkan(html: str) -> None:
    st.markdown(rapatkan(html), unsafe_allow_html=True)


LOGO_URI = _data_uri(str(LOGO))
MAPS_URL = KANTOR_LINK or "https://www.google.com/maps/search/?api=1&query=" + quote_plus(KANTOR_QUERY)
MAPS_EMBED = "https://maps.google.com/maps?q=" + quote_plus(KANTOR_QUERY) + "&output=embed"
WA_URL = f"https://wa.me/{WA_NOMOR}?text={quote_plus(WA_PESAN)}"


# =============================================================================
# BAGIAN 3 - PENYUSUN HALAMAN  (tidak perlu diubah)
# =============================================================================

def bagian_nav(aktif: str) -> str:
    tautan = "".join(
        f'<a href="?hal={kode}" target="_self" class="{"on" if kode == aktif else ""}">{escape(teks)}</a>'
        for teks, kode in MENU
    )
    return (
        f'<div class="nav"><div class="brand"><img src="{LOGO_URI}" alt="Logo WRS">'
        f'<span>{escape(PERUSAHAAN["nama"])}</span></div><div class="links">{tautan}</div></div>'
    )


def kepala(judul: str, sub: str) -> None:
    tampilkan(
        f'<div class="phead"><div class="inner"><h1>{escape(judul)}</h1><p>{escape(sub)}</p></div></div>'
    )


# ------------------------------------ HOME -----------------------------------

def halaman_home() -> None:
    galeri = "".join(
        f'<figure class="gal">{foto(f, "gal-img", ket)}<figcaption>{escape(ket)}</figcaption></figure>'
        for f, ket in GALERI_HOME
    )
    misi = "".join(f"<li>{escape(m)}</li>" for m in MISI)
    tampilkan(f"""
<div class="hero"><div>
<h1>{escape(HERO['judul'])}</h1>
<p>{escape(HERO['deskripsi'])}</p>
{tombol(*HERO['tombol_utama'], 'gold')}{tombol(*HERO['tombol_kedua'], 'line')}
</div><img class="logo" src="{LOGO_URI}" alt="Logo {escape(PERUSAHAAN['nama'])}"></div>

<div class="sec"><div class="inner two">
<h2>{escape(PROFIL['judul'])}</h2>
<div>{paragraf(PROFIL['paragraf'])}{foto(PROFIL['foto'], 'foto-about', PROFIL['judul'])}</div>
</div></div>

<div class="sec" style="padding-top:0"><div class="inner pendiri">
{foto(PENDIRI['foto'], 'potret', PENDIRI['nama'])}
<div><h2>{escape(PENDIRI['nama'])}</h2>
<p class="jab">{escape(PENDIRI['jabatan'])}</p>{paragraf(PENDIRI['cerita'])}</div>
</div></div>

<div class="sec band"><div class="inner">
<h2>Visi dan misi kami</h2>
<p class="visi">{escape(VISI)}</p>
<ul class="misi">{misi}</ul>
</div></div>

<div class="sec"><div class="inner two">
<h2>{escape(LATAR['judul'])}</h2>
<div>{paragraf(LATAR['paragraf'])}</div>
</div></div>

<div class="sec" style="padding-top:0"><div class="inner">
<h2 style="margin-bottom:36px">{escape(GALERI_JUDUL)}</h2>
<div class="galeri">{galeri}</div>
</div></div>
""")


# ------------------------------------ EVENT ----------------------------------

def artikel_event(i: int, e: dict) -> str:
    kelas = "art rev" if i % 2 else "art"
    fotos = "".join(foto(f, "mo", e["judul"]) for f in e["foto"])
    return (
        f'<article class="{kelas}" id="{escape(e["judul"].lower().replace(" ", "-"))}">'
        f'<div class="art-teks"><h2>{escape(e["judul"])}</h2>'
        f'<p class="lead">{escape(e["lead"])}</p>{paragraf(e["isi"])}</div>'
        f'<div class="mosaic">{fotos}</div></article>'
    )


def halaman_event() -> None:
    kepala(EVENT_JUDUL, EVENT_DESKRIPSI)
    artikel = "".join(artikel_event(i, e) for i, e in enumerate(EVENT_TIPE))
    tampilkan(f'<div class="sec" style="padding-top:40px"><div class="inner">{artikel}</div></div>')


# ------------------------------------ LOKASI ---------------------------------

def daftar_mal(kata: str) -> str:
    hasil, no = [], 0
    for wilayah, grup in MAL:
        blok = []
        for label, kueri, daftar in grup:
            kartu = []
            for m in daftar:
                no += 1  # nomor tetap walau daftar difilter
                nama, q = m if isinstance(m, tuple) else (m, f"{m} {kueri}".strip())
                if kata and kata not in f"{nama} {label} {wilayah}".lower():
                    continue
                url = "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)
                kartu.append(
                    f'<a class="mal" href="{escape(url)}" target="_blank" rel="noopener">'
                    f'<span class="no">{no:02d}</span>{escape(nama)}</a>'
                )
            if kartu:
                blok.append(f'<h3 class="grp">{escape(label)}</h3><div class="malgrid">{"".join(kartu)}</div>')
        if blok:
            hasil.append(f'<h2 class="wil">{escape(wilayah)}</h2>' + "".join(blok))
    return "".join(hasil) or '<div class="kosong">Mal tidak ditemukan. Coba kata kunci lain.</div>'


def halaman_lokasi() -> None:
    total = sum(len(d) for _, grup in MAL for _, _, d in grup)
    kepala("Lokasi mal mitra WRS", f"{total} lokasi proyek WRS. Klik nama mal untuk membuka Google Maps.")
    with st.container(key="cari"):
        kata = st.text_input("Cari mal atau wilayah", placeholder="Contoh: Season City atau Tangerang")
    tampilkan(
        f'<div class="sec" style="padding-top:8px"><div class="inner">{daftar_mal(kata.strip().lower())}</div></div>'
    )


# ------------------------------------ KONTAK ---------------------------------

def info_kontak() -> str:
    alamat = "<br>".join(escape(b) for b in KONTAK["alamat"])
    telepon = "<br>".join(escape(b) for b in KONTAK["telepon"])
    sosmed = "<br>".join(
        f'{escape(n)}: <a href="{escape(u)}" target="_blank" rel="noopener">{escape(t)}</a>'
        for n, t, u in SOSMED
    )
    return f"""
<p class="ci"><b>Alamat kantor pusat</b><br>{alamat}</p>
<p class="ci"><b>Telepon</b><br>{telepon}</p>
<p class="ci"><b>Email</b><br>{escape(KONTAK['email'])}</p>
<p class="ci"><b>Sosial media</b><br>{sosmed}</p>
{tombol("Chat via WhatsApp", WA_URL, "wa")}
"""


def halaman_kontak() -> None:
    kepala(KONTAK["judul"], KONTAK["deskripsi"])
    with st.container(key="kontak"):
        kiri, kanan = st.columns([1, 1.2], gap="large")
        with kiri:
            tampilkan(info_kontak())
        with kanan:
            iframe(MAPS_EMBED, height=340)
            tampilkan(tombol("Buka di Google Maps", MAPS_URL, "gold"))
        tampilkan('<h2 style="margin-top:48px">Kirim pesan</h2>')
        with st.form("form_kontak", clear_on_submit=True):
            nama = st.text_input("Nama")
            email = st.text_input("Email")
            pesan = st.text_area("Pesan", height=120)
            kirim = st.form_submit_button("Kirim pesan")
        if kirim:
            if nama and email and pesan:
                # Hubungkan ke email/Google Sheets/database di sini.
                st.success("Pesan Anda sudah kami terima.")
            else:
                st.error("Lengkapi nama, email, dan pesan sebelum mengirim.")


# =============================================================================
# BAGIAN 4 - MERAKIT HALAMAN  (tidak perlu diubah)
# =============================================================================

HALAMAN = {
    "home": halaman_home,
    "event": halaman_event,
    "lokasi": halaman_lokasi,
    "kontak": halaman_kontak,
}

aktif = st.query_params.get("hal", "home")
if aktif not in HALAMAN:
    aktif = "home"

CSS = (BASE / "style.css").read_text(encoding="utf-8")
tampilkan(f"<style>{CSS}</style>")
tampilkan(bagian_nav(aktif))
HALAMAN[aktif]()
tampilkan(f'<div class="foot">{escape(FOOTER)}</div>')
