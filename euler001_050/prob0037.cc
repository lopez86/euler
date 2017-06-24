/* Solution to Project Euler #37
https://projecteuler.net
*/


#include "eulertools.h"

#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

long
TrunctableSum(){

  int nfound=0;
  cout <<"Building list"<<endl;
  euler::buildListOfPrimes(1000000);
  cout <<"Done"<<endl;
  vector<int> v = euler::get_primes();
  long sum = 0;
  for (auto& p : v){
    if (p<10) continue;
    int lshift = p;
    int rshift = p;
    int nplaces=static_cast<int>(log10(p))+1;
    int pten = pow(10,nplaces-1);
    bool isTrunctable = true;
    while(lshift>0&&rshift>0){
      int test1 = lshift;
      lshift = lshift % pten;
      pten/=10;
      rshift = rshift/10;

      if (lshift!=0 && find(v.begin(),v.end(),lshift)==v.end()){
        isTrunctable = false;
        break;
      }
 
      if (rshift!=0 && find(v.begin(),v.end(),rshift)==v.end()){
        isTrunctable = false;
        break;
      }
 

    }  

    if (isTrunctable){
      cout <<"Found one: "<<p<<" count "<<nfound+1<<endl;
      sum += p;
      nfound++;
    }
    if (nfound==11) break;

  }

  return sum;
}

int main(){
  cout <<"Sum of trunctable primes: "<<TrunctableSum()<<endl;
  return 0;

}
