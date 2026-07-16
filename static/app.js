// Menghubungkan antarmuka pencarian dengan REST API Flask (/api/aktor/<nama>)

const form = document.getElementById("form-cari");
const input = document.getElementById("input-nama");
const panel = document.getElementById("hasil-pencarian");

async function cariAktor(nama) {
  panel.classList.remove("hidden", "error");
  panel.innerHTML = `<p style="color:#9aa4bd;margin:0;">Mencari data untuk "${nama}"…</p>`;

  try {
    const res = await fetch(`/api/aktor/${encodeURIComponent(nama)}`);
    const json = await res.json();

    if (res.ok && json.status === "berhasil") {
      const a = json.data;
      panel.innerHTML = `
        <div class="result-head">
          <div class="result-avatar">${a.nama.charAt(0)}</div>
          <div>
            <p class="result-name">${a.nama}</p>
            <span class="result-status">Data ditemukan &middot; 200 OK</span>
          </div>
        </div>
        <div class="result-grid">
          <div class="result-item"><label>Tanggal Lahir</label><span>${a.tanggal_lahir}</span></div>
          <div class="result-item"><label>Jenis Kelamin</label><span>${a.jenis_kelamin}</span></div>
          <div class="result-item"><label>Negara Asal</label><span>${a.negara_asal}</span></div>
          <div class="result-item"><label>Profil</label><a href="${a.url_profil}" target="_blank" rel="noopener">Lihat di IMDb ↗</a></div>
        </div>
      `;
    } else {
      panel.classList.add("error");
      panel.innerHTML = `
        <div class="result-head">
          <div class="result-avatar" style="background:#3a2230;">⚠</div>
          <div>
            <p class="result-name">Aktor tidak ditemukan</p>
            <span class="result-status gagal">404 &middot; ${json.pesan || "Data tidak tersedia"}</span>
          </div>
        </div>
      `;
    }
  } catch (err) {
    panel.classList.add("error");
    panel.innerHTML = `<p style="color:#ff6b81;margin:0;">Terjadi kesalahan saat menghubungi server.</p>`;
  }
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const nama = input.value.trim();
  if (nama) cariAktor(nama);
});

document.querySelectorAll(".actor-card").forEach((card) => {
  card.addEventListener("click", () => {
    const nama = card.dataset.nama;
    input.value = nama;
    cariAktor(nama);
    panel.scrollIntoView({ behavior: "smooth", block: "center" });
  });
});
