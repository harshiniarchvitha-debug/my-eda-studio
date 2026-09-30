import click
from scipy import stats
from my_eda_cli.reader import load_data
from my_eda_cli.quality import assess_quality
from my_eda_cli.stats import generate_stats
from my_eda_cli.reporter import render_report

@click.command()
@click.option('--input', '-i', 'input_file', required=True, help='Path to input CSV/Parquet file')
@click.option('--output', '-o', default='report.html', help='Path for output HTML report')
def main(input_file, output):
    """CLI tool to generate automated data quality & EDA reports."""
    click.echo(f"🔍 Loading dataset: {input_file}...")
    df = load_data(input_file)
    
    click.echo("📊 Performing data quality checks...")
    quality = assess_quality(df)
    
    click.echo("📈 Generating statistical summaries...")
    stats = generate_stats(df)
    
    click.echo(f"📄 Rendering report to {output}...")
    render_report(quality, stats, output)  # <-- Make sure 'stats' is passed here!
    
    click.echo("✅ Done! Report successfully generated.")

    stats = generate_stats(df)
    print("Generated charts count:", len(stats.get('charts', [])))

if __name__ == '__main__':
    main()