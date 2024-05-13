
from pathlib import Path
from timeit import timeit
from search_kmp import kmp_search
from search_bm import boyer_moore_search
from search_rk import rabin_karp_search

art_pattern_1 = "lementToSearch - integers[startIndex]"
art_pattern_2 = "розгорнутого списку дуже проста, тож в подальшому це дасть можливість використовувати багатопот"

def load_text_file(path):
    path = Path(path)
    with path.open(mode='r', encoding='utf8') as file:
        return file.read()

def test_search(main_text, pattern, comment):
    print(comment)
    
    t = timeit(lambda: kmp_search(main_text, pattern), number=500)
    print(f"Пошук по Кнута-Морріса-Пратта: {t}ms")
    
    t = timeit(lambda: boyer_moore_search(main_text, pattern), number=500)
    print(f"Пошук по Боєра-Мура: {t}ms")
    
    t = timeit(lambda: rabin_karp_search(main_text, pattern), number=500)
    print(f"Пошук по Рабіна-Карпа: {t}ms")

def main():
    article1 = load_text_file('./article1.txt')
    article2 = load_text_file('./article2.txt')
    
    test_search(article1, art_pattern_1, '\nПошук в "стаття 1" існуючого патерну\n')
    test_search(article2, art_pattern_2, '\nПошук в "стаття 2" існуючого патерну\n')
    test_search(article1, art_pattern_2, '\nПошук в "стаття 1" не існуючого патерну\n')
    test_search(article2, art_pattern_1, '\nПошук в "стаття 2" не існуючого патерну\n')
    
main()
