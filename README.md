
# Log Archive Tool

A Dockerized Python tool that archives logs from Unix-based systems based on specific criteria such as age or size. The tool is designed to help manage log files by moving older or larger logs to a specified archive directory, freeing up space and making log management easier.

## Idea Source

The idea for the Log Archive Tool project was inspired by the need for a simple yet effective tool to manage logs on Unix-based systems. Visit [roadmap.sh's Log Archive Tool project](https://roadmap.sh/projects/log-archive-tool) to see more details and learn about similar project ideas.

## Usage

To use the Log Archive Tool, you need to have Docker installed on your system. The most common location for logs on a Unix-based system is `/var/log`.

### Build the Docker Image

```bash
docker build -t log-archive-tool .
```

### Run the Docker Container

```bash
sudo docker run -v /var/log:/var/log -v /path/to/archive:/archive log-archive-tool --archive /archive --days-old 30
```

Replace `/path/to/archive` with your desired archive directory.

### Available Options

- `--source`: Source directory for logs (default: `/var/log`)
- `--archive`: Destination directory for archived logs (required)
- `--days-old`: Archive logs older than specified days
- `--max-size`: Archive logs larger than specified size (MB)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [abdulmajidyunusov18@gmail.com].

---

Happy managing your logs!
