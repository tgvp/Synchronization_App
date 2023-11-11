import os
import time
import pytest
import shutil
import hashlib
import tempfile


from unittest.mock import patch, call, MagicMock
from freezegun import freeze_time

from sync_app import *

# Create folders
@pytest.fixture
def temp_folders(request):
    temp_dir = tempfile.mkdtemp()
    
    # addfinalizer pytest fixture that will run after the test is done
    request.addfinalizer(lambda: shutil.rmtree(temp_dir))
    
    return temp_dir

# must create files that will go inside the folders
@pytest.fixture
def temp_file(request):
    
    # TODO: test this copilot suggestion later
    #temp_file = tempfile.NamedTemporaryFile()
    #request.addfinalizer(lambda: temp_file.close())
    #return temp_file

    content = b"test"
    
    # temp
    temp_filepath = os.path.join(tempfile.mkdtemp(), 'test.txt')
    
    # create a temp file
    with open(temp_filepath, "wb") as f:
        f.write(content)

    # addfinalizer pytest fixture that will run after the test is done
    request.addfinalizer(lambda: os.remove(temp_filepath))
    return temp_filepath

# Test functions

# Test if the folders are created
def test_create_folders(temp_folders):
    
    # source, replica, .log
    source_folder = os.path.join(temp_folders, "source_test")
    replica_folder = os.path.join(temp_folders, "replica_test")
    log_folder = os.path.join(temp_folders, ".log_test")
    
    # create folders
    create_folders(source_folder, replica_folder, log_folder)
    
    # check if the folders are created
    assert os.path.exists(os.path.join(temp_folders, "source_test"))
    assert os.path.exists(os.path.join(temp_folders, "replica_test"))
    assert os.path.exists(os.path.join(temp_folders, ".log_test"))

def test_copy_file(temp_file, temp_folders):  # Fix the function signature
    destination = os.path.join(temp_folders, "test_file.txt")  # Correct the variable name
    
    copy_file(temp_file, destination)
    
    # check if content is the same
    with open(temp_file, "rb") as source_f, open(destination, "rb") as dest_f:
        assert source_f.read() == dest_f.read()

# Test if MD5 is calculated correctly
def test_calculate_md5(temp_file):
    
    # calculate md5
    md5 = calculate_md5(temp_file)
    
    # check if the expected md5 is the same as the calculated md5
    assert md5 == hashlib.md5(b"test").hexdigest()
