#include "eulertools.h"

#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

vector<int> abundants;
vector<int> primes;

void get_abundants(int n)
{

  for (int i = 2; i <= n; i++){
    vector<int> divs = euler::getAllDivisors(i,primes);

    int sum = -i;
    for (auto& d : divs) sum += d;

    if (sum > i){
  //    cout <<"Abundant found: "<<i << " "<<sum<<endl;
      abundants.push_back(i);
    }
  
  }

}

long count_nums(int Nmax = 28123)
{
  vector<int> has_sum(Nmax+1);
  euler::getListOfPrimes(Nmax+1,primes);
  get_abundants(Nmax);
  for (auto iter = abundants.begin(); iter!=abundants.end(); iter++){
      if ( 2*(*iter)>Nmax) break;
    for (auto iter2 = iter; iter2!=abundants.end(); iter2++){
      if ( (*iter)+(*iter2) > Nmax) break;
      has_sum[(*iter)+(*iter2)] = 1;
    }

  }

  long sum = 0;
  for (unsigned int i = 1; i<=Nmax; i++){
    sum += (!has_sum[i])*i;
  }
  return sum;
}


int main(){

  long sum = count_nums();
  cout <<"The sum of all pos. integers that can't"<<endl;
  cout <<"be written as the sume of two abundant numbers is"<<endl;
  cout <<sum<<endl;
  return 0;
}
