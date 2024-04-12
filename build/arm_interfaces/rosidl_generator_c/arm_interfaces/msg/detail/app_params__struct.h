// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:msg/AppParams.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__STRUCT_H_
#define ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/AppParams in the package arm_interfaces.
/**
  * repetitions,start_point,end_point,speed
 */
typedef struct arm_interfaces__msg__AppParams
{
  int32_t repeat;
  double start;
  double end;
  int32_t speed;
  int32_t torque;
  int32_t threshold;
  int32_t delay;
} arm_interfaces__msg__AppParams;

// Struct for a sequence of arm_interfaces__msg__AppParams.
typedef struct arm_interfaces__msg__AppParams__Sequence
{
  arm_interfaces__msg__AppParams * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__msg__AppParams__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__STRUCT_H_
