/*https://codeforces.com/problemset/problem/1910/G?locale=en*/

#include <stdio.h>

int main()
{
	int c;
	scanf_s("%d", &c);

	for (int i = 0; i < c; i++)
	{
		int n, t, t1, t2, s1, s2;
		scanf_s("%d%d", &n, &t1);
		t2 = -1;
		s2 = 2000000000;
		s1 = t1 * 2;
		char answer;
		answer = 1;
		for (int j = 0; j < n - 1; j++)
		{
			scanf_s("%d", &t);
			if (answer == 0)
				continue;
			if (t > s1 || t > s2 || (t2 != -1 && t != s1 && t != s2))
				answer = 0;
			if (t == s1)
				s1 += t1;
			if (t == s2)
				s2 += t2;
			if (t2 == -1 && t % t1 != 0)
			{
				t2 = t;
				s2 = t2 + t;
			}	
		}
		if (answer)
			printf("VALID\n");
		else
			printf("INVALID\n");
	}
	return 0;
}