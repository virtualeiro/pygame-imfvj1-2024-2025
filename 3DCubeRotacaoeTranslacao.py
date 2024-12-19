import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rotating 3D Cube")
clock = pygame.time.Clock()

# Define the 3D cube vertices
cube_vertices = np.array([
    [-1, -1, -1],  # Vertex 0
    [1, -1, -1],   # Vertex 1
    [1, 1, -1],    # Vertex 2
    [-1, 1, -1],   # Vertex 3
    [-1, -1, 1],   # Vertex 4
    [1, -1, 1],    # Vertex 5
    [1, 1, 1],     # Vertex 6
    [-1, 1, 1]     # Vertex 7
])

# Define the edges of the cube (pairs of vertex indices)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]


#A simple orthographic projection projects 3D points onto a 2D screen. 
# We scale and offset the points to fit them on the Pygame window.
def project_3d_to_2d(point, scale=100, offset=(320, 240)):
    x, y, z = point
    # Simple orthographic projection (ignores z-depth)
    screen_x = int(x * scale) + offset[0]
    screen_y = int(-y * scale) + offset[1]  # Negative y because Pygame's y-axis is inverted
    return (screen_x, screen_y)

# Function to rotate points in 3D space
def rotate_3d(points, angle_x, angle_y, angle_z):
    # Convert angles to radians
    angle_x = np.radians(angle_x)
    angle_y = np.radians(angle_y)
    angle_z = np.radians(angle_z)

    # Rotation matrices
    rotation_x = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])

    rotation_y = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)]
    ])

    rotation_z = np.array([
        [np.cos(angle_z), -np.sin(angle_z), 0],
        [np.sin(angle_z), np.cos(angle_z), 0],
        [0, 0, 1]
    ])

    # Combined rotation matrix: Z * Y * X
    rotation_matrix = rotation_z @ rotation_y @ rotation_x

    # Rotate all points
    rotated_points = np.dot(points, rotation_matrix.T)  # Apply rotation
    return rotated_points

# Main loop
running = True
angle_x, angle_y, angle_z = 0, 0, 0  # Rotation angles
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Rotate the cube
    rotated_vertices = rotate_3d(cube_vertices, angle_x, angle_y, angle_z)

    # Project rotated 3D points to 2D
    projected_points = [project_3d_to_2d(point) for point in rotated_vertices]

    # Draw the edges of the cube
    for edge in cube_edges:
        start = projected_points[edge[0]]
        end = projected_points[edge[1]]
        pygame.draw.line(screen, (0, 255, 0), start, end, 2)

    # Update angles for rotation
    angle_x += 1
    angle_y += 1
    angle_z += 1

    # Update display and tick clock
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
