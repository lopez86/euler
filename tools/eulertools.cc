#include "eulertools.h"

#include <vector>
#include <unordered_set>
#include <map>
#include <cmath>
#include <iostream>
using namespace std;

void
euler::getListOfPrimes(int Nmax,vector<int>& primes,int maxp){


  if (primes.size()>0 && (*(primes.end()-1)>=Nmax || maxp>Nmax)){
    return;
  }

  if (Nmax<2) {
    primes = {};
    return;
  }

  primes = {2};
  if (Nmax==2){
    return;
  }


  int maxval = primes[primes.size()-1] > maxp ? primes[primes.size()-1] +1 : maxp+1;

  for (int i = maxval; i < Nmax+1; i++){
    bool isPrime = true;

    for (auto& p : primes){
      if (i%p==0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime==true) {
      primes.push_back(i);
        
    }
    
  }

  return;
}


vector<int>
euler::getPrimeDivisors(int N, vector<int>& primes, int maxp)
{
  getListOfPrimes(N,primes,maxp);
  for (auto& p : primes){
    if (p > N) break;
    if (p==N) return vector<int>({N});
  }

  vector<int> divs;
  int Ntmp = N;

  for (auto& p : primes){
    if (p > Ntmp) break;
    while(Ntmp%p==0){
      divs.push_back(p);
      Ntmp /= p;
    }


  }

  return divs;

}

vector<int>
euler::getAllDivisors(int N, vector<int>& primes, int maxp){

  vector<int> divs = getPrimeDivisors(N,primes,maxp);

  int ndivs = (int)divs.size();

  int nmax = pow(2,ndivs);
  unordered_set<int> all_divs;

  for (int i = 0; i < nmax; i++){
    int n = 1;
    for (int j = 0; j<ndivs; j++){
      int bit = (i>>j)&1;
      if (bit == 1)
        n *= divs[j];

    }
    all_divs.emplace(n);

  }

  vector<int> div_vec(all_divs.size());
  int i = 0;
  for (auto& d : all_divs){
    div_vec[i] = d;
    i++;
  }

  return div_vec;

}

