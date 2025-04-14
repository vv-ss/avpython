import matplotlib.pyplot as plt
import numpy as np



# Tree type 1 – Symmetrical
def draw_tree_type1(branches, x, y, angle, branch_len, angle_diff, shorten_factor, min_branch_len, depth=0):
    if branch_len < min_branch_len:
        return
    x_end = x + branch_len * np.cos(np.radians(angle))
    y_end = y + branch_len * np.sin(np.radians(angle))
    branches.append((x, y, x_end, y_end, depth))
    draw_tree_type1(branches, x_end, y_end, angle - angle_diff, branch_len * shorten_factor, angle_diff, shorten_factor, min_branch_len, depth + 1)
    draw_tree_type1(branches, x_end, y_end, angle + angle_diff, branch_len * shorten_factor, angle_diff, shorten_factor, min_branch_len, depth + 1)

# Tree type 2 – Chaotic angles
def draw_tree_type2(branches, x, y, angle, branch_len, angle_diff, shorten_factor, min_branch_len, depth=0):
    if branch_len < min_branch_len:
        return
    x_end = x + branch_len * np.cos(np.radians(angle))
    y_end = y + branch_len * np.sin(np.radians(angle))
    branches.append((x, y, x_end, y_end, depth))
    new_diff = angle_diff + np.random.uniform(-5, 5)
    draw_tree_type2(branches, x_end, y_end, angle - new_diff, branch_len * shorten_factor, angle_diff, shorten_factor, min_branch_len, depth + 1)
    draw_tree_type2(branches, x_end, y_end, angle + new_diff, branch_len * shorten_factor, angle_diff, shorten_factor, min_branch_len, depth + 1)

# Tree type 3 – Denser fractal
def draw_tree_type3(branches, x, y, angle, branch_len, angle_diff, shorten_factor, min_branch_len, depth=0):
    if branch_len < min_branch_len:
        return
    x_end = x + branch_len * np.cos(np.radians(angle))
    y_end = y + branch_len * np.sin(np.radians(angle))
    branches.append((x, y, x_end, y_end, depth))
    draw_tree_type3(branches, x_end, y_end, angle - angle_diff / 2, branch_len * shorten_factor, angle_diff, shorten_factor, min_branch_len, depth + 1)
    draw_tree_type3(branches, x_end, y_end, angle + angle_diff / 2, branch_len * shorten_factor, angle_diff, shorten_factor, min_branch_len, depth + 1)


def create_fractal_tree():
    # Set up the plot
    plt.figure(figsize=(7, 7))
    plt.axis('off')  # Hide axes

    # Starting position and parameters
    x_start, y_start = 0, 0
    branch_len = 200  # Larger initial branch length
    angle = 90  # Start facing upwards
    angle_diff = 25  # Angle difference between left and right branches
    shorten_factor = 0.75  # Slower branch length reduction
    min_branch_len = 10  # Minimum length for recursion to stop

    # Draw the tree starting from the base
    draw_tree_type1(x_start, y_start, angle, branch_len, angle_diff, shorten_factor, min_branch_len)

    # Display the plot
    plt.show()


# Create and display the fractal tree
create_fractal_tree()
