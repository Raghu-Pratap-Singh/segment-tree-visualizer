from setuptools import setup, find_packages

setup(
    # --- Package Name and Version ---
    # This is the name people use with 'pip install'
    name="segment-tree-visualizer", 
    version="0.1.0", 
    
    # --- Metadata ---
    description="A generic visualization tool for Static and Dynamic Segment Trees.",
    # You should replace these with your details
    author="Raghu Pratap Singh",
    author_email="raghupratapsinghparmar@gmail.com",
    url="https://github.com/Raghu-Pratap-Singh/segment-tree-visualizer",
    license="MIT", 
    
    # --- Dependencies ---
    install_requires=[
        "networkx",
        "matplotlib",
    ],
    
    # --- Finding the Code ---
    # This tells setuptools to look in the current directory for packages
    # (i.e., the SEGMENT_TREE_VISUALIZER folder)
    packages=find_packages(),
    
    # --- Python Version Requirement ---
    python_requires='>=3.8',
    
    # --- Classifiers (Recommended for PyPI) ---
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)