import base64
from html import escape
from pathlib import Path

import streamlit as st

BASE = Path(__file__).parent
LOGO = BASE / "logo.png"

st.set_page_config(
    page_title="PT. Wahana Rezeki Sempurna",
    page_icon=str(LOGO),
    layout="wide",
    initial_sidebar_state="collapsed",
)

logo_uri = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()

# ---------------------------------------------------------------- PALET
# Diambil dari logo WRS:
#   espresso #1B1108  latar gelap di dalam lingkaran logo
#   maroon   #5C1010  cincin luar logo
#   bronze   #8C5A14  bayangan huruf emas
#   gold     #D9982B  emas utama huruf WRS
#   gold-lt  #F6D98A  kilau emas
#   amber    #E8901E  warna latar logo
#   ivory    #FFF7E3  cincin putih logo
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Instrument+Sans:wght@400;500;600&display=swap');
:root{
  --espresso:#1B1108; --maroon:#5C1010; --bronze:#8C5A14;
  --gold:#D9982B; --gold-lt:#F6D98A; --amber:#E8901E; --ivory:#FFF7E3;
}
html{scroll-behavior:smooth}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"]{display:none!important}
.stApp{background:var(--ivory);color:var(--espresso);font-family:'Instrument Sans',sans-serif}
.stApp .block-container{padding:0!important;max-width:100%!important}
.stApp .block-container > [data-testid="stVerticalBlock"]{gap:0}
.stApp [data-testid="stElementContainer"]{margin:0}
.stApp h1,.stApp h2,.stApp h3{font-family:'Fraunces',serif;letter-spacing:-.01em;padding:0}
.stApp a:focus-visible,.stApp button:focus-visible{outline:3px solid var(--gold-lt);outline-offset:3px}

/* navigasi */
.stApp .nav{position:fixed;top:0;left:0;right:0;z-index:999;display:flex;justify-content:space-between;
  align-items:center;padding:10px clamp(16px,5vw,64px);background:rgba(27,17,8,.95);
  border-bottom:1px solid rgba(217,152,43,.4)}
.stApp .nav .brand{display:flex;align-items:center;gap:12px;color:var(--ivory);
  font-family:'Fraunces',serif;font-weight:800;font-size:1.05rem}
