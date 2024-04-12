// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from arm_interfaces:msg/AppParams.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "arm_interfaces/msg/detail/app_params__struct.h"
#include "arm_interfaces/msg/detail/app_params__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool arm_interfaces__msg__app_params__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[41];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("arm_interfaces.msg._app_params.AppParams", full_classname_dest, 40) == 0);
  }
  arm_interfaces__msg__AppParams * ros_message = _ros_message;
  {  // repeat
    PyObject * field = PyObject_GetAttrString(_pymsg, "repeat");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->repeat = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // start
    PyObject * field = PyObject_GetAttrString(_pymsg, "start");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->start = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // end
    PyObject * field = PyObject_GetAttrString(_pymsg, "end");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->end = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "speed");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->speed = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // torque
    PyObject * field = PyObject_GetAttrString(_pymsg, "torque");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->torque = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // threshold
    PyObject * field = PyObject_GetAttrString(_pymsg, "threshold");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->threshold = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // delay
    PyObject * field = PyObject_GetAttrString(_pymsg, "delay");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->delay = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * arm_interfaces__msg__app_params__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of AppParams */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("arm_interfaces.msg._app_params");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "AppParams");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  arm_interfaces__msg__AppParams * ros_message = (arm_interfaces__msg__AppParams *)raw_ros_message;
  {  // repeat
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->repeat);
    {
      int rc = PyObject_SetAttrString(_pymessage, "repeat", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // start
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->start);
    {
      int rc = PyObject_SetAttrString(_pymessage, "start", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // end
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->end);
    {
      int rc = PyObject_SetAttrString(_pymessage, "end", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // speed
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // torque
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->torque);
    {
      int rc = PyObject_SetAttrString(_pymessage, "torque", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // threshold
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->threshold);
    {
      int rc = PyObject_SetAttrString(_pymessage, "threshold", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // delay
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->delay);
    {
      int rc = PyObject_SetAttrString(_pymessage, "delay", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
