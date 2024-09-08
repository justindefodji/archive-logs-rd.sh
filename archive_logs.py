
import os
import shutil
import argparse
from datetime import datetime, timedelta

def archive_logs(source_dir, archive_dir, days_old=None, max_size=None):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB

            # Check if the file matches the criteria
            if days_old and file_modified_time < datetime.now() - timedelta(days=days_old):
                shutil.move(file_path, archive_dir)
            elif max_size and file_size > max_size:
                shutil.move(file_path, archive_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Archive logs based on criteria.')
    parser.add_argument('--source', default='/var/log', help='Source directory for logs')
    parser.add_argument('--archive', required=True, help='Destination directory for archived logs')
    parser.add_argument('--days-old', type=int, help='Archive logs older than specified days')
    parser.add_argument('--max-size', type=float, help='Archive logs larger than specified size (MB)')

    args = parser.parse_args()
    archive_logs(args.source, args.archive, args.days_old, args.max_size)
