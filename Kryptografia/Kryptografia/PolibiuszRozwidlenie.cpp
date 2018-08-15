//Szyfr Polibiusza z rozwidleniem, wersja koñcowa, Alicja Piotrowska L2
#include <iostream>

int main(int argc, char** argv) {
	int i;
	int n;
	string P; //tekst jawny
	int d; //dlugosc tekstu
	string K; //s³owo klucz

        cout<<"Podaj wyrazenie do zaszyfrowania:"<<endl;
        getline(cin, P);
        d=P.length();
        
        cout<<"Podaj s³owo klucz:"<<endl;
        getline(cin, K);

          for(i=0;i<d;i++){
            if(P[i]!=32) //rozne od spacji
			{
							//duze litery						
              if(P[i]>=65 && P[i]<=72){
                    cout<<((P[i]-65)/5)+1;
                    cout<<((P[i]-65)%5)+1<<' ';
                }
              else if(P[i]==73 || P[i]==74){
                    cout<<24<<' ';
               }
              else if(P[i]>=75 && P[i]<=90){
                  cout<<((P[i]-66)/5)+1;
                  cout<<((P[i]-66)%5)+1<<' ';
                }
              //ma³e litery
			  else if(P[i]>=97 && P[i]<=104){
                    cout<<((P[i]-97)/5)+1;
                    cout<<((P[i]-97)%5)+1<<' ';
                }
              else if(P[i]==105 || P[i]==106){
                    cout<<24<<' ';
               }
              else if(P[i]>=107 && P[i]<=122){
                  cout<<((P[i]-98)/5)+1;
                  cout<<((P[i]-98)%5)+1<<' ';
                }
			}
                
          }
	return 0;
}
