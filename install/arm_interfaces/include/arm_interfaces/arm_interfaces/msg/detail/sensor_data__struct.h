// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__SENSOR_DATA__STRUCT_H_
#define ARM_INTERFACES__MSG__DETAIL__SENSOR_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/SensorData in the package arm_interfaces.
typedef struct arm_interfaces__msg__SensorData
{
  double current;
  int32_t velocity;
  int32_t position;
} arm_interfaces__msg__SensorData;

// Struct for a sequence of arm_interfaces__msg__SensorData.
typedef struct arm_interfaces__msg__SensorData__Sequence
{
  arm_interfaces__msg__SensorData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__msg__SensorData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__SENSOR_DATA__STRUCT_H_