.stApp .nav img{height:44px;width:44px}
.stApp .nav .links a{color:var(--gold-lt);text-decoration:none;margin-left:24px;font-size:.95rem;font-weight:500}
.stApp .nav .links a:hover{color:#fff}

/* hero */
.stApp .hero{display:grid;grid-template-columns:1.25fr 1fr;gap:48px;align-items:center;
  padding:150px clamp(20px,6vw,96px) 100px;
  background:radial-gradient(circle at 78% 45%,#4b2a0b 0%,var(--espresso) 62%)}
.stApp .hero h1{margin:0 0 22px;font-weight:800;font-size:clamp(2.4rem,5.4vw,4.4rem);line-height:1.05;
  background:linear-gradient(180deg,#FFF1BF 0%,#E3A537 52%,#9A6414 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.stApp .hero p{color:#EBD9B4;font-size:1.1rem;line-height:1.65;max-width:34em;margin:0}
.stApp .hero .logo{width:min(100%,400px);justify-self:center;border-radius:50%;
  box-shadow:0 0 0 8px rgba(246,217,138,.12),0 0 100px rgba(232,144,30,.35)}
.stApp .btn{display:inline-block;margin:26px 12px 0 0;padding:13px 28px;border-radius:999px;
  font-weight:600;text-decoration:none;transition:transform .15s}
.stApp .btn:hover{transform:translateY(-2px)}
.stApp .btn.gold{background:linear-gradient(180deg,var(--gold-lt),var(--gold));color:var(--espresso)}
.stApp .btn.line{border:1.5px solid var(--gold-lt);color:var(--gold-lt)}

/* seksi umum */
.stApp .sec{padding:92px clamp(20px,6vw,96px);scroll-margin-top:64px}
.stApp .inner{max-width:1080px;margin:0 auto}
.stApp .sec h2{margin:0;font-weight:800;font-size:clamp(1.8rem,3.4vw,2.6rem);line-height:1.15}
.stApp .sec p{line-height:1.7;font-size:1.05rem;margin:0 0 14px;max-width:38em}
.stApp .two{display:grid;grid-template-columns:1fr 1.5fr;gap:56px}

/* layanan: baris berpemisah, bukan kartu */
.stApp .svc{display:grid;grid-template-columns:auto 1fr;gap:22px;padding:26px 0;
  border-top:1px solid rgba(140,90,20,.4)}
.stApp .svc:last-child{border-bottom:1px solid rgba(140,90,20,.4)}
.stApp .dot{width:16px;height:16px;margin-top:9px;border-radius:50%;
  background:linear-gradient(180deg,var(--gold-lt),var(--gold));box-shadow:0 0 0 3px rgba(140,90,20,.2)}
.stApp .svc h3{margin:0 0 6px;font-size:1.35rem;font-weight:600}
.stApp .svc p{margin:0}

/* event: baris berpemisah, sama seperti layanan */
.stApp .evt{display:grid;grid-template-columns:170px 1fr auto;gap:24px;align-items:center;padding:24px 0;
  border-top:1px solid rgba(140,90,20,.4)}
.stApp .evt:last-of-type{border-bottom:1px solid rgba(140,90,20,.4)}
.stApp .evt .tgl{font-family:'Fraunces',serif;font-weight:600;font-size:1.15rem;line-height:1.3;color:var(--maroon)}
.stApp .evt h3{margin:0 0 4px;font-size:1.25rem;font-weight:600}
.stApp .evt .meta{margin:0;font-size:.95rem;line-height:1.5;color:#5b4526}
.stApp .evt .tag{display:inline-block;margin-left:8px;padding:2px 10px;border-radius:999px;
  background:var(--espresso);color:var(--gold-lt);font-size:.75rem;font-weight:600;vertical-align:middle}
.stApp .evt .aksi{text-align:right}
.stApp .evt .stat{display:block;margin-bottom:8px;font-size:.85rem;font-weight:600}
.stApp .evt .stat.ok{color:var(--bronze)}
.stApp .evt .stat.full{color:#8a7a5a}
.stApp .evt .btn{margin:0;padding:9px 20px;font-size:.9rem}
.stApp .btn.dark{border:1.5px solid var(--espresso);color:var(--espresso)}
.stApp .area{margin-top:28px;font-size:.95rem}
.stApp .kosong{padding:26px 0;border-top:1px solid rgba(140,90,20,.4);border-bottom:1px solid rgba(140,90,20,.4)}

/* pita nilai (warna latar logo) */
.stApp .band{background:var(--amber);color:var(--espresso)}
.stApp .band h2{max-width:14em;margin-bottom:44px}
.stApp .vals{display:grid;grid-template-columns:repeat(3,1fr)}
.stApp .val{padding:0 28px;border-left:2px solid var(--espresso)}
.stApp .val:first-child{padding-left:0;border-left:0}
.stApp .val h3{margin:0 0 8px;font-size:1.3rem;font-weight:600}
.stApp .val p{margin:0;font-size:1rem}

/* kontak */
.stApp .st-key-kontak{background:var(--maroon);padding:92px clamp(20px,6vw,96px);scroll-margin-top:64px}
.stApp .st-key-kontak,.stApp .st-key-kontak p,.stApp .st-key-kontak label,.stApp .st-key-kontak h2{color:var(--ivory)}
.stApp .st-key-kontak h2{font-weight:800;font-size:clamp(1.8rem,3.4vw,2.6rem);margin:0 0 18px}
.stApp .st-key-kontak .ci{margin:0 0 16px;line-height:1.6}
.stApp .st-key-kontak .ci b{color:var(--gold-lt)}
.stApp .st-key-kontak [data-testid="stForm"]{border:1px solid rgba(246,217,138,.4);border-radius:16px;padding:24px}
.stApp .st-key-kontak button{background:linear-gradient(180deg,var(--gold-lt),var(--gold));border:0;font-weight:600}
.stApp .st-key-kontak button p{color:var(--espresso)}

.stApp .foot{background:var(--espresso);color:#CDB98F;text-align:center;padding:26px 16px;font-size:.9rem}

@media (max-width:820px){
  .stApp .nav .links{display:none}
  .stApp .hero,.stApp .two,.stApp .vals{grid-template-columns:1fr}
  .stApp .hero{padding-top:120px}
  .stApp .hero .logo{order:-1;width:220px}
  .stApp .val{padding:18px 0 0;margin-top:18px;border-left:0;border-top:2px solid var(--espresso)}
  .stApp .val:first-child{border-top:0;margin-top:0;padding-top:0}
  .stApp .evt{grid-template-columns:1fr;gap:10px}
  .stApp .evt .aksi{text-align:left}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.stApp .btn{transition:none}}
</style>
"""

NAV = f"""<div class="nav"><div class="brand"><img src="{logo_uri}" alt="Logo WRS">PT. Wahana Rezeki Sempurna</div>
<div class="links"><a href="#tentang">Tentang</a><a href="#layanan">Layanan</a><a href="#event">Event</a><a href="#prinsip">Prinsip</a><a href="#kontak">Kontak</a></div></div>"""

HERO = f"""<div class="hero"><div>
<h1>Mau jualan di mal? Kami bantu usaha Anda naik kelas.</h1>
<p>PT. Wahana Rezeki Sempurna adalah Exhibition Organizer yang sejak 2003 menyelenggarakan pameran, bazaar, dan penyewaan space di berbagai mal dan pusat perbelanjaan.</p>
<a class="btn gold" href="#layanan">Lihat layanan</a><a class="btn line" href="#kontak">Konsultasi gratis</a>
</div><img class="logo" src="{logo_uri}" alt="Logo PT. Wahana Rezeki Sempurna"></div>"""

ABOUT = """<div class="sec" id="tentang"><div class="inner two">
<h2>Sejak 2003, kami membantu bisnis tampil dan tumbuh di mal.</h2>
<div><p>PT. Wahana Rezeki Sempurna adalah perusahaan profesional di bidang Exhibition Organizer, penyelenggara event pameran dan promosi. Berdiri sejak 2003, kami telah membantu puluhan ribu bisnis dan pameran di berbagai industri: otomotif, properti, teknologi, furniture, perbankan, travel, fashion, F&amp;B, hingga aksesori.</p>
<p>Kami ingin menjadi Exhibition &amp; Promotion Organizer profesional berskala nasional hingga internasional, yang melayani beragam kebutuhan klien dengan integritas dan inovasi, serta menghadirkan ide dan konsep kreatif untuk setiap event.</p></div>
</div></div>"""

SERVICES = """<div class="sec" id="layanan" style="padding-top:0"><div class="inner">
<h2 style="margin-bottom:36px">Layanan kami</h2>
<div class="svc"><span class="dot"></span><div><h3>Pameran di mal</h3><p>Kami merancang dan menyelenggarakan pameran di mal dan pusat perbelanjaan mitra di berbagai kota, dari otomotif hingga fashion dan furniture.</p></div></div>
<div class="svc"><span class="dot"></span><div><h3>Bazaar dan event promosi</h3><p>Bazaar dan event promosi yang mempertemukan produk Anda langsung dengan pengunjung mal dan membantu memperkuat pemasaran.</p></div></div>
<div class="svc"><span class="dot"></span><div><h3>Sewa space dan counter</h3><p>Sewa lahan, counter, dan kios untuk berjualan di mal. Pilih tanggal dan lokasi di mal mitra WRS.</p></div></div>
<div class="svc"><span class="dot"></span><div><h3>Konsultasi strategi gratis</h3><p>Baru pertama kali ikut pameran di mal? Tim kami siap membantu menyusun strategi terbaik tanpa biaya.</p></div></div>
</div></div>"""

VALUES = """<div class="sec band" id="prinsip"><div class="inner">
<h2>Jabat tangan adalah cara kami memulai setiap kerja sama.</h2>
<div class="vals">
<div class="val"><h3>Analisa yang matang</h3><p>Setiap event kami mulai dengan analisa yang detail dan menyeluruh.</p></div>
<div class="val"><h3>Eksekusi yang rapi</h3><p>Tim profesional kami menjalankan setiap proyek dengan persiapan yang matang.</p></div>
<div class="val"><h3>Biaya jadi investasi</h3><p>Kami berupaya agar setiap biaya yang Anda keluarkan menjadi investasi yang menguntungkan.</p></div>
</div></div></div>"""

# ---------------------------------------------------------------- EVENT
# Ganti isi daftar ini dengan jadwal asli dari menu Event di wrs-eo.com.
# status: "tersedia" (slot masih ada) atau "penuh" (daftar tunggu).
EVENTS = [
    {"tanggal": "[Tanggal event]", "nama": "[Nama event]", "mal": "[Nama mal]",
     "kota": "[Kota]", "kategori": "Otomotif", "status": "tersedia"},
    {"tanggal": "[Tanggal event]", "nama": "[Nama event]", "mal": "[Nama mal]",
     "kota": "[Kota]", "kategori": "Fashion", "status": "tersedia"},
    {"tanggal": "[Tanggal event]", "nama": "[Nama event]", "mal": "[Nama mal]",
     "kota": "[Kota]", "kategori": "Furniture", "status": "penuh"},
]

AREA = "Jabodetabek, Palembang, Surabaya, Kupang, Lampung, Pekanbaru, Semarang, Pontianak, Jambi, Malang, Sidoarjo, Manado, Pangkal Pinang"


def event_row(e):
    ok = e["status"] == "tersedia"
    stat = ('<span class="stat ok">Slot tersedia</span>' if ok
            else '<span class="stat full">Slot penuh</span>')
    btn = ('<a class="btn gold" href="#kontak">Booking slot</a>' if ok
           else '<a class="btn dark" href="#kontak">Daftar tunggu</a>')
    return (
        f'<div class="evt"><div class="tgl">{escape(e["tanggal"])}</div>'
        f'<div><h3>{escape(e["nama"])}<span class="tag">{escape(e["kategori"])}</span></h3>'
        f'<p class="meta">{escape(e["mal"])} &middot; {escape(e["kota"])}</p></div>'
        f'<div class="aksi">{stat}{btn}</div></div>'
    )


EVENT_ROWS = "".join(event_row(e) for e in EVENTS) or (
    '<div class="kosong">Jadwal event terbaru segera hadir. Hubungi kami untuk info slot.</div>'
)

EVENT = f"""<div class="sec" id="event" style="padding-top:0"><div class="inner">
<h2 style="margin-bottom:12px">Event &amp; slot terbaru</h2>
<p style="margin-bottom:32px">Pantau jadwal pameran dan slot yang masih tersedia di mal mitra WRS.</p>
{EVENT_ROWS}
<p class="area"><b>Area jangkauan:</b> {AREA}.</p>
</div></div>"""

FOOT = '<div class="foot">© 2026 PT. Wahana Rezeki Sempurna. Semua hak dilindungi.</div>'

st.markdown(CSS, unsafe_allow_html=True)
st.markdown(NAV + HERO + ABOUT + SERVICES + EVENT + VALUES, unsafe_allow_html=True)

with st.container(key="kontak"):
    st.markdown('<div id="kontak"></div>', unsafe_allow_html=True)
    kiri, kanan = st.columns([1, 1.2], gap="large")
    with kiri:
        st.markdown(
            """<h2>Hubungi kami</h2>
<p class="ci"><b>Alamat</b><br>Graha WRS, Ruko Season City Blok A No. 33-35,<br>Jl. Jembatan Besi, Latumenten, Jakarta Barat 11320</p>
<p class="ci"><b>Telepon</b><br>(021) 2907 1225<br>Call center: 0816 1415 671</p>
<p class="ci"><b>Email</b><br>[Alamat email]</p>
<p class="ci"><b>Instagram</b><br>@wrs.eo</p>""",
            unsafe_allow_html=True,
        )
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

st.markdown(FOOT, unsafe_allow_html=True)
