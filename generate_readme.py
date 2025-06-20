import re

def generate_tool_name(filename):
    """Converts a filename to a user-friendly tool name."""
    name_parts = filename.replace(".html", "").split("_")
    return " ".join([part.capitalize() for part in name_parts])

def generate_description(tool_name):
    """Generates a brief description based on the tool name."""
    name_lower = tool_name.lower()
    if name_lower == "comma separator generator":
        return "Generates text with comma separators."
    if name_lower == "csv to json converter":
        return "Converts CSV data to JSON."
    if name_lower == "json validator":
        return "Validates JSON data."
    if name_lower == "xml validator":
        return "Validates XML data."
    if name_lower == "word count":
        return "Counts words in text data."

    # Handle hash generators specifically
    if "hash generator" in name_lower:
        hash_type = tool_name.split()[0] # e.g., MD5, SHA1
        return f"Generates {hash_type} hash of data."

    words = tool_name.split()
    action = words[-1]
    obj = " ".join(words[:-1])

    # Adjust action verb for pluralization if it ends with 's' (like 'Generators' -> 'Generates')
    if action.endswith("s") and not action.endswith("ss"): # Avoid changing 'Process' to 'Proces'
        # Check if it's a known plural that should be singular (e.g. Validators -> Validate)
        if action.lower() in ["validators", "converters", "generators", "escapers", "unescapers", "counters"]:
            action = action[:-1] # Make it singular, e.g., "Validators" -> "Validator"
        # Then ensure it's in third person singular form (e.g., "Validator" -> "Validates")
        if not action.endswith("s"):
             action += "s"
    elif not action.endswith("s"): # if action does not end with 's', add 's' (e.g. Decode -> Decodes)
        action += "s"


    if not obj: # Handle cases like "Decode" where there's no object
        return f"{action} data."
    return f"{action} {obj} data."

def generate_readme_content(html_files):
    """Generates the Markdown content for README.md."""
    readme_parts = ["# Online Tools - Comprehensive Guide\n"]
    readme_parts.append("This document provides a list of all available tools in this repository and basic instructions on how to use them.\n")

    for html_file in html_files:
        tool_name = generate_tool_name(html_file)
        description = generate_description(tool_name)
        link = f"[{html_file}]({html_file})"

        readme_parts.append(f"\n## {tool_name}\n")
        readme_parts.append(f"- **Description:** {description}")
        readme_parts.append(f"- **Link:** {link}")
        readme_parts.append("- **Usage:**")
        readme_parts.append(f"    1. Navigate to the `{html_file}` page.")

        # Adjust instructions based on tool type (heuristic: "encode/decode/convert" usually text, "generator" might be different)
        if any(keyword in tool_name.lower() for keyword in ["encode", "decode", "convert", "escape", "unescape", "encrypt", "decrypt", "hash"]):
            readme_parts.append(f"    2. Input your data into the provided text area.")
        elif "generator" in tool_name.lower():
             readme_parts.append(f"    2. Configure the options as needed.")
        else: # Default for other tools or file-based tools
            readme_parts.append(f"    2. Input your data (either text or file, depending on the tool).")
        readme_parts.append(f"    3. The result will be displayed on the page.")

    return "\n".join(readme_parts)

if __name__ == "__main__":
    # This list should be obtained from the previous step in a real scenario
    # For now, I'll use a placeholder list.
    # The actual list of HTML files will be determined in a later step by listing the files in the directory.
    html_files = [
        "base32_decode.html",
        "base32_encode.html",
        "base64_decode.html",
        "base64_encode.html",
        "comma_separator_generator.html",
        "csv_to_json_converter.html",
        "html_escape.html",
        "html_unescape.html",
        "json_validator.html",
        "md5_hash_generator.html",
        "sha1_hash_generator.html",
        "sha256_hash_generator.html",
        "sha512_hash_generator.html",
        "text_reverse.html",
        "url_decode.html",
        "url_encode.html",
        "word_count.html",
        "xml_validator.html"
    ]
    markdown_content = generate_readme_content(html_files)
    print(markdown_content)
