# WolframAlpha Formula Scraper

🔬 **Alat untuk scraping rumus dari WolframAlpha untuk tujuan pendidikan**  
🔬 **Tool for scraping formulas from WolframAlpha for educational purposes**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)

## 📖 Deskripsi / Description

Tool ini dibuat untuk membantu pelajar dan pendidik mengambil rumus dan informasi matematis dari WolframAlpha secara otomatis untuk keperluan pembelajaran. 

This tool is created to help students and educators retrieve formulas and mathematical information from WolframAlpha automatically for educational purposes.

## ✨ Fitur / Features

- ✅ Scraping rumus matematika, fisika, dan kimia / Scrape math, physics, and chemistry formulas
- ✅ Mencari multiple queries sekaligus / Search multiple queries at once
- ✅ Menyimpan hasil ke JSON / Save results to JSON
- ✅ Format output yang rapi / Clean output format
- ✅ Error handling yang baik / Good error handling
- ✅ Rate limiting untuk menghindari blocking / Rate limiting to avoid blocking

## 🚀 Instalasi / Installation

### 1. Clone Repository

```bash
git clone https://github.com/syaharip005/WolframAlpha.git
cd WolframAlpha
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

atau install manual / or install manually:

```bash
pip install requests beautifulsoup4 lxml urllib3
```

## 📚 Cara Penggunaan / Usage

### Penggunaan Dasar / Basic Usage

```python
from wolframalpha_scraper import WolframAlphaScraper

# Inisialisasi scraper
scraper = WolframAlphaScraper()

# Cari rumus
result = scraper.search_formula("quadratic formula")

# Tampilkan hasil
scraper.print_results(result)

# Simpan ke file
scraper.save_results(result, 'quadratic_formula.json')
```

### Mencari Multiple Formulas / Search Multiple Formulas

```python
from wolframalpha_scraper import WolframAlphaScraper

scraper = WolframAlphaScraper()

# List rumus yang ingin dicari
queries = [
    "pythagorean theorem",
    "area of circle",
    "quadratic equation",
    "derivative of sin(x)"
]

# Cari semua rumus
results = scraper.search_multiple(queries, delay=2.0)

# Simpan hasil
scraper.save_results(results, 'all_formulas.json')
```

### Menjalankan Examples / Run Examples

```bash
python examples.py
```

atau jalankan contoh spesifik / or run specific examples:

```python
from examples import example_1_basic_search

example_1_basic_search()
```

## 📝 Contoh Query / Example Queries

### Matematika / Mathematics
- `"quadratic formula"`
- `"pythagorean theorem"`
- `"distance formula"`
- `"area of circle"`
- `"volume of sphere"`
- `"derivative of x^2"`
- `"integral of sin(x)"`

### Fisika / Physics
- `"newton's second law"`
- `"kinetic energy formula"`
- `"speed of light"`
- `"gravitational force"`
- `"ohm's law"`

### Kimia / Chemistry
- `"ideal gas law"`
- `"molarity formula"`
- `"pH formula"`

## 🔧 Struktur Project / Project Structure

```
WolframAlpha/
│
├── wolframalpha_scraper.py    # Main scraper module
├── examples.py                # Example usage scripts
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
├── LICENSE                    # MIT License
└── .gitignore                # Git ignore file
```

## 📦 Dependencies

- **requests** - Untuk HTTP requests
- **beautifulsoup4** - Untuk parsing HTML
- **lxml** - Parser HTML yang cepat
- **urllib3** - HTTP client utilities

## ⚙️ Konfigurasi / Configuration

### Mengubah Delay / Change Delay

```python
scraper = WolframAlphaScraper()
result = scraper.search_formula("your query", delay=3.0)  # 3 detik delay
```

### Custom Headers

Headers sudah dikonfigurasi secara default, tapi bisa diubah:

```python
scraper = WolframAlphaScraper()
scraper.headers['User-Agent'] = 'Your Custom User Agent'
scraper.session.headers.update(scraper.headers)
```

## 🎯 Output Format

Hasil scraping disimpan dalam format JSON:

```json
{
  "query": "quadratic formula",
  "url": "https://www.wolframalpha.com/input?i=quadratic+formula",
  "status": "success",
  "error": null,
  "results": [
    {
      "title": "Formula",
      "content": [...],
      "images": [...],
      "formulas": [...]
    }
  ]
}
```

## ⚠️ Penting / Important Notes

1. **Untuk Pendidikan** / **For Educational Purposes**: Tool ini dibuat khusus untuk tujuan pendidikan
2. **Rate Limiting**: Gunakan delay yang wajar (minimal 2 detik) untuk menghindari blocking
3. **Terms of Service**: Pastikan penggunaan sesuai dengan Terms of Service WolframAlpha
4. **Internet Connection**: Memerlukan koneksi internet yang stabil

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Achmad Syarifudin**
- GitHub: [@syaharip005](https://github.com/syaharip005)

## 🙏 Acknowledgments

- WolframAlpha untuk menyediakan platform pendidikan yang luar biasa
- Komunitas Python untuk library-library yang digunakan

## 📞 Support

Jika ada pertanyaan atau masalah, silakan buka issue di GitHub repository.

---

**Disclaimer**: Tool ini dibuat untuk tujuan pendidikan. Gunakan dengan bijak dan sesuai dengan Terms of Service WolframAlpha.
