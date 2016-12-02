#Makefile demo
#Created by Jollen @ 6 Sep 2016 @ HK SMiT
#

sources = common.c trace.c
target = common

CFLAGS = -Wall -O0 -g -I.
all : $(target)

$(target) : $(sources)
	@$(CC) $(CFLAGS) -c $^
	@$(AR) rcs $@.a *.o
	@rm -rf *.o

clean:
	@rm -rf $(lib) *.a *.o

