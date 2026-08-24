import numpy as np


def softmax(logits):
    # Step 1: Exponentiate the logits to scale them
    # Subtracting max for numerical stability
    exp_values = np.exp(logits - np.max(logits))
    # Step 2: Normalize the exponentials by dividing with their sum
    probabilities = exp_values / np.sum(exp_values)
    return probabilities


# Example usage
logits = np.array([2.0, 1.0, 0.1])
probabilities = softmax(logits)

print("Logits:", logits)
print("Probabilities:", probabilities)
