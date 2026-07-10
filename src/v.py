from predict import predict
import pandas as pd

student = pd.DataFrame({
    "cgpa":[8.8],
    "branch":["CSE"],
    "college_tier":["Tier 1"],
    "coding_skills":[90],
    "dsa_score":[88],
    "aptitude_score":[85],
    "communication_skills":[80],
    "ml_knowledge":[75],
    "system_design":[70],
    "internships":[2],
    "projects_count":[4],
    "hackathons":[2],
    "open_source_contributions":[20],
    "backlogs":[0]
})

print(predict(student))
