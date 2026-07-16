# -*- coding: utf-8 -*-
"""
Studi Kasus 5: API Informasi Aktor
-----------------------------------
Sebuah perusahaan penyedia informasi film ingin membuat layanan API yang
dapat menampilkan informasi seorang aktor berdasarkan nama yang dimasukkan
pengguna. Informasi tersebut digunakan oleh aplikasi katalog film.

Aplikasi ini terdiri dari dua bagian:
1. REST API murni  -> GET /api/aktor/<nama>   (response JSON)
2. Antarmuka web    -> GET /                  (halaman pencarian modern
                                                yang mengonsumsi API di atas)
"""

from flask import Flask, jsonify, render_template
from actors_data import DATA_AKTOR

app = Flask(__name__)


# ----------------------------------------------------------------------
# ANTARMUKA WEB (frontend modern yang mengonsumsi API di bawah)
# ----------------------------------------------------------------------
@app.route("/", methods=["GET"])
def beranda():
    """Menampilkan halaman pencarian aktor beserta daftar aktor yang tersedia."""
    daftar_aktor = sorted(DATA_AKTOR.values(), key=lambda a: a["nama"])
    return render_template("index.html", daftar_aktor=daftar_aktor, total=len(daftar_aktor))


# ----------------------------------------------------------------------
# REST API — digunakan oleh aplikasi katalog film (atau frontend di atas)
# ----------------------------------------------------------------------
@app.route("/api/aktor/<string:nama>", methods=["GET"])
def get_info_aktor(nama):
    """
    Mengembalikan informasi aktor berdasarkan nama yang dimasukkan user.
    - 200 + status "berhasil" jika data ditemukan
    - 404 + status "gagal"    jika data tidak ditemukan
    """
    kunci = nama.strip().lower()
    aktor = DATA_AKTOR.get(kunci)

    if aktor is None:
        return jsonify({
            "status": "gagal",
            "pesan": f"Aktor dengan nama '{nama}' tidak ditemukan."
        }), 404

    return jsonify({"status": "berhasil", "data": aktor}), 200


@app.route("/api/aktor", methods=["GET"])
def get_semua_aktor():
    """Mengembalikan seluruh daftar aktor yang tersedia pada sistem."""
    return jsonify({
        "status": "berhasil",
        "total": len(DATA_AKTOR),
        "data": list(DATA_AKTOR.values())
    }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
