#include <iostream>
using namespace std;
int main () {
int v1 = 5 , v2 = 15 ;
int *p1 , *p2 ;
p1 = &v1 ;
p2 = &v2 ;
*p1 = 10 ;  // v1=10
*p2 = *p1 ; // v2=10
p1 = p2 ;  
*p1 = 20 ;  // v1=20
cout << " v1 ␣=␣" << v1 << "\n" ;
cout << " v2 ␣=␣" << v2 << "\n" ;
return 0 ;
}