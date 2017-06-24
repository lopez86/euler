#include "eulertools.h"

#include <vector>
#include <unordered_set>

#include <iostream>
using namespace std;
int main()
{
  
  euler::buildListOfPrimes(20);
  cout <<"Primes <= 20: "<<endl;
  for (auto& p : euler::get_primes()){
    cout <<p<<" ";
  }
  cout << endl;

  euler::buildListOfPrimes(40);
  cout <<"Primes <= 40: "<<endl;
  for (auto& p : euler::get_primes()){
    cout <<p<<" ";
  }
  cout << endl;
  
  
  int gcd = euler::GCD(12,18);
  cout <<endl<<"GCD of 12 and 18: "<<gcd<<endl;

  int lcm = euler::LCM(12,18);
  cout <<endl<<"LCM of 12 and 18: "<<lcm<<endl;

  return 0;
}



