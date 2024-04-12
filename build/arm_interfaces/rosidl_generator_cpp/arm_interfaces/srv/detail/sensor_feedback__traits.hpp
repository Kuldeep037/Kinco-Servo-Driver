// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from arm_interfaces:srv/SensorFeedback.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__TRAITS_HPP_
#define ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "arm_interfaces/srv/detail/sensor_feedback__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace arm_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SensorFeedback_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: sensor
  {
    out << "sensor: ";
    rosidl_generator_traits::value_to_yaml(msg.sensor, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SensorFeedback_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sensor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sensor: ";
    rosidl_generator_traits::value_to_yaml(msg.sensor, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SensorFeedback_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace arm_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use arm_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const arm_interfaces::srv::SensorFeedback_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  arm_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use arm_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const arm_interfaces::srv::SensorFeedback_Request & msg)
{
  return arm_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<arm_interfaces::srv::SensorFeedback_Request>()
{
  return "arm_interfaces::srv::SensorFeedback_Request";
}

template<>
inline const char * name<arm_interfaces::srv::SensorFeedback_Request>()
{
  return "arm_interfaces/srv/SensorFeedback_Request";
}

template<>
struct has_fixed_size<arm_interfaces::srv::SensorFeedback_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<arm_interfaces::srv::SensorFeedback_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<arm_interfaces::srv::SensorFeedback_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace arm_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SensorFeedback_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: data
  {
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SensorFeedback_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SensorFeedback_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace arm_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use arm_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const arm_interfaces::srv::SensorFeedback_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  arm_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use arm_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const arm_interfaces::srv::SensorFeedback_Response & msg)
{
  return arm_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<arm_interfaces::srv::SensorFeedback_Response>()
{
  return "arm_interfaces::srv::SensorFeedback_Response";
}

template<>
inline const char * name<arm_interfaces::srv::SensorFeedback_Response>()
{
  return "arm_interfaces/srv/SensorFeedback_Response";
}

template<>
struct has_fixed_size<arm_interfaces::srv::SensorFeedback_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<arm_interfaces::srv::SensorFeedback_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<arm_interfaces::srv::SensorFeedback_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<arm_interfaces::srv::SensorFeedback>()
{
  return "arm_interfaces::srv::SensorFeedback";
}

template<>
inline const char * name<arm_interfaces::srv::SensorFeedback>()
{
  return "arm_interfaces/srv/SensorFeedback";
}

template<>
struct has_fixed_size<arm_interfaces::srv::SensorFeedback>
  : std::integral_constant<
    bool,
    has_fixed_size<arm_interfaces::srv::SensorFeedback_Request>::value &&
    has_fixed_size<arm_interfaces::srv::SensorFeedback_Response>::value
  >
{
};

template<>
struct has_bounded_size<arm_interfaces::srv::SensorFeedback>
  : std::integral_constant<
    bool,
    has_bounded_size<arm_interfaces::srv::SensorFeedback_Request>::value &&
    has_bounded_size<arm_interfaces::srv::SensorFeedback_Response>::value
  >
{
};

template<>
struct is_service<arm_interfaces::srv::SensorFeedback>
  : std::true_type
{
};

template<>
struct is_service_request<arm_interfaces::srv::SensorFeedback_Request>
  : std::true_type
{
};

template<>
struct is_service_response<arm_interfaces::srv::SensorFeedback_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__TRAITS_HPP_
