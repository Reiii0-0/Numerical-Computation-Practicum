#include <stdio.h>
#include <math.h>

double f(double x)
{
    return sin(x);
}

double IntegrasiRomberg(double a, double b, int n)
{
    double R[n][n];

    for (int i = 0; i < n; i++)
    {
        int N = pow(2, i + 1);
        double h = (b - a) / N;
        double sum = 0.5 * (f(a) + f(b));
        for (int j = 1; j < N; j++)
        {
            sum += f(a + j * h);
        }
        R[i][0] = h * sum;
    }

    for (int j = 1; j < n; j++)
    {
        for (int i = j; i < n; i++)
        {
            double factor = pow(4, j);
            R[i][j] = (factor * R[i][j - 1] - R[i - 1][j - 1]) / (factor - 1);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("%12.10f ", R[i][j]);
        }
        printf("\n");
    }

    return R[n - 1][n - 1];
}

int main()
{
    double a, b;
    int n;

    printf("Masukkan batas bawah integral (a): ");
    scanf("%lf", &a);
    printf("Masukkan batas atas integral (b): ");
    scanf("%lf", &b);
    printf("Masukkan jumlah tingkat Romberg (n): ");
    scanf("%d", &n);

    double result = IntegrasiRomberg(a, b, n);
    printf("\nHasil integrasi Romberg: %.10f\n", result);

    getchar();
    getchar();

    return 0;
}
