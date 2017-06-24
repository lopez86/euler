/* Solution to Project Euler #34
https://projecteuler.net
*/

#include <iostream>
#include <cmath>

int facts[10] = {1,1,2,6,24,120,720,5040,40320,362880};

bool
IsDigitFactorial(int N){
  
  int Ndig = 0;
  int n = N;
  while(n>0){
    Ndig+=1;
    n/=10;
  }

  int sum = 0;
  int M = N;
  for (int i = 0; i < Ndig; i++){
    sum += facts[M%10];
    M /= 10;
  }
  return sum==N;
}

long
GetSum(){
  long sum = 0;
  for (long i = 3; i<2540161; i++){//2540161 = 7 * 9! (for 9999999)
    sum += IsDigitFactorial(i)*i;
  }
  return sum;
}


int main(){

  std::cout <<"The sum of all digit factorials is "<<GetSum()<<std::endl;

  return 0;
}
