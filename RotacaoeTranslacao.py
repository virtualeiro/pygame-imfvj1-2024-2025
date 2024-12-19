import pygame
import random
import math
from pygame.math import Vector2

import numpy as np

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Window")
clock = pygame.time.Clock()


p1 = [200, 150]
p2 = [150, 200]
p3 = [250, 200]
triangulo=np.matrix([p1,p2,p3])

#print (numpy.add(triangulo, a))
def graficos():
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,0,0), p1, p2)
    pygame.draw.line(screen, (255,0,0), p2, p3)
    pygame.draw.line(screen, (255,0,0), p3, p1)

def rotate_matrix_2d(points, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    # Rotation matrix
    rotation_matrix = np.array([  # Changed to np.array
        [np.cos(angle_radians), -np.sin(angle_radians)],
        [np.sin(angle_radians),  np.cos(angle_radians)]
    ])
    """
    rotated_points = []
    for point in points:  # Each point is a row
        point = np.array(point).flatten()  # Ensure it's a flat array
        new_x = point[0] * rotation_matrix[0, 0] + point[1] * rotation_matrix[1, 0]
        new_y = point[0] * rotation_matrix[0, 1] + point[1] * rotation_matrix[1, 1]
        rotated_points.append([new_x, new_y])
    """
    # Apply rotation
    #rotated_points = points @ rotation_matrix.T

    # Subtract center of rotation (optional for rotation around origin)
    center = np.mean(points, axis=0)  # Center of the triangle
    points_centered = points - center  # Shift to origin
    
    # Perform matrix multiplication (use @ operator)
    rotated_points = points_centered @ rotation_matrix.T

    # Shift back to the original center
    rotated_points += center


    rotated_points = np.array(rotated_points).astype(int).tolist()  # Convert to int and list

    # Draw the rotated triangle
    pygame.draw.line(screen, (0, 255, 0), rotated_points[0], rotated_points[1])
    pygame.draw.line(screen, (0, 255, 0), rotated_points[1], rotated_points[2])
    pygame.draw.line(screen, (0, 255, 0), rotated_points[2], rotated_points[0])

running = True
ang=1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    graficos()
    ang+=1
    rotate_matrix_2d(triangulo,ang)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()