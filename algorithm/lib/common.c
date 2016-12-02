#include "common.h"

void swap(uint8_t *a, uint8_t *b)
{
    uint8_t tmp = *a;

    *a = *b;
    *b = tmp;
}

void dump_bytes(const char *prefix, uint8_t *bytes, uint32_t count)
{
    int i;

    printf(">%s[%d]:", prefix, count);
    for (i = 0; i < count; i++) {
        printf(" %02x", bytes[i]);
        if (!((i + 1) % 16))
            printf("\r\n");
    }
    printf("\r\n");
}
