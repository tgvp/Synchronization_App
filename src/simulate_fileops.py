import shutil
import time
import os

def simulate_file_operations():
    """Simulate file operations by copying files to the source folder and removing them after a certain time."""
    
    source_folder = '../raw/source_folder'
    example_files = '../raw/example_files'

    # Sleep for 80 seconds
    time.sleep(80)

    # Copy dummy_text.txt
    shutil.copy(os.path.join(example_files, 'dummy_text.txt'), source_folder)

    # Sleep for 70 seconds
    time.sleep(70)

    # Copy modified dummy_text.txt
    shutil.copy(os.path.join(example_files, 'dummy_text-modify_1.txt'), os.path.join(source_folder, 'dummy_text.txt'))

    # Sleep for 15 seconds
    time.sleep(15)

    # Copy modified dummy_text.txt again
    shutil.copy(os.path.join(example_files, 'dummy_text-modify_2.txt'), os.path.join(source_folder, 'dummy_text.txt'))

    # Sleep for 5 seconds
    time.sleep(5)

    # Copy ratings_matrix.csv
    shutil.copy(os.path.join(example_files, 'ratings_matrix.csv'), source_folder)

    # Sleep for 90 seconds
    time.sleep(90)

    # Copy ratings_matrix.csv again
    shutil.copy(os.path.join(example_files, 'ratings_matrix.csv'), source_folder)

    # Sleep for 20 seconds
    time.sleep(20)

    # Copy Veeam-Logo.png
    shutil.copy(os.path.join(example_files, 'Veeam-Logo.png'), source_folder)

    # Sleep for 10 seconds
    time.sleep(10)

    # Remove Veeam-Logo.png
    os.remove(os.path.join(source_folder, 'Veeam-Logo.png'))

    # Sleep for 70 seconds
    time.sleep(70)

    # Copy Veeam-Logo.png again
    shutil.copy(os.path.join(example_files, 'Veeam-Logo.png'), source_folder)

if __name__ == "__main":
    simulate_file_operations()
