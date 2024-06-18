import click
from parser import parse_comments
from generator import generate_markdown_documentation
from server import run_preview_server
from versioning import manage_versions
from integration import integrate_with_git
from search import implement_search_functionality

@click.group()
def cli():
    """Command-line interface for QuickDoc."""
    pass

@cli.command()
@click.argument('input_directory', type=click.Path(exists=True))
@click.argument('output_directory', type=click.Path())
def generate(input_directory, output_directory):
    """Generate documentation from code comments."""
    click.echo(f"Generating documentation from {input_directory} to {output_directory}...")
    comments = parse_comments(input_directory)
    documentation = generate_markdown_documentation(comments)
    # Save documentation to output_directory or integrate with templates

@cli.command()
def preview():
    """Start live preview server."""
    click.echo("Starting live preview server...")
    run_preview_server()

@cli.command()
def version():
    """Manage documentation versions."""
    click.echo("Managing documentation versions...")
    manage_versions()

@cli.command()
def integrate():
    """Integrate with source code repositories."""
    click.echo("Integrating with source code repositories...")
    integrate_with_git()

@cli.command()
def search():
    """Implement search functionality."""
    click.echo("Implementing search functionality...")
    implement_search_functionality()

if __name__ == '__main__':
    cli()
