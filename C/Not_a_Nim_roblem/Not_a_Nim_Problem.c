/*https://codeforces.com/problemset/problem/2004/E?locale=en*/

#include <stdio.h>
#include <stdlib.h>

int *less_div;
int *primes_ind;

void calc_less_div()
{
	less_div = (int*)calloc(10000000, sizeof(int));
	primes_ind = (int*)calloc(10000000, sizeof(int));

	int ind = 1;
	for (int i = 2; i < 10000000; i++)
		if (!less_div[i])
		{
			primes_ind[i] = ind;
			ind++;
			for (int j = i; j < 10000000; j += i)
				if (!less_div[j])
					less_div[j] = i;
		}
}

int main()
{
	calc_less_div();
	int t;
	scanf_s("%d", &t);

	for (int k = 0; k < t; k++)
	{
		int n, a, sprague_grundy_val_xor;
		sprague_grundy_val_xor = 0;
		scanf_s("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf_s("%d", &a);
			if (a == 1)
			{
				sprague_grundy_val_xor ^= 1;
				continue;
			}
			if (a % 2 == 0)
				continue;
			int p_i = primes_ind[a];
			if (p_i)
			{
				sprague_grundy_val_xor ^= p_i;
				continue;
			}
			sprague_grundy_val_xor ^= primes_ind[less_div[a]];
		}
		if (sprague_grundy_val_xor)
			printf("Alice\n");
		else
			printf("Bob\n");

	}
	return 0;
}