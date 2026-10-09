import json
from statistics import mean

with open("evaluated_results.jsonl", "r", encoding="utf-8") as file:
    evaluated_results = [json.loads(line) for line in file]
    
experiment = {
    "experiment": "experiment_v1_k3",
    "retriever_k": 3,
    "number_of_test_cases": len(evaluated_results),
    
    "metrics":{
        "answer_relevancy": mean([result["answer_relevancy_score"] for result in evaluated_results]),
        "faithfulness": mean([result["faithfulness_score"] for result in evaluated_results]),
        "context_relevancy": mean([result["context_relevancy_score"] for result in evaluated_results]),
        "correctness": mean([result["correctness_score"] for result in evaluated_results])
    }
}

with open("experiment_v1.jsonl", "w", encoding="utf-8") as file:
    json.dump(experiment, file, indent=4)
    
    
print("Experiment summary saved to experiment_v1.jsonl")