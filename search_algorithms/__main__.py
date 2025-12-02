#!/usr/bin/env python3
"""
Search Algorithms Explainer - Main Entry Point

A comprehensive command-line application for learning and comparing search algorithms.
Supports Linear Search, Binary Search, and performance comparisons.

Usage:
    python -m search_algorithms [command]
    search-algorithms [command]

Commands:
    /start        - Start the interactive program (default)
    /end          - Exit the program
    /history      - Show search history
    /clearresult  - Clear the last search result
    -h, --help    - Show help message
    -v, --version - Show version
"""

import sys
import argparse
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from search_algorithms.utils import load_questions, show_history, clear_last_result
from search_algorithms.cli.commands import process_main_menu
from search_algorithms import __version__


def main():
    """Entry point with argparse for CLI commands."""
    
    parser = argparse.ArgumentParser(
        prog="search-algorithms",
        description="Search Algorithms Explainer - Interactive CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Start interactive mode
  %(prog)s /start             # Start interactive mode
  %(prog)s /history           # Show search history
  %(prog)s /clearresult       # Clear last search result
  %(prog)s -v                 # Show version
        """
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        default='/start',
        help='Command: /start (default), /end, /history, /clearresult'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )