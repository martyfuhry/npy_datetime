#include <Python.h>
#include <datetime.h>
#include <time.h>

// Frequency Defines
#define FR_Y     9  
#define FR_MTH   8
#define FR_D     7
#define FR_H     6
#define FR_MIN   5
#define FR_SEC   4
#define FR_MICRO 3
#define FR_NANO  2
#define FR_PICO  1
#define FR_FEM   0

// For defaults and errors
#define FR_ERR  -1

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

//=============
// parsing
// ============

long date_to_long(int year, int month,  int day,
				  int hour, int minute, int second,
				  int microsecond,
				  int freq)
{
	switch (freq)
	{
		case FR_Y:    return (year - 1970);
		case FR_MTH:  return ((year - 1970) * 12 + month);
		case FR_D:    return (((year - 1970) * 365.25) + (28 * (month - 1)) +
							   (day - 1));
		default:      return 0;
	}
}

int freq_to_int(char* freq)
{
	// Absurdidly stupid way of doing this. Should be changed later.
	if (memcmp(freq, "Y", 1) == 0)
		return FR_Y;
	if (memcmp(freq, "MTH", 3) == 0)
		return FR_MTH;
	if (memcmp(freq, "D", 1) == 0)
		return FR_D;
	if (memcmp(freq, "H", 1) == 0)
		return FR_H;
	if (memcmp(freq, "MIN", 3) == 0)
		return FR_MIN;
	if (memcmp(freq, "MICRO", 5) == 0) 
		return FR_MICRO;
	if (memcmp(freq, "NANO", 4) == 0)
		return FR_NANO;
	if (memcmp(freq, "PICO", 4) == 0)
		return FR_PICO;
	if (memcmp(freq, "FEM", 3) == 0)
		return FR_FEM;

	return FR_ERR;
}

static PyObject *
parse_date(PyObject *self, PyObject *args)
{
	PyObject *string   = NULL;
	PyObject *freq_obj = NULL;
	PyObject *datetime = NULL;
	PyObject *result   = PyTuple_New(2);
	int year = 0, month  = 0, day    = 0, 
		hour = 0, minute = 0, second = 0,
		microsecond = 0;

	int freq = FR_ERR;

	if (!PyCallable_Check(callback))
	{
		PyErr_SetString(PyExc_TypeError, "callback not set.");
		return NULL;
	}

	if (!PyArg_ParseTuple(args, "OO", &string, &freq_obj))
	{
		return NULL;
	}

	// Make sure freq_obj is a PyString
	if (PyString_Check(freq_obj))
	{
		// Turn the PyString freq_obj into an int representing a freq
		freq = freq_to_int(PyString_AsString(freq_obj));
		if (freq == FR_ERR)
		{
			PyErr_SetString(PyExc_TypeError, "invalid frequency");
			return NULL;
		}
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "no frequency set.");
		return NULL;
	}

	if (string)
	{
		// Make the string into a tuple
		PyObject *string_arg = PyTuple_New(1);
		PyTuple_SET_ITEM(string_arg, 0, string);
		Py_INCREF(string);

		// Run the callback function
		datetime = PyEval_CallObject(callback, string_arg);

		Py_DECREF(string_arg);
	
		// Set each time int from the datetime
		if (datetime)
		{
			year        = PyDateTime_GET_YEAR(datetime);
			month       = PyDateTime_GET_MONTH(datetime);
			day         = PyDateTime_GET_DAY(datetime);
			hour        = PyDateTime_DATE_GET_HOUR(datetime);
			minute      = PyDateTime_DATE_GET_MINUTE(datetime);
			second      = PyDateTime_DATE_GET_SECOND(datetime);
			microsecond = PyDateTime_DATE_GET_MICROSECOND(datetime);
		}
		else
		{
			PyErr_SetString(PyExc_TypeError, "error processing datetime");
			return NULL;
		}
	}

	// Return a tuple with (long,  
	PyTuple_SetItem(result, 0, 
			 PyLong_FromLong(date_to_long(
		     year, month, day, hour, minute, second, microsecond,
			 freq)));

	PyTuple_SetItem(result, 1,
			 PyLong_FromLong(freq));

	return result;
}

//=============
// module
// ============

static PyMethodDef methods[] = {
	{"set_callback", (PyCFunction)set_callback, 
	 METH_VARARGS, ""},
	{"test_callback", (PyCFunction)test_callback,
	 METH_VARARGS, ""},
	{"parse_date", (PyCFunction)parse_date,
	 METH_VARARGS, ""},
	{NULL, NULL}
};

PyMODINIT_FUNC
initparsedates(void)
{
	PyObject *parser;

	parser = Py_InitModule("parsedates", methods);
	if (parser == NULL)
		return;
}
