#include "./lib/common.h"

int insert_sort(uint8_t *a, uint32_t n)
{
    int i;

    printf("$>>>>%s():\n", __func__);
    if (n < 1) {
        printf("#>invalid arrary size %d!\n", n);
        return -1;
    }

    for (i = 1; i < n; i++) {
        if (a[i] < a[i - 1]) {
            int j = i - 1;
            int x = a[i];

            while (x < a[j] && j >= 0) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = x;
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
    ret = insert_sort(a, sizeof(a));
    if (!ret)
        dump_bytes("new", a, sizeof(a));

    return ret;
}

