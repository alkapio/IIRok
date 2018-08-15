//Szyfr Atbash - wersja ko�cowa, Alicja Piotrowska L2

#include <iostream>
#include <string>

using namespace std;

int main() {
	string P; 
	int d; 
	int i;
	string C;
		

		cout<<"Podaj wyrazenie do zaszyfrowania:"<<endl;
				getline(cin, P);
				d=P.length()+1; 
				C=P;
				
		//78 - litera N
		//77 - litera M
		
		/*Dziel� alfabet na p� - od A(a) do M(m) i od N(n) do Z(z). */
		//duze litery
		for(i=0;i<d;i++){							
			if(P[i]>=65 && P[i]<78){		//bior� pod uwag� litery A-M	
				C[i]=78+('M'-P[i]); 		//do litery 'N'(78) dodajemy 'odleg�o��' litery kt�r� chcemy zaszyfrowa� od litery 'M' - przechodzimy do 'drugiej' cz�ci alfabetu  
			}
			else if(P[i]>=78 && P[i]<=90){ //bior� pod uwag� litery N-Z
				C[i]=77-(P[i]-'N');	//od litery 'M' odejmuj� 'odleg�o��' litery kt�r� chc� zaszyfrowa� od litery 'N' - tutaj cofamy si� (przechodzimy do 'pierwszej' cz�sci) w alfabecie 
			}
			//male litery
			else if(P[i]>=97 && P[i]<110){ //to co wyzej tylko ma�e litery
				C[i]=110+('m'-P[i]);
			}
			else if(P[i]>=110 && P[i]<=122){
				C[i]=109-(P[i]-'n');
			}
		}
		
		cout<<C<<endl;	

	cout<<"Podaj wyrazenie do odszyfrowania:"<<endl;
				getline(cin, C);
				d=C.length()+1; 
				P=C;
				
		//78 - litera N
		//77 - litera M
		
		/*Dziel� alfabet na p� - od A(a) do M(m) i od N(n) do Z(z). */
		//duze litery
		for(i=0;i<d;i++){							
			if(C[i]>=65 && C[i]<78){		//bior� pod uwag� litery A-M	
				P[i]=78+('M'-C[i]); 		//do litery 'N'(78) dodajemy 'odleg�o��' litery kt�r� chcemy zaszyfrowa� od litery 'M' - przechodzimy do 'drugiej' cz�ci alfabetu  
			}
			else if(C[i]>=78 && C[i]<=90){ //bior� pod uwag� litery N-Z
				P[i]=77-(C[i]-'N');	//od litery 'M' odejmuj� 'odleg�o��' litery kt�r� chc� zaszyfrowa� od litery 'N' - tutaj cofamy si� (przechodzimy do 'pierwszej' cz�sci) w alfabecie 
			}
			//male litery
			else if(C[i]>=97 && C[i]<110){ //to co wyzej tylko ma�e litery
				P[i]=110+('m'-C[i]);
			}
			else if(C[i]>=110 && C[i]<=122){
				P[i]=109-(C[i]-'n');
			}
		}
		
		cout<<P;	


	return 0;
}
