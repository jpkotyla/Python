#ifndef ROUND_H
#define ROUND_H

#include <iostream>
#include "Card.h"
#include "Deck.h"
class Round
{
	public:
		// Initalizer
		Round();
		~Round();
		// Get functions
		//Card get_flop()[3]{return this->flop;}
		Card get_turn(){return this->turn;}
		Card get_river(){return this->river;}
		// Set functions
		void set_Deck(Deck d){this->deck = d;}
		int set_flop();
		int set_turn();
		int set_river();
		// Display function
		int display_hand();
	private:
		Deck deck;
		Card flop[3];
		Card turn;
		Card river;
};

// Setter Functions

int Round::set_flop()
{
	for (int i; i < 3; i++)
	{
		this->flop[i] = (this->deck).Draw_Card();
	}
	return 0;
}

int Round::set_turn()
{
	this->turn = (this->deck).Draw_Card(); // Returns a Card Object
	return 0;
}

int Round::set_river()
{
	this->river = (this->deck).Draw_Card();
	return 0;
}

int Round::display_hand()
{
	for(int i = 0; i < 3 ;i++)
	{
		cout << flop[i].get_rank() << flop[i].get_suit() << " ";
	}
	
	cout << turn.get_rank() << turn.get_suit()<<" ";
	cout << river.get_rank() << river.get_suit();
	return 0;
}

#endif
