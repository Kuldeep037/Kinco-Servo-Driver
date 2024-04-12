// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:msg/SensorData.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/sensor_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
arm_interfaces__msg__SensorData__init(arm_interfaces__msg__SensorData * msg)
{
  if (!msg) {
    return false;
  }
  // current
  // velocity
  // position
  return true;
}

void
arm_interfaces__msg__SensorData__fini(arm_interfaces__msg__SensorData * msg)
{
  if (!msg) {
    return;
  }
  // current
  // velocity
  // position
}

bool
arm_interfaces__msg__SensorData__are_equal(const arm_interfaces__msg__SensorData * lhs, const arm_interfaces__msg__SensorData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // current
  if (lhs->current != rhs->current) {
    return false;
  }
  // velocity
  if (lhs->velocity != rhs->velocity) {
    return false;
  }
  // position
  if (lhs->position != rhs->position) {
    return false;
  }
  return true;
}

bool
arm_interfaces__msg__SensorData__copy(
  const arm_interfaces__msg__SensorData * input,
  arm_interfaces__msg__SensorData * output)
{
  if (!input || !output) {
    return false;
  }
  // current
  output->current = input->current;
  // velocity
  output->velocity = input->velocity;
  // position
  output->position = input->position;
  return true;
}

arm_interfaces__msg__SensorData *
arm_interfaces__msg__SensorData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__SensorData * msg = (arm_interfaces__msg__SensorData *)allocator.allocate(sizeof(arm_interfaces__msg__SensorData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__msg__SensorData));
  bool success = arm_interfaces__msg__SensorData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__msg__SensorData__destroy(arm_interfaces__msg__SensorData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    arm_interfaces__msg__SensorData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
arm_interfaces__msg__SensorData__Sequence__init(arm_interfaces__msg__SensorData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__SensorData * data = NULL;

  if (size) {
    data = (arm_interfaces__msg__SensorData *)allocator.zero_allocate(size, sizeof(arm_interfaces__msg__SensorData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__msg__SensorData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__msg__SensorData__fini(&data[i - 1]);
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
arm_interfaces__msg__SensorData__Sequence__fini(arm_interfaces__msg__SensorData__Sequence * array)
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
      arm_interfaces__msg__SensorData__fini(&array->data[i]);
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

arm_interfaces__msg__SensorData__Sequence *
arm_interfaces__msg__SensorData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__SensorData__Sequence * array = (arm_interfaces__msg__SensorData__Sequence *)allocator.allocate(sizeof(arm_interfaces__msg__SensorData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__msg__SensorData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
arm_interfaces__msg__SensorData__Sequence__destroy(arm_interfaces__msg__SensorData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    arm_interfaces__msg__SensorData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
arm_interfaces__msg__SensorData__Sequence__are_equal(const arm_interfaces__msg__SensorData__Sequence * lhs, const arm_interfaces__msg__SensorData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!arm_interfaces__msg__SensorData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
arm_interfaces__msg__SensorData__Sequence__copy(
  const arm_interfaces__msg__SensorData__Sequence * input,
  arm_interfaces__msg__SensorData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(arm_interfaces__msg__SensorData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    arm_interfaces__msg__SensorData * data =
      (arm_interfaces__msg__SensorData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!arm_interfaces__msg__SensorData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          arm_interfaces__msg__SensorData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!arm_interfaces__msg__SensorData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
