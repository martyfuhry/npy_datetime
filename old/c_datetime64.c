#include <Python.h>
#include <structmember.h>

/************************************************************
**   Helper functions, etc?
************************************************************/




/*************************************************************
**   PyGenericDateTime Type Definition
**   This should just inherit the PyLongLongArrType_Type
**************************************************************/

/* Tell the compiler what PyGenericDateTimeType is */
staticforward PyTypeObject PyGenericDatetimeType;

/* PyGenericDateTime Object */
typedef struct
{
	PyObject_HEAD   // macro used for refcount & pointer
	long long time; // 64 bit time since epoch
} PyGenericDateTime;

/* Create new PyGenericDateTime objects
 *     Returns the PyGenericDateTime Object (should probably be deleted)? */
static PyObject *
PyGenericDateTime_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	PyGenericDateTime *self;

	self = (PyGenericDateTime*)type->tp_alloc(type, 0);
	if (self !=NULL)
	{
		/* initialize attributes here */
		//self->freq = 1;
		//self->time = 1;
	}

	return (PyObject *)self;
}

/* The initilization function */
static int
PyGenericDateTime_init(PyGenericDateTime *self, PyObject *args, PyObject *kwds)
{
	char *arg_freq = NULL;
	long long *arg_time = 0;

	static char* kwlist[] = {"freq", "time", NULL};

	if (! PyArg_ParseTupleAndKeywords(args, kwds, "c|L", kwlist,
			      &arg_freq, &arg_time))
		return -1;

	if (arg_freq)
	{
		// Figure out which dt_X to construct based on frequency
		//    based on the freq
		self->freq = 10;
	}

	if (arg_time)
	{
		self->time = arg_time;
	}

	return 0;
}

/* The Print function */
static PyObject *
PyGenericDateTime_str(PyGenericDateTime *self)
{
	return PyString_FromFormat("<PyGenericDateTime: --time: %ld --freq: %d>", 
								self->time, self->freq);
}

/* The deallocation function */
static void
PyGenericDateTime_dealloc(PyObject* self)
{
	PyObject_Del(self);
}

//******************************************
// PyGenericDateTime Members
static PyMemberDef PyGenericDateTime_members[] = {
	{"freq", T_INT, offsetof(PyGenericDateTime, freq), 0,
	 "frequency"},
	{"time", T_LONGLONG, offsetof(PyGenericDateTime, time), 0,
	 "64 bit representation of the Date"},
	{NULL} /* Sentinel */
};

//******************************************
// PyGenericDateTime Methods 
static PyMethodDef PyGenericDateTime_methods[] = {
	{NULL}

};

//******************************************
// The PyGenericDateTime object type         
static PyTypeObject PyGenericDateTimeType_Type = {
	PyObject_HEAD_INIT(NULL)
	0,			   /*ob_size*/
	"datetime.PyGenericDateTime",   /*tp_name*/
	sizeof(PyGenericDateTime),        /*tp_basicsize*/
	0,                         /*tp_itemsize*/
    (destructor)PyGenericDateTime_dealloc,        /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    (reprfunc)PyGenericDateTime_str,  /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT,        /*tp_flags*/
    "PyGenericDateTime objects",      /*tp_doc*/
    0,                         /*tp_traverse*/
    0,                         /*tp_clear*/
    0,                         /*tp_richcompare*/
    0,                         /*tp_weaklistoffset*/
    0,                         /*tp_iter*/
    0,                         /*tp_iternext*/
    PyGenericDateTime_methods,        /*tp_methods*/
    PyGenericDateTime_members,        /*tp_members*/
    0,                         /*tp_getset*/
    0,                         /*tp_base*/
    0,                         /*tp_dict*/
    0,                         /*tp_descr_get*/
    0,                         /*tp_descr_set*/
    0,                         /*tp_dictoffset*/
    (initproc)PyGenericDateTime_init, /*tp_init*/
    0,                         /*tp_alloc*/
    PyGenericDateTime_new             /*tp_new*/
};

static void
initialize_datetime_types(void)
{
	PyGenericDateTimeType_Type.tp_dealloc   = (destructor)gendt_dealloc;
	PyGenericDateTimeType_Type.tp_as_number = &gendt_as_number;
	PyGenericDateTimeType_Type.tp_flags     = BASEFLAGS;
	PyGenericDateTimeType_Type.tp_methods   = gendt_methods;
	PyGenericDateTimeType_Type.tp_getset    = gnedt_getsets;
	// Can not create gendt objects
	PyGenericDateTimeType_Type.tp_new       = NULL; 
	PyGenericDateTimeType_Type.tp_alloc     = gendt_alloc;
	PyGenericDateTimeType_Type.tp_str       = gendt_str;

/* The initialization of PyGenericDateTime module */
PyMODINIT_FUNC
initPyGenericDateTime(void)
{
	PyObject *date_object;

	/* Default new object creation */
	PyGenericDateTimeType.tp_new = PyType_GenericNew;

	/* Initilize the PyGenericDateTimeType */
	if (PyType_Ready(&PyGenericDateTimeType) < 0)
		return;

	/* Create a new module object based on a name and table of functions, 
	   returning the module object */
	date_object = Py_InitModule3("PyGenericDateTime", PyGenericDateTime_methods, "Generic DateTime");

	/* Increment the reference count for this object */	
	Py_INCREF(&PyGenericDateTimeType);

	/* Adds the type to the module dictionary */
	PyModule_AddObject(date_object, "PyGenericDateTime", (PyObject *)&PyGenericDateTimeType);
}
