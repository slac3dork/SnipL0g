/**
  _________      .__       .____   _______
 /   _____/ ____ |__|_____ |    |  \   _  \    ____
 \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
 /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
/_______  /___|  /__|   __/|_______ \_____  /\___  /
        \/     \/   |__|           \/     \//_____/
http://snippet.c0de.me
slac3dork@gmail.com
*/

#include <stdio.h>

void converter(float temp, char temp_type) {
	float result;

	if (temp_type == 2) {
		result = ((9 * temp) / 5) + 32;
		printf("\nResult = %.2f Fahrenheit\n", result);
	} else {
		result = (temp / 5) * 4;
		printf("\nResult = %.2f Reamur\n", result);
	}
}

int main(void) {
	float c;
	int temp_type;

	printf("---------------------------------------------------\n");
	printf("celciusconv.c\n");
	printf("Convert Celcius temperature to Reamur or Fahrenheit\n");
	printf("Coded By slac3dork\n");
	printf("---------------------------------------------------\n\n");
	printf("Celcius temperature: ");
	scanf("%f", &c);
	printf("Convert to Reamur/Fahrenheit (1 / 2): ");
	scanf("%d", &temp_type);

	if ((temp_type == 1) || (temp_type == 2)) {
		converter(c, temp_type);
	} else {
		printf("\nUnknown...Plase input 1 or 2");
	}

	return 0;
}

