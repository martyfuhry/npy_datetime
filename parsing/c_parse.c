#include <Python.h>
#include <datetime.h>
#include <time.h>

// Frequency Defines
#define FR_Y  13  
#define FR_M  12
#define FR_W  11
#define FR_B  10
#define FR_D  9
#define FR_h  8
#define FR_m  7
#define FR_s  6
#define FR_ms 5
#define FR_us 4
#define FR_ns 3
#define FR_ps 2
#define FR_fs 1
#define FR_as 0

// For defaults and errors
#define FR_ERR  -1

int freq_to_int(char* freq)
{
	// Absurdidly stupid way of doing this. Should be changed later.
	if (memcmp(freq, "Y", 1) == 0)
		return FR_Y;
	if (memcmp(freq, "M", 1) == 0)
		return FR_M;
	if (memcmp(freq, "W", 1) == 0)
		return FR_W;
	if (memcmp(freq, "B", 1) == 0)
		return FR_B;
	if (memcmp(freq, "D", 1) == 0)
		return FR_D;
	if (memcmp(freq, "h", 1) == 0)
		return FR_h;
	if (memcmp(freq, "m", 2) == 0)
		return FR_m;
	if (memcmp(freq, "s", 1) == 0) 
		return FR_s;
	if (memcmp(freq, "ms", 2) == 0)
		return FR_ms;
	if (memcmp(freq, "us", 2) == 0)
		return FR_us;
	if (memcmp(freq, "ns", 2) == 0)
		return FR_ns;
	if (memcmp(freq, "ps", 2) == 0)
		return FR_ps;
	if (memcmp(freq, "fs", 2) == 0)
		return FR_fs;
	if (memcmp(freq, "as", 2) == 0)
		return FR_as;

	return FR_ERR;
}

//=============
// callbacks
// ============

static PyObject *callback = NULL;

static PyObject *
set_callback(PyObject *dummy, PyObject *args)
{
	PyObject *result = NULL;
	PyObject *temp;

	if (PyArg_ParseTuple(args, "O:set_callback", &temp))
	{
		if (!PyCallable_Check(temp))
		{
			PyErr_SetString(PyExc_TypeError, "parameter must be callable");
			return NULL;
		}
		// Reference to new callback
		Py_XINCREF(temp);
		// Dispose of previous callback
		Py_XDECREF(callback);
		// Remember new callback
		callback = temp;
		// Boilerplate to return "None"
		Py_INCREF(Py_None);
		result = Py_None;
	}
	
	return result;
}

static PyObject *
test_callback()
{
	PyObject *result = NULL;
	PyObject *arglist = NULL;
	int a = 1, b = 2;
	arglist = Py_BuildValue("ii", a, b);
	if (callback == NULL)
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}
	result = PyEval_CallObject(callback, arglist);
	Py_DECREF(arglist);
	if (result == NULL)
		return NULL;
	// Use result HERE
	
	return result;
}


//DERIVED FROM mx.DateTime
/*
    Functions in the following section are borrowed from mx.DateTime version
    2.0.6, and hence this code is subject to the terms of the egenix public
    license version 1.0.0
*/

#define Py_AssertWithArg(x,errortype,errorstr,a1) {if (!(x)) {PyErr_Format(errortype,errorstr,a1);goto onError;}}
#define Py_Error(errortype,errorstr) {PyErr_SetString(errortype,errorstr);goto onError;}

 /* Error Exception objects */
static PyObject *DateCalc_Error;
static PyObject *DateCalc_RangeError;

#define SECONDS_PER_DAY ((double) 86400.0)

/* Table with day offsets for each month (0-based, without and with leap) */
static int month_offset[2][13] = {
    { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 },
    { 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366 }
};

/* Table of number of days in a month (0-based, without and with leap) */
static int days_in_month[2][12] = {
    { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 },
    { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }
};

/* Return 1/0 iff year points to a leap year in calendar. */
static
int is_leapyear(register long year)
{
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}

/*
 * static
int dInfoCalc_ISOWeek(struct date_info *dinfo)
{
    int week;

  * Estimate *
    week = (dinfo->day_of_year-1) - dinfo->day_of_week + 3;
    if (week >= 0) week = week / 7 + 1;

    * Verify *
    if (week < 0) {
        * The day lies in last week of the previous year *
        if ((week > -2) ||
            (week == -2 && dInfoCalc_Leapyear(dinfo->year-1, dinfo->calendar)))
            week = 53;
        else
            week = 52;
    } else if (week == 53) {
    * Check if the week belongs to year or year+1 *
        if (31-dinfo->day + dinfo->day_of_week < 3) {
            week = 1;
        }
    }

    return week;
}
*/


/* Return the day of the week for the given absolute date. */
static
int dInfoCalc_DayOfWeek(register long absdate)
{
    int day_of_week;

    if (absdate >= 1) {
        day_of_week = (absdate - 1) % 7;
    } else {
        day_of_week = 6 - ((-absdate) % 7);
    }
    return day_of_week;
}

