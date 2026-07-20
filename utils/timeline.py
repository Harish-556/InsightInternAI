import plotly.figure_factory as ff
import json

_QUERY = """Extract all tasks, phases, or milestones mentioned in this document.

Return ONLY a JSON array like this (no extra text):
[
  {"Task": "Data Collection", "Start": "2024-01-01", "Finish": "2024-01-07", "Phase": "Phase 1"},
  {"Task": "Model Training", "Start": "2024-01-08", "Finish": "2024-01-20", "Phase": "Phase 2"}
]

If exact dates are not mentioned, estimate reasonable dates.
Return valid JSON only."""

def extract_timeline(chain):
    result = chain.invoke(_QUERY)
    try:
        data = json.loads(result)
        df = [dict(Task=d["Task"], Start=d["Start"],
                   Finish=d["Finish"], Resource=d["Phase"]) for d in data]
        fig = ff.create_gantt(df, index_col='Resource',
                              show_colorbar=True, group_tasks=True)
        fig.update_layout(title="Project Timeline", height=400)
        return fig
    except:
        return None