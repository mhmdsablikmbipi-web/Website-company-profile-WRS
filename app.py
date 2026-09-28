"""
Website PT. Wahana Rezeki Sempurna (WRS)

CARA MENGEDIT
  1. Teks, layanan, event, kontak  -> ubah di BAGIAN 1 (KONTEN) di bawah ini.
  2. Foto                          -> taruh file di folder  images/  lalu tulis
                                      nama filenya, contoh: "foto": "kantor.jpg"
                                      (boleh juga link https://... ).
                                      Kolom "foto" boleh dikosongkan ("").
  3. Warna, font, ukuran           -> ubah di file style.css
  4. Bagian BAGIAN 2 ke bawah adalah mesin penyusun halaman, tidak perlu diubah.

Susunan file:
  app.py  style.css  logo.png  config.toml  requirements.txt  images/
"""

import base64
import mimetypes
from html import escape
from pathlib import Path

import streamlit as st

BASE = Path(__file__).resolve().parent
FOLDER_FOTO = BASE / "images"

# =============================================================================
# BAGIAN 1 - KONTEN  (edit di sini)
# =============================================================================

PERUSAHAAN = {
    "nama": "PT. Wahana Rezeki Sempurna",
    "logo": "logo.png",  # file ada di folder yang sama dengan app.py
}

# Menu navigasi: (teks menu, id seksi). Menu "Galeri" otomatis hilang kalau GALERI kosong.
MENU = [
    ("Tentang", "tentang"),
    ("Layanan", "layanan"),
    ("Event", "event"),
    ("Galeri", "galeri"),
    ("Prinsip", "prinsip"),
    ("Kontak", "kontak"),
]

# Bagian paling atas. Tombol = (teks, tujuan). Tujuan diawali # untuk pindah ke seksi.
HERO = {
    "judul": "Mau jualan di mal? Kami bantu usaha Anda naik kelas.",
    "deskripsi": (
        "PT. Wahana Rezeki Sempurna adalah Exhibition Organizer yang sejak 2003 "
        "menyelenggarakan pameran, bazaar, dan penyewaan space di berbagai mal "
        "dan pusat perbelanjaan."
    ),
    "tombol_utama": ("Lihat layanan", "#layanan"),
    "tombol_kedua": ("Konsultasi gratis", "#kontak"),
}

TENTANG = {
    "judul": "Sejak 2003, kami membantu bisnis tampil dan tumbuh di mal.",
    "paragraf": [
        "PT. Wahana Rezeki Sempurna adalah perusahaan profesional di bidang Exhibition "
        "Organizer, penyelenggara event pameran dan promosi. Berdiri sejak 2003, kami "
        "telah membantu puluhan ribu bisnis dan pameran di berbagai industri: otomotif, "
        "properti, teknologi, furniture, perbankan, travel, fashion, F&B, hingga aksesori.",
        "Kami ingin menjadi Exhibition & Promotion Organizer profesional berskala nasional "
        "hingga internasional, yang melayani beragam kebutuhan klien dengan integritas dan "
        "inovasi, serta menghadirkan ide dan konsep kreatif untuk setiap event.",
    ],
    "foto": "",  # contoh: "kantor.jpg"  (tampil di bawah paragraf)
}

LAYANAN_JUDUL = "Layanan kami"
# Tambah layanan baru = salin satu blok { ... }, lalu tempel di bawahnya.
LAYANAN = [
    {
        "judul": "Pameran di mal",
        "isi": "Kami merancang dan menyelenggarakan pameran di mal dan pusat perbelanjaan mitra di berbagai kota, dari otomotif hingga fashion dan furniture.",
        "foto": "",  # contoh: "pameran.jpg"
    },
    {
        "judul": "Bazaar dan event promosi",
        "isi": "Bazaar dan event promosi yang mempertemukan produk Anda langsung dengan pengunjung mal dan membantu memperkuat pemasaran.",
        "foto": "",
    },
    {
        "judul": "Sewa space dan counter",
        "isi": "Sewa lahan, counter, dan kios untuk berjualan di mal. Pilih tanggal dan lokasi di mal mitra WRS.",
        "foto": "",
    },
    {
        "judul": "Konsultasi strategi gratis",
        "isi": "Baru pertama kali ikut pameran di mal? Tim kami siap membantu menyusun strategi terbaik tanpa biaya.",
        "foto": "",
    },
]

