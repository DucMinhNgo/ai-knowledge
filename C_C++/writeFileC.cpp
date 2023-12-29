#include <stdio.h>

int main()
{
    FILE *fp = fopen("data.ahihi", "w");
    char ch[] = "Hello";
    if (fp)
    {
        if (fputs(ch, fp) != EOF)
        {
            printf("In thanh cong");
        }
    }
    fclose(fp);
    return 0;
}