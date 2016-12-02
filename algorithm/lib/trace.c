#include <stdio.h>
#include <stdint.h>
#include "./common.h"

void __func_entry(const char *parent, const char *msg)
{
    printf("$>>>>>>>>%s():entry,%s.\n", parent, msg);
}

int32_t __func_return(const char *parent, int32_t status)
{
    printf("#<<<<<<<<%s():return,status=%s.\n", parent, 
            (status) ? "failed-_-!" : "success^_^!");
    return status;
}
