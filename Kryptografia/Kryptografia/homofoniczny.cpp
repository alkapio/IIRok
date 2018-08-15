//Alicja Piotrowska, L2, Szyfr homofoniczny
#include <iostream>
#include <cstdlib>
#include <map>

using namespace std;

int main() {
	int i;
	int n=0;
	string P; //tekst jawny
	int d; //dlugosc tekstu
	string C; //szyfrogram
	char litera;
	char tablica[26][1] = {};
	
	//map<char, int[2]> alfabet{{'a', 0}, {'b', 0}};

	

      cout<<"Podaj wyrazenie do zaszyfrowania:"<<endl;
      getline(cin, P);
      d=P.length();

	
/*	for(i=0;i<d;i++) 	
	{
		if(P[i])
		n++;
				
	}*/
	return 0;
}
