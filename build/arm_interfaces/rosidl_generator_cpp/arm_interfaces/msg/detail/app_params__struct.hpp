// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from arm_interfaces:msg/AppParams.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__STRUCT_HPP_
#define ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__arm_interfaces__msg__AppParams __attribute__((deprecated))
#else
# define DEPRECATED__arm_interfaces__msg__AppParams __declspec(deprecated)
#endif

namespace arm_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AppParams_
{
  using Type = AppParams_<ContainerAllocator>;

  explicit AppParams_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->repeat = 0l;
      this->start = 0.0;
      this->end = 0.0;
      this->speed = 0l;
      this->torque = 0l;
      this->threshold = 0l;
      this->delay = 0l;
    }
  }

  explicit AppParams_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->repeat = 0l;
      this->start = 0.0;
      this->end = 0.0;
      this->speed = 0l;
      this->torque = 0l;
      this->threshold = 0l;
      this->delay = 0l;
    }
  }

  // field types and members
  using _repeat_type =
    int32_t;
  _repeat_type repeat;
  using _start_type =
    double;
  _start_type start;
  using _end_type =
    double;
  _end_type end;
  using _speed_type =
    int32_t;
  _speed_type speed;
  using _torque_type =
    int32_t;
  _torque_type torque;
  using _threshold_type =
    int32_t;
  _threshold_type threshold;
  using _delay_type =
    int32_t;
  _delay_type delay;

  // setters for named parameter idiom
  Type & set__repeat(
    const int32_t & _arg)
  {
    this->repeat = _arg;
    return *this;
  }
  Type & set__start(
    const double & _arg)
  {
    this->start = _arg;
    return *this;
  }
  Type & set__end(
    const double & _arg)
  {
    this->end = _arg;
    return *this;
  }
  Type & set__speed(
    const int32_t & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__torque(
    const int32_t & _arg)
  {
    this->torque = _arg;
    return *this;
  }
  Type & set__threshold(
    const int32_t & _arg)
  {
    this->threshold = _arg;
    return *this;
  }
  Type & set__delay(
    const int32_t & _arg)
  {
    this->delay = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    arm_interfaces::msg::AppParams_<ContainerAllocator> *;
  using ConstRawPtr =
    const arm_interfaces::msg::AppParams_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::msg::AppParams_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::msg::AppParams_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__arm_interfaces__msg__AppParams
    std::shared_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__arm_interfaces__msg__AppParams
    std::shared_ptr<arm_interfaces::msg::AppParams_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AppParams_ & other) const
  {
    if (this->repeat != other.repeat) {
      return false;
    }
    if (this->start != other.start) {
      return false;
    }
    if (this->end != other.end) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->torque != other.torque) {
      return false;
    }
    if (this->threshold != other.threshold) {
      return false;
    }
    if (this->delay != other.delay) {
      return false;
    }
    return true;
  }
  bool operator!=(const AppParams_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AppParams_

// alias to use template instance with default allocator
using AppParams =
  arm_interfaces::msg::AppParams_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__APP_PARAMS__STRUCT_HPP_
