#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ffmpeg_image_transport::ffmpeg_image_transport_component" for configuration "RelWithDebInfo"
set_property(TARGET ffmpeg_image_transport::ffmpeg_image_transport_component APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(ffmpeg_image_transport::ffmpeg_image_transport_component PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libffmpeg_image_transport_component.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libffmpeg_image_transport_component.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS ffmpeg_image_transport::ffmpeg_image_transport_component )
list(APPEND _IMPORT_CHECK_FILES_FOR_ffmpeg_image_transport::ffmpeg_image_transport_component "${_IMPORT_PREFIX}/lib/libffmpeg_image_transport_component.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
