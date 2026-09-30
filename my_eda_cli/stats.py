import pandas as pd
import plotly.express as px

def generate_stats(df: pd.DataFrame) -> dict:
    """Calculates numerical summaries and generates styled distribution charts."""
    clean_df = df.copy()

    for col in clean_df.select_dtypes(include=['object', 'string']).columns:
        converted = pd.to_numeric(clean_df[col].astype(str).str.replace(',', ''), errors='coerce')
        if converted.notnull().sum() > 0.5 * clean_df[col].notnull().sum():
            clean_df[col] = converted

    num_df = clean_df.select_dtypes(include=['number'])
    
    summary = []
    charts = []
    
    if not num_df.empty:
        summary = num_df.describe().T.reset_index().rename(columns={"index": "column"}).to_dict(orient="records")
        
        for col in num_df.columns:
            if num_df[col].dropna().empty:
                continue

            # Create histogram with distinct outline borders and visible bin gaps
            fig = px.histogram(
                num_df, 
                x=col, 
                title=f"Distribution of {col}",
                template="plotly_white",
                color_discrete_sequence=["#d4dcc2"]
            )
            
            fig.update_traces(
                marker_line_color='#c5a059',  # Gold border around bars
                marker_line_width=1.5,
                opacity=0.9
            )

            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='#fcfbf9',
                font_family="Plus Jakarta Sans",
                font_color="#e6cc9a",
                title_font_family="Playfair Display",
                title_font_size=18,
                title_font_color="#1b263b",
                bargap=0.2,  # Adds spacing between bars so they don't look like thin lines
                margin=dict(l=20, r=20, t=50, b=20)
            )
            
            chart_html = fig.to_html(full_html=False, include_plotlyjs=False)
            charts.append(chart_html)

    return {
        "summary": summary,
        "charts": charts
    }