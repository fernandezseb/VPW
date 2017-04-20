#include <stdio.h>
#include <math.h>

int main(int argc, char**argv)
{
    int amount;
    int i;
    double input;
    int count;
    double max;
    double estimate;

    scanf("%d", &amount);

    for(i = 0; i < amount; i++) {
         scanf("%lf", &input);
         count = 1;
         max = input;

        while(input > 0) {
	    if(input > max) {
		max = input;
            }

	    scanf("%lf", &input);
	    count++;
        }
	count -= 1;

	estimate = (((count + 1) * max) / count) -1;
	printf("%d %d\n", (i+1), (int) round(estimate));
    }
    
    return 0;
}
