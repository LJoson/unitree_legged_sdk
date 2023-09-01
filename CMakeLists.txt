if(NOT DEFINED unitree_legged_sdk_VERSION)
    string(TIMESTAMP unitree_legged_sdk_VERSION "%Y%m%d")
endif()

set(unitree_legged_sdk_VERSION_MAJOR 1)
set(unitree_legged_sdk_VERSION_MINOR 0)
set(unitree_legged_sdk_VERSION_PATCH ${unitree_legged_sdk_VERSION})
set(unitree_legged_sdk_VERSION_STRING ${unitree_legged_sdk_VERSION_MAJOR}.${unitree_legged_sdk_VERSION_MINOR}.${unitree_legged_sdk_VERSION_PATCH})
message(STATUS "unitree_legged_sdk_VERSION_STRING = ${unitree_legged_sdk_VERSION_STRING}")

cmake_minimum_required(VERSION 2.8.3)
project(unitree_legged_sdk)

# check arch and os
message("-- CMAKE_SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR}")
if("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "x86_64.*")
  set(ARCH amd64)
endif()
if("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "aarch64.*")
  set(ARCH arm64)
endif()

include_directories(include)
link_directories(lib/cpp/${ARCH})

option(PYTHON_BUILD "build python wrapper" OFF)
if(PYTHON_BUILD)
  add_subdirectory(python_wrapper)
endif()

set(EXTRA_LIBS -pthread libunitree_legged_sdk.a)
set(CMAKE_CXX_FLAGS "-O3 -fPIC -no-pie")
set(CMAKE_CXX_STANDARD 14)



