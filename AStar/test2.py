def supercover_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    
    ddy = 2 * dy
    ddx = 2 * dx
    
    points.append((x, y))
    
    if ddx >= ddy:  # First octant (0 <= slope <= 1)
        errorprev = error = dx  # Start in the middle of the square
        for _ in range(dx):
            x += xstep
            error += ddy
            if error > ddx:  # Increment y if AFTER the middle
                y += ystep
                error -= ddx
                # Check additional points
                if error + errorprev < ddx:
                    points.append((x, y - ystep))  # Bottom square
                elif error + errorprev > ddx:
                    points.append((x - xstep, y))  # Left square
                else:
                    points.append((x, y - ystep))  # Corner case
                    points.append((x - xstep, y))
            points.append((x, y))
            errorprev = error
    else:  # Second octant (1 < slope)
        errorprev = error = dy
        for _ in range(dy):
            y += ystep
            error += ddx
            if error > ddy:
                x += xstep
                error -= ddy
                # Check additional points
                if error + errorprev < ddy:
                    points.append((x - xstep, y))  # Left square
                elif error + errorprev > ddy:
                    points.append((x, y - ystep))  # Bottom square
                else:
                    points.append((x - xstep, y))
                    points.append((x, y - ystep))
            points.append((x, y))
            errorprev = error
    
    return points

# Example usage
line_points = supercover_line(2, 3, 10, 7)
print(line_points)
