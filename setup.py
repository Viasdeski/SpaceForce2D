import cx_Freeze 
executables = [cx_Freeze.Executable(script="SpaceForce.py", icon="nave.ico")]
cx_Freeze.setup(
    name = "Space Force",
    options = {"build.exe":{
        "packages":["pygame"],
        "include_files": ["assets"]
    }
  },
  executables = executables
)