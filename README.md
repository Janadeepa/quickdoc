
# QuickDoc

QuickDoc is a lightweight, command-line tool designed to simplify the generation of project documentation from code comments. It automates the tedious task of manually writing and updating documentation by extracting comments directly from source code files and formatting them into readable documentation files.

## Repository Structure

```
quickdoc/
│
├── docs/                   # Documentation templates and resources
│   ├── templates/          # Template files (Markdown, HTML, etc.)
│   └── assets/             # Assets like CSS, images, etc.
│
├── src/                    # Source code
│   ├── cli.py              # Command-line interface
│   ├── parser.py           # Code comment parsing logic
│   ├── generator.py        # Documentation generation logic
│   ├── server.py           # Live preview server
│   ├── versioning.py       # Versioning and history management
│   ├── integration.py      # Integration with source code repositories
│   └── search.py           # Search functionality implementation
│
├── tests/                  # Unit tests
│
└── README.md               # Project documentation
```

## Features

- **Markdown-based Documentation:** Developers write documentation using Markdown, ensuring easy formatting without the need for complex HTML or formatting tools.
- **Command Line Interface (CLI):** Includes a CLI tool for initializing, generating, and updating documentation directly from the terminal, facilitating seamless integration into build scripts and CI pipelines.
- **Customizable Templates:** Provides default templates (e.g., API reference, user guides) and allows customization to tailor styles, layouts, and navigation to specific project needs.
- **Live Preview Server:** Enables developers to preview documentation locally while writing, ensuring accuracy and visual representation before publication.
- **Versioning and History:** Supports documentation versioning for maintaining multiple software versions, with a change history feature for tracking modifications and easy rollback.
- **Integration with Source Code Repositories:** Integrates with Git repositories to automatically update documentation based on code commits or pull requests, ensuring documentation remains current.
- **Search Functionality:** Includes a search feature within generated documentation for quick information retrieval.
- **Multi-language Support:** Offers localization capabilities for creating documentation in multiple languages, accommodating international users.

## Usage

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd quickdoc
   ```

2. Install dependencies (if any):

   ```bash
   # Example for Click dependency
   pip install click
   ```

### Generating Documentation

To generate documentation from your project's source code, use the following command:

```bash
python src/cli.py generate <input_directory> <output_directory>
```

Replace `<input_directory>` with the directory containing your source code files and `<output_directory>` with the directory where you want the documentation to be generated.

### Previewing Documentation

To start the live preview server for locally previewing your documentation, run:

```bash
python src/cli.py preview
```

### Managing Versions

For managing documentation versions, you can use the following command:

```bash
python src/cli.py version
```

### Integrating with Source Code Repositories

To integrate with Git for automatic updates to documentation, use:

```bash
python src/cli.py integrate
```

### Searching Documentation

Implement search functionality within generated documentation using:

```bash
python src/cli.py search
```

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests to contribute new features, improvements, or fixes.

## License

This project is licensed under the [MIT License](LICENSE).
```
