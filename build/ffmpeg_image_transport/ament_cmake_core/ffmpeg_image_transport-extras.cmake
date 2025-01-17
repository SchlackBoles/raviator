set(FFMPEG_PKGCONFIG "" CACHE STRING "extra path to pkgconfig")
set(ENV{PKG_CONFIG_PATH} ${FFMPEG_PKGCONFIG})

find_package(PkgConfig REQUIRED)

pkg_check_modules(LIBAV REQUIRED IMPORTED_TARGET
    libavcodec
    libswresample
    libswscale
    libavutil)
