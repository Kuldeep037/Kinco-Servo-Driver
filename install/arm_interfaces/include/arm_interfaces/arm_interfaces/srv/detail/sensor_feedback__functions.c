// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:srv/SensorFeedback.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/srv/detail/sensor_feedback__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
arm_interfaces__srv__SensorFeedback_Request__init(arm_interfaces__srv__SensorFeedback_Request * msg)
{
  if (!msg) {
    return false;
  }
  // sensor
  return true;
}

void
arm_interfaces__srv__SensorFeedback_Request__fini(arm_interfaces__srv__SensorFeedback_Request * msg)
{
  if (!msg) {
    return;
  }
  // sensor
}

bool
arm_interfaces__srv__SensorFeedback_Request__are_equal(const arm_interfaces__srv__SensorFeedback_Request * lhs, const arm_interfaces__srv__SensorFeedback_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sensor
  if (lhs->sensor != rhs->sensor) {
    return false;
  }
  return true;
}

bool
arm_interfaces__srv__SensorFeedback_Request__copy(
  const arm_interfaces__srv__SensorFeedback_Request * input,
  arm_interfaces__srv__SensorFeedback_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // sensor
  output->sensor = input->sensor;
  return true;
}

arm_interfaces__srv__SensorFeedback_Request *
arm_interfaces__srv__SensorFeedback_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__srv__SensorFeedback_Request * msg = (arm_interfaces__srv__SensorFeedback_Request *)allocator.allocate(sizeof(arm_interfaces__srv__SensorFeedback_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__srv__SensorFeedback_Request));
  bool success = arm_interfaces__srv__SensorFeedback_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__srv__SensorFeedback_Request__destroy(arm_interfaces__srv__SensorFeedback_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    arm_interfaces__srv__SensorFeedback_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
arm_interfaces__srv__SensorFeedback_Request__Sequence__init(arm_interfaces__srv__SensorFeedback_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__srv__SensorFeedback_Request * data = NULL;

  if (size) {
    data = (arm_interfaces__srv__SensorFeedback_Request *)allocator.zero_allocate(size, sizeof(arm_interfaces__srv__SensorFeedback_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__srv__SensorFeedback_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__srv__SensorFeedback_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
arm_interfaces__srv__SensorFeedback_Request__Sequence__fini(arm_interfaces__srv__SensorFeedback_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      arm_interfaces__srv__SensorFeedback_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

arm_interfaces__srv__SensorFeedback_Request__Sequence *
arm_interfaces__srv__SensorFeedback_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__srv__SensorFeedback_Request__Sequence * array = (arm_interfaces__srv__SensorFeedback_Request__Sequence *)allocator.allocate(sizeof(arm_interfaces__srv__SensorFeedback_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__srv__SensorFeedback_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
arm_interfaces__srv__SensorFeedback_Request__Sequence__destroy(arm_interfaces__srv__SensorFeedback_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    arm_interfaces__srv__SensorFeedback_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
arm_interfaces__srv__SensorFeedback_Request__Sequence__are_equal(const arm_interfaces__srv__SensorFeedback_Request__Sequence * lhs, const arm_interfaces__srv__SensorFeedback_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!arm_interfaces__srv__SensorFeedback_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
arm_interfaces__srv__SensorFeedback_Request__Sequence__copy(
  const arm_interfaces__srv__SensorFeedback_Request__Sequence * input,
  arm_interfaces__srv__SensorFeedback_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(arm_interfaces__srv__SensorFeedback_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    arm_interfaces__srv__SensorFeedback_Request * data =
      (arm_interfaces__srv__SensorFeedback_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!arm_interfaces__srv__SensorFeedback_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          arm_interfaces__srv__SensorFeedback_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!arm_interfaces__srv__SensorFeedback_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
arm_interfaces__srv__SensorFeedback_Response__init(arm_interfaces__srv__SensorFeedback_Response * msg)
{
  if (!msg) {
    return false;
  }
  // data
  return true;
}

void
arm_interfaces__srv__SensorFeedback_Response__fini(arm_interfaces__srv__SensorFeedback_Response * msg)
{
  if (!msg) {
    return;
  }
  // data
}

bool
arm_interfaces__srv__SensorFeedback_Response__are_equal(const arm_interfaces__srv__SensorFeedback_Response * lhs, const arm_interfaces__srv__SensorFeedback_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // data
  if (lhs->data != rhs->data) {
    return false;
  }
  return true;
}

bool
arm_interfaces__srv__SensorFeedback_Response__copy(
  const arm_interfaces__srv__SensorFeedback_Response * input,
  arm_interfaces__srv__SensorFeedback_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // data
  output->data = input->data;
  return true;
}

arm_interfaces__srv__SensorFeedback_Response *
arm_interfaces__srv__SensorFeedback_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__srv__SensorFeedback_Response * msg = (arm_interfaces__srv__SensorFeedback_Response *)allocator.allocate(sizeof(arm_interfaces__srv__SensorFeedback_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__srv__SensorFeedback_Response));
  bool success = arm_interfaces__srv__SensorFeedback_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__srv__SensorFeedback_Response__destroy(arm_interfaces__srv__SensorFeedback_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    arm_interfaces__srv__SensorFeedback_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
arm_interfaces__srv__SensorFeedback_Response__Sequence__init(arm_interfaces__srv__SensorFeedback_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__srv__SensorFeedback_Response * data = NULL;

  if (size) {
    data = (arm_interfaces__srv__SensorFeedback_Response *)allocator.zero_allocate(size, sizeof(arm_interfaces__srv__SensorFeedback_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__srv__SensorFeedback_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__srv__SensorFeedback_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
arm_interfaces__srv__SensorFeedback_Response__Sequence__fini(arm_interfaces__srv__SensorFeedback_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      arm_interfaces__srv__SensorFeedback_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

arm_interfaces__srv__SensorFeedback_Response__Sequence *
arm_interfaces__srv__SensorFeedback_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__srv__SensorFeedback_Response__Sequence * array = (arm_interfaces__srv__SensorFeedback_Response__Sequence *)allocator.allocate(sizeof(arm_interfaces__srv__SensorFeedback_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__srv__SensorFeedback_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
arm_interfaces__srv__SensorFeedback_Response__Sequence__destroy(arm_interfaces__srv__SensorFeedback_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    arm_interfaces__srv__SensorFeedback_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
arm_interfaces__srv__SensorFeedback_Response__Sequence__are_equal(const arm_interfaces__srv__SensorFeedback_Response__Sequence * lhs, const arm_interfaces__srv__SensorFeedback_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!arm_interfaces__srv__SensorFeedback_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
arm_interfaces__srv__SensorFeedback_Response__Sequence__copy(
  const arm_interfaces__srv__SensorFeedback_Response__Sequence * input,
  arm_interfaces__srv__SensorFeedback_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(arm_interfaces__srv__SensorFeedback_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    arm_interfaces__srv__SensorFeedback_Response * data =
      (arm_interfaces__srv__SensorFeedback_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!arm_interfaces__srv__SensorFeedback_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          arm_interfaces__srv__SensorFeedback_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!arm_interfaces__srv__SensorFeedback_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
