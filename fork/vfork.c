#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(void)
{
	pid_t pid;
	int cnt = 0;

	pid = vfork();
	if (pid < 0) {
		printf("#>%s,%d:fork error!\n", __func__, __LINE__);
		return -1;
	}

	if (pid == 0) {
		cnt++;
		printf("$>I'm the child process!,ID:%d,cnt=%d.\n", getpid(), cnt);
		_exit(0);
	} else {
		cnt++;
		printf("#>I'm the parent process!,ID:%d,CNT=%d.\n", getpid(), cnt);
	}

	sleep(1);
	return 0;
}
