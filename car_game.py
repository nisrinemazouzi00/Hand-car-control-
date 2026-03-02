import cv2
import mediapipe as mp
import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Controlled Car Game")
clock = pygame.time.Clock()

# Load images
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (80, 160))
car_x = WIDTH // 2 - 40
car_y = HEIGHT - 180

road = pygame.image.load("road.png")
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

# Variables for scrolling road
road_y1 = 0
road_y2 = -HEIGHT
road_speed = 5  # Adjust speed for scrolling effect

# Setup MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Open webcam
cap = cv2.VideoCapture(0)

def get_hand_x():
    success, frame = cap.read()
    if not success:
        return None
    frame = cv2.flip(frame, 1)  # Mirror image
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        x_norm = hand_landmarks.landmark[9].x  # Palm base landmark
        return int(x_norm * WIDTH)
    return None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the road images down
    road_y1 += road_speed
    road_y2 += road_speed

    # Reset road position to loop scrolling
    if road_y1 >= HEIGHT:
        road_y1 = road_y2 - HEIGHT
    if road_y2 >= HEIGHT:
        road_y2 = road_y1 - HEIGHT

    # Draw two roads for seamless scrolling
    screen.blit(road, (0, road_y1))
    screen.blit(road, (0, road_y2))

    # Get hand x position and move car
    hand_x = get_hand_x()
    if hand_x is not None:
        target_x = hand_x - 40
        car_x += (target_x - car_x) * 0.2  # Smooth movement

    # Draw car
    screen.blit(car, (car_x, car_y))
    pygame.display.flip()
    clock.tick(30)

# Cleanup
cap.release()
pygame.quit()
sys.exit()
