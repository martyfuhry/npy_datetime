#include <stdio.h>

// Define the Frequencies
#define NS  1
#define US  2
#define MS  3
#define SEC 4
#define MIN 5
#define H   6
#define D   7
#define B   8
#define W   9
#define MON 10
#define Y   11

/*
 * Takes a string and a frequency and returns
 * a longlong value corresponding to that datea
 *
 * -- Valid Strings
 *    > 2008-07-03T17:31:00
 *    July 3, 2008 at 5:31:00PM
 *
 * 	  > 
 */

int str_to_date(char* d_string, int freq)
{
//	printf("--Date: %c --Freq: %i", d_string, freq);
	
}
