#include <stdio.h>
#include <stdlib.h>


void update(int *a,int *b) {
    // Complete this function
    int value_a , value_b;
    value_a = *a;
    value_b = *b;
    *a = value_a + value_b;
    *b = abs(value_a - value_b);

    return ;

}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
