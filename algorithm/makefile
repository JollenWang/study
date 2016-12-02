CFLAGS := -Wall -O0 -g
LDFLAGS := -L./lib -lcommon

target = sort.exe
COMPILE := bubble_sort.c
OBJECTS := $(COMPILE:.c=.o)

.PHONY: default build clean

build : $(target)

%.o : %.c
	$(CC) -c $(CFLAGS) -o $@ $<

$(target) : $(OBJECTS)
	@rm -rf $@
	@$(CC) *.o ./lib/common.a -lc -o $@

clean:
	@rm -rf *.o *.exe

