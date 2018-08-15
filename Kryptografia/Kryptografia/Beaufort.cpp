//Alicja Piotrowska, L2, Szyfr Beauforta
#include <iostream>

using namespace std;

int main() {
	//char tabRect[26][26];
	int i, j=0;
	int d; //dlugosc szyfrogramu
	int x; //dlugosc klucza
	string P, C; //tekst jawny, szyfrogram
	string klucz;
	char litera;
	
	cout<<"Podaj haslo do zaszyfrowania:"<<endl;
	getline(cin, P);
  	d=P.length();

	cout<<"Podaj klucz:"<<endl;
	getline(cin, klucz);
  	x=klucz.length();	
	
	
	for(i=0;i<d;i++){
		if(P[i]>=65 && P[i]<=90){ //wielkie litery
			if(klucz[j]>=P[i])
				litera = (klucz[j]-P[i])+65;
			else
				litera = 91-(P[i]-klucz[j]);	
		}
		if(P[i]>=97 && P[i]<=122){	//ma³e litery
			if(klucz[j]>=P[i])
				litera = (klucz[j]-P[i])+97;
			else
				litera = 123-(P[i]-klucz[j]);
		}
			 
		cout<<litera;
		
	j++;			
	if(j==x)		//jesli 'j' jest rowne dlugosci klucza to zerujemy jej wartosc, aby liczba liter tekstu jawnego pokrywala sie z liczba liter klucza
		j=0;
	}
	j=0; //zerujemy licznik liter dla klucza
	
	cout<<endl<<endl<<endl;
	
	
	cout<<"Podaj szyfrogram do odszyfrowania:"<<endl;
	getline(cin, C);
  	d=C.length();

	cout<<"Podaj klucz:"<<endl;
	getline(cin, klucz);
  	x=klucz.length();
  	
  	for(i=0;i<d;i++){
		if(C[i]>=65 && C[i]<=90){ //wielkie litery
			if(klucz[j]>=C[i])
				litera = (klucz[j]-C[i])+65;
			else
				litera = 91-(C[i]-klucz[j]);	
		}
		if(C[i]>=97 && C[i]<=122){	//ma³e litery
			if(klucz[j]>=C[i])
				litera = (klucz[j]-C[i])+97;
			else
				litera = 123-(C[i]-klucz[j]);
		}
			 
		cout<<litera;
		
	j++;
	if(j==x)
		j=0;
	}
  	
  	
  	
  	
	return 0;
}
