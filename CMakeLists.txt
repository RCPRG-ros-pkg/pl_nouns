cmake_minimum_required(VERSION 3.5)
project(pl_nouns)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
# If you are using any messages, services, or actions, find them here
# For example:
# find_package(rclcpp REQUIRED)
# find_package(std_msgs REQUIRED)

# Include CMake module for Python
find_package(ament_cmake_python REQUIRED)

# Declare the package
ament_package()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})