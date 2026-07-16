# -*- coding: utf-8 -*-
"""
Dataset Aktor
-------------
Menyimpan data aktor secara sementara dalam bentuk dictionary Python
(berperan sebagai 'basis data mini' / in-memory database).

Setiap entri berisi:
- nama            : Nama lengkap aktor
- tanggal_lahir   : Format YYYY-MM-DD
- jenis_kelamin   : "Laki-laki" / "Perempuan"
- negara_asal     : Negara asal aktor
- url_profil      : Tautan profil resmi (IMDb)
"""

DATA_AKTOR = {
    "leonardo dicaprio": {
        "nama": "Leonardo DiCaprio", "tanggal_lahir": "1974-11-11",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Amerika Serikat",
        "url_profil": "https://www.imdb.com/name/nm0000138/",
    },
    "song kang-ho": {
        "nama": "Song Kang-ho", "tanggal_lahir": "1967-01-17",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Korea Selatan",
        "url_profil": "https://www.imdb.com/name/nm0813325/",
    },
    "marion cotillard": {
        "nama": "Marion Cotillard", "tanggal_lahir": "1975-09-30",
        "jenis_kelamin": "Perempuan", "negara_asal": "Prancis",
        "url_profil": "https://www.imdb.com/name/nm0182839/",
    },
    "zendaya": {
        "nama": "Zendaya", "tanggal_lahir": "1996-09-01",
        "jenis_kelamin": "Perempuan", "negara_asal": "Amerika Serikat",
        "url_profil": "https://www.imdb.com/name/nm3918035/",
    },
    "idris elba": {
        "nama": "Idris Elba", "tanggal_lahir": "1972-09-06",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Inggris",
        "url_profil": "https://www.imdb.com/name/nm0252961/",
    },
    "penelope cruz": {
        "nama": "Penélope Cruz", "tanggal_lahir": "1974-04-28",
        "jenis_kelamin": "Perempuan", "negara_asal": "Spanyol",
        "url_profil": "https://www.imdb.com/name/nm0000133/",
    },
    "rami malek": {
        "nama": "Rami Malek", "tanggal_lahir": "1981-05-12",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Amerika Serikat",
        "url_profil": "https://www.imdb.com/name/nm1659221/",
    },
    "priyanka chopra": {
        "nama": "Priyanka Chopra", "tanggal_lahir": "1982-07-18",
        "jenis_kelamin": "Perempuan", "negara_asal": "India",
        "url_profil": "https://www.imdb.com/name/nm1620031/",
    },
    "choi woo-shik": {
        "nama": "Choi Woo-shik", "tanggal_lahir": "1990-03-26",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Korea Selatan",
        "url_profil": "https://www.imdb.com/name/nm5178713/",
    },
    "tilda swinton": {
        "nama": "Tilda Swinton", "tanggal_lahir": "1960-11-05",
        "jenis_kelamin": "Perempuan", "negara_asal": "Inggris",
        "url_profil": "https://www.imdb.com/name/nm0842330/",
    },
    "mahershala ali": {
        "nama": "Mahershala Ali", "tanggal_lahir": "1974-02-16",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Amerika Serikat",
        "url_profil": "https://www.imdb.com/name/nm1806398/",
    },
    "charlize theron": {
        "nama": "Charlize Theron", "tanggal_lahir": "1975-08-07",
        "jenis_kelamin": "Perempuan", "negara_asal": "Afrika Selatan",
        "url_profil": "https://www.imdb.com/name/nm0000234/",
    },
    "ken watanabe": {
        "nama": "Ken Watanabe", "tanggal_lahir": "1959-10-21",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Jepang",
        "url_profil": "https://www.imdb.com/name/nm0001998/",
    },
    "cate blanchett": {
        "nama": "Cate Blanchett", "tanggal_lahir": "1969-05-14",
        "jenis_kelamin": "Perempuan", "negara_asal": "Australia",
        "url_profil": "https://www.imdb.com/name/nm0000949/",
    },
    "oscar isaac": {
        "nama": "Oscar Isaac", "tanggal_lahir": "1979-03-09",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Guatemala",
        "url_profil": "https://www.imdb.com/name/nm0002064/",
    },
    "lupita nyong'o": {
        "nama": "Lupita Nyong'o", "tanggal_lahir": "1983-03-01",
        "jenis_kelamin": "Perempuan", "negara_asal": "Kenya",
        "url_profil": "https://www.imdb.com/name/nm2933757/",
    },
    "javier bardem": {
        "nama": "Javier Bardem", "tanggal_lahir": "1969-03-01",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Spanyol",
        "url_profil": "https://www.imdb.com/name/nm0000849/",
    },
    "awkwafina": {
        "nama": "Awkwafina", "tanggal_lahir": "1988-06-02",
        "jenis_kelamin": "Perempuan", "negara_asal": "Amerika Serikat",
        "url_profil": "https://www.imdb.com/name/nm6073955/",
    },
    "dev patel": {
        "nama": "Dev Patel", "tanggal_lahir": "1990-04-23",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Inggris",
        "url_profil": "https://www.imdb.com/name/nm2199632/",
    },
    "yalitza aparicio": {
        "nama": "Yalitza Aparicio", "tanggal_lahir": "1993-12-11",
        "jenis_kelamin": "Perempuan", "negara_asal": "Meksiko",
        "url_profil": "https://www.imdb.com/name/nm9770305/",
    },
    "michelle yeoh": {
        "nama": "Michelle Yeoh", "tanggal_lahir": "1962-08-06",
        "jenis_kelamin": "Perempuan", "negara_asal": "Malaysia",
        "url_profil": "https://www.imdb.com/name/nm0000474/",
    },
    "ana de armas": {
        "nama": "Ana de Armas", "tanggal_lahir": "1988-04-30",
        "jenis_kelamin": "Perempuan", "negara_asal": "Kuba",
        "url_profil": "https://www.imdb.com/name/nm3053338/",
    },
    "chadwick boseman": {
        "nama": "Chadwick Boseman", "tanggal_lahir": "1976-11-29",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Amerika Serikat",
        "url_profil": "https://www.imdb.com/name/nm1569276/",
    },
    "gael garcia bernal": {
        "nama": "Gael García Bernal", "tanggal_lahir": "1978-11-30",
        "jenis_kelamin": "Laki-laki", "negara_asal": "Meksiko",
        "url_profil": "https://www.imdb.com/name/nm0074586/",
    },
}
