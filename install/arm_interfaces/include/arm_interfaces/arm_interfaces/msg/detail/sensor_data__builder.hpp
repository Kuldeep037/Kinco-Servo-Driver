// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interfaces/msg/detail/sensor_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_SensorData_position
{
public:
  explicit Init_SensorData_position(::arm_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  ::arm_interfaces::msg::SensorData position(::arm_interfaces::msg::SensorData::_position_type arg)
  {
    msg_.position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::SensorData msg_;
};

class Init_SensorData_velocity
{
public:
  explicit Init_SensorData_velocity(::arm_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_position velocity(::arm_interfaces::msg::SensorData::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_SensorData_position(msg_);
  }

private:
  ::arm_interfaces::msg::SensorData msg_;
};

class Init_SensorData_current
{
public:
  Init_SensorData_current()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SensorData_velocity current(::arm_interfaces::msg::SensorData::_current_type arg)
  {
    msg_.current = std::move(arg);
    return Init_SensorData_velocity(msg_);
  }

private:
  ::arm_interfaces::msg::SensorData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::SensorData>()
{
  return arm_interfaces::msg::builder::Init_SensorData_current();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_
