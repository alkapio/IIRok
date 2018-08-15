//Alicja Piotrowska, L2, Szyfr ROT 13
#include <iostream>

using namespace std;

int main() {
	string P, C;
	int d, i, x;
		
	
	cout<<"Podaj tekst do zaszyfrowania: ";    
	getline(cin, P);
	d = P.length();

	for(i=0; i<d; i++){
		//duze litery
		if(P[i]>64 && P[i]< 91){
			if(P[i]+13<=90)
				C[i]=P[i]+13;
			else							//jesli sie okaze ze po dodaniu 13 do wartosci naszej litery wyjdziemy poza zakres liter, musimy zaczac liczyc od poczatku liter
				C[i] = 64+(13-(90-P[i]));			
		}
		//male litery
		if(P[i]>96 && P[i]<123){
			if(P[i]+13<=122)
				C[i]=P[i]+13;
			else
				C[i]= 96+(13-(122-P[i]));
			
		}
				
	cout<<C[i];	
	}
	
	cout<<endl<<endl<<endl;
	cout<<"Podaj tekst do odszyfrowania: ";    
	getline(cin, C);
	d = P.length();

	for(i=0; i<d; i++){
		//duze litery
		if(C[i]>64 && C[i]< 91){
			if(C[i]-13>=65)
				P[i]=C[i]-13;
			else							//jesli sie okaze ze po odjeciu 13 od wartosci naszej litery wyjdziemy poza zakres liter, musimy zaczac liczyc od konca liter
				P[i] = 91 - (13-(C[i]-65));			
		}
		//male litery
		if(C[i]>96 && C[i]<123){
			if(C[i]-13>=97)
				P[i]=C[i]-13;
			else
				P[i]= 123-(13-(C[i]-97));
			
		}
				
	cout<<P[i];	
	}
	
	return 0;
}
