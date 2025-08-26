#include <stdio.h>
void sort(int *pa, int size);
void print_array(int *pa, int size);
void swap(int *pa, int *pb);
int main(void)
{
	int N;
	scanf("%d", &N);
	int array[N];

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
	}
	// 오름차순 정렬
	// 오른쪽으로 갈수록 커져야 한다
	// 인접한 두 요소 비교해
	// 만약 왼쪽이 더 크면 오른쪽 값과 치환
	sort(array, N);
	print_array(array, N);

	return 0;
}
void sort(int *pa, int size)
{
	for (int j = 1; j < size; j++)
	{
		for (int i = 0; i < size - j; i++)
		{
			if (*(pa + i) > *(pa + i + 1))
			{
				swap(pa + i, pa + i + 1);
			}
		}
	}
}
void swap(int *pa, int *pb)
{
	int temp = *pa;
	*pa = *pb;
	*pb = temp;
}
void print_array(int *pa, int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", pa[i]);
	}
	printf("\n");
}
