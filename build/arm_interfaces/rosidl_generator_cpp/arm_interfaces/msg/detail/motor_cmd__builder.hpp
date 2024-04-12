// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/MotorCmd.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__MOTOR_CMD__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__MOTOR_CMD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interfaces/msg/detail/motor_cmd__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_MotorCmd_cmd
{
public:
  explicit Init_MotorCmd_cmd(::arm_interfaces::msg::MotorCmd & msg)
  : msg_(msg)
  {}
  ::arm_interfaces::msg::MotorCmd cmd(::arm_interfaces::msg::MotorCmd::_cmd_type arg)
  {
    msg_.cmd = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::MotorCmd msg_;
};

class Init_MotorCmd_data
{
public:
  Init_MotorCmd_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorCmd_cmd data(::arm_interfaces::msg::MotorCmd::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_MotorCmd_cmd(msg_);
  }

private:
  ::arm_interfaces::msg::MotorCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::MotorCmd>()
{
  return arm_interfaces::msg::builder::Init_MotorCmd_data();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__MOTOR_CMD__BUILDER_HPP_
