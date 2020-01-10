cmake_minimum_required(VERSION 3.9.2 FATAL_ERROR)

macro(_setup_ios_exe exe)

    project(${exe})
    add_catalog_recursive(${PROJECT_SOURCE_DIR} / SOURCE)
    file(GLOB ASSETS ${ASSETS_DIRECTORY})
    add_executable(${PROJECT_NAME} ${SOURCE} ${ASSETS})

    link_conan_if_needed()
    link_deps()

 #   link_project_at_path(test_engine ${test_engine_path})

    find_library(UIKIT UIKit)
    find_library(GLKIT GLKit)
    find_library(OPEN_GLES OpenGLES)
    find_library(FOUNDATION Foundation)

    target_link_libraries(${PROJECT_NAME} ${UIKIT})
    target_link_libraries(${PROJECT_NAME} ${GLKIT})
    target_link_libraries(${PROJECT_NAME} ${FOUNDATION})
    target_link_libraries(${PROJECT_NAME} ${OPEN_GLES})

    set_target_properties(${PROJECT_NAME} PROPERTIES
            MACOSX_BUNDLE TRUE
            MACOSX_BUNDLE_GUI_IDENTIFIER org.cmake.${PROJECT_NAME}d
            MACOSX_BUNDLE_BUNDLE_VERSION 1
            MACOSX_BUNDLE_SHORT_VERSION_STRING 1
            RESOURCE "${ASSETS}"
            )

endmacro()
