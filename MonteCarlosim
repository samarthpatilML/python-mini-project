import random

def estimate_pi(num_darts):
  """
  Estimates the value of pi using the Monte Carlo method with a specified number of darts.

  Args:
      num_darts: The number of darts to throw.

  Returns:
      The estimated value of pi.
  """
  inside_circle = 0
  for _ in range(num_darts):
    x = random.random()
    y = random.random()
    if (x*2 + y*2) <= 1.0:
      inside_circle += 1
  pi_estimate = (4.0 * inside_circle) / num_darts
  return pi_estimate

num_darts = 1000
estimated_pi = estimate_pi(num_darts)
print(f"Estimated value of pi with {num_darts} darts: {estimated_pi}")