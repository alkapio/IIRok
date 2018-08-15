//Szyfr Bacona, Alicja Piotrowska, L2
#include <iostream>
#include <cstring>

using namespace std;

int main() {
	int i, j=0, n=0;
	int d; //dlugosc szyfrogramu
	string P;
	char znak;
	char alfabet[26]={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	string kod[26]={"aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "abaaa", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab", 
					"abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb", "baabb", "babaa", "babab", "babba", "babbb"};
	
	cout<<"Podaj haslo do zaszyfrowania:"<<endl;
	getline(cin, P);
  	d=P.length();
  	
  	//Jedna litere w szyfrze zastepuje 5 liter, wiec sprawdzamy ile liter zawiera tekst jawny (+5) i ile innych znakow jak np. spacji (+1)
  	for(i=0; i<d; i++){
  		if((P[i]>64 && P[i]<91) || (P[i]>96 && P[i]<123))
  			n+=5;
  		else
		  	n+=1;	
	  }
	  string C[n]; //szyfrogram 
	  
	  for(i=0;i<d;i++){
	  		if((P[i]>64 && P[i]<91) || (P[i]>96 && P[i]<123)){
	  			if(P[i]>96 && P[i]<123)  
	  				{
	  					znak = P[i];
	  					j = znak - 97;
	  					C[i] = kod[j];  
					}
	  			if(P[i]>64 && P[i]<91) 	 
				  	{
					  znak = P[i]+32;
					  j=znak - 97;
					  C[i] = kod[j];  
					  
					  }									  			
			  }
			else
				C[i] = P[i];  
			
	  }
	
	for(i=0; i<d;i++){
		cout<<C[i]<<" ";
	}
	
	
	
	return 0;
}
