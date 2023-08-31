import glob
import os.path
from distutils.core import setup
__version__ = "0.0.1"

# make sure the working directory is BASE_DIR
# BASE_DIR = os.path.dirname(__file__)
# os.chdir(BASE_DIR)

ext_modules = []

try:
    from pybind11.setup_helpers import Pybind11Extension, ParallelCompile, naive_recompile

    # `N` is to set the bumer of threads
    # `naive_recompile` makes it recompile only if the source file changes. It does not check header files!
    ParallelCompile("NPY_NUM_BUILD_JOBS", needs_recompile=naive_recompile, default=4).install()

    # could only be relative paths, otherwise the `build` command would fail if you use a MANIFEST.in to distribute your package
    # only source files (.cpp, .c, .cc) are needed
    source_files = glob.glob('python_wrapper/*.cpp', recursive=True)

    # If any libraries are used, e.g. libabc.so
    include_dirs = ["include"]
    library_dirs = ["lib/cpp/amd64"]
    # (optional) if the library is not in the dir like `/usr/lib/`
    # either to add its dir to `runtime_library_dirs` or to the env variable "LD_LIBRARY_PATH"
    # MUST be absolute path
    runtime_library_dirs = [os.path.abspath("lib/cpp/amd64")]
    libraries = ["unitree_legged_sdk"]

    ext_modules = [
        Pybind11Extension(
            "unitree_legged_sdk.robot_interface", # depends on the structure of your package
            source_files,
            # Example: passing in the version to the compiled code
            define_macros=[('VERSION_INFO', __version__)],
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            runtime_library_dirs=runtime_library_dirs,
            libraries=libraries,
            cxx_std=14,
            language='c++'
        ),
    ]
except ImportError:
    pass

setup(
    name='unitree_legged_sdk',  # used by `pip install`
    version='0.0.1',
    description='xxx',
    ext_modules=ext_modules,
    packages=['unitree_legged_sdk'], # the directory would be installed to site-packages
    setup_requires=["pybind11"],
    install_requires=["pybind11"],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
)