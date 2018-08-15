//Alicja Piotrowska, L2, Szyfr Polibiusza
#include <iostream>

using namespace std;

int main(){
int i;
	int n;
	string P; //tekst jawny
	int d; //dlugosc tekstu
	string C; //szyfrogram
	char litera;

        cout<<"Podaj wyrazenie do zaszyfrowania:"<<endl;
        getline(cin, P);
        d=P.length();

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
          cout<<"\n\n\n";
          
          cout<<"Podaj wyrazenie do odszyfrowania:"<<endl;
        	getline(cin, C);
        	d=C.length();
			char *z = new char[d];			
		for(i=0; i<d; i++){
				z[i] = C[i];
		}
		
		for(i=0;i<d;i++){
			if(z[i]!=32){		//rozne od spacji
				if(z[i]==49){	//49 to zapis cyfry 1; czyli jesli pierwsza cyfra szyfrogramu to 1 to wchodzimy do tego ifa
					/*przypisanie zmiennej "litera" wartoœci drugiej cyfry z szyfrogramu [litere tworza dwie cyfry, 
					pierwsza decyduje do ktorego ifa idziemy ^, a ta decyduje jaka litere wypiszemy na ekranie*/
					litera = z[i+=1]; 
					litera+=16; //16, poniewaz litera A to 65, od niej odejmujemy zapis cyfr 1-5 
					if(litera>64 && litera<70) 
					cout<<litera;					
				}
				if(z[i]==50){
					litera = z[i+=1];
					litera+=21; //litera F to 70
					if(litera>69 && litera<76){
					 
					if(litera==73){
						cout<<"I";
					}
						
					else if(litera==74){
						cout<<"K"; //74 to tutaj litera K, a nie J, poniewaz ta tu wystêpuje jakos litera I (ew. litera I jako J)
					}
								
					else
					{
					 cout<<litera;				
					 } 
				}
				}
				if(z[i]==51){
					litera = z[i+=1];
					litera+=27; //litera L to 76
					if(litera>75 && litera<81) 
					cout<<litera;					
				}
				if(z[i]==52){
					litera = z[i+=1];
					litera+=32; //litera Q to 81
					if(litera>80 && litera<86) 
					cout<<litera;					
				}
				if(z[i]==53){
					litera = z[i+=1];
					litera+=37; //litera V to 86
					if(litera>85 && litera<91) 
					cout<<litera;					
				}
				
			}
		}
	delete [] z;
return 0;
}
