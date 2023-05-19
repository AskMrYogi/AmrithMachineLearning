import numpy as np


def quantize_weights(weights, num_bits):
    # Calculate the range of values spanned by the weight matrix
    min_value = np.min(weights)
    max_value = np.max(weights)

    # Calculate the interval size based on the number of bits
    num_intervals = 2 ** num_bits
    interval_size = (max_value - min_value) / num_intervals

    # Map each weight value to its closest quantized value
    quantized_weights = np.round((weights - min_value) / interval_size) * interval_size + min_value

    return quantized_weights


# Example usage
weight_matrix = np.array([0.9, 0.003, 0.8])
quantized_matrix = quantize_weights(weight_matrix, num_bits=8)

print("Original weight matrix:", weight_matrix)
print("Quantized weight matrix:", quantized_matrix)
