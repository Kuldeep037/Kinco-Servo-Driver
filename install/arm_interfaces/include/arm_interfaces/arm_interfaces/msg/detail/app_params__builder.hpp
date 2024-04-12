// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/AppParams.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interfaces/msg/detail/app_params__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_AppParams_delay
{
public:
  explicit Init_AppParams_delay(::arm_interfaces::msg::AppParams & msg)
  : msg_(msg)
  {}
  ::arm_interfaces::msg::AppParams delay(::arm_interfaces::msg::AppParams::_delay_type arg)
  {
    msg_.delay = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

class Init_AppParams_threshold
{
public:
  explicit Init_AppParams_threshold(::arm_interfaces::msg::AppParams & msg)
  : msg_(msg)
  {}
  Init_AppParams_delay threshold(::arm_interfaces::msg::AppParams::_threshold_type arg)
  {
    msg_.threshold = std::move(arg);
    return Init_AppParams_delay(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

class Init_AppParams_torque
{
public:
  explicit Init_AppParams_torque(::arm_interfaces::msg::AppParams & msg)
  : msg_(msg)
  {}
  Init_AppParams_threshold torque(::arm_interfaces::msg::AppParams::_torque_type arg)
  {
    msg_.torque = std::move(arg);
    return Init_AppParams_threshold(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

class Init_AppParams_speed
{
public:
  explicit Init_AppParams_speed(::arm_interfaces::msg::AppParams & msg)
  : msg_(msg)
  {}
  Init_AppParams_torque speed(::arm_interfaces::msg::AppParams::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_AppParams_torque(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

class Init_AppParams_end
{
public:
  explicit Init_AppParams_end(::arm_interfaces::msg::AppParams & msg)
  : msg_(msg)
  {}
  Init_AppParams_speed end(::arm_interfaces::msg::AppParams::_end_type arg)
  {
    msg_.end = std::move(arg);
    return Init_AppParams_speed(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

class Init_AppParams_start
{
public:
  explicit Init_AppParams_start(::arm_interfaces::msg::AppParams & msg)
  : msg_(msg)
  {}
  Init_AppParams_end start(::arm_interfaces::msg::AppParams::_start_type arg)
  {
    msg_.start = std::move(arg);
    return Init_AppParams_end(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

class Init_AppParams_repeat
{
public:
  Init_AppParams_repeat()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AppParams_start repeat(::arm_interfaces::msg::AppParams::_repeat_type arg)
  {
    msg_.repeat = std::move(arg);
    return Init_AppParams_start(msg_);
  }

private:
  ::arm_interfaces::msg::AppParams msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::AppParams>()
{
  return arm_interfaces::msg::builder::Init_AppParams_repeat();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__BUILDER_HPP_
