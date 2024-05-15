# Висновки

## Завдання 3:

### The time it took to find a substring in article_1:

- 0.036637125071138144 using Knuth–Morris–Pratt algorithm;
- 0.01307620806619525 using Boyer-Moore algorithm;
- 0.08483529090881348 using Rabin-Karp algorithm.

### The time it took to find a substring in article_2:

- 0.08460425026714802 using Knuth–Morris–Pratt algorithm;
- 0.038538540713489056 using Boyer-Moore algorithm;
- 0.21001012483611703 using Rabin-Karp algorithm.

### The time it took to go through article_1 and fail to find the substring:

- 0.03972624987363815 using Knuth–Morris–Pratt algorithm;
- 0.02977391565218568 using Boyer-Moore algorithm;
- 0.09512787498533726 using Rabin-Karp algorithm.

### The time it took to go through article_2 and fail to find the substring:

- 0.09262341680005193 using Knuth–Morris–Pratt algorithm;
- 0.06681704195216298 using Boyer-Moore algorithm;
- 0.2125286660157144 using Rabin-Karp algorithm.

## Результати:

Отже, алгоритм Бойєра-Мура є найшвидшим, а метод Рабіна-Карпа є найповільнішим.
Продуктивність окремих текстів показує, що алгоритми KMP та Рабіна-Карпа краще оптимізовані для тексту 1, тоді як текст 2 є проблемним для всіх алгоритмів.

