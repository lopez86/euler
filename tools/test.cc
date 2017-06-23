#include "eulertools.h"

#include <vector>
#include <unordered_set>

#include <iostream>
using namespace std;
int main()
{
  
  vector<int> primes;
  euler::getListOfPrimes(20, primes);
  cout <<"Primes <= 20: "<<endl;
  for (auto& p : primes){
    cout <<p<<" ";
  }
  cout << endl;

  return 0;
}



