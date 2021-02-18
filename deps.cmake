
macro(clone_dep DEP)
    set(DEP_PATH ${DEPS_ROOT}/${DEP})
    set(${DEP}_path ${DEPS_ROOT}/${DEP}/source/${DEP})
    if (EXISTS ${DEP_PATH})
        execute_process(COMMAND git -C ${DEP_PATH} pull)
    else()
        execute_process(COMMAND
                git clone https://github.com/vladasz/${DEP}
                ${DEP_PATH})
    endif()
endmacro(clone_dep)
