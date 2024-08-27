# Roadmap.sh Archive logs Project

https://roadmap.sh/projects/log-archive-tool

## Description

This project is a simple cli tool written in python that allows you to archive your logs from your provided log directory to a specified archive directory. 

## Usage


### Run form the project directory

```bash
chmod +x log_archive
```

```bash
./log_archive <log_directory>
```

### Run from any directory

```bash
chmod +x log_archive
```

```bash
cp log_archive /usr/local/bin
```

> If permission denied, use `sudo`

```bash
sudo log_archive <log_directory>
```

```bash
log_archive <log_directory>
```

## Example

```bash
log_archive /var/log
```