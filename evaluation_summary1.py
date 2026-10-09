import json
from statistics import mean
from deepeval.metrics import AnswerRelevancyMetric, ContextualRelevancyMetric, FaithfulnessMetric, GEval 

with open("evaluated_results.jsonl", "r", encoding="utf-8") as file:
    evaluated_results = [json.loads(line) for line in file]
    
    
metrics = ["answer_relevancy_score", "faithfulness_score", "context_relevancy_score", "correctness_score"]


threshold = 0.7

print("\n RAG Evaluation Summary \n")

for metric in metrics:
    scores = [result[metric] for result in evaluated_results]
    average_score = mean(scores)
    
    passed = sum(score >= threshold for score in scores)
    failed = len(scores) - passed
    
    pass_rate = passed / len(scores) * 100
    
    print(metric.replace("_", " ").title())
    print(f"Average Score: {average_score:.2f}")
    print(f"Passed: {passed} / {len(scores)}")
    print(f"Failed: {failed} / {len(scores)}")
    print(f"Pass Rate: {pass_rate:.1f}%")
    print()