

#include "stdio.h"
#include "stdlib.h"

#include "unistd.h"
#include "omp.h"


int main()
{
    printf("Openmp test...\n");
#pragma omp parallel num_threads(4)
    printf("Hellow from thread %d in process %d.\n",
           omp_get_thread_num(), getpid());



    int x;
#pragma omp parallel for private(x)
    for (x = 0; x < 1000000000; x++)
    {
        int y;
        int s;

        if (0 == (x % 100000))
        {
            printf("Startin on row %d\n", x);
        }
    }
    return 0;
}


