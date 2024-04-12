// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from arm_interfaces:srv/SensorFeedback.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__STRUCT_HPP_
#define ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__arm_interfaces__srv__SensorFeedback_Request __attribute__((deprecated))
#else
# define DEPRECATED__arm_interfaces__srv__SensorFeedback_Request __declspec(deprecated)
#endif

namespace arm_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SensorFeedback_Request_
{
  using Type = SensorFeedback_Request_<ContainerAllocator>;

  explicit SensorFeedback_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sensor = 0l;
    }
  }

  explicit SensorFeedback_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sensor = 0l;
    }
  }

  // field types and members
  using _sensor_type =
    int32_t;
  _sensor_type sensor;

  // setters for named parameter idiom
  Type & set__sensor(
    const int32_t & _arg)
  {
    this->sensor = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__arm_interfaces__srv__SensorFeedback_Request
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__arm_interfaces__srv__SensorFeedback_Request
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SensorFeedback_Request_ & other) const
  {
    if (this->sensor != other.sensor) {
      return false;
    }
    return true;
  }
  bool operator!=(const SensorFeedback_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SensorFeedback_Request_

// alias to use template instance with default allocator
using SensorFeedback_Request =
  arm_interfaces::srv::SensorFeedback_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace arm_interfaces


#ifndef _WIN32
# define DEPRECATED__arm_interfaces__srv__SensorFeedback_Response __attribute__((deprecated))
#else
# define DEPRECATED__arm_interfaces__srv__SensorFeedback_Response __declspec(deprecated)
#endif

namespace arm_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SensorFeedback_Response_
{
  using Type = SensorFeedback_Response_<ContainerAllocator>;

  explicit SensorFeedback_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0.0;
    }
  }

  explicit SensorFeedback_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0.0;
    }
  }

  // field types and members
  using _data_type =
    double;
  _data_type data;

  // setters for named parameter idiom
  Type & set__data(
    const double & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__arm_interfaces__srv__SensorFeedback_Response
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__arm_interfaces__srv__SensorFeedback_Response
    std::shared_ptr<arm_interfaces::srv::SensorFeedback_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SensorFeedback_Response_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const SensorFeedback_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SensorFeedback_Response_

// alias to use template instance with default allocator
using SensorFeedback_Response =
  arm_interfaces::srv::SensorFeedback_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace arm_interfaces

namespace arm_interfaces
{

namespace srv
{

struct SensorFeedback
{
  using Request = arm_interfaces::srv::SensorFeedback_Request;
  using Response = arm_interfaces::srv::SensorFeedback_Response;
};

}  // namespace srv

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__SRV__DETAIL__SENSOR_FEEDBACK__STRUCT_HPP_
