#!/usr/bin/env python
"""
Script to create a new Jekyll blog post with proper naming convention and frontmatter.
"""
import argparse
import os
from datetime import datetime


def slugify(title):
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    # Replace spaces with hyphens
    slug = slug.replace(' ', '-')
    # Remove any characters that aren't alphanumeric, hyphens, or underscores
    slug = ''.join(c for c in slug if c.isalnum() or c in '-_')
    # Remove consecutive hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug


def create_post(title, category='Coding', tags=''):
    """Create a new Jekyll blog post file."""
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    datetime_str = now.strftime('%Y-%m-%d %H:%M:%S')

    # Create slug from title
    slug = slugify(title)

    # Create filename
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join('_posts', filename)

    # Check if file already exists
    if os.path.exists(filepath):
        print(f"Error: File {filepath} already exists!")
        return

    # Create frontmatter
    frontmatter = f"""---
layout: post
title: "{title}"
date: {datetime_str}
category: {category}
tags: {tags}
---

Write your post content here...
"""

    # Write the file
    with open(filepath, 'w') as f:
        f.write(frontmatter)

    print(f"Created new post: {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description='Create a new Jekyll blog post',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "My First Post"
  %(prog)s "Python Tips" --category Coding --tags "python tips"
  %(prog)s "Travel Story" -c Travel -t "travel adventure"
        """
    )
    parser.add_argument('title', help='Title of the blog post')
    parser.add_argument(
        '-c', '--category',
        default='Coding',
        help='Post category (default: Coding)'
    )
    parser.add_argument(
        '-t', '--tags',
        default='',
        help='Space-separated tags (default: empty)'
    )

    args = parser.parse_args()

    create_post(args.title, args.category, args.tags)


if __name__ == '__main__':
    main()
