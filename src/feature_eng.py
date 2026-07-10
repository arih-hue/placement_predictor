import pandas as pd
def add_features(df:pd.DataFrame)->pd.DataFrame:
    df=df.copy()
    df['technical_scr'] = 0.35 * df["coding_skills"] + 0.35 * df['dsa_score'] + 0.15 * df['ml_knowledge'] + 0.15 * df['system_design']
    df['experience_scr'] = df["internships"] * 3 + df['projects_count'] * 2 + df['hackathons'] + df['open_source_contributions'] / 10
    df['academic_scr'] = df['cgpa'] * 10 - df['backlogs'] * 15
    df['dsa_coding'] = (df['coding_skills'] * df['dsa_score']) / 100
    df['resume_strgth'] = df["projects_count"] + df["internships"] * 2 + df["hackathons"] + df["open_source_contributions"] / 10
    return df