

#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"

#include "unistd.h"
#include "omp.h"



void evaluate(int x_min, int x_max,
              int y_min, int y_max,
              int x_velocity,
              int y_velocity, 
              bool* is_hit,
              int* highest_y)
{
    int x_pos = 0;
    int y_pos = 0;

    *is_hit = false;

    while (y_pos >= y_min)
    {
        // printf("In loop %d, %d\n", x_pos, y_pos);
        x_pos += x_velocity;
        y_pos += y_velocity;

        if (x_velocity > 0) x_velocity--;
        y_velocity--;

        if (y_velocity == 0) *highest_y = y_pos;

        bool within_x_target = (x_min <= x_pos) && (x_pos <= x_max);
        bool within_y_target = (y_min <= y_pos) && (y_pos <= y_max);

        if (within_x_target  &&  within_y_target) 
        {
            *is_hit = true;
            return;
        }
    }
}





int main()
{
    printf("Openmp test...\n");
#pragma omp parallel num_threads(4)
    printf("Hellow from thread %d in process %d.\n",
           omp_get_thread_num(), getpid());


    // target area: x=20..30, y=-10..-5    -> 6, 9, maxy->45
    // 
    // 
    // target area: x=257..286, y=-101..-57

    int x_velocity;
    int y_velocity;

    int best_x_velocity = 0; 
    int best_y_velocity = 0; 
    int best_y_height   = 0; 

    int total_hits = 0;

    for (x_velocity = -1000; x_velocity < 2000; x_velocity++)
    {
        for (y_velocity = -1000; y_velocity < 2000; y_velocity++)
        {
            // printf("trying %d, %d\n", x_velocity, y_velocity);
            int y_peak_height = 0;
            bool is_hit = false;

            //evaluate(20, 30, -10, -5,
            evaluate(257, 286, -101, -57,
                     x_velocity, y_velocity,
                     &is_hit, &y_peak_height);
            if (!is_hit) continue;

            total_hits++;
            if (y_peak_height > best_y_height)
            {
                best_x_velocity = x_velocity; 
                best_y_velocity = y_velocity; 
                best_y_height   = y_peak_height;

                printf("FOUND BETTER: %d, %d  went to %d\n",
                       best_x_velocity,
                       best_y_velocity,
                       best_y_height);
            }
        }
    }

    printf("TERMINAL WAS: %d, %d  went to highest %d, and there were %d total\n",
           best_x_velocity,
           best_y_velocity,
           best_y_height,
           total_hits);

    int temp;
#pragma omp parallel for private(temp)
    for (temp = 0; temp < 100000; temp++)
    {
        int y_velocity_temp;
        int s;

        if (0 == (temp % 100000))
        {
            printf("Startin on row %d\n", temp);
        }
    }
    return 0;
}


