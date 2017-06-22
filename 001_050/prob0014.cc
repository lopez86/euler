/**
Solution to Project Euler prob 14
https://projecteuler.net/

compile with: g++ -o prob0014.exe prob0014.cc
*/

#include <cmath>
#include <iostream>
using std::cout;
using std::endl;

int main()
{
  int max = 1000000;
  int maxlength = 0;
  int bestval = 0;
  for (int i = 2; i < max; i++){
    long cur_val = i;
    int len = 1;
    while(cur_val >=1){
      if (cur_val<=1) break;
        
      if (cur_val%2 == 0){
        cur_val /= 2;
      }else{
        cur_val = 3* cur_val + 1;
      }
      len++;
    }
    if (len > maxlength){
      maxlength = len;
      bestval = i;
    }
  }
  cout <<"The best value is "<<bestval<<" length: "<<maxlength<<endl;


}

