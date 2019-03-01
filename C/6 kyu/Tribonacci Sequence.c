#include <stdlib.h>

long long *tribonacci(const long long signature[3], size_t n) {
  if (n <= 0)
    return NULL;
  long long *arr = (long long*)malloc(n * sizeof(long long));
  for (size_t i = 0; i < n; i++) {
    if (i < 3)
      *(arr + i) = signature[i];
    else
      *(arr + i) = *(arr + i - 1) + *(arr + i - 3) + *(arr + i - 2);
  }
  return arr;
}
