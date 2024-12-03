def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def line_intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return None  # Lines are parallel

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

    # Check if intersection point is within both line segments
    if 0 <= ua <= 1 and 0 <= ub <= 1:
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return (int(x), int(y))
    return None

def calculate_star_intensity(lines, star_point):
    x, y = star_point
    intensities = []

    for line in lines:
        x1, y1, x2, y2 = line
        # Check if line passes through the star point
        if (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2)):
            # Determine direction
            dx = sign(x2 - x1)
            dy = sign(y2 - y1)

            # Count cells from the star point in both directions
            count1 = 0
            xi, yi = x, y
            while (xi, yi) != (x2, y2):
                xi += dx
                yi += dy
                count1 += 1

            count2 = 0
            xi, yi = x, y
            while (xi, yi) != (x1, y1):
                xi -= dx
                yi -= dy
                count2 += 1

            # Handle cases where line is on one side or cuts through the star
            if x1 == x2 or y1 == y2:  # Vertical or horizontal line
                intensities.append(min(count1, count2))
            else:
                intensities.extend([count1, count2])

    return min(intensities) if intensities else 0

# Read input
N = int(input())  # Number of lines
lines = [tuple(map(int, input().split())) for _ in range(N)]
K = int(input())  # The type of star we need to calculate intensity for

# Find all intersection points
intersections = {}
for i in range(N):
    for j in range(i + 1, N):
        point = line_intersection(lines[i], lines[j])
        if point:
            if point not in intersections:
                intersections[point] = []
            if lines[i] not in intersections[point]:
                intersections[point].append(lines[i])
            if lines[j] not in intersections[point]:
                intersections[point].append(lines[j])

# Calculate total intensity for K-stars
total_intensity = 0
for point, star_lines in intersections.items():
    unique_lines = list(set(star_lines))
    if len(unique_lines) == K:
        intensity = calculate_star_intensity(unique_lines, point)
        total_intensity += intensity

# Output the total intensity of all K-stars
print(total_intensity)