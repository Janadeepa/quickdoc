def generate_markdown_documentation(comments):
    markdown_content = ''
    for comment in comments:
        markdown_content += f"### {comment['function_name']}\n\n"
        markdown_content += f"**Description:** {comment['description']}\n\n"
        # Add more fields like parameters, return values, examples, etc.
    return markdown_content
