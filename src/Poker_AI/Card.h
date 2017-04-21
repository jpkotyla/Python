#ifndef CARD_H
#define CARD_H

#include <iostream>
using namespace std;

char SUITS[4] = {'C','D','H','S'};
int ALL_RANKS[13] = {2,3,4,5,6,7,8,9,10,11,12,13,14};

class Card
{
	public:
		Card(int i)
		{	this->suit = SUITS[i%4];
			this->rank = ALL_RANKS[i%13];
		}
		int get_rank(){return this->rank;}
		char get_suit(){return this->suit;}
		void show(){cout << this->rank<<this->suit;}
	private:
		char suit;
		int rank;
};

#endif
