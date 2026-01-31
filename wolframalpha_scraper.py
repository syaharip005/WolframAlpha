"""
WolframAlpha Formula Scraper
Alat untuk mengambil rumus dari WolframAlpha untuk tujuan pendidikan.
Tool for scraping formulas from WolframAlpha for educational purposes.

Copyright (c) 2026 Achmad Syarifudin
Licensed under MIT License
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import Dict, List, Optional
import urllib.parse


class WolframAlphaScraper:
    """
    Kelas untuk scraping rumus dan informasi dari WolframAlpha.
    Class for scraping formulas and information from WolframAlpha.
    """
    
    def __init__(self):
        """Inisialisasi scraper dengan headers yang sesuai."""
        self.base_url = "https://www.wolframalpha.com/input"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def search_formula(self, query: str, delay: float = 2.0) -> Dict:
        """
        Mencari rumus atau informasi dari WolframAlpha.
        Search for formulas or information from WolframAlpha.
        
        Args:
            query (str): Query pencarian (misal: "quadratic formula", "pythagorean theorem")
            delay (float): Waktu delay antara request dalam detik (default: 2.0)
            
        Returns:
            Dict: Dictionary berisi hasil scraping dengan keys:
                - query: Query yang dicari
                - url: URL hasil pencarian
                - results: List hasil yang ditemukan
                - status: Status scraping (success/error)
                - error: Pesan error jika ada
        """
        result = {
            'query': query,
            'url': '',
            'results': [],
            'status': 'pending',
            'error': None
        }
        
        try:
            # Encode query untuk URL
            encoded_query = urllib.parse.quote(query)
            url = f"{self.base_url}?i={encoded_query}"
            result['url'] = url
            
            # Delay untuk menghindari rate limiting
            time.sleep(delay)
            
            # Request ke WolframAlpha
            print(f"Mencari: {query}")
            print(f"URL: {url}")
            
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Ekstrak hasil dari berbagai section
            results = self._extract_results(soup)
            
            if results:
                result['results'] = results
                result['status'] = 'success'
                print(f"Berhasil menemukan {len(results)} hasil")
            else:
                result['status'] = 'no_results'
                result['error'] = 'Tidak ada hasil yang ditemukan'
                print("Tidak ada hasil yang ditemukan")
            
        except requests.exceptions.RequestException as e:
            result['status'] = 'error'
            result['error'] = f'Network error: {str(e)}'
            print(f"Error: {result['error']}")
        except Exception as e:
            result['status'] = 'error'
            result['error'] = f'Error: {str(e)}'
            print(f"Error: {result['error']}")
        
        return result
    
    def _extract_results(self, soup: BeautifulSoup) -> List[Dict]:
        """
        Ekstrak hasil dari HTML WolframAlpha.
        Extract results from WolframAlpha HTML.
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            
        Returns:
            List[Dict]: List hasil yang diekstrak
        """
        results = []
        
        # Mencari pod-pod (section hasil) di WolframAlpha
        pods = soup.find_all('section', class_='_2vZr')
        
        if not pods:
            # Coba alternatif selector
            pods = soup.find_all('div', {'data-testid': lambda x: x and 'pod' in str(x).lower()})
        
        for pod in pods:
            pod_data = self._extract_pod_data(pod)
            if pod_data:
                results.append(pod_data)
        
        # Jika tidak menemukan dengan selector di atas, coba ekstrak dari script tags
        if not results:
            results = self._extract_from_scripts(soup)
        
        return results
    
    def _extract_pod_data(self, pod) -> Optional[Dict]:
        """
        Ekstrak data dari pod individual.
        Extract data from individual pod.
        
        Args:
            pod: BeautifulSoup element dari pod
            
        Returns:
            Optional[Dict]: Data pod jika berhasil diekstrak
        """
        try:
            pod_data = {
                'title': '',
                'content': [],
                'images': [],
                'formulas': []
            }
            
            # Ekstrak title
            title_elem = pod.find(['h2', 'h3', 'h4'])
            if title_elem:
                pod_data['title'] = title_elem.get_text(strip=True)
            
            # Ekstrak text content
            text_elems = pod.find_all(['p', 'span', 'div'])
            for elem in text_elems:
                text = elem.get_text(strip=True)
                if text and len(text) > 2 and text not in pod_data['content']:
                    pod_data['content'].append(text)
            
            # Ekstrak images
            images = pod.find_all('img')
            for img in images:
                img_src = img.get('src', '')
                img_alt = img.get('alt', '')
                if img_src:
                    pod_data['images'].append({
                        'src': img_src,
                        'alt': img_alt
                    })
            
            # Ekstrak formulas (biasanya dalam img dengan alt text)
            for img in images:
                alt_text = img.get('alt', '')
                if alt_text and any(char in alt_text for char in ['=', '+', '-', '*', '/', '^', '∫', '∑', 'x', 'y']):
                    pod_data['formulas'].append(alt_text)
            
            # Hanya return jika ada content
            if pod_data['title'] or pod_data['content'] or pod_data['formulas']:
                return pod_data
            
        except Exception as e:
            print(f"Error extracting pod data: {e}")
        
        return None
    
    def _extract_from_scripts(self, soup: BeautifulSoup) -> List[Dict]:
        """
        Ekstrak data dari script tags (fallback method).
        Extract data from script tags (fallback method).
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            
        Returns:
            List[Dict]: List hasil
        """
        results = []
        
        try:
            # Cari script tags yang mungkin berisi data JSON
            scripts = soup.find_all('script', type='application/json')
            
            for script in scripts:
                try:
                    data = json.loads(script.string)
                    # Proses data JSON jika ada
                    if isinstance(data, dict):
                        results.append({
                            'title': 'Data from JSON',
                            'content': [str(data)],
                            'images': [],
                            'formulas': []
                        })
                except (json.JSONDecodeError, TypeError):
                    continue
        except Exception as e:
            print(f"Error extracting from scripts: {e}")
        
        return results
    
    def search_multiple(self, queries: List[str], delay: float = 2.0) -> List[Dict]:
        """
        Mencari beberapa query sekaligus.
        Search multiple queries at once.
        
        Args:
            queries (List[str]): List query untuk dicari
            delay (float): Waktu delay antara request
            
        Returns:
            List[Dict]: List hasil untuk semua query
        """
        results = []
        
        for i, query in enumerate(queries):
            print(f"\n[{i+1}/{len(queries)}] Processing: {query}")
            result = self.search_formula(query, delay=delay)
            results.append(result)
        
        return results
    
    def save_results(self, results: Dict, filename: str = 'results.json'):
        """
        Simpan hasil ke file JSON.
        Save results to JSON file.
        
        Args:
            results: Hasil scraping
            filename (str): Nama file output
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"\nHasil disimpan ke: {filename}")
        except Exception as e:
            print(f"Error saving results: {e}")
    
    def print_results(self, result: Dict):
        """
        Cetak hasil ke console dengan format yang rapi.
        Print results to console in a neat format.
        
        Args:
            result (Dict): Hasil scraping
        """
        print("\n" + "="*80)
        print(f"Query: {result['query']}")
        print(f"Status: {result['status']}")
        print(f"URL: {result['url']}")
        
        if result['error']:
            print(f"Error: {result['error']}")
        
        if result['results']:
            print(f"\nDitemukan {len(result['results'])} hasil:\n")
            
            for i, pod in enumerate(result['results'], 1):
                print(f"\n--- Hasil {i} ---")
                if pod.get('title'):
                    print(f"Title: {pod['title']}")
                
                if pod.get('formulas'):
                    print(f"\nFormulas:")
                    for formula in pod['formulas']:
                        print(f"  • {formula}")
                
                if pod.get('content'):
                    print(f"\nContent:")
                    for content in pod['content'][:5]:  # Limit to first 5
                        print(f"  • {content}")
                
                if pod.get('images'):
                    print(f"\nImages: {len(pod['images'])} gambar ditemukan")
        
        print("\n" + "="*80)


def main():
    """
    Fungsi utama untuk demonstrasi penggunaan.
    Main function for usage demonstration.
    """
    print("="*80)
    print("WolframAlpha Formula Scraper - Educational Tool")
    print("="*80)
    
    # Inisialisasi scraper
    scraper = WolframAlphaScraper()
    
    # Contoh penggunaan - cari satu formula
    print("\nContoh 1: Mencari rumus kuadrat")
    result = scraper.search_formula("quadratic formula")
    scraper.print_results(result)
    
    # Simpan hasil
    scraper.save_results(result, 'quadratic_formula.json')
    
    # Contoh penggunaan - cari beberapa formula
    print("\n\nContoh 2: Mencari beberapa formula sekaligus")
    queries = [
        "pythagorean theorem",
        "area of circle"
    ]
    
    results = scraper.search_multiple(queries, delay=2.0)
    
    # Cetak semua hasil
    for result in results:
        scraper.print_results(result)
    
    # Simpan semua hasil
    scraper.save_results(results, 'multiple_formulas.json')
    
    print("\n" + "="*80)
    print("Selesai! Hasil telah disimpan.")
    print("="*80)


if __name__ == "__main__":
    main()
