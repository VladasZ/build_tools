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

macro(setup_mbed)
  set(MICROCONTROLLER_BUILD TRUE)
  set(BOARD_NAME NODE_${BOARD})
  set(MBED_ROOT ${CMAKE_SOURCE_DIR}/${MBED_LOCATION}/mbed${BOARD})
  set(MBED_PATH ${MBED_ROOT}/mbed-os)
  set(FIRMWARE_FILE ${PROJECT_NAME}.bin)
  set(MBED_CONFIG_FILE ${MBED_ROOT}/mbed_config.h)
  include(${MBED_PATH}/source.cmake)
  set(BOARD_PATH /Volumes/${BOARD_NAME}/${FIRMWARE_FILE})
  include_recursive(${MBED_PATH})
  include_directories(/usr/src/mbed-sdk)
  prepend(SOURCE ${MBED_ROOT} ${MBED_SOURCE})
  set(${SOURCE} ${SOURCE} ${MBED_CONFIG_FILE})
  add_definitions(
          -DMICROCONTROLLER_BUILD
          -DMBED_BUILD
          ${DEFINITIONS})
endmacro()

macro(mbed_cli_setup)
  ##########################################################################
  # mbed-cli specific targets
  ##########################################################################

  # detect the build type and select the corresponding cli profile
  set(MBED_BUILD_PROFILE "")
  string(TOLOWER ${CMAKE_BUILD_TYPE} LOWERCASE_CMAKE_BUILD_TYPE)
  if(LOWERCASE_CMAKE_BUILD_TYPE MATCHES debug)
    set(MBED_BUILD_PROFILE "${MBED_PATH}/tools/profiles/debug.json")
  elseif(LOWERCASE_CMAKE_BUILD_TYPE MATCHES relwithdebinfo)
    set(MBED_BUILD_PROFILE "${MBED_PATH}/tools/profiles/develop.json")
  elseif(LOWERCASE_CMAKE_BUILD_TYPE MATCHES release)
    set(MBED_BUILD_PROFILE "${MBED_PATH}/tools/profiles/release.json")
  elseif(LOWERCASE_CMAKE_BUILD_TYPE MATCHES minsizerel)
    set(MBED_BUILD_PROFILE "${MBED_PATH}/tools/profiles/release.json")
  else()
    message(WARNING "Build type '${CMAKE_BUILD_TYPE}' is unknown, using debug profile")
    set(MBED_BUILD_PROFILE "${MBED_PATH}/tools/profiles/debug.json")
  endif()

  add_custom_target(mbed-cli-build
          COMMAND ${CMAKE_COMMAND} -E echo "mbed compile --build BUILD/${CMAKE_BUILD_TYPE} --profile ${MBED_BUILD_PROFILE}"
          COMMAND mbed compile --build BUILD/${CMAKE_BUILD_TYPE} --profile ${MBED_BUILD_PROFILE}
          WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
          SOURCES ${SOURCE_FILES} ${SYS_SOURCE_FILES})

  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/project.cmake)
    include(${CMAKE_CURRENT_SOURCE_DIR}/project.cmake)
  else()
    MESSAGE(STATUS "Add a local project.cmake file to add your own targets.")
  endif()

  file(GENERATE OUTPUT "${CMAKE_BINARY_DIR}/.mbedignore" CONTENT "*")

endmacro()

macro(setup_mbed_targets)

  set_target_properties(${PROJECT_NAME} PROPERTIES ENABLE_EXPORTS 1)
  target_link_libraries(${PROJECT_NAME} -lstdc++ -lsupc++ -lm -lc -lgcc -lnosys)

  if(${BOARD} STREQUAL F446RE)
    message(F446RE)
    add_custom_command(TARGET ${PROJECT_NAME} PRE_LINK
            COMMAND "arm-none-eabi-cpp" -E -P -Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_memalign_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ${MBED_PATH}/targets/TARGET_STM/TARGET_STM32F4/TARGET_STM32F446xE/device/TOOLCHAIN_GCC_ARM/STM32F446XE.ld -o ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_pp.link_script.ld
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            BYPRODUCTS "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_pp.link_script.ld"
            )

  elseif(${BOARD} STREQUAL F746ZG)
    message(F746ZG)
    add_custom_command(TARGET ${PROJECT_NAME} PRE_LINK
            COMMAND "arm-none-eabi-cpp" -E -P -Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_memalign_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n -mcpu=cortex-m7 -mthumb -mfpu=fpv5-sp-d16 -mfloat-abi=softfp ${MBED_PATH}/targets/TARGET_STM/TARGET_STM32F7/TARGET_STM32F746xG/device/TOOLCHAIN_GCC_ARM/STM32F746xG.ld -o ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_pp.link_script.ld
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            BYPRODUCTS "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}_pp.link_script.ld"
            )
  else()
    message("Invalid board")
  endif()

  add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
          COMMAND ${ELF2BIN} -O binary $<TARGET_FILE:${PROJECT_NAME}> $<TARGET_FILE:${PROJECT_NAME}>.bin
          COMMAND ${CMAKE_COMMAND} -E echo "-- built: $<TARGET_FILE:${PROJECT_NAME}>.bin"
          COMMAND cp ${FIRMWARE_FILE} ${BOARD_PATH}
          COMMAND echo "Flashed successfully"
          )

  mbed_cli_setup()

endmacro()
