/// Michal Franczyk i Alicja Piotrowska

#include <iostream>
#include <string>
#include <fstream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main()
{
    string P; /// Tekst jawny.
    string C; /// Szyfrogram

    int d; /// dlugosc szyfrowania;
    int option,option2; /// Do switchy
    fstream plik;

    int i,licznik, x, y;
    char znak;
    int ilosc[40];

    cout<<"MENU"<<endl;
    cout<<"1. Zaszyfruj"<<endl;
    cout<<"2. Odszyfruj z pliku"<<endl;
    cout<<"3. Odszyfruj"<<endl;
    cout<<"4. Exit"<<endl<<endl;

    option = 0;
    while(option != 4)
    {
        cout<<"Podaj opcje: ";
        cin>>option;
        switch(option)
        {
        case 1:
            {
                cout<<"Podaj tekst do zaszyfrowania: ";
                cin.ignore( 1, '\n' ); /// Funkcja getline, bez tej linii przed nia, nie dziala w switchu.
                getline(cin, P);

                d = P.length();

                C = P;
                i = 0;
                cout<<"Tekst jawny: "<<P<<endl;

                /// Szyfrowanie
                while(i<d)
                {

                    /// Duze litery
                   if(P[i] >= 65 && P[i] <= 87)
                   {
                        C[i] = P[i] + 3;
                   }

                    else if(P[i] >= 88 && P[i] <= 90)
                   {
                       C[i] = P[i] - 23;
                   }
                    /// Male litery
                   else if(P[i] >= 97 && P[i] <= 119)
                   {
                        C[i] = P[i] + 3;
                   }

                   else if(P[i] >= 120 && P[i] <= 122)
                   {
                       C[i] = P[i] - 23;
                   }
                i++;
                }
             /// Zapis szyfru do pliku.

                plik.open("zaszyfrowane.txt", ios::app);
                ///plik.open( "zaszyfrowane.txt", ios::in | ios::out );
                if( plik.good() != true )
                {
                    cout << "Cos poszlo nie tak xD" << endl;
                    exit(1);
                }

                plik<<C<<endl;

                plik.close();

                cout<<"Szyfrogram: "<<C;
                break;

            }
        case 2:
            {
                /// Deszyfrowanie
                /// odczyt szyfru z pliku.

                plik.open( "zaszyfrowane.txt", ios::in | ios::out );

                /// Zliczamy liczbe wierszy
                licznik = 0;

                while(getline(plik, C)) /// Pobiera linie z pliku i zapisuje ja do zmiennej C(szyfrogramu).
                {
                    ilosc[licznik] = C.length();
                    licznik++;
                }

                if(licznik == 0) exit(1);
                //if(licznik == 1) licznik++;
                //licznik--;  /// ze wzgledu na znak nowej linii na koncu ostatniego wiersza;

                char **tabC = new char * [licznik]; /// Alokacja pamieci, tablica wskaznikow.

                /// Alokowanie pamieci, tablicy dla kazdego szyfrogramu zapisanego w pliku.
                for(i = 0; i<licznik; i++)
                {
                    tabC[i] = new char [ilosc[i]];
                }

                plik.close();

                /// Otwieramy ponownie plik, aby przesunac wskaznik na poczatek pliku.

                plik.open( "zaszyfrowane.txt", ios::in | ios::out );    /// Tryb do zapisu i odczytu.
                if( plik.good() != true )
                {
                    cout << "Cos poszlo nie tak xD" << endl;
                    exit(1);
                }

                /// Kopiowanie z typu string do zmiennej typu char, dla wszystkich zaszyfrowanych informacji z pliku.
                i = 0;
                while(getline(plik, C))
                {
                    //cout<<"Tyle: "<<C.length()<<endl;;
                    //tabC[i] = new char [C.lenght()];
                    for(x=0;x<ilosc[i];x++)
                    {
                        tabC[i][x] = C[x];
                    }
                    i++;
                }

                ///
                cout<<endl;
                cout<<"Szyfry"<<endl;
                for(i=0; i<licznik; i++)
                {
                    cout<<i+1<<". ";
                    for(x=0; x<ilosc[i]; x++)
                        cout<<tabC[i][x];
                    cout<<endl;
                }

                cout<<"Wybierz szyfr do rozszyfrowania: ";
                cin>>option2;   /// Wybieramy szyfrogram.

                plik.close();

                C = tabC[option2-1];    /// tabC jest to tablica dwuwymiarowa, zawierajaca szyfrogramy.
                                        /// W tym przypadku, przypisujemy do C, wybrany szyfrogram.
                P = C;

                d = ilosc[option2-1];


                i = 0;

                /// Deszyfrujemy wybrany szyfr
                while(i<d)
                {
                    /// Duze litery
                   if(C[i] >= 68 && C[i] <= 90)
                   {


                        P[i] = C[i] - 3;
                   }

                   if(C[i] >= 65 && C[i] <= 67)
                   {
                       P[i] = C[i] + 23;
                   }
                    /// Male litery
                   if(C[i] >= 100 && C[i] <= 122)
                   {
                        P[i] = C[i] - 3;
                   }

                   if(C[i] >= 97 && C[i] <= 99)
                   {
                       P[i] = C[i] + 23;
                   }
                i++;
                }
                system( "cls" );
                /// Wypisujemy tekst jawny i szyfrogram
                cout<<endl<<"Tekst jawny szyfrogramu: ";
                for(x=0; x<d; x++) cout<<C[x];
                cout<<endl<<"To: ";
                for(x=0; x<d; x++) cout<<P[x];

                delete [] tabC;
                break;
            }

        case 3:
            {
                    /// Deszyfrowanie

                    cout<<"Podaj tekst do deszyfrowania: ";
                    cin.ignore( 1, '\n' ); /// Funkcja getline, bez tej linii przed nia, nie dziala w switchu.
                    getline(cin, C);

                    d = C.length();

                    P = C;

                    i = 0;

                    while(i<d)
                    {
                        /// Duze litery
                       if(C[i] >= 68 && C[i] <= 90)
                       {
                            P[i] = C[i] - 3;
                       }

                       if(C[i] >= 65 && C[i] <= 67)
                       {
                           P[i] = C[i] + 23;
                       }
                        /// Male litery
                       if(C[i] >= 100 && C[i] <= 122)
                       {
                            P[i] = C[i] - 3;
                       }

                       if(C[i] >= 97 && C[i] <= 99)
                       {
                           P[i] = C[i] + 23;
                       }
                    i++;
                    }
                system( "cls" );
                cout<<"Tekst jawny szyfrogramu "<<"To: "<<C<<endl<<P<<endl;
                break;
            }
        case 4:
            {
                break;
                exit(1);
            }
        default:
            {
                exit(1);
            }
        }

        cout<<endl<<endl;
        cout<<"MENU"<<endl;
        cout<<"1. Zaszyfruj"<<endl;
        cout<<"2. Odszyfruj z pliku"<<endl;
        cout<<"3. Odszyfruj"<<endl;
        cout<<"4. Exit"<<endl<<endl;

    }

    return 0;
}


