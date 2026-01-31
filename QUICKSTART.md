# 🚀 Panduan Cepat - WolframAlpha Scraper

## Instalasi

```bash
# 1. Clone repository
git clone https://github.com/syaharip005/WolframAlpha.git
cd WolframAlpha

# 2. Install dependencies
pip install -r requirements.txt
```

## Cara Pakai

### Metode 1: Command Line (Paling Mudah)

```bash
# Cari satu rumus
python cli.py "quadratic formula"

# Cari dan simpan ke file tertentu
python cli.py "pythagorean theorem" -o hasil.json

# Cari beberapa rumus dari file
python cli.py -f sample_queries.txt -o hasil_batch.json

# Mode interaktif
python cli.py -i
```

### Metode 2: Jalankan Contoh

```bash
# Jalankan file contoh
python examples.py
```

### Metode 3: Gunakan di Code Python Anda

```python
from wolframalpha_scraper import WolframAlphaScraper

# Buat scraper
scraper = WolframAlphaScraper()

# Cari rumus
hasil = scraper.search_formula("quadratic formula")

# Tampilkan hasil
scraper.print_results(hasil)

# Simpan ke file
scraper.save_results(hasil, 'output.json')
```

## Contoh Query

### Matematika
- `"quadratic formula"` - Rumus ABC/Kuadrat
- `"pythagorean theorem"` - Teorema Pythagoras
- `"area of circle"` - Luas Lingkaran
- `"volume of sphere"` - Volume Bola
- `"distance formula"` - Rumus Jarak

### Fisika
- `"newton's second law"` - Hukum Newton 2
- `"kinetic energy formula"` - Rumus Energi Kinetik
- `"speed of light"` - Kecepatan Cahaya
- `"ohm's law"` - Hukum Ohm

### Kimia
- `"ideal gas law"` - Hukum Gas Ideal
- `"pH formula"` - Rumus pH
- `"molarity formula"` - Rumus Molaritas

## Fitur Utama

✅ Scraping rumus matematika, fisika, dan kimia  
✅ Batch processing untuk banyak query  
✅ Export ke JSON  
✅ Command Line Interface (CLI)  
✅ Mode interaktif  
✅ Error handling yang baik  

## Tips

1. **Delay**: Gunakan delay minimal 2 detik untuk menghindari blocking
2. **Query**: Gunakan bahasa Inggris untuk hasil terbaik
3. **Batch**: Untuk banyak query, gunakan mode file (`-f`)
4. **Simpan**: Selalu simpan hasil agar tidak perlu scraping ulang

## Troubleshooting

**Tidak ada hasil?**
- Cek koneksi internet
- Pastikan query dalam bahasa Inggris
- Coba query yang lebih spesifik

**Error saat install?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Rate limited?**
- Tingkatkan delay: `python cli.py "query" -d 5.0`
- Tunggu beberapa menit sebelum mencoba lagi

## File Penting

- `wolframalpha_scraper.py` - Modul utama scraper
- `cli.py` - Command line interface
- `examples.py` - Contoh penggunaan
- `requirements.txt` - Dependencies
- `sample_queries.txt` - Contoh list queries
- `README.md` - Dokumentasi lengkap
- `USAGE.md` - Panduan penggunaan detail

## Bantuan Lebih Lanjut

- Dokumentasi lengkap: Lihat `README.md`
- Panduan detail: Lihat `USAGE.md`
- Contoh code: Lihat `examples.py`
- CLI help: `python cli.py --help`

## License

MIT License - Bebas digunakan untuk pendidikan dan non-komersial

---

**Selamat menggunakan WolframAlpha Scraper! 🎓**

Jika ada pertanyaan, silakan buka issue di GitHub repository.
