#include <vector>
#include <iostream>
using namespace std;


int main()
{
  const int Ncoin = 8;
  int coins[Ncoin] = {1,2,5,10,20,50,100,200};
  const int N = 200;
  long ncoins[N+1][Ncoin];
  for (int i = 0; i<N+1; i++){
    for (int j = 0; j<Ncoin; j++){
      ncoins[i][j] = 0;
    }
  }
  for (int i =0; i < Ncoin; i++)
    ncoins[0][i] = 1;

  for (int i = 1; i < N+1; i++ )
  {
    long sum = 0;
    for (int j = 0; j<Ncoin; j++){
      if (coins[j]>i) continue;       
      if (coins[j]==i) {
        ncoins[i][j] = 1;
      }
      for (int k = 0; k<=j; k++){
        if (coins[j]+coins[k] > i) continue;
        ncoins[i][j] += ncoins[i-coins[j]][k];
        cout <<i<<" "<<coins[j]<<" "<<coins[k]<<" "<<ncoins[i-coins[j]][k]<<endl;
      }
      sum += ncoins[i][j];

    }
      cout <<i <<" "<<sum<<endl;
  }


  long sum = 0;
  for (int i = 0; i < Ncoin; i++)
    sum+=ncoins[N][i];
  cout <<"There are "<< sum<<" ways to make 200p from the coins."<<endl;

  return 0;




}
