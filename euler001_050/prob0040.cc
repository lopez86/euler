/** Solution ro Project Euler #40
https://projecteuler.net
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int GetDigit(int n){

  vector<long> starts(10,0);
  for (int i = 1; i < 10; i++){
    starts[i] = starts[i-1] + pow(10,i)*i - i*pow(10,i-1)+1;
  }

  auto it = upper_bound(starts.begin(),starts.end(),n);

  
  int ndigits = it-starts.begin();
  int nplaces = n - *(it-1);
  if (ndigits==1) nplaces--;
//  cout <<ndigits<<" "<<nplaces<<endl;
  int num = pow(10,ndigits-1) + nplaces / ndigits;
//  cout <<"Num: "<<num<<endl;
  int digit = (num/static_cast<int>(pow(10,ndigits-1-num%ndigits)))%10;
//  cout <<"Digit: "<<digit<<endl;
  return digit;
}

int main(){

  int prod = 1;
  for (int i = 0; i < 7; i++){
    int dig = GetDigit(pow(10,i));
//    cout << dig<<endl;
    prod *= dig;
  }
  cout <<"Product: "<<prod<<endl;

  return 0;
}
