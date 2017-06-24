/* Solution to Project Euler # 33
https://projecteuler.net


*/
#include <iostream>
#include <vector>
#include <utility>
#include "eulertools.h"
using namespace std;

bool 
IsDigitCancelling(int num, int denom){
  int num_0 = num%10;
  int num_1 = num/10;
  int denom_0 = denom%10;
  int denom_1 = denom/10;
  if (num==denom || (num_0==0 && denom_0==0)) return false;//trivial case
  

  if (num_0 == denom_0 &&
      num_1 * denom == denom_1 * num)
      return true;

  if (num_1 == denom_1 &&
      num_0 * denom == denom_0 * num)
      return true;
  
  if (num_0 == denom_1 &&
      num_1 * denom == denom_0 * num)
      return true;
  
  if (num_1 == denom_0 &&
      num_0 * denom == denom_1 * num)
      return true;
  
  return false;
}


vector<pair<int,int> >
GetDigitCancellingFracs(){

  vector<pair<int,int> > fracs;  

  for (int denom=11; denom<100; denom++)
    for (int nom=10; nom<denom; nom++)
      if (IsDigitCancelling(nom,denom)){
        cout <<"Found digit cancelling "<<nom<<" / "<<denom<<endl;
        fracs.push_back(make_pair(nom,denom));
      }
  return fracs;
}

pair<int,int>
ReduceFracs(const vector<pair<int,int> >&fracs){

  // First multiply
  int nom=1, denom=1;
  for (auto& f : fracs){
    nom *= f.first;
    denom *= f.second;
  }
  cout <<"Nom: "<<nom<<" denom: "<<denom<<endl;
  int gcd = static_cast<int>( euler::GCD(nom,denom));
  nom /= gcd;
  denom /= gcd;

  return make_pair(nom,denom);
}

int main(){

  euler::buildListOfPrimes(100);

  vector<pair<int,int> > fracs =
       GetDigitCancellingFracs();
  
  pair<int,int> frac = ReduceFracs(fracs);

  cout <<"The product of the digit cancelling fractions"<<endl;
  cout <<" is equal to "<<frac.first<<" / "<<frac.second<<endl;

}