EVENT_JUDUL = "Event & slot terbaru"
EVENT_DESKRIPSI = "Pantau jadwal pameran dan slot yang masih tersedia di mal mitra WRS."
# status: "tersedia" (bisa booking) atau "penuh" (daftar tunggu)
# Ganti isi placeholder di bawah dengan jadwal asli dari wrs-eo.com.
EVENTS = [
    {
        "tanggal": "[Tanggal event]",
        "nama": "[Nama event]",
        "mal": "[Nama mal]",
        "kota": "[Kota]",
        "kategori": "Otomotif",
        "status": "tersedia",
        "foto": "",  # contoh: "event-otomotif.jpg"
    },
    {
        "tanggal": "[Tanggal event]",
        "nama": "[Nama event]",
        "mal": "[Nama mal]",
        "kota": "[Kota]",
        "kategori": "Fashion",
        "status": "tersedia",
        "foto": "",
    },
    {
        "tanggal": "[Tanggal event]",
        "nama": "[Nama event]",
        "mal": "[Nama mal]",
        "kota": "[Kota]",
        "kategori": "Furniture",
        "status": "penuh",
        "foto": "",
    },
]
AREA = [
    "Jabodetabek", "Palembang", "Surabaya", "Kupang", "Lampung", "Pekanbaru",
    "Semarang", "Pontianak", "Jambi", "Malang", "Sidoarjo", "Manado", "Pangkal Pinang",
]

# Galeri foto. Kosongkan ([]) kalau belum ada foto; seksi dan menunya otomatis hilang.
GALERI_JUDUL = "Galeri"
GALERI = [
    # {"foto": "pameran-1.jpg", "keterangan": "Pameran otomotif di Margo City"},
    # {"foto": "pameran-2.jpg", "keterangan": "Bazaar fashion"},
]

PRINSIP = {
    "judul": "Jabat tangan adalah cara kami memulai setiap kerja sama.",
    "poin": [
        {"judul": "Analisa yang matang", "isi": "Setiap event kami mulai dengan analisa yang detail dan menyeluruh."},
        {"judul": "Eksekusi yang rapi", "isi": "Tim profesional kami menjalankan setiap proyek dengan persiapan yang matang."},
        {"judul": "Biaya jadi investasi", "isi": "Kami berupaya agar setiap biaya yang Anda keluarkan menjadi investasi yang menguntungkan."},
    ],
}

KONTAK = {
    "judul": "Hubungi kami",
    "alamat": [
        "Graha WRS, Ruko Season City Blok A No. 33-35,",
        "Jl. Jembatan Besi, Latumenten, Jakarta Barat 11320",
    ],
    "telepon": ["(021) 2907 1225", "Call center: 0816 1415 671"],
    "email": "[Alamat email]",
    "instagram": "@wrs.eo",
}

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
def _data_uri(path_str: str) -> str:
    path = Path(path_str)
    if not path.exists():
        print(f"[foto] file tidak ditemukan: {path}")
        return ""
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def foto_uri(nama: str) -> str:
    """Ubah nama file di folder images/ (atau link https) menjadi alamat gambar untuk HTML."""
    if not nama:
        return ""
    if nama.startswith(("http://", "https://", "data:")):
        return nama
    return _data_uri(str(FOLDER_FOTO / nama))


def gambar(nama: str, kelas: str, alt: str = "") -> str:
    """Tag <img>; kosong kalau foto tidak diisi atau file tidak ada."""
    uri = foto_uri(nama)
    if not uri:
        return ""
    return f'<img class="{kelas}" src="{uri}" alt="{escape(alt)}" loading="lazy">'


def tombol(teks: str, tujuan: str, gaya: str) -> str:
    return f'<a class="btn {gaya}" href="{escape(tujuan)}">{escape(teks)}</a>'


def rapatkan(html: str) -> str:
    """Hapus baris kosong dan spasi depan agar Markdown tidak merusak HTML."""
    return "\n".join(b.strip() for b in html.splitlines() if b.strip())


def tampilkan(html: str) -> None:
    st.markdown(rapatkan(html), unsafe_allow_html=True)


LOGO_URI = _data_uri(str(LOGO))


# =============================================================================
# BAGIAN 3 - PENYUSUN SEKSI  (tidak perlu diubah)
# =============================================================================

def bagian_nav() -> str:
    tampil_galeri = any(g.get("foto") and foto_uri(g["foto"]) for g in GALERI)
    tautan = "".join(
        f'<a href="#{anchor}">{escape(teks)}</a>'
        for teks, anchor in MENU
        if anchor != "galeri" or tampil_galeri
    )
    nama = escape(PERUSAHAAN["nama"])
    return (
        f'<div class="nav"><div class="brand"><img src="{LOGO_URI}" alt="Logo WRS">{nama}</div>'
        f'<div class="links">{tautan}</div></div>'
    )


def bagian_hero() -> str:
    return f"""
<div class="hero"><div>
<h1>{escape(HERO['judul'])}</h1>
<p>{escape(HERO['deskripsi'])}</p>
{tombol(*HERO['tombol_utama'], 'gold')}{tombol(*HERO['tombol_kedua'], 'line')}
</div><img class="logo" src="{LOGO_URI}" alt="Logo {escape(PERUSAHAAN['nama'])}"></div>
"""


def bagian_tentang() -> str:
    paragraf = "".join(f"<p>{escape(p)}</p>" for p in TENTANG["paragraf"])
    foto = gambar(TENTANG["foto"], "foto-about", TENTANG["judul"])
    return f"""
<div class="sec" id="tentang"><div class="inner two">
<h2>{escape(TENTANG['judul'])}</h2>
<div>{paragraf}{foto}</div>
</div></div>
"""


