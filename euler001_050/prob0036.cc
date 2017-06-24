/* Solution to Project Euler #36
https://projecteuler.net
*/


#include <sstream>
#include <iostream>
#include <vector>
using namespace std;

const char digits[10] = {'0','1','2','3','4','5','6','7','8','9'};

string
convertToBase2(int N){

  long place=0;
  vector<int> v;
  while(N>0){
    v.push_back(N%2);
    place += 1;
    N = N >> 1;
  }
  
  char b2[place+1];
  b2[place] ='\0';
  for (unsigned int i = 0 ; i < v.size();i++){
    b2[v.size()-1-i] = digits[v[i]];
  }
  string base2(b2);
  return base2;
}

bool
isPalindrome(string str){

  for (int i = 0; i <str.size()/2; i++)
    if (str[i] != str[str.size()-1-i]){
      return false;     
    }
  
  return true;
}

long
SumPalindromes(int Nmax=1000000)
{
  long sum = 0;
  for (int i = 1 ; i < Nmax; i++){
    if (i%10 == 0) continue;
    string ibase2(convertToBase2(i));
    if (ibase2[ibase2.size()-1]=='0') continue;

    stringstream ss;
    ss << i;
    string istr = ss.str();
    if (i==585585) cout <<i<<" "<<ibase2<<endl;
    if (isPalindrome(istr) && isPalindrome(ibase2)){
      cout <<i<<" "<<ibase2<<endl;
      sum += i;
    }
   
  }
  return sum;
}

int main()
{
  std::cout <<"Sum of all (base10 & base2) palindromes: "<<SumPalindromes()<<std::endl;
  return 0;
}
