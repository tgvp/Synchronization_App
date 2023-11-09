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

- Jupyter Notebook:
  - `Run All Cells` in [``src/sync_app.ipynb``](src/sync_app.ipynb): the program will be running and any change made to the source folder will be reflected into the replica folder within 60 seconds (default).

- CLI app:
  - [`src/sync_app.py`](src/sync_app.py): python sync_app.py --source ../raw/source --replica ../replica --log ../.log --interval 5

## Latest Logfile:
- [`.log/sync_log_Thu_Nov__9_08%3A46%3A23_2023.txt`](.log/sync_log_Thu_Nov__9_08%3A46%3A23_2023.txt)

```bash
[Thu Nov  9 08:46:23 2023] Syncing ../raw/source_folder and ../replica_folder folders
[Thu Nov  9 08:46:23 2023] Sync interval: 60 seconds
[Thu Nov  9 08:48:23 2023] Copied: ../raw/source_folder/dummy_text.txt -> ../replica_folder/dummy_text.txt
[Thu Nov  9 08:49:23 2023] Copied: ../raw/source_folder/dummy_text.txt -> ../replica_folder/dummy_text.txt
[Thu Nov  9 08:49:23 2023] Copied: ../raw/source_folder/ratings_matrix.csv -> ../replica_folder/ratings_matrix.csv
[Thu Nov  9 08:50:23 2023] Deleted: ../replica_folder/ratings_matrix.csv
[Thu Nov  9 08:51:23 2023] Copied: ../raw/source_folder/ratings_matrix.csv -> ../replica_folder/ratings_matrix.csv
[Thu Nov  9 08:52:23 2023] Copied: ../raw/source_folder/Veeam-Logo.png -> ../replica_folder/Veeam-Logo.png
[Thu Nov  9 08:56:36 2023] Stopping folders synchronization.
```

## Issues created:

- [X] [Issue #1](https://github.com/tgvp/Synchronization_App/issues/1)
- [X] [Issue #2](https://github.com/tgvp/Synchronization_App/issues/2)
