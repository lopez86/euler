/* Solution to Project Euler #35
https://projecteuler.net
*/


#include "eulertools.h"
#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>

using std::cout;
using std::endl;

int countCircularPrimes(int N=1000000){
  cout <<"Building primes"<<endl;
  euler::buildListOfPrimes(N);
  std::vector<int> primes = euler::get_primes();
  cout <<"Done. # of primes: "<<primes.size()<<endl;
  int count = 0;
  int np = 0;
  for (auto& p : primes){
    if (np%10000==0) cout <<" on prime # "<<np<<endl;
    np++;
    int ptmp = p;
    int ndigits = 0;
    while(ptmp>0){
      ndigits++;
      ptmp/=10;
    }
    bool isCircular = true;
    int ptest = p;
    for (int i = 0; i < ndigits-1; i++){
      int tens = pow(10,ndigits-1);
      ptest = 10 * (ptest % tens) + (ptest/tens);
      if ( std::find(primes.begin(),primes.end(),ptest)==primes.end()){
        isCircular = false;
        break;
      }
    }
   
    if (isCircular)
      count++;

  }

  return count;
}

int main(){

 std::cout <<"# of circular primes: "<< countCircularPrimes()<<std::endl;

}
