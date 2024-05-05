from importlib.metadata import version

pkgs = ["matplotlib",
        "pandas",
        "numpy",
        "torch",
       ]
for p in pkgs:
    print(f"{p} version: {version(p)}")
# matplotlib version: 3.8.4
# pandas version: 2.2.2
# numpy version: 1.26.4
# torch version: 2.3.0+cu121
