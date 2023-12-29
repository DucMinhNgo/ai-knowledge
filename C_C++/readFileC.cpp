#include <stdio.h>

int main()
{
    FILE *fp = fopen("input.txt", "r");
    if (fp != NULL)
    {
        int c = fgetc(fp);
        while (c != EOF)
        {
            printf("%c", c);
            c = fgetc(fp);
        }
    }

    fclose(fp);
    return 0;
}