#include "./lib/common.h"

int bubble_sort(uint8_t *a, uint32_t n)
{
    int i, j;

    printf("$>>>>%s():\n", __func__);
    if (n < 1) {
        printf("#>invalid arrary size %d!\n", n);
        return -1;
    }

    for (i = n -1; i > 0; i--) {
        for (j = 0; j < i; j++) {
            if (a[j] > a[j + 1])
                swap(&a[j], &a[j + 1]);
        }
    }
    
    return 0;
}

int main(int argc, char **argv)
{
    uint8_t a[] = {0x02,0x05,0x03,0x06,0x98,0x23,0x56,0x13,
                   0x16,0x45,0x00,0x31,0x93,0x84,0x17,0x52,0x73};
    int ret;

    dump_bytes("old", a, sizeof(a));
    ret = bubble_sort(a, sizeof(a));
    if (!ret)
        dump_bytes("new", a, sizeof(a));

    return ret;
}

