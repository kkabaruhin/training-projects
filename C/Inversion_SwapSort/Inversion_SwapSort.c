/*https://codeforces.com/problemset/problem/1375/E?locale=en*/

#include <stdio.h>
#include <stdlib.h>

struct pair
{
	int a, b;
};
struct pair* answer;

int main()
{
	int n, answer_len = 0;
	answer = (struct pair*)(malloc(1000000 * sizeof(struct pair)));
	double arr[1001];
	scanf_s("%d", &n);

	for (int i = 0; i < n; i++)
		scanf_s("%lf", &arr[i]);

	for (int i = 0; i < n; i++)
	{
		int mult;
		mult = 1;
		for (int j = i + 1; j < n; j++)
		{
			if (arr[i] == arr[j])
			{
				arr[j] = arr[j] + (0.00001 * mult);
				mult++;
			}
		}
	}

	arr[1000] = 10000000000;
	int ind_r = n - 1, ind_l;
	while (ind_r > 0)
	{
		ind_l = 1000;
		for (int i = 0 ; i < ind_r; i++)
			if ((arr[i] > arr[ind_r]) && (arr[i] - arr[ind_r] < arr[ind_l] - arr[ind_r])) 
				ind_l = i;
		if (ind_l == 1000)
		{
			ind_r--;
			continue;
		}
		
		answer[answer_len].a = ind_l + 1;
		answer[answer_len].b = ind_r + 1;
		answer_len++;
		double x = arr[ind_l];
		arr[ind_l] = arr[ind_r];
		arr[ind_r] = x;
	}

	printf("%d\n", answer_len);

	for (int i = 0; i < answer_len; i++)
	{
		printf("%d %d\n", answer[i].a, answer[i].b);
	}
	return 0;
}