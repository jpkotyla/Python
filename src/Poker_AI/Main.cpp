#include <iostream>
#include "Deck.h"
#include "Card.h"
#include "Pot1.h"
#include "Round.h"

#include <algorithm>    // std::random_shuffle
#include <random>       //std::random_generator
#include <vector>       // std::vector
#include "time.h"

using namespace std;

struct RNG {
    int operator() (int n) {
        return std::rand() / (1.0 + RAND_MAX) * n;
    }
};


int main()
{	
	srand(time(0));
	Pot *p1 = new Pot(0,1,2);
	Round *r1 = new Round(8);
	r1->set_flop();
	srand(3);		
	vector<int> myvector;
        for (int j=0; j<53; ++j) {myvector.push_back(j);}
	for (std::vector<int>::iterator it = myvector.begin();it!=myvector.end();it++)
	{	
		cout << "  "<<*(it)<<"  ";
	}
	std::random_shuffle(myvector.begin(),myvector.end(),RNG());
	
	for (std::vector<int>::iterator it = myvector.begin();it!=myvector.end();it++)
	{	
		cout << "  "<<*(it)<<"  ";
	}
	cout<<"\n";
	Card *c1 = new Card(myvector[1]);
	//c1->show();
	r1->display_hand(3);	
	cout << "\n";	
	return 0;
}

