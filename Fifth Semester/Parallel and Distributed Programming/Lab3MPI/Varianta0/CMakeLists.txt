cmake_minimum_required(VERSION 3.25)
project(Varianta0)

set(CMAKE_CXX_STANDARD 20)

add_executable(Varianta0 main.cpp)

# Copy the .txt files to the output directory
add_custom_command(TARGET Varianta0 POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_SOURCE_DIR}/Numar1.txt
        ${CMAKE_SOURCE_DIR}/Numar2.txt
        $<TARGET_FILE_DIR:Varianta0>)