def baris_layanan(item: dict) -> str:
    foto = gambar(item.get("foto", ""), "thumb", item["judul"])
    return (
        '<div class="svc"><span class="dot"></span>'
        f'<div><h3>{escape(item["judul"])}</h3><p>{escape(item["isi"])}</p></div>'
        f"{foto}</div>"
    )


def bagian_layanan() -> str:
    baris = "".join(baris_layanan(i) for i in LAYANAN)
    return f"""
<div class="sec" id="layanan" style="padding-top:0"><div class="inner">
<h2 style="margin-bottom:36px">{escape(LAYANAN_JUDUL)}</h2>
{baris}
</div></div>
"""


def baris_event(e: dict) -> str:
    tersedia = e.get("status", "tersedia") == "tersedia"
    status = (
        '<span class="stat ok">Slot tersedia</span>'
        if tersedia
        else '<span class="stat full">Slot penuh</span>'
    )
    aksi = tombol("Booking slot", "#kontak", "gold") if tersedia else tombol("Daftar tunggu", "#kontak", "dark")
    foto = gambar(e.get("foto", ""), "thumb", e["nama"])
    return (
        f'<div class="evt"><div class="tgl">{escape(e["tanggal"])}</div>'
        f'<div class="evt-main">{foto}<div>'
        f'<h3>{escape(e["nama"])}<span class="tag">{escape(e["kategori"])}</span></h3>'
        f'<p class="meta">{escape(e["mal"])} &middot; {escape(e["kota"])}</p></div></div>'
        f'<div class="aksi">{status}{aksi}</div></div>'
    )


def bagian_event() -> str:
    baris = "".join(baris_event(e) for e in EVENTS) or (
        '<div class="kosong">Jadwal event terbaru segera hadir. Hubungi kami untuk info slot.</div>'
    )
    area = escape(", ".join(AREA))
    return f"""
<div class="sec" id="event" style="padding-top:0"><div class="inner">
<h2 style="margin-bottom:12px">{escape(EVENT_JUDUL)}</h2>
<p style="margin-bottom:32px">{escape(EVENT_DESKRIPSI)}</p>
{baris}
<p class="area"><b>Area jangkauan:</b> {area}.</p>
</div></div>
"""


def bagian_galeri() -> str:
    item = []
    for g in GALERI:
        img = gambar(g.get("foto", ""), "", g.get("keterangan", ""))
        if not img:
            continue
        img = img.replace(' class=""', "")
        cap = g.get("keterangan", "")
        cap_html = f"<figcaption>{escape(cap)}</figcaption>" if cap else ""
        item.append(f'<figure class="gal">{img}{cap_html}</figure>')
    if not item:
        return ""
    return f"""
<div class="sec" id="galeri" style="padding-top:0"><div class="inner">
<h2 style="margin-bottom:36px">{escape(GALERI_JUDUL)}</h2>
<div class="galeri">{''.join(item)}</div>
</div></div>
"""


def bagian_prinsip() -> str:
    poin = "".join(
        f'<div class="val"><h3>{escape(p["judul"])}</h3><p>{escape(p["isi"])}</p></div>'
        for p in PRINSIP["poin"]
    )
    return f"""
<div class="sec band" id="prinsip"><div class="inner">
<h2>{escape(PRINSIP['judul'])}</h2>
<div class="vals">{poin}</div>
</div></div>
"""


def bagian_kontak_info() -> str:
    alamat = "<br>".join(escape(b) for b in KONTAK["alamat"])
    telepon = "<br>".join(escape(b) for b in KONTAK["telepon"])
    return f"""
<h2>{escape(KONTAK['judul'])}</h2>
<p class="ci"><b>Alamat</b><br>{alamat}</p>
<p class="ci"><b>Telepon</b><br>{telepon}</p>
<p class="ci"><b>Email</b><br>{escape(KONTAK['email'])}</p>
<p class="ci"><b>Instagram</b><br>{escape(KONTAK['instagram'])}</p>
"""


# =============================================================================
# BAGIAN 4 - MERAKIT HALAMAN  (tidak perlu diubah)
# =============================================================================

CSS = (BASE / "style.css").read_text(encoding="utf-8")
tampilkan(f"<style>{CSS}</style>")

tampilkan(
    bagian_nav()
    + bagian_hero()
    + bagian_tentang()
    + bagian_layanan()
    + bagian_event()
    + bagian_galeri()
    + bagian_prinsip()
)

# Kontak memakai widget Streamlit (form), jadi dirakit terpisah.
with st.container(key="kontak"):
    st.markdown('<div id="kontak"></div>', unsafe_allow_html=True)
    kiri, kanan = st.columns([1, 1.2], gap="large")
    with kiri:
        tampilkan(bagian_kontak_info())
    with kanan:
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

tampilkan(f'<div class="foot">{escape(FOOTER)}</div>')
