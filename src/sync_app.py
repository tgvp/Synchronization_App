import os
import time
import hashlib
import argparse

def calculate_md5(file_path: str) -> hashlib.md5:
    """Calculate the MD5 hash of a file

    Args:
        file_path (str): file path

    Returns:
        _type_: hash_md5
    """
    
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def copy_file(source_file: str, replica_file: str):
    """Copy file from source to replica

    Args:
        source_file (str): source file path
        replica_file (str): replaica file path
    """
    
    with open(source_file, 'rb') as src_file:
        with open(replica_file, 'wb') as dest_file:
            for chunk in iter(lambda: src_file.read(4096), b""):
                dest_file.write(chunk)

def create_folders(source_folder: str, replica_folder: str, log_folder: str):
    """Create folders if they don't exist
    """
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)

    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

def synchronize_folders(source_folder: str, replica_folder: str, log_file_path: str, sync_interval: int, run_sync: bool = True):
    """Sync folders and log each addition, modification and removal of files
    """
    
    # Tracking replica folder
    replica_state = {}
    
    current_time = time.ctime()
    
    print(f"[{current_time}] Syncing {source_folder} and {replica_folder} folders")
    
    print(f"[{current_time}] Sync interval: {sync_interval} seconds")
    
    print(f"[{current_time}] Logging to {log_file_path}")
    
    with open(log_file_path, "w") as log_file:
        log_file.write(f"[{current_time}] Syncing {source_folder} and {replica_folder} folders\n")
        log_file.write(f"[{current_time}] Sync interval: {sync_interval} seconds\n")
    
    while run_sync:
        for root, dirs, files in os.walk(source_folder):
            for file_name in files:
                source_file_path = os.path.join(root, file_name).replace('\\', '/')
                replica_file_path = os.path.join(replica_folder, os.path.relpath(source_file_path, source_folder)).replace('\\', '/')

                # MD5 hash of source file
                source_file_md5 = calculate_md5(source_file_path)

                # Verify here
                if replica_file_path in replica_state:
                    replica_file_md5 = replica_state[replica_file_path]
                else:
                    replica_file_md5 = ""

                # checkinfg if file is new or has been modified
                if source_file_md5 != replica_file_md5:
                    copy_file(source_file_path, replica_file_path)
                    replica_state[replica_file_path] = source_file_md5
                    current_time = time.ctime()
                    print(f"[{current_time}] Copied: {source_file_path} -> {replica_file_path}")
                    with open(log_file_path, "a") as log_file:
                        log_file.write(f"[{current_time}] Copied: {source_file_path} -> {replica_file_path}\n")

        # Check for files to delete in replica folder
        for replica_file_path, replica_file_md5 in list(replica_state.items()):
            source_file_path = os.path.join(source_folder, os.path.relpath(replica_file_path, replica_folder))
            # deletes in replica folder if it was deleted in source
            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                del replica_state[replica_file_path]
                current_time = time.ctime()
                print(f"[{current_time}] Deleted: {replica_file_path}")
                with open(log_file_path, "a") as log_file:
                    log_file.write(f"[{time.ctime()}] Deleted: {replica_file_path}\n")

        time.sleep(sync_interval)

def main():
    
    # Parse arguments: source, replica, log and sync_interval
    parser = argparse.ArgumentParser(description='Sync folders')
    parser.add_argument('--source', type=str, help='Source folder')
    parser.add_argument('--replica', type=str, help='Replica folder')
    parser.add_argument('--log', type=str, help='Log folder')
    parser.add_argument('--interval', type=int, help='Sync interval in seconds')
    args = parser.parse_args()

    if args.source:
        source_folder = args.source

    if args.replica:
        replica_folder = args.replica

    if args.log:
        log_folder = args.log

    if args.interval:
        sync_interval = args.interval

    # Create source folder, replica and log folders if they doesn't exist
    create_folders(source_folder, replica_folder, log_folder)
    
    try:

        log_file_path = log_folder + f'/sync_log_{time.ctime()}.txt'.replace(' ', '_')

        # Synchronization
        synchronize_folders(source_folder, replica_folder, log_file_path, sync_interval)

        # Logging the end of the synchronization application
        current_time = time.ctime()
        print(f"[{current_time}] Stopping synchronization thread...")
        with open(log_file_path, "a") as log_file: # append to log file
            log_file.write(f"[{current_time}] Stopping folders synchronization.\n")

    except Exception as e:
        # log exception if not KeyboardInterrupt
        if not isinstance(e, KeyboardInterrupt):
            current_time = time.ctime()
            print(f"{[current_time]} Error: {e}")
            with open(log_file_path, "a") as log_file: # append exception to log file
                log_file.write(f"{[current_time]} Error: {e}\n")

if __name__ == '__main__':
    main()
    
main()