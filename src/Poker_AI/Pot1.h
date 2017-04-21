/*
Description: Header file for the pot in a poker game.
Author: JohnPaul Kotyla.
Date: Feburary 21, 2016.
*/
#ifndef POT_H
#define POT_H

#include <iostream>

using namespace std;


class Pot
{
	public:
		Pot(float val,float min, float max)
		{
			value = val;
			min_bet = min;
			max_bet = max;
		}
		float get_value();
		float add_to_pot(float bet);
		float get_minimum_bet();
		float get_maximum_bet();
		float change_min_bet(float new_min);
		float change_max_bet(float new_max);	
	private:
		float value;
		float min_bet;
		float max_bet;
};
float Pot::get_value(){return this->value;}

float Pot::get_minimum_bet(){return this->min_bet;}

float Pot::get_maximum_bet(){return this->max_bet;}

float Pot::add_to_pot(float bet)
{
	if ((bet > this->min_bet) && (bet < this->max_bet))
	{
		this->value +=bet;
	}
	else{
		cout<< "Not within Pot limits of";
		cout<< "("<<this->min_bet<<','<<this->max_bet<<")\n";	
	}
	return this->value;
}

float Pot::change_min_bet(float new_min)
{
	if(new_min > 0)
	{
		this->min_bet = new_min;
	} 
	return this->min_bet;
}
#endif 
