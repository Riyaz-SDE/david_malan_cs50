#include <stdio.h>

typedef __UINT8_TYPE__ BYTE;
int main (int argc, char* argv[]){
    FILE *src = fopen(argv[1],"rb");
    FILE *dst = fopen(argv[2],"wb");
    BYTE b;
    while (fread(&b,sizeof(b),1,src) != 0)
    {
        /* code */
        fwrite(&b,sizeof(b),1,dst);
    }
    fclose(src);
    fclose(dst);
    printf("%s %s", argv[1], argv[2]);
    return 0;
}