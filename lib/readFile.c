#include <stdio.h>
#include <stdlib.h>

char *readFile(char *filePath) {
    int c;
    int fileSize = 0;
    char *chars;
    FILE *file = NULL;

    printf("File Path: %s\n", filePath);
    file = fopen(filePath, "rb");

    if (file) {
        while ((c = getc(file)) != EOF) {
            ++fileSize;
        }
        printf("File Size: %d bytes\n", fileSize);
        fclose(file);
        chars = malloc(fileSize * sizeof(int));
        file = fopen(filePath, "rb");
        int i = 0;
        while ((c = getc(file)) != EOF) {
            chars[i] = c;
            ++i;
        }
        fclose(file);
    }

    return chars;
}

//int main() {
//    char *filePath = "/Users/xiyuexin/Workspace/WebImpact-Private-Project/Python-Web-APIs/Flask/index.py";
//    char *content = readFile(filePath);
//    printf("%s", content);
//    return 0;
//}