from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def render_report(quality_data: dict, stats_data: dict, output_path: str):
    """Renders Jinja2 HTML report and writes it to disk."""
    template_dir = Path(__file__).parent.parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("report.html")
    
    # Passing both quality and stats dictionary to the HTML template
    html_content = template.render(quality=quality_data, stats=stats_data)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)