import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from io import StringIO

class MaternalHealthDashboard:
    """
    Lightweight helper to fetch maternal health CSV data from an API and
    render a bubble chart and pie chart in Streamlit. This is a minimal
    implementation so the app can run even if the upstream API returns
    only a small sample. Adjust field names if the API schema changes.
    """

    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint
        self.df = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        try:
            resp = requests.get(self.api_endpoint, timeout=10)
            resp.raise_for_status()
            csv_buf = StringIO(resp.text)
            df = pd.read_csv(csv_buf)
            return df
        except Exception as exc:
            st.warning(f"Failed to load dashboard data: {exc}")
            return pd.DataFrame()

    def create_bubble_chart(self):
        if self.df.empty:
            st.info("No data available for bubble chart.")
            return
        # Pick a few numeric columns heuristically for plotting
        numeric_cols = [c for c in self.df.columns if pd.api.types.is_numeric_dtype(self.df[c])]
        if len(numeric_cols) < 3:
            st.info("Insufficient numeric columns for bubble chart.")
            return
        x_col, y_col = numeric_cols[0], numeric_cols[1]
        size_col = numeric_cols[2]
        fig = px.scatter(self.df, x=x_col, y=y_col, size=size_col, hover_data=self.df.columns)
        st.plotly_chart(fig, use_container_width=True)

    def create_pie_chart(self):
        if self.df.empty:
            st.info("No data available for pie chart.")
            return
        # Try to find a categorical column; fallback to the first column
        cat_cols = [c for c in self.df.columns if not pd.api.types.is_numeric_dtype(self.df[c])]
        if not cat_cols:
            st.info("No categorical columns available for pie chart.")
            return
        cat_col = cat_cols[0]
        pie_df = self.df[cat_col].value_counts().reset_index()
        pie_df.columns = [cat_col, "count"]
        fig = px.pie(pie_df, names=cat_col, values="count")
        st.plotly_chart(fig, use_container_width=True)

    def get_bubble_chart_data(self):
        return self.df.head().to_string(index=False) if not self.df.empty else "No data"

    def get_pie_graph_data(self):
        return self.df.head().to_string(index=False) if not self.df.empty else "No data"
