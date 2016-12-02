#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(void)
{
	pid_t pid;

	pid = fork();
	if (pid < 0) {
		printf("#>%s,%d:fork error!\n", __func__, __LINE__);
		return -1;
	}

	if (pid == 0)
		printf("$>I'm the child process!\n");
	else
		printf("#>I'm the parent process!\n");

	return 0;
}
