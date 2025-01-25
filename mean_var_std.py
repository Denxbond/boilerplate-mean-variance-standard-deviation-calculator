import numpy as np

def calculate(input_list):
    # Validate input
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert input list to 3x3 Numpy array
    matrix = np.array(input_list).reshape(3, 3)

    # Perform calculations
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of columns
            matrix.mean(axis=1).tolist(),  # Mean of rows
            matrix.mean().item()           # Mean of entire matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),  # Variance of columns
            matrix.var(axis=1).tolist(),  # Variance of rows
            matrix.var().item()           # Variance of entire matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),  # Std Dev of columns
            matrix.std(axis=1).tolist(),  # Std Dev of rows
            matrix.std().item()           # Std Dev of entire matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),  # Max of columns
            matrix.max(axis=1).tolist(),  # Max of rows
            matrix.max().item()           # Max of entire matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),  # Min of columns
            matrix.min(axis=1).tolist(),  # Min of rows
            matrix.min().item()           # Min of entire matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),  # Sum of columns
            matrix.sum(axis=1).tolist(),  # Sum of rows
            matrix.sum().item()           # Sum of entire matrix
        ]
    }

    return calculations

# Example usage
if __name__ == "__main__":
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
