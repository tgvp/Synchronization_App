## Test Task

Please implement a program that synchronizes two folders: source and
replica. The program should maintain a full, identical copy of source
folder at replica folder. Solve the test task by writing a program in
Python.

- Synchronization must be one-way: after the synchronization content of the
  replica folder should be modified to exactly match content of the source
  folder;
  Synchronization should be performed periodically;

- File creation/copying/removal operations should be logged to a file and to the
  console output;
  Folder paths, synchronization interval and log file path should be provided
  using the command line arguments;
  It is undesirable to use third-party libraries that implement folder
  synchronization;
  
- It is allowed (and recommended) to use external libraries implementing other
  well-known algorithms. For example, there is no point in implementing yet
  another function that calculates MD5 if you need it for the task – it is perfectly
  acceptable to use a third-party (or built-in) library.

# Comments:

**This application was developed using **Jupyter Notebook** because it is a great tool to not only run code but also expose my thought process.**

**This is an improved version that performs the required tasks but a better finished product will need more time and thought into it.**

**The first version was developed and released in November 08 2023 and was able to do the required tasks. The improvement was necessary to present a better product.

**Since it was specified that this is a 3-5 days test, code optimizations and refactoring will be made during this time to present a better release version.**

## Application:

- [``src/sync_app.ipynb``](src/sync_app.ipynb)

## Simulation of file operations:

- [``src/simulate_fileops.py``](simulate_fileops.py)

## How to run me:

- `Run All Cells` in [``src/sync_app.ipynb``](src/sync_app.ipynb): the program will be running and any change made to the source folder will be reflected into the replica folder within 60 seconds (default).

## Issues created:

- [X] [Issue #1](https://github.com/tgvp/Synchronization_App/issues/1)
- [ ] [Issue #2](https://github.com/tgvp/Synchronization_App/issues/2)
