#ifndef ROUND_H
#define ROUND_H

#include <iostream>
#include "Card.h"
#include "Deck.h"
class Round
{
	public:
		// Initalizer
		Round(int i); 
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
		void display_hand(int j);
	private:
		Deck deck = *(new Deck(18));
		Card flop[3] = {deck.Draw_Card(),deck.Draw_Card(),deck.Draw_Card()};
		Card turn = deck.Draw_Card();
		Card river = deck.Draw_Card();
};
// Initializer
Round::Round(int i)
{
	this->deck = *(new Deck(i));
	for(int i =0; i<3; i++)
	{
		this->flop[i] = this->deck.Draw_Card();
	}
	this->turn = (this->deck).Draw_Card();
	this->river = (this->deck).Draw_Card();
}

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

void Round::display_hand(int j)
{
	for(int i = 0; i < 3 ;i++)
	{
		if (i< j ){cout << flop[i].get_rank() << flop[i].get_suit() << " ";}
	}
	if(j>3){cout << turn.get_rank() << turn.get_suit()<<" ";}
	if(j>4){cout << river.get_rank() << river.get_suit();}
	return;
}

#endif
