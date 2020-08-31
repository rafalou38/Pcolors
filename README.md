<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://res.cloudinary.com/dr844cxrp/image/upload/v1592208914/Fichier_3_omuqch.png" alt="Project logo"></a>
</p>

<h3 align="center">Pcolors</h3>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/status-active-success.svg)]() -->
[![GitHub issues](https://img.shields.io/github/issues/rafalou38/Pcolors)](https://github.com/rafalou38/Pcolors/issues)
[![GitHub forks](https://img.shields.io/github/forks/rafalou38/Pcolors)](https://github.com/rafalou38/Pcolors/network)
[![GitHub stars](https://img.shields.io/github/stars/rafalou38/Pcolors)](https://github.com/rafalou38/Pcolors/stargazers)
[![GitHub license](https://img.shields.io/github/license/rafalou38/Pcolors)](https://github.com/rafalou38/Pcolors/blob/master/LICENSE)

</div>

---

<p align="center"> Pcolors is made to simplify printing colors in the console.
    <br> 

## 📝 Table of Contents
- [📝 &nbsp;&nbsp;Table of Contents](#pencil-table-of-contents)
- [🧐 &nbsp;&nbsp;About](#-about)
- [🏁 &nbsp;&nbsp;Getting Started](#-getting-started)
	- [Installing](#installing)
- [📚&nbsp;&nbsp; Usage](#-usage)
	- [cprint](#cprint)
	- [style](#style)
- [🖌&nbsp;&nbsp; styling rules](#-styling-rules)
	- [color](#color)
	- [end](#end)
	- [format](#format)
- [✒ &nbsp;&nbsp;shortcuts](#-shortcuts)
- [✍️ &nbsp;&nbsp;Authors](#️-authors)
- [🔎 &nbsp;&nbsp;Examples](#-examples)
	- [powershell](#powershell)
	- [cmd](#cmd)
	- [windows terminal](#windows-terminal)
	- [pycharm](#pycharm)


## 🧐 &nbsp;&nbsp;About

This package is perfect if you want to display fancy text on the console
without having to worry about ANSI escape codes ASGR sequences and all theses boring an complicated stuff Pcolors do all that for you

## 🏁 &nbsp;&nbsp;Getting Started

### Installing

You can install Pcolors using pip:

>__pip install Pcolors__

to verify the installation you can do

>__python -m Pcolors__

## 📚&nbsp;&nbsp; Usage



### cprint

`cprint()` is the base function of Pcolors use it to directly print colored text using the [styling rules](#styling):

`cprint("text", styling rules)`

```python
from Pcolors import cprint

cprint("text", fg_color="red", bg_color="lblue")
```

### style

`style()` is used to define styles using the [styling rules](#styling):

```python
from Pcolors import style

header = style(
	fg_color="green",
	bg_color="lblack",
	format=["framed", "bold", "underline_bold"],
)

cprint("my header", style=header)
...
cprint("my second header", style=header)

```

## 🖌&nbsp;&nbsp; styling rules

### color

use fg_color and bg_color to define the forground color and the background color
	

```python
from Pcolors import cprint, style

cprint("text", fg_color="red", bg_color="lblue")
style(fg_color="red", bg_color="lblue")
```
you can use color names:
- white / lwhite
- cyan / lcyan
- magenta / lmagenta
- blue / lblue
- yellow / lyellow
- green / lgreen
- red / lred
- black / lblack
 
or you can use codes:

- 97 / 37
- 96 / 36
- 95 / 35
- 94 / 34
- 93 / 33
- 92 / 32
- 91 / 31
- 90 / 30


  
### end

use end to define what should be appended to the output, default : "\n"

```python
from Pcolors import cprint, style


cprint("text", fg_color="red", bg_color="lblue", end="")
style(fg_color="red", bg_color="lblue", end="")
```
defining end to "" make the  print don't go to a new line at the end
permitting to print multiple colors on a single line

### format

use format to define the formatting of the text

```python
from Pcolors import cprint, style


cprint("text", format=["bold","underline"])
style(format=["bold","underline"])
```
you can use format names:
- normal
- bold
- faint
- italic
- underline
- slow_blink
- rapid_blink
- reverse
- hidden
- crossed
- underline_bold
- framed
- rounded
 
or you can use codes:

- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 21
- 51
- 52

## ✒ &nbsp;&nbsp;shortcuts

you can also use shortcuts for styling :

you can found them in `Pcolors.shortcuts`

```python
from Pcolors import style
from Pcolors.shortcuts import light, dark, format


header = style(
	fg_color=dark.green,
	bg_color=light.black,
	format=[
		format.framed,
		format.bold,
		format.underline_bold
	],
)
```

or for using manually with `code()` and [styling rules](#styling):

```python
from Pcolors import code
from Pcolors.shortcuts import light, dark, format

code(light.green) #>

```

  

## ✍️ &nbsp;&nbsp;Authors

-   [@rafalou38](https://github.com/rafalou38) - Idea & Initial work

## 🔎 &nbsp;&nbsp;Examples

### powershell

<img width=200px height=200px src="https://res.cloudinary.com/dr844cxrp/image/upload/v1592208914/Fichier_3_omuqch.png" alt="Project logo">

### cmd

<img width=200px height=200px src="https://github.com/rafalou38/Pcolors/blob/master/images/examples/cmd.jpg" alt="Project logo">

### windows terminal

<img width=200px height=200px src="https://res.cloudinary.com/dr844cxrp/image/upload/v1592208914/Fichier_3_omuqch.png" alt="Project logo">

### pycharm

<img width=200px height=200px src="https://res.cloudinary.com/dr844cxrp/image/upload/v1592208914/Fichier_3_omuqch.png" alt="Project logo">
