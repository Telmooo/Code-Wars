#include <stdbool.h>
#include <stdlib.h>

bool is_opposite(const char *s1, const char *s2) {
    int sizeS1 = strlen(s1);
    int sizeS2 = strlen(s2);
    if (sizeS1 == 0 || sizeS2 == 0 || sizeS1 != sizeS2)
        return false;
    for (int i = 0; i < sizeS1; i++)
        if (abs(*(s1 + i) - *(s2 + i)) != 32)
            return false;
    
    return true;
}
