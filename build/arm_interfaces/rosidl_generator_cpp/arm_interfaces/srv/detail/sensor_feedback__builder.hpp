// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:srv/SensorFeedback.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__BUILDER_HPP_
#define ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interfaces/srv/detail/sensor_feedback__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interfaces
{

namespace srv
{

namespace builder
{

class Init_SensorFeedback_Request_sensor
{
public:
  Init_SensorFeedback_Request_sensor()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::arm_interfaces::srv::SensorFeedback_Request sensor(::arm_interfaces::srv::SensorFeedback_Request::_sensor_type arg)
  {
    msg_.sensor = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::srv::SensorFeedback_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::srv::SensorFeedback_Request>()
{
  return arm_interfaces::srv::builder::Init_SensorFeedback_Request_sensor();
}

}  // namespace arm_interfaces


namespace arm_interfaces
{

namespace srv
{

namespace builder
{

class Init_SensorFeedback_Response_data
{
public:
  Init_SensorFeedback_Response_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::arm_interfaces::srv::SensorFeedback_Response data(::arm_interfaces::srv::SensorFeedback_Response::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::srv::SensorFeedback_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::srv::SensorFeedback_Response>()
{
  return arm_interfaces::srv::builder::Init_SensorFeedback_Response_data();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__BUILDER_HPP_
