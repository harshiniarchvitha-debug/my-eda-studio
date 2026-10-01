import pandas as pd
import plotly.express as px

def generate_stats(df: pd.DataFrame) -> dict:
    clean_df = df.copy()

    # Numeric conversion for formatted strings
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

            # Compute frequency counts so bars draw explicitly
            counts = num_df[col].value_counts().reset_index()
            counts.columns = [col, 'count']
            counts = counts.sort_values(by=col)

            fig = px.bar(
                counts, 
                x=col, 
                y='count',
                title=f"Distribution of {col}",
                template="plotly_white",
                color_discrete_sequence=['#1b263b']
            )

            fig.update_layout(
                height=380,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='#f8f9fa',
                font_family="Plus Jakarta Sans",
                font_color="#1b263b",
                title_font_family="Playfair Display",
                title_font_size=20,
                title_font_color="#1b263b",
                bargap=0.2,
                margin=dict(l=40, r=40, t=60, b=40)
            )
            
            # Crucial: include_plotlyjs='cdn' ensures the JS library loads to render bars!
            chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
            charts.append(chart_html)

    return {
        "summary": summary,
        "charts": charts
    }