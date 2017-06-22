/**
Solution to Project Euler prob 21 in C++
https://projecteuler.net

to compile:
g++ -std=c++1y -o prob0021 prob0021.cc 

to run:
prob0021 N
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;


static vector<int> primes = {2};
static int prime_max = 2;


void GetPrimes(int Nmax){

  if (prime_max >= Nmax) return;

  for (int i = prime_max+1; i< Nmax; i+=2){
    bool isPrime = true;
    for (auto p : primes){
      if (i % p == 0){
        isPrime = false;
        break;
      }
   
    }//loop over primes
    if (isPrime) {
      primes.push_back(i);
#ifdef DEBUG
      cout <<"Adding prime: "<<i<<endl;
#endif
    }
  }//loop over divisors of nmax

#ifdef DEBUG
  cout <<"List of Primes <= sqrt of: " <<Nmax<<endl;
  for (auto p : primes) cout<<p<<" ";  
  cout << endl;
#endif

  prime_max = Nmax;

}

int GetSum(int N){

  GetPrimes(static_cast<int>(sqrt(N))+1);

  // Get divisors
  unordered_map<int,int> divisors;
  vector<int> divs;
  for (auto p : primes){
    if (p > sqrt(N)) break;
    int count = 0;
    while(N%p == 0){
      count += 1;
      N /= p;
      divs.push_back(p);
    }
    if (count > 0) {
      divisors[p] = count;//not really using this anymore but left it in as an example
      //divs.push_back(p);
    }
  }
  if (N>1){ // N is prime
    divisors[N] = 1;
    divs.push_back(N);
  }
#ifdef DEBUG
  cout <<"N = "<<N<<endl;
  for (auto& kv : divisors){
    cout <<"\tPrime: "<<kv.first << " num: "<<kv.second<<endl;
  }
#endif

  int sum = 0;
  int ndivisors = 0;
  long n = pow(2,divs.size());
#ifdef DEBUG
  cout <<"Divisors of "<<N<<endl;
#endif
  unordered_set<int> divs_tmp;
  for (unsigned int i = 0; i < n-1; i++){//1 to get proper divisors    
    int divisor = 1;
    for (unsigned int j = 0; j < divs.size(); j++){
      int fac =  ( (i>>j)& (1) ) * divs[j];
      if (fac>0) divisor*= fac;
    }

    divs_tmp.emplace(divisor);
  }

  for (auto& d : divs_tmp){
    sum += d;
  }

#ifdef DEBUG
  cout <<endl;
  cout <<"d("<<N<<") = "<<sum<<endl;
#endif

  return sum;
}


void AmicableNumbers(const int N){
  GetPrimes(N);
  vector<int> sums(N);
  long amicable_sum = 0;
  for (int i = 2; i < N; i++){
    if (sums[i] == 0)
      sums[i] = GetSum(i);

    if ( (sums[i] <= 1) || (sums[i]>=N) ) 
      continue;//primes are not amicable


    if (sums[sums[i]] == 0) sums[sums[i]] = GetSum(sums[i]);
    if ((sums[sums[i]] == i) && sums[i] != i){
      cout <<"Amicable pair: "<< i<<" "<<sums[i]<<endl;
      amicable_sum += i;
    }

  }
  cout <<"Sum of amicable numbers below "<<N<<": "<< amicable_sum<<endl;

}


int main(int argc,const char* argv[]){

  if (argc < 2){
    cout <<"Usage: prob0021.exe N"<<endl;
    return -1;
  }

 // GetSum(220);
  int N = atoi(argv[1]);
  AmicableNumbers(N);

}