/* Return the year offset, that is the absolute date of the day
   31.12.(year-1) in the given calendar.

   Note:
   For the Julian calendar we shift the absdate (which is measured
   using the Gregorian Epoch) value by two days because the Epoch
   (0001-01-01) in the Julian calendar lies 2 days before the Epoch in
   the Gregorian calendar. */
static
int year_offset(register long year)
{
    year--;
    if (year >= 0 || -1/4 == -1)
        return year*365 + year/4 - year/100 + year/400;
    else
        return year*365 + (year-3)/4 - (year-99)/100 + (year-399)/400;
    
	Py_Error(DateCalc_Error, "unknown calendar");
 onError:
    return -1;
}


/* Set the instance's value using the given date and time. calendar
   may be set to the flags: GREGORIAN_CALENDAR,
   JULIAN_CALENDAR to indicate the calendar to be used. */

// Modified version of mxDateTime function
// Returns absolute number of days since Jan 1, 1970
static
long absdays_from_ymd(int year, int month, int day)
{

	// Offset for number of days between Jan 1, 1970 and Jan 1, 0001
	#define DAYS_EPOCH 719163

    /* Calculate the absolute date */
    int leap;
    long yearoffset, absdate;

    /* Range check */
    Py_AssertWithArg(year > -(INT_MAX / 366) && year < (INT_MAX / 366),
             DateCalc_RangeError,
             "year out of range: %i",
             year);

    /* Is it a leap year ? */
    leap = is_leapyear(year);

    /* Negative month values indicate months relative to the years end */
    if (month < 0) month += 13;
    Py_AssertWithArg(month >= 1 && month <= 12,
             DateCalc_RangeError,
             "month out of range (1-12): %i",
             month);

    /* Negative values indicate days relative to the months end */
    if (day < 0) day += days_in_month[leap][month - 1] + 1;
    Py_AssertWithArg(day >= 1 && day <= days_in_month[leap][month - 1],
                 DateCalc_RangeError,
                 "day out of range: %i",
				 day);

	// Number of days between (year - 1) and 1970
    yearoffset = year_offset(year) - DAYS_EPOCH;

    if (PyErr_Occurred()) goto onError;

	// Calculate the number of days using yearoffset
    absdate = day + month_offset[leap][month - 1] + yearoffset;

	return absdate;

onError:
	// do bad stuff
	return 0;

}

// Returns absolute seconds from an hour, minute, and second
long abssecs_from_hms(int hour, int minute, int second)
{
	// Needs to perform checks for valid times
	return hour * 3600 + minute * 60 + second;
}


/* Sets the time part of the DateTime object. */
static
int dInfoCalc_SetFromAbsTime( double abstime)
{
    int inttime;
    int hour,minute;
    double second;

    inttime = (int)abstime;
    hour = inttime / 3600;
    minute = (inttime % 3600) / 60;
    second = abstime - (double)(hour*3600 + minute*60);

	/*
    dinfo->hour = hour;
    dinfo->minute = minute;
    dinfo->second = second;

    dinfo->abstime = abstime;
	*/
    return 0;
}
/*
====================================================
== End of section borrowed from mx.DateTime       ==
====================================================
*/

//=============
// parsing
// ============

// Takes a datetime object and a string as frequency
// Returns the number of (frequency) since Jan 1, 1970
long datetime_to_long(PyObject* datetime, int frequency)
{
	int year = 0, month = 0, day = 0, hour = 0, 
		minute = 0, second = 0, microsecond = 0;

	// Get the time units from PyDateTime
	year        = PyDateTime_GET_YEAR(datetime);
	month       = PyDateTime_GET_MONTH(datetime);
	day         = PyDateTime_GET_DAY(datetime);
	hour        = PyDateTime_DATE_GET_HOUR(datetime);
	minute      = PyDateTime_DATE_GET_MINUTE(datetime);
	second      = PyDateTime_DATE_GET_SECOND(datetime);
	microsecond = PyDateTime_DATE_GET_MICROSECOND(datetime);
	
	int leap = (year % 4 == 0) ? 1 : 0;
	
	// These calculations depend on the frequency
	switch (frequency)
	{
		case FR_Y:
			return year - 1970;
		case FR_M:
			// Positive number if year >= 1970
			if (year >= 1970)
				return (year - 1970) * 12 + month - 1;
			else
				return (year - 1970) * 12 - (12 - month) + 1;
		case FR_W:
			// Positive number if year >= 1970
			if (year >= 1970)
				return absdays_from_ymd(year, month, day) / 7;
		case FR_B:
			PyErr_SetString(PyExc_NotImplementedError, "business day not implemented");
			return 0;
			// I'll think about this one
			break;
		case FR_D:
			// Positive number if year >= 1970
			if (year >= 1970)
				return absdays_from_ymd(year, month, day);
			else
				return (year - 1970) * 365.25
			   		+ (365 - month_offset[leap][month - 1])
				   	+ (days_in_month[leap][month - 1] - day);	
		case FR_h:
			// Positive number if year >= 1970
			if (year >= 1970)
			{
				return absdays_from_ymd(year, month, day) * 24 
				   	+ hour;
			}
			else
			{
				return (year - 1970) * 365.25 * 24
				   	+ (365 - month_offset[leap][month - 1]) * 24
				   	+ (days_in_month[leap][month - 1] * 24 - hour);
			}
		case FR_m:
			if (year >= 1970)
				return absdays_from_ymd(year, month, day) * 1440 
				   	+ hour * 60
				   	+ minute;
		case FR_s:
			if (year >= 1970)
				return absdays_from_ymd(year, month, day) * 86400
				 	+ abssecs_from_hms(hour, minute, second);
		case FR_ms:
			if (year >= 1970)
				return absdays_from_ymd(year, month, day) * 86400000
				 	+ abssecs_from_hms(hour, minute, second) * 1000
				 	+ (microsecond / 1000);
		case FR_us:
			if (year >= 1970)
				return absdays_from_ymd(year, month, day) * 86400000000
				 	+ abssecs_from_hms(hour, minute, second) * 1000000
				 	+ microsecond;
		
		//  ////////////////////
		// Starting from here, we need extra units (ns, ps, fs, as)
		//  for correct precision
		//  ////////////////////

		case FR_ns:
		case FR_ps:
		case FR_fs:
		case FR_as:
			// Raise the NotImplementedError for the previous frequencies
			PyErr_SetString(PyExc_NotImplementedError, "not implemented yet");
			return 0;
		default: return 0;
	}

}

