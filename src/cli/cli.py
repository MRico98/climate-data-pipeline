import logging
import argparse
from ..data_logging.logging_config import setup_logging
import sys

logger = logging.getLogger(__name__)
setup_logging(log_dir='logs', verbose=True)

def handle_init_command(args: argparse.Namespace) -> None:
    config_file = args.config_file or 'config.json'
    db_path = args.db_path or 'database.db'

    logger.info(f'Initializing project with config file: {config_file} and database path: {db_path}')
    logger.info('Project initialized successfully.')

    try:
        print('Initializing project...')
        print("Finished initializing project.")
    except Exception as e:
        logger.error(f'Error initializing project: {e}')
        print(f'Error initializing project: {e}')
        sys.exit(1)

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Climate Data Scraper - Command Line Interface',
        epilog='For more information, read the DOC'
    )

    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    scrape_parser = subparsers.add_parser('scrape', help='Scrape climate data')
    scrape_parser.add_argument(
        '--city',
        type=str,
        required=True,
        help='City name to scrape data for'
    )
    scrape_parser.add_argument(
        '--start-date',
        type=str,
        required=True,
        help='Start date for scraping data (YYYY-MM-DD)'
    )
    scrape_parser.add_argument(
        '--end-date',
        type=str,
        required=True,
        help='End date for scraping data (YYYY-MM-DD)'
    )
    scrape_parser.add_argument(
        '--output',
        choices=['csv', 'json', 'db'],
        default='db',
        help='Output format for scraped data'
    )
    scrape_parser.add_argument(
        '--metrics',
        nargs='+',
        choices=['temperature', 'humidity', 'precipitation'],
        default=['temperature', 'humidity'],
        help='Metrics to scrape'
    )
    scrape_parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    init_parser = subparsers.add_parser('init', help='Initialize the project')
    init_parser.add_argument(
        '--config-file',
        type=str,
        help='Path to the configuration file'
    )
    init_parser.add_argument(
        '--db-path',
        type=str,
        help='Path to the database file',
    )

    return parser

def main():
    parser = setup_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == 'init':
        handle_init_command(args)
    """
    if args.command == 'scrape':
        handle_scrape_command(args)
    elif args.command == 'query':
        handle_query_command(args)
    elif args.command == 'analyze':
        handle_analyze_command(args)
    elif args.command == 'visualize': 
        handle_visualize_command(args)
    elif args.command == 'init': 
        handle_init_command(args)
    else:
        parser.print_help()
    """
