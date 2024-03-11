# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\SESIUNE_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\SESIUNE_autogen.dir\\ParseCache.txt"
  "SESIUNE_autogen"
  )
endif()
