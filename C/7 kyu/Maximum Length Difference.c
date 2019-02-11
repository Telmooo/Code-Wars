#include <stdlib.h>

int mxdiflg(const char **a1, size_t a1len, const char **a2, size_t a2len) {
    if (a1 == NULL || a2 == NULL)
        return -1;
        
    int max = -1, aux;
    for (int i = 0; i < a1len; i++) {
        for (int j = 0; j < a2len; j++) {
            aux = abs(strlen(*(a1 + i)) - strlen(*(a2 + j)));
            if (aux > max)
                max = aux;
        }
    }
    return max;
}
