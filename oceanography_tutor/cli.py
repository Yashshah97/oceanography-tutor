"""
Command-line interface for Oceanography Flashcard Tutor.

Usage:
    oceanography_tutor [options] <command>

Options:
    -h --help     Show this screen.
    --version     Show version.

Commands:
    add          Add a new flashcard.
    review       Review existing flashcards.
    progress     Display progress tracking statistics.
"""

import sys
from docopt import docopt

def main():
    """
    Entry point for CLI interface.
    """
    args = docopt(__doc__, version='Oceanography Flashcard Tutor 1.0')
    
    if args['<command>'] == 'add':
        add_flashcard(args)
    elif args['<command>'] == 'review':
        review_flashcards(args)
    elif args['<command>'] == 'progress':
        display_progress(args)

def add_flashcard(args):
    """
    Add a new flashcard to the database.
    """
    # TO DO: implement adding a flashcard
    print("Not implemented yet.")

def review_flashcards(args):
    """
    Review existing flashcards.
    """
    # TO DO: implement reviewing flashcards
    print("Not implemented yet.")

def display_progress(args):
    """
    Display progress tracking statistics.
    """
    # TO DO: implement displaying progress stats
    print("Not implemented yet.")

if __name__ == '__main__':
    main()
