project(phone)

set(SOURCES
    main.cpp
    phone.cpp
)

add_executable(${PROJECT_NAME} ${SOURCES})
target_compile_options(${PROJECT_NAME} PUBLIC -Wall -Wextra -Wno-narrowing)
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 17)
cmake_minimum_required(VERSION 3.1.0)
