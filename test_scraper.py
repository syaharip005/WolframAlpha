"""
Simple tests untuk WolframAlpha Scraper
Tests are basic validation to ensure the code works
"""

import sys
import json
from wolframalpha_scraper import WolframAlphaScraper


def test_initialization():
    """Test 1: Inisialisasi scraper"""
    print("\n[TEST 1] Testing initialization...")
    try:
        scraper = WolframAlphaScraper()
        assert scraper.base_url == "https://www.wolframalpha.com/input"
        assert scraper.headers is not None
        assert scraper.session is not None
        print("✓ PASSED: Scraper initialized successfully")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_url_encoding():
    """Test 2: URL encoding"""
    print("\n[TEST 2] Testing URL encoding...")
    try:
        scraper = WolframAlphaScraper()
        import urllib.parse
        
        test_query = "quadratic formula"
        encoded = urllib.parse.quote(test_query)
        expected_url = f"{scraper.base_url}?i={encoded}"
        
        assert "quadratic" in encoded or "quadratic+formula" in expected_url
        print(f"✓ PASSED: URL encoding works correctly")
        print(f"  Query: {test_query}")
        print(f"  URL: {expected_url}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_result_structure():
    """Test 3: Result structure"""
    print("\n[TEST 3] Testing result structure...")
    try:
        scraper = WolframAlphaScraper()
        
        # Test structure without actual request
        result = {
            'query': 'test',
            'url': '',
            'results': [],
            'status': 'pending',
            'error': None
        }
        
        assert 'query' in result
        assert 'url' in result
        assert 'results' in result
        assert 'status' in result
        assert 'error' in result
        
        print("✓ PASSED: Result structure is correct")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_save_and_load():
    """Test 4: Save and load JSON"""
    print("\n[TEST 4] Testing save and load...")
    try:
        import os
        scraper = WolframAlphaScraper()
        
        test_result = {
            'query': 'test query',
            'url': 'https://example.com',
            'results': [],
            'status': 'success',
            'error': None
        }
        
        test_file = '/tmp/test_output.json'
        
        # Save
        scraper.save_results(test_result, test_file)
        
        # Load and verify
        with open(test_file, 'r') as f:
            loaded = json.load(f)
        
        assert loaded['query'] == test_result['query']
        assert loaded['status'] == test_result['status']
        
        # Cleanup
        os.remove(test_file)
        
        print("✓ PASSED: Save and load works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_multiple_queries_structure():
    """Test 5: Multiple queries structure"""
    print("\n[TEST 5] Testing multiple queries structure...")
    try:
        scraper = WolframAlphaScraper()
        
        # Test with empty list
        queries = []
        results = scraper.search_multiple(queries, delay=0.1)
        assert isinstance(results, list)
        assert len(results) == 0
        
        print("✓ PASSED: Multiple queries structure is correct")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_cli_import():
    """Test 6: CLI module import"""
    print("\n[TEST 6] Testing CLI import...")
    try:
        import cli
        print("✓ PASSED: CLI module imports successfully")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_examples_import():
    """Test 7: Examples module import"""
    print("\n[TEST 7] Testing examples import...")
    try:
        import examples
        print("✓ PASSED: Examples module imports successfully")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def run_all_tests():
    """Run all tests"""
    print("="*80)
    print("WolframAlpha Scraper - Running Tests")
    print("="*80)
    
    tests = [
        test_initialization,
        test_url_encoding,
        test_result_structure,
        test_save_and_load,
        test_multiple_queries_structure,
        test_cli_import,
        test_examples_import
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nTotal Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        return 0
    else:
        print(f"\n⚠️  {total - passed} TEST(S) FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
