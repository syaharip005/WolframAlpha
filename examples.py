"""
Contoh penggunaan WolframAlpha Scraper
Examples of using WolframAlpha Scraper
"""

from wolframalpha_scraper import WolframAlphaScraper


def example_1_basic_search():
    """Contoh 1: Pencarian dasar"""
    print("\n" + "="*80)
    print("CONTOH 1: Pencarian Dasar / Basic Search")
    print("="*80)
    
    scraper = WolframAlphaScraper()
    
    # Cari rumus kuadrat
    result = scraper.search_formula("quadratic formula")
    scraper.print_results(result)
    
    # Simpan ke file
    scraper.save_results(result, 'example1_quadratic.json')


def example_2_multiple_searches():
    """Contoh 2: Pencarian multiple"""
    print("\n" + "="*80)
    print("CONTOH 2: Pencarian Multiple / Multiple Searches")
    print("="*80)
    
    scraper = WolframAlphaScraper()
    
    # List rumus yang ingin dicari
    formulas_to_search = [
        "pythagorean theorem",
        "area of circle",
        "quadratic equation",
        "derivative of sin(x)",
        "integral of x^2"
    ]
    
    # Cari semua rumus
    results = scraper.search_multiple(formulas_to_search, delay=2.0)
    
    # Simpan semua hasil
    scraper.save_results(results, 'example2_multiple.json')
    
    print(f"\nTotal {len(results)} pencarian selesai!")


def example_3_math_formulas():
    """Contoh 3: Rumus-rumus matematika"""
    print("\n" + "="*80)
    print("CONTOH 3: Rumus Matematika / Math Formulas")
    print("="*80)
    
    scraper = WolframAlphaScraper()
    
    math_queries = [
        "distance formula",
        "slope formula",
        "volume of sphere",
        "circumference of circle"
    ]
    
    for query in math_queries:
        print(f"\n--- Mencari: {query} ---")
        result = scraper.search_formula(query, delay=2.0)
        
        # Cetak hanya formulas yang ditemukan
        if result['status'] == 'success':
            for pod in result['results']:
                if pod.get('formulas'):
                    print(f"\nFormulas ditemukan:")
                    for formula in pod['formulas']:
                        print(f"  {formula}")


def example_4_physics_formulas():
    """Contoh 4: Rumus-rumus fisika"""
    print("\n" + "="*80)
    print("CONTOH 4: Rumus Fisika / Physics Formulas")
    print("="*80)
    
    scraper = WolframAlphaScraper()
    
    physics_queries = [
        "newton's second law",
        "kinetic energy formula",
        "speed of light",
        "gravitational force"
    ]
    
    results = scraper.search_multiple(physics_queries, delay=2.0)
    scraper.save_results(results, 'example4_physics.json')


def example_5_custom_search():
    """Contoh 5: Pencarian custom"""
    print("\n" + "="*80)
    print("CONTOH 5: Pencarian Custom / Custom Search")
    print("="*80)
    
    scraper = WolframAlphaScraper()
    
    # Tanya query apapun yang Anda inginkan
    custom_query = input("Masukkan query Anda (atau tekan Enter untuk skip): ")
    
    if custom_query.strip():
        result = scraper.search_formula(custom_query)
        scraper.print_results(result)
        
        # Simpan hasil
        filename = f"custom_{custom_query.replace(' ', '_')[:30]}.json"
        scraper.save_results(result, filename)
    else:
        print("Skipped.")


def run_all_examples():
    """Jalankan semua contoh"""
    print("\n" + "="*80)
    print("WOLFRAM ALPHA SCRAPER - SEMUA CONTOH")
    print("Educational Tool for Formula Scraping")
    print("="*80)
    
    # Uncomment contoh yang ingin dijalankan:
    
    example_1_basic_search()
    # example_2_multiple_searches()
    # example_3_math_formulas()
    # example_4_physics_formulas()
    # example_5_custom_search()
    
    print("\n" + "="*80)
    print("Semua contoh selesai!")
    print("="*80)


if __name__ == "__main__":
    # Pilih mode:
    # 1. Jalankan semua contoh
    run_all_examples()
    
    # 2. Atau jalankan contoh individual:
    # example_1_basic_search()
    # example_2_multiple_searches()
    # example_3_math_formulas()
    # example_4_physics_formulas()
    # example_5_custom_search()
