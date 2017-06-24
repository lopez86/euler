/**
To compile a shared library:

  g++ -c tools/eulertools.cc -shared -fPIC -std=c++1y -Itools -o eulertools.so

To compile test.cc using the shared library:

  export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
  g++ tools/test.cc -std=c++1y -Itools -L. -leulertools -o test.out
  ./test.out 

To compile a program for test.cc with no library

   g++ tools/test.cc tools/eulertools.cc -std=c++1y -Itools -o test.out
   ./test.out

To compile a static library:

  g++ -c tools/eulertools.cc -std=c++1y -Itools -o eulertools.o
  ar rcs libeulertools.a eulertools.o

To compile test.cc using the static library:

  g++ tools/test.cc -std=c++1y -Itools -L. -leulertools -o test.out
  ./test.out

*/

#ifndef __EULERTOOLS_H__
#define __EULERTOOLS_H__

#include <vector>

namespace euler{

  std::vector<int>& get_primes();

  void clear_primes();
  int prime_bound();

  void buildListOfPrimes(int N);
  std::vector<int> getPrimeDivisors(int N);
  std::vector<int> getAllDivisors(int N);


  long GCD(long n1, long n2);

  long LCM(long n1, long n2);

}

#endif
