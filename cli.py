#!/usr/bin/env python3
"""
WolframAlpha Scraper CLI
Command-line interface untuk WolframAlpha Formula Scraper
"""

import sys
import argparse
from wolframalpha_scraper import WolframAlphaScraper


def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description='WolframAlpha Formula Scraper - Educational Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Contoh penggunaan / Examples:
  %(prog)s "quadratic formula"
  %(prog)s "pythagorean theorem" -o output.json
  %(prog)s "area of circle" -d 3.0
  %(prog)s --interactive
  %(prog)s --file queries.txt
        '''
    )
    
    parser.add_argument(
        'query',
        nargs='?',
        help='Query untuk dicari di WolframAlpha'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Nama file output JSON (default: results.json)',
        default='results.json'
    )
    
    parser.add_argument(
        '-d', '--delay',
        type=float,
        help='Delay antara request dalam detik (default: 2.0)',
        default=2.0
    )
    
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Mode interaktif'
    )
    
    parser.add_argument(
        '-f', '--file',
        help='File berisi list queries (satu query per baris)'
    )
    
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Mode quiet (tidak print ke console)'
    )
    
    args = parser.parse_args()
    
    # Inisialisasi scraper
    scraper = WolframAlphaScraper()
    
    # Mode interactive
    if args.interactive:
        run_interactive_mode(scraper, args)
        return
    
    # Mode file
    if args.file:
        run_file_mode(scraper, args)
        return
    
    # Mode single query
    if args.query:
        run_single_query(scraper, args)
        return
    
    # Jika tidak ada argument, show help
    parser.print_help()


def run_single_query(scraper, args):
    """Run single query mode"""
    result = scraper.search_formula(args.query, delay=args.delay)
    
    if not args.quiet:
        scraper.print_results(result)
    
    scraper.save_results(result, args.output)
    
    if not args.quiet:
        print(f"\n✓ Hasil disimpan ke: {args.output}")


def run_file_mode(scraper, args):
    """Run file mode - read queries from file"""
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            queries = [line.strip() for line in f if line.strip()]
        
        if not queries:
            print("Error: File kosong atau tidak ada query yang valid")
            return
        
        print(f"Membaca {len(queries)} queries dari {args.file}")
        
        results = scraper.search_multiple(queries, delay=args.delay)
        
        if not args.quiet:
            for result in results:
                scraper.print_results(result)
        
        scraper.save_results(results, args.output)
        
        print(f"\n✓ Semua hasil ({len(results)}) disimpan ke: {args.output}")
        
    except FileNotFoundError:
        print(f"Error: File '{args.file}' tidak ditemukan")
    except Exception as e:
        print(f"Error: {e}")


def run_interactive_mode(scraper, args):
    """Run interactive mode"""
    print("="*80)
    print("WolframAlpha Scraper - Mode Interaktif")
    print("="*80)
    print("\nKetik query Anda (atau 'exit' untuk keluar)")
    print("Contoh: quadratic formula, pythagorean theorem, etc.\n")
    
    results = []
    
    while True:
        try:
            query = input("\nQuery: ").strip()
            
            if query.lower() in ['exit', 'quit', 'q']:
                break
            
            if not query:
                continue
            
            result = scraper.search_formula(query, delay=args.delay)
            results.append(result)
            
            if not args.quiet:
                scraper.print_results(result)
            
        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
            break
        except Exception as e:
            print(f"Error: {e}")
    
    if results:
        scraper.save_results(results, args.output)
        print(f"\n✓ Total {len(results)} hasil disimpan ke: {args.output}")
    
    print("\nTerima kasih telah menggunakan WolframAlpha Scraper!")


if __name__ == '__main__':
    main()
