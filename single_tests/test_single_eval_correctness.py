from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams
import json

test_case = LLMTestCase(
    input = "Where do penguins live?",
    actual_output = "Penguins are flightless seabirds that live primarily in the Southern Hemisphere. They are commonly associated with Antarctica, but they also inhabit a variety of environments including the cool shores of South America, southern Africa, and even the Galapagos Islands near the equator. Penguins are adapted to live in these diverse habitats, ranging from icy coasts to more temperate regions.", 
    expected_output = "Penguins live in the Southern Hemisphere, including Antarctica, South America, southern Africa, and the Galapagos Islands."

)

metric =  GEval(
    name =  "Correctness",
    criteria = (
        "Determine whether the model's response is factually correct and aligns with the expected answer. "
    ),
    evaluation_params=[
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT
    ]
)

metric.measure(test_case= test_case)

print ("Score:", metric.score)
print ("Reason:", metric.reason)
print ("Passed:", metric.is_successful())
