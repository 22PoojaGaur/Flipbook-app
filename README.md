# Flipbook App

###### _This repository contains programming task given by Hasura company._

##### Author - Pooja Gaur (@22PoojaGaur)

### Problem Statement
look at `Flipbook_problem.pdf` to see the detailed problem statement.

### Broad Solution Idea
- The repository implements a compiler for a language defined for flipbook generation.
- The flipbooks can be specified in two ways
-- if image is position insensitive (i.e either there is single image or the image is not going to move during flipbook). User can give just range and image name
-- if image can vary in position or multiple images are to be placed, user can provide a grid size. This way the pdf page is treated as a grid and for each image the user can provide grid positions to place the image in.
- The project also give a simple GUI tool implemented in Tkinter to run the program through GUI.

### Product Progress
look at `Flipbook_progress.pdf` to see the product iterations and future possible iterations.

### Defined Flipbook Language

```
Tokens ->
FILENAME - '\w+\.(png|jpg|jpeg)'
NUMBER   - '\d+'
DASH     - '-'
CROSS    - 'X'
COMMA    - ','

Rules ->
<expr> : <imrange> FILENAME
        | <imrange> FILENAME <gridpose> <gridpose>
        | NUMBER CROSS NUMBER
        
<imrange> : NUMBER DASH NUMBER
           | NUMBER

<gridpose> : NUMBER COMMA NUMBER
```

### Libraries used
rply - To implement lexer, parser and abstract syntax tree.

tkinter - To implement basic gUI

argparse - To handle command line flags

fpdf - To write a pdf file

convert - To generate gif

### Running instructions 
1. Make sure you have `conda` on your system. (You can choose to use `pip`. The requirements.txt is generated for conda, if you choose to use pip install the packages individually.)
2. Run `conda create --name flipbook --file requirements.txt` to create the environment and `conda activate flipbook` to activate the environment.
3. Install `convert` tool of `imagemagick`
4. To use cli version, run `python fc.py --program your_programe.flip --outputfile outputname.gif`, to use gui version, run `python fc-gui.py` and follow instructions.
5. That's all!

There are multiple demo .flip files in `examples/` folder. To see the demo, you can run - `python fc.py --program examples/play_catch.flip --outputfile play_catch.gif` and checkout the output files generated.

### Code structure
- The driver modules `fc.py` and `fc-gui.py` are located in root folder
- The utility functions created to builder lexer, parser, AST and pdf / gif generation are in `utils` folder