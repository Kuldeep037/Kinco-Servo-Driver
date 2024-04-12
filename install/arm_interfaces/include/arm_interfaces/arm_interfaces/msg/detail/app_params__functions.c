// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:msg/AppParams.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/app_params__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
arm_interfaces__msg__AppParams__init(arm_interfaces__msg__AppParams * msg)
{
  if (!msg) {
    return false;
  }
  // repeat
  // start
  // end
  // speed
  // torque
  // threshold
  // delay
  return true;
}

void
arm_interfaces__msg__AppParams__fini(arm_interfaces__msg__AppParams * msg)
{
  if (!msg) {
    return;
  }
  // repeat
  // start
  // end
  // speed
  // torque
  // threshold
  // delay
}

bool
arm_interfaces__msg__AppParams__are_equal(const arm_interfaces__msg__AppParams * lhs, const arm_interfaces__msg__AppParams * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // repeat
  if (lhs->repeat != rhs->repeat) {
    return false;
  }
  // start
  if (lhs->start != rhs->start) {
    return false;
  }
  // end
  if (lhs->end != rhs->end) {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  // torque
  if (lhs->torque != rhs->torque) {
    return false;
  }
  // threshold
  if (lhs->threshold != rhs->threshold) {
    return false;
  }
  // delay
  if (lhs->delay != rhs->delay) {
    return false;
  }
  return true;
}

bool
arm_interfaces__msg__AppParams__copy(
  const arm_interfaces__msg__AppParams * input,
  arm_interfaces__msg__AppParams * output)
{
  if (!input || !output) {
    return false;
  }
  // repeat
  output->repeat = input->repeat;
  // start
  output->start = input->start;
  // end
  output->end = input->end;
  // speed
  output->speed = input->speed;
  // torque
  output->torque = input->torque;
  // threshold
  output->threshold = input->threshold;
  // delay
  output->delay = input->delay;
  return true;
}

arm_interfaces__msg__AppParams *
arm_interfaces__msg__AppParams__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__AppParams * msg = (arm_interfaces__msg__AppParams *)allocator.allocate(sizeof(arm_interfaces__msg__AppParams), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__msg__AppParams));
  bool success = arm_interfaces__msg__AppParams__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__msg__AppParams__destroy(arm_interfaces__msg__AppParams * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    arm_interfaces__msg__AppParams__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
arm_interfaces__msg__AppParams__Sequence__init(arm_interfaces__msg__AppParams__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__AppParams * data = NULL;

  if (size) {
    data = (arm_interfaces__msg__AppParams *)allocator.zero_allocate(size, sizeof(arm_interfaces__msg__AppParams), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__msg__AppParams__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__msg__AppParams__fini(&data[i - 1]);
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
arm_interfaces__msg__AppParams__Sequence__fini(arm_interfaces__msg__AppParams__Sequence * array)
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
      arm_interfaces__msg__AppParams__fini(&array->data[i]);
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

arm_interfaces__msg__AppParams__Sequence *
arm_interfaces__msg__AppParams__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__AppParams__Sequence * array = (arm_interfaces__msg__AppParams__Sequence *)allocator.allocate(sizeof(arm_interfaces__msg__AppParams__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__msg__AppParams__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
arm_interfaces__msg__AppParams__Sequence__destroy(arm_interfaces__msg__AppParams__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    arm_interfaces__msg__AppParams__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
arm_interfaces__msg__AppParams__Sequence__are_equal(const arm_interfaces__msg__AppParams__Sequence * lhs, const arm_interfaces__msg__AppParams__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!arm_interfaces__msg__AppParams__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
arm_interfaces__msg__AppParams__Sequence__copy(
  const arm_interfaces__msg__AppParams__Sequence * input,
  arm_interfaces__msg__AppParams__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(arm_interfaces__msg__AppParams);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    arm_interfaces__msg__AppParams * data =
      (arm_interfaces__msg__AppParams *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!arm_interfaces__msg__AppParams__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          arm_interfaces__msg__AppParams__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!arm_interfaces__msg__AppParams__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
