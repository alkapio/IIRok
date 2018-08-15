#include <iostream>
#include <cstdlib>
#include <time.h>
#include <bitset>

using namespace std;


int main() {
string P, K;
int d; //dlugosc 
srand(time(NULL));
int i;
char znak;
string B;

cout<<"Podaj zwrot do zaszyfrowania:"<<endl;
getline(cin, P);
d=P.length();


bitset<CHAR_BIT> C[d];
bitset<CHAR_BIT> letter[d];
bitset<CHAR_BIT> letterKey[d];

cout<<"Postac binarna tekstu jawnego:"<<endl;
for(i=0;i<d;i++)
{
	cout<<bitset<CHAR_BIT>(P[i])<<" ";
	letter[i] = bitset<CHAR_BIT>(P[i]);
	}
cout<<endl;	

//klucz tworzymy losowo z zakresu liter a-z
for(i=0;i<d;i++){
	znak = 'a' + (rand()%('z'-'a' + 1));
	K[i] = znak;
}
cout<<"Klucz:"<<endl;
for(i=0;i<d;i++)
	cout<<K[i];
cout<<endl;


cout<<"Postac binarna klucza:"<<endl;
for(i=0;i<d;i++)
	{
			cout<<bitset<CHAR_BIT>(K[i])<<" ";
			letterKey[i] = bitset<CHAR_BIT>(K[i]);
		}	
	cout<<endl;

cout<<"Szyfrogram:"<<endl;
for(i=0; i<d;i++){
		C[i]=((letter[i]^letterKey[i]));
		cout<<C[i]<<" ";
}	


	return 0;
}
