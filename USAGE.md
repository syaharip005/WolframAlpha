# Panduan Penggunaan WolframAlpha Scraper
# WolframAlpha Scraper Usage Guide

## 📋 Daftar Isi / Table of Contents

1. [Quick Start](#quick-start)
2. [Penggunaan Dasar](#penggunaan-dasar--basic-usage)
3. [Penggunaan CLI](#penggunaan-cli--cli-usage)
4. [Penggunaan Programmatic](#penggunaan-programmatic--programmatic-usage)
5. [Contoh-contoh](#contoh-contoh--examples)
6. [Tips dan Trik](#tips-dan-trik--tips-and-tricks)
7. [Troubleshooting](#troubleshooting)

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Cari formula menggunakan CLI
python cli.py "quadratic formula"

# 3. Atau jalankan contoh
python examples.py
```

---

## Penggunaan Dasar / Basic Usage

### 1. Import Module

```python
from wolframalpha_scraper import WolframAlphaScraper

# Inisialisasi scraper
scraper = WolframAlphaScraper()
```

### 2. Cari Formula

```python
# Cari satu formula
result = scraper.search_formula("quadratic formula")

# Tampilkan hasil
scraper.print_results(result)

# Simpan ke file JSON
scraper.save_results(result, 'output.json')
```

### 3. Cari Multiple Formulas

```python
queries = [
    "pythagorean theorem",
    "area of circle",
    "quadratic equation"
]

results = scraper.search_multiple(queries, delay=2.0)
scraper.save_results(results, 'multiple_results.json')
```

---

## Penggunaan CLI / CLI Usage

### Mode Single Query

```bash
# Format dasar
python cli.py "your query here"

# Dengan custom output file
python cli.py "quadratic formula" -o my_output.json

# Dengan custom delay
python cli.py "pythagorean theorem" -d 3.0

# Mode quiet (no console output)
python cli.py "area of circle" -q -o results.json
```

### Mode File (Batch Processing)

```bash
# Buat file dengan list queries (satu per baris)
cat > my_queries.txt << EOF
quadratic formula
pythagorean theorem
area of circle
volume of sphere
EOF

# Jalankan batch processing
python cli.py -f my_queries.txt -o batch_results.json

# Dengan custom delay
python cli.py -f my_queries.txt -d 3.0 -o results.json
```

### Mode Interactive

```bash
# Jalankan mode interaktif
python cli.py -i

# Atau dengan custom output
python cli.py -i -o interactive_results.json
```

Output:
```
================================================================================
WolframAlpha Scraper - Mode Interaktif
================================================================================

Ketik query Anda (atau 'exit' untuk keluar)
Contoh: quadratic formula, pythagorean theorem, etc.

Query: quadratic formula
[Hasil ditampilkan...]

Query: exit
✓ Total 1 hasil disimpan ke: results.json
```

---

## Penggunaan Programmatic / Programmatic Usage

### Contoh Lengkap

```python
from wolframalpha_scraper import WolframAlphaScraper
import json

def main():
    # Inisialisasi
    scraper = WolframAlphaScraper()
    
    # Cari formula
    query = "quadratic formula"
    result = scraper.search_formula(query, delay=2.0)
    
    # Cek status
    if result['status'] == 'success':
        print(f"✓ Berhasil menemukan {len(result['results'])} hasil")
        
        # Proses hasil
        for pod in result['results']:
            print(f"\nTitle: {pod.get('title', 'N/A')}")
            
            # Cetak formulas
            if pod.get('formulas'):
                print("Formulas:")
                for formula in pod['formulas']:
                    print(f"  - {formula}")
            
            # Cetak content
            if pod.get('content'):
                print("Content:")
                for content in pod['content'][:3]:
                    print(f"  - {content}")
        
        # Simpan hasil
        scraper.save_results(result, f'{query.replace(" ", "_")}.json')
    else:
        print(f"✗ Error: {result.get('error', 'Unknown error')}")

if __name__ == '__main__':
    main()
```

### Custom Configuration

```python
from wolframalpha_scraper import WolframAlphaScraper

# Inisialisasi dengan custom settings
scraper = WolframAlphaScraper()

# Ubah headers jika perlu
scraper.headers['User-Agent'] = 'Custom User Agent'
scraper.session.headers.update(scraper.headers)

# Ubah timeout
scraper.session.timeout = 60

# Cari dengan delay custom
result = scraper.search_formula("your query", delay=5.0)
```

---

## Contoh-contoh / Examples

### 1. Rumus Matematika / Math Formulas

```python
from wolframalpha_scraper import WolframAlphaScraper

scraper = WolframAlphaScraper()

math_formulas = [
    "quadratic formula",
    "pythagorean theorem",
    "distance formula",
    "slope formula",
    "area of circle",
    "volume of sphere",
    "circumference formula",
    "surface area of cylinder"
]

results = scraper.search_multiple(math_formulas, delay=2.0)
scraper.save_results(results, 'math_formulas.json')
```

### 2. Calculus Formulas

```python
calculus_formulas = [
    "derivative of sin(x)",
    "derivative of cos(x)",
    "integral of x^2",
    "integral of e^x",
    "chain rule",
    "product rule",
    "quotient rule"
]

results = scraper.search_multiple(calculus_formulas, delay=2.0)
scraper.save_results(results, 'calculus_formulas.json')
```

### 3. Physics Formulas

```python
physics_formulas = [
    "newton's second law",
    "kinetic energy formula",
    "potential energy formula",
    "speed of light",
    "gravitational force",
    "ohm's law",
    "power formula"
]

results = scraper.search_multiple(physics_formulas, delay=2.0)
scraper.save_results(results, 'physics_formulas.json')
```

### 4. Chemistry Formulas

```python
chemistry_formulas = [
    "ideal gas law",
    "molarity formula",
    "pH formula",
    "avogadro's number",
    "density formula"
]

results = scraper.search_multiple(chemistry_formulas, delay=2.0)
scraper.save_results(results, 'chemistry_formulas.json')
```

---

## Tips dan Trik / Tips and Tricks

### 1. Optimal Delay

```python
# Delay minimal (risk of blocking)
result = scraper.search_formula("query", delay=1.0)

# Delay recommended (safe)
result = scraper.search_formula("query", delay=2.0)

# Delay conservative (very safe)
result = scraper.search_formula("query", delay=5.0)
```

### 2. Error Handling

```python
from wolframalpha_scraper import WolframAlphaScraper

scraper = WolframAlphaScraper()

try:
    result = scraper.search_formula("your query")
    
    if result['status'] == 'success':
        print("Success!")
    elif result['status'] == 'no_results':
        print("No results found")
    else:
        print(f"Error: {result['error']}")
        
except Exception as e:
    print(f"Exception occurred: {e}")
```

### 3. Batch Processing dengan Error Handling

```python
queries = ["query1", "query2", "query3", ...]
results = []
failed = []

for query in queries:
    try:
        result = scraper.search_formula(query, delay=2.0)
        if result['status'] == 'success':
            results.append(result)
        else:
            failed.append(query)
    except Exception as e:
        print(f"Failed to process {query}: {e}")
        failed.append(query)

print(f"Success: {len(results)}, Failed: {len(failed)}")
```

### 4. Filter Hanya Formulas

```python
result = scraper.search_formula("quadratic formula")

# Extract hanya formulas
all_formulas = []
for pod in result['results']:
    if pod.get('formulas'):
        all_formulas.extend(pod['formulas'])

print("All formulas found:")
for formula in all_formulas:
    print(f"  - {formula}")
```

---

## Troubleshooting

### Problem: "No results found"

**Solusi:**
- Cek koneksi internet
- Coba query yang lebih spesifik
- Cek apakah WolframAlpha bisa diakses di browser

### Problem: Rate limiting / Blocked

**Solusi:**
- Tingkatkan delay antara requests
- Gunakan delay minimal 3-5 detik
- Jangan scrape terlalu banyak dalam waktu singkat

```python
# Gunakan delay yang lebih besar
result = scraper.search_formula("query", delay=5.0)
```

### Problem: Import Error

**Solusi:**
```bash
# Install ulang dependencies
pip install --upgrade -r requirements.txt

# Atau install manual
pip install requests beautifulsoup4 lxml urllib3
```

### Problem: Timeout

**Solusi:**
```python
# Tingkatkan timeout di code
scraper = WolframAlphaScraper()
# Note: Timeout configuration perlu ditambahkan di session.get()
```

### Problem: JSON Decode Error

**Solusi:**
- Cek koneksi internet
- Cek apakah response dari server valid
- Gunakan error handling yang proper

---

## Format Output JSON

```json
{
  "query": "quadratic formula",
  "url": "https://www.wolframalpha.com/input?i=quadratic+formula",
  "status": "success",
  "error": null,
  "results": [
    {
      "title": "Formula",
      "content": ["Content text here"],
      "images": [
        {
          "src": "image_url",
          "alt": "image description"
        }
      ],
      "formulas": ["x = (-b ± √(b²-4ac)) / 2a"]
    }
  ]
}
```

---

## Best Practices

1. **Gunakan delay yang wajar** (minimal 2 detik)
2. **Handle errors dengan baik**
3. **Simpan hasil untuk menghindari re-scraping**
4. **Batch processing untuk multiple queries**
5. **Respect Terms of Service WolframAlpha**

---

## Kontribusi / Contributing

Jika menemukan bug atau ingin menambahkan fitur:
1. Fork repository
2. Buat branch baru
3. Commit changes
4. Push ke branch
5. Create Pull Request

---

## Support

Untuk pertanyaan atau masalah, buka issue di:
https://github.com/syaharip005/WolframAlpha/issues

---

**Happy Scraping! 🚀**
