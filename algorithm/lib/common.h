#include <stdio.h>
#include <stdint.h>

void swap(uint8_t *a, uint8_t *b);
void dump_bytes(const char *prefix, uint8_t *bytes, uint32_t count);
void __func_entry(const char *parent, const char *msg);
int32_t __func_return(const char *parent, int32_t status);
