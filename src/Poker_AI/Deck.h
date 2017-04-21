#ifndef DECK_H
#define DECK_H

#include <iostream>     // std::cout
#include <algorithm>    // std::random_shuffle
#include <random>       //std::random_generator
#include <vector>       // std::vector
#include <ctime>        // std::time
#include <cstdlib>      // std::rand, std::srand
#include "Card.h"	// Card Class
using namespace std;

class Deck 
{

	public:
		Deck(int i);
		Card Draw_Card();
		int get_cards_left(){return this->cards_left;}
		Card get_deck_member(int i){return this->s_deck[i];}
	private:
		int cards_left = 52;
		vector<Card> s_deck;
};

Deck::Deck(int i)
{
  	vector<int> myvector;
  // set some values:
  	for (int j=0; j<52; ++j) {myvector.push_back(j);} // 1 2 3 4 5 6 7 8 9
	cout<< "Deck constructor called with parameter"<< i<<"\n";
  // using built-in random generator:
	std::random_shuffle( myvector.begin(),myvector.end());
	vector<Card> myDeck;
	for (int j=0;j<52;++j)
	{
		Card *c = new Card(myvector[j]);
 		myDeck.push_back(*c);
	}
	this->s_deck = myDeck;
	this->cards_left = 52;
}


Card Deck::Draw_Card()
{
	this->cards_left -= 1;
	Card c = this->s_deck[this->cards_left];
	(this->s_deck).pop_back();
	return c; 
}
#endif
