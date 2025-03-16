cmake_minimum_required(VERSION 3.25)
project(Varianta2)

set(CMAKE_CXX_STANDARD 20)
find_package(MPI REQUIRED)
include_directories(${MPI_INCLUDE_PATH})

add_executable(Varianta2 main.cpp)
target_link_libraries(Varianta2 ${MPI_LIBRARIES})