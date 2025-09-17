from setuptools import setup, find_packages

setup(
    name='figma-mcp-server',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi',
        'httpx',
        'pydantic',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'figma-mcp-server=figma_mcp.server:main',
        ],
    },
)
