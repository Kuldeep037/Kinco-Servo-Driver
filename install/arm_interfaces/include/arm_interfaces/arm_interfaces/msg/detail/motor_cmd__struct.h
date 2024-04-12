// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:msg/MotorCmd.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__MOTOR_CMD__STRUCT_H_
#define ARM_INTERFACES__MSG__DETAIL__MOTOR_CMD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MotorCmd in the package arm_interfaces.
typedef struct arm_interfaces__msg__MotorCmd
{
  int32_t data;
  int32_t cmd;
} arm_interfaces__msg__MotorCmd;

// Struct for a sequence of arm_interfaces__msg__MotorCmd.
typedef struct arm_interfaces__msg__MotorCmd__Sequence
{
  arm_interfaces__msg__MotorCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__msg__MotorCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__MOTOR_CMD__STRUCT_H_
