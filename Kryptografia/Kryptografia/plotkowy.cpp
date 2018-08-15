//szyfr p³otkowy przestawieniowy
#include <iostream>

using namespace std;

int main() {
	int n=1, x, i, j, d, y, z=0;
	string P;
	string C;
	int wiersz = 0;
	string szyfrogram;
	
	
	cout<<"Podaj zwrot do zaszyfrowania:"<<endl;
    getline(cin, P);	
	d=P.length(); //d = dlugosc zwrotu
	cout<<"Podaj w ilu wierszach zaszyfrowaæ zwrot:"<<endl;
	cin>>x; 		//x = ilosc wierszy
	if(x>(d/2)) {		//liczba wierszy nie moze byc zbyt duza w stosunku do dlugosci zwrotu do zaszyfrowania 
	cout<<"Zbyt duzo wierszy"<<endl;

		do{
			cout<<"Podaj ponownie w ilu wierszach zaszyfrowaæ zwrot:"<<endl;
			cin>>x;
			}while(x>(d/2));
	
	}
	y = (d/x)+2;
	
	for(i=0, j=x; i<y; i++){
		while(j>0 && z<d){
			j--;
			C[j]=P[z];
			z++;
		}
		while(j<x && z<d){
			C[j] = P[z];
			z++;
			j++;
		}
		i++;
	}
		for(i=0;i<d;i++)
		cout<<C[i];
	
	
	
	
	
	
	return 0;
}