// Takes a string object as the date, and a string as frequency, 
//  parses that into a datetime and passes the datetime object 
//  to datetime_to_long
// Returns the number of (frequency) since Jan 1, 1970
long datestring_to_long(PyObject *string, int frequency)
{
	// Send to datetime_to_long
	PyObject *datetime = NULL;
	long result = 0;

	// Make the string into a tuple for the callback function
	PyObject *string_arg = PyTuple_New(1);
	PyTuple_SET_ITEM(string_arg, 0, string);
	Py_INCREF(string);

	// Parse the string into a datetime object
	datetime = PyEval_CallObject(callback, string_arg);

	Py_DECREF(string_arg);

	// If the parsing worked, send the datetime and frequency 
	//  to datetime_to_long
	if (datetime)
	{
		return result;
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "error processing datetime");
		//return NULL;
		//Return bad stuff
		return 0;
	}
}

// This is the callable wrapper for datestring/datetime_to_long
// Decides if the arguments are a string or a datetime object
//  and passes them to the correct datestring/datetime function
// Returns a PyLong generated from the appropriate function
PyObject *
date_to_long(PyObject *self, PyObject *args)
{
	PyObject *date_obj = NULL;    // string or datetime
	PyObject *freq_obj = NULL;	  // frequency as string
	PyObject *result   = NULL;	  // long result

	int freq = FR_ERR;			  // freq_obj is a PyObject to be parsed to freq

	// Make sure the callback function is set
	//  ! This doesn't check to make sure it's the right callback function
	//  ! This should all be done in some init script
	if (!PyCallable_Check(callback))
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}

	// Parse out date_obj & freq_obj
	if (!PyArg_ParseTuple(args, "OO", &date_obj, &freq_obj))
	{
		return NULL;
	}

	// Make sure frequency is not NULL
	if (!freq_obj)
	{	
		PyErr_SetString(PyExc_TypeError, "frequency not set.");
		return NULL;
	}

	// Parse out frequency into an int so we can use it easily
	if ((freq = freq_to_int(PyString_AsString(freq_obj))) == FR_ERR)
	{
		// If the frequency is invalid, set an error and return null
		PyErr_SetString(PyExc_TypeError, "invalid frequency.");
		return NULL;
	}

	// Decide if the date_obj is a string or a datetime
	if (PyString_Check(date_obj))
	{
		// XXX PyINCREF here?
		// date_obj is a string, so return datestring_to_long
		result = PyLong_FromLong(datestring_to_long(date_obj, freq));
	}
	else if (PyDateTime_Check(date_obj))
	{
		// XXX PyINCREF here?
		// date_obj is a datetime, so return datetime_to_long
		result = PyLong_FromLong(datetime_to_long(date_obj, freq));
	}
	else
	{
		// date_obj is neither a string, nor a datetime
		PyErr_SetString(PyExc_TypeError, "invalid date type");
		return NULL;
	}
	
	// Check if an error occured in either of the parsing functions
	if (PyErr_Occurred())
		return NULL;

	return result;
}


//=============
// module
// ============


// Sets which methods are callable by Python
static PyMethodDef methods[] = {
	{"set_callback", (PyCFunction)set_callback, 
	 METH_VARARGS, ""},
	{"test_callback", (PyCFunction)test_callback,
	 METH_VARARGS, ""},
	{"date_to_long", (PyCFunction)date_to_long,
	 METH_VARARGS, ""},
	{NULL, NULL}
};

PyMODINIT_FUNC
initparsedates(void)
{
	PyObject *parser;

	// Initialize the parsedates module (mainly for testing)
	parser = Py_InitModule("parsedates", methods);
	if (parser == NULL)
		return;
}
