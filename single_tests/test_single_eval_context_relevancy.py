from deepeval.metrics import ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase


test_case = LLMTestCase(
        input="Where do penguins live?",
        actual_output="Penguins are flightless seabirds that live primarily in the Southern Hemisphere. They are commonly associated with Antarctica, but they also inhabit a variety of environments including the cool shores of South America, southern Africa, and even the Galapagos Islands near the equator. Penguins are adapted to live in these diverse habitats, ranging from icy coasts to more temperate regions.",
        retrieval_context = ["Penguins are flightless seabirds that are specially adapted for life in the Southern Hemisphere. Although people often associate them only with Antarctica, penguins live in a wide range of environments, including the icy coasts of Antarctica, the cool shores of South America and southern Africa, and even the Galapagos Islands near the equator. Their upright posture, compact bodies, and distinctive black-and-white coloring make them among the most recognizable birds in the world."]
)


metric = ContextualRelevancyMetric(threshold=0.7)

metric.measure(test_case)

print("Score:", metric.score)
print("Reason:", metric.reason)
print("Passed:", metric.is_successful())
