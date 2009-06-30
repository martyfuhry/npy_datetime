#include <stdio.h>

// Define the Frequencies
#define NS  0
#define US  1
#define MS  2
#define SEC 3
#define MIN 4
#define H   5
#define D   6
#define B   7
#define W   8
#define MON 9
#define Y   10

/*
 * Takes a string and a frequency and returns
 * a longlong value corresponding to that datea
 *
 * -- Valid Strings
 *    > 2008-07-03T17:31:00
 *    July 3, 2008 at 5:31:00PM
 *	  f = S
 *
 * 	  > 2001
 *    2001
 *    f = Y
 *
 *    > 
 */

struct date_info
{
	long long time;
	int freq;
	int ns;
	int us;
	int ms;
	int s;
	int min;
	int h;
	int d;
	int b;
	int w;
	int mon;
	int y;
};

struct date_info dinfo(char* d_string, int freq)
{
	struct date_info *self;
	
	// Set freq
	self->freq = freq;

		
}

int str_to_time(char* d_string, int freq)
{
	printf("--Date: %s --Freq: %i\n", d_string, freq);

	// Parse String, receive dates:
	date(d_string, freq);

	// 
}


