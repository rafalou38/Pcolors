import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="Pcolors",
	version="0.2",
	author="rafalou38",
	author_email="rafaloulou2@gmail.com",
	description="Package to simplify printing colors in the console.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/rafalou38/Pcolors",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Topic :: Printing",
	],
	python_requires='>=3.6',
)
