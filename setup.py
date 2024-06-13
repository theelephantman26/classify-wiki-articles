from distutils.core import setup

setup(
    name="classify wikipedia articles",
    version="1.0",
    description="Python Distribution Utilities",
    author="Bhalchandra Naik",
    author_email="bnaik2611@gmail.com",
    packages=[
        "distutils", 
        "distutils.command",
        "black",
        "flake8",
        "ipython",
        "isort",
        "jupyterlab",
        "matplotlib",
        "mkdocs",
        "notebook",
        "numpy",
        "pandas",
        "pip",
        "python-dotenv",
        "scikit-learn",
        "tqdm",
        "typer"
    ],
)