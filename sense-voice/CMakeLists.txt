add_subdirectory(csrc)

add_executable(sense-voice-main csrc/main.cc)
target_link_libraries(sense-voice-main PRIVATE sense-voice-core ggml)

add_library(sense-voice SHARED csrc/sense-voice-shared.cc)
target_link_libraries(sense-voice PRIVATE sense-voice-core ggml)

