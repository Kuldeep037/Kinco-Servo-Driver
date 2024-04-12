// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:srv/SensorFeedback.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__STRUCT_H_
#define ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/SensorFeedback in the package arm_interfaces.
typedef struct arm_interfaces__srv__SensorFeedback_Request
{
  int32_t sensor;
} arm_interfaces__srv__SensorFeedback_Request;

// Struct for a sequence of arm_interfaces__srv__SensorFeedback_Request.
typedef struct arm_interfaces__srv__SensorFeedback_Request__Sequence
{
  arm_interfaces__srv__SensorFeedback_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__srv__SensorFeedback_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SensorFeedback in the package arm_interfaces.
typedef struct arm_interfaces__srv__SensorFeedback_Response
{
  double data;
} arm_interfaces__srv__SensorFeedback_Response;

// Struct for a sequence of arm_interfaces__srv__SensorFeedback_Response.
typedef struct arm_interfaces__srv__SensorFeedback_Response__Sequence
{
  arm_interfaces__srv__SensorFeedback_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__srv__SensorFeedback_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__STRUCT_H_
