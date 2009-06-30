#include <Python.h>
#include <structmember.h>

staticforward PyTypeObject DateTime_Gen_Type;

typedef struct
{
	PyObject_HEAD   // macro used for refcount & pointer
} DateTime_Gen_Object;

typedef struct
{
	PyObject_HEAD   // macro used for refcount & pointer
} DateTime_Y_Object;

//******************************************
// DateTime_Gen_Type stuff

// Initialize base attributes
static int
DateTime_Gen_init(DateTime_Gen_Object* self, PyObject* args, PyObject* kwds)
{
	return 0;
}

static void
DateTime_Gen_dealloc(PyObject* self)
{
	PyObject_Del(self);
}

static PyObject *
DateTime_Gen_str(PyObject *self)
{
	return PyString_FromFormat("<datetime64 Object>");
}

// Members
static PyMemberDef DateTime_Gen_members[] = {
	{NULL} 
};

// Methods 
static PyMethodDef DateTime_Gen_methods[] = {
	{NULL}
};

//******************************************
// DateTime_Y_Type stuff

static PyObject *
DateTime_Y_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	DateTime_Y_Object *self;
	// Set up self
	return (PyObject *)self;
}

//******************************************
// The PyGenericDateTime object type         
static PyTypeObject DateTime_Gen_Type = {
	PyObject_HEAD_INIT(NULL)
	0,			               /*ob_size*/
	"numpy.datetime64",        /*tp_name*/
	sizeof(PyObject),          /*tp_basicsize*/
	0,                         /*tp_itemsize*/
    0,                         /*tp_dealloc*/
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
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    0,                         /*tp_flags*/
    0,                         /*tp_doc*/
    0,                         /*tp_traverse*/
    0,                         /*tp_clear*/
    0,                         /*tp_richcompare*/
    0,                         /*tp_weaklistoffset*/
    0,                         /*tp_iter*/
    0,                         /*tp_iternext*/
    0,                         /*tp_methods*/
    0,                         /*tp_members*/
    0,                         /*tp_getset*/
    0,                         /*tp_base*/
    0,                         /*tp_dict*/
    0,                         /*tp_descr_get*/
    0,                         /*tp_descr_set*/
    0,                         /*tp_dictoffset*/
    0,                         /*tp_init*/
    0,                         /*tp_alloc*/
    0                          /*tp_new*/
};

//******************************************
// The PyGenericDateTime object type         
static PyTypeObject DateTime_Y_Type = {
	PyObject_HEAD_INIT(NULL)
	0,			               /*ob_size*/
	"numpy.datetime64",        /*tp_name*/
	sizeof(PyObject),          /*tp_basicsize*/
	0,                         /*tp_itemsize*/
    0,                         /*tp_dealloc*/
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
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    0,                         /*tp_flags*/
    0,                         /*tp_doc*/
    0,                         /*tp_traverse*/
    0,                         /*tp_clear*/
    0,                         /*tp_richcompare*/
    0,                         /*tp_weaklistoffset*/
    0,                         /*tp_iter*/
    0,                         /*tp_iternext*/
    0,                         /*tp_methods*/
    0,                         /*tp_members*/
    0,                         /*tp_getset*/
    0,                         /*tp_base*/
    0,                         /*tp_dict*/
    0,                         /*tp_descr_get*/
    0,                         /*tp_descr_set*/
    0,                         /*tp_dictoffset*/
    0,                         /*tp_init*/
    0,                         /*tp_alloc*/
    0                          /*tp_new*/
};


static void
initialize_datetime_types(void)
{
	// Initialize the Generic DateTime Type
	DateTime_Gen_Type.tp_dealloc = (destructor)DateTime_Gen_dealloc;
	DateTime_Gen_Type.tp_flags   = Py_TPFLAGS_DEFAULT;
	DateTime_Gen_Type.tp_new     = NULL; 
	//DateTime_Gen_Type.tp_alloc   = DateTime_Gen_alloc;
	DateTime_Gen_Type.tp_str     = DateTime_Gen_str;
	DateTime_Gen_Type.tp_init    = (initproc)DateTime_Gen_init;
	// Inherit the numpy Long Long Type
	// DateTime_Gen_Type.tp_base = npy_LONGLONG;

	// Initialize the DateTime Year Type
	DateTime_Y_Type.tp_base = DateTime_Gen_Object; // Inherits the DTG
	DateTime_Y_Type.tp_new  = DateTime_Y_new;

	PyObject *datetime_object;
	datetime_object = Py_InitModule3("datetime64 Object", DateTime_Gen_methods, "DateTime Object");
	Py_INCREF(&DateTime_Gen_Object);
	PyModule_AddObject(date_object, "datetime64", 
					  (PyObject *)&DateTime_Gen_Type);

}
