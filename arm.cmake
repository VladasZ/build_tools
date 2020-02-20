cmake_minimum_required(VERSION 3.9.2 FATAL_ERROR)

macro(_setup_arm_lib lib)

  project(${lib} C CXX ASM)

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
