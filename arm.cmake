cmake_minimum_required(VERSION 3.9.2 FATAL_ERROR)

macro(_setup_arm_lib lib)

  set(MBED_PATH ${CMAKE_SOURCE_DIR}/mbed-os)
  set(MBED_CMAKE_DATA ${MBED_PATH}/source.cmake)

  project(${lib} C CXX ASM)

  include(${MBED_CMAKE_DATA})

  set(FIRMWARE_FILE ${PROJECT_NAME}.bin)

  set(BOARD_NAME NODE_F446RE)
  set(BOARD_PATH /Volumes/${BOARD_NAME}/${FIRMWARE_FILE})

  add_definitions(
          -DMICROCONTROLLER_BUILD
          ${DEFINITIONS}
  )

  include_recursive(${MBED_PATH})
  include_directories(/usr/src/mbed-sdk)

  add_catalog_recursive(${PROJECT_SOURCE_DIR} /source setup_arm_lib)
  add_library(${PROJECT_NAME} ${setup_arm_lib})

  setup_deps()
  link_deps()

  set_target_properties(${PROJECT_NAME} PROPERTIES ENABLE_EXPORTS 1)
  target_link_libraries(${PROJECT_NAME} -lstdc++ -lsupc++ -lm -lc -lgcc -lnosys)

endmacro()
